# create_first_user.py

from auth import db_add_user

def create_initial_users():
    """
    This function creates the first Admin and User accounts.
    Run this script ONCE after creating the 'users' table.
    """
    print("Attempting to create initial users...")

    # --- Create an Admin User ---
    # IMPORTANT: Change 'admin_password' to a strong password
    admin_created = db_add_user(
        username='Phang',
        password='1234',
        privilege='Admin'
    )
    if admin_created:
        print(">>> Admin user 'admin' created successfully.")
    else:
        print(">>> Failed to create 'admin'. The user may already exist.")

    # --- Create a standard User ---
    # IMPORTANT: Change 'user_password' to a strong password
    user_created = db_add_user(
        username='user',
        password='password',
        privilege='User'
    )
    if user_created:
        print(">>> Standard user 'user' created successfully.")
    else:
        print(">>> Failed to create 'user'. The user may already exist.")

if __name__ == '__main__':
    create_initial_users()