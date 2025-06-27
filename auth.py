# auth.py (Corrected for SQLAlchemy)
import psycopg2
from sqlalchemy import create_engine, text
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Dict, Any, Optional, List
from db.connection import get_db_connection


def hash_password(password: str) -> str:
    """Generates a secure hash for a password."""
    return generate_password_hash(password)

def check_password(password_hash: str, password: str) -> bool:
    """Checks a password against a stored hash."""
    return check_password_hash(password_hash, password)

def db_add_user(username: str, password: str, privilege: str) -> bool:
    """Adds a new user to the database with a hashed password."""
    password_h = hash_password(password)
    sql = text("INSERT INTO users (username, password_hash, privilege) VALUES (:username, :password_hash, :privilege)")
    try:
        with get_db_connection() as conn:
            conn.execute(sql, {"username": username, "password_hash": password_h, "privilege": privilege})
            conn.commit()
        return True
    except psycopg2.IntegrityError:
        return False
    except Exception as e:
        print(f"Error adding user: {e}")
        return False

def db_get_user(username: str) -> Optional[Dict[str, Any]]:
    """Fetches a user's details by username."""
    sql = text("SELECT user_id, username, password_hash, privilege FROM users WHERE username = :username")
    with get_db_connection() as conn:
        result = conn.execute(sql, {"username": username}).fetchone()
        if result:
            # ._asdict() is a convenient way to convert the result row to a dict
            return result._asdict()
    return None

def db_get_all_users() -> List[Dict[str, Any]]:
    """Fetches all users for the management page."""
    sql = text("SELECT user_id, username, privilege, to_char(created_at, 'YYYY-MM-DD') as created_at FROM users ORDER BY username")
    users = []
    with get_db_connection() as conn:
        result = conn.execute(sql).fetchall()
        for row in result:
            users.append(row._asdict())
    return users

def db_update_user_password(user_id: int, new_password: str) -> bool:
    """Updates a user's password. For use by Admins."""
    password_h = hash_password(new_password)
    sql = text("UPDATE users SET password_hash = :password_hash WHERE user_id = :user_id")
    try:
        with get_db_connection() as conn:
            conn.execute(sql, {"password_hash": password_h, "user_id": user_id})
            conn.commit()
        return True
    except Exception as e:
        print(f"Error updating password for user {user_id}: {e}")
        return False

def db_delete_user(user_id: int) -> bool:
    """Deletes a user from the database."""
    sql = text("DELETE FROM users WHERE user_id = :user_id")
    try:
        with get_db_connection() as conn:
            conn.execute(sql, {"user_id": user_id})
            conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting user {user_id}: {e}")
        return False