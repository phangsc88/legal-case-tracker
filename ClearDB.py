import psycopg2
from typing import Dict, Any

# Database settings from your main application
DB_SETTINGS = {
    "dbname": "legal_tracker",
    "user": "legal_app_user",
    "password": "1234",
    "host": "localhost",
    "port": "5432"
}


def clear_database_content(db_settings: Dict[str, Any]):
    """
    Connects to the PostgreSQL database and truncates (clears) the specified tables.
    It then attempts to reset sequences for auto-incrementing IDs if possible.
    """
    conn = None
    try:
        conn = psycopg2.connect(**db_settings)
        cur = conn.cursor()

        # List of tables to clear, in reverse order of foreign key dependencies
        tables_to_clear = [
            "tasks",
            "task_templates",
            "cases",
            "template_types"
        ]

        # Get sequence names for tables with serial primary keys
        sequence_names = []
        cur.execute("""
            SELECT relname
            FROM pg_class
            WHERE relkind = 'S' AND relnamespace = (SELECT oid FROM pg_namespace WHERE nspname = 'public');
        """)
        all_sequences = [row[0] for row in cur.fetchall()]

        # Filter for sequences related to your tables
        for table in tables_to_clear:
            seq_candidate = f"{table}_{table.removesuffix('s')}_id_seq"  # Common pattern: tablename_singular_id_seq
            if seq_candidate in all_sequences:
                sequence_names.append(seq_candidate)
            # Add other common naming conventions if your primary keys are named differently
            elif f"{table}_id_seq" in all_sequences:  # simpler: tablename_id_seq
                sequence_names.append(f"{table}_id_seq")

        print("Clearing database content...")

        # TRUNCATE tables without RESTART IDENTITY first
        for table in tables_to_clear:
            sql_truncate = f"TRUNCATE TABLE {table} CASCADE;"  # Removed RESTART IDENTITY
            cur.execute(sql_truncate)
            print(f"  - Table '{table}' truncated successfully (identity not reset yet).")

        # Now, attempt to reset sequences separately
        print("\nAttempting to reset sequences...")
        for seq_name in sequence_names:
            try:
                sql_reset_seq = f"ALTER SEQUENCE {seq_name} RESTART WITH 1;"
                cur.execute(sql_reset_seq)
                print(f"  - Sequence '{seq_name}' reset successfully.")
            except psycopg2.Error as seq_e:
                print(f"  - WARNING: Could not reset sequence '{seq_name}': {seq_e}")
                print("    This usually means the user does not own the sequence. Data will still be cleared,")
                print("    but new IDs might not start from 1 until a superuser resets them.")

        conn.commit()
        print("\nAll specified tables cleared successfully. Database is fresh!")

    except psycopg2.Error as e:
        print(f"\nDatabase error occurred: {e}")
        if conn:
            conn.rollback()  # Rollback any changes on error
        print("Database clear failed. Rolled back changes.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    # WARNING: This will delete all data. Uncomment to run.
    user_input = input("Are you sure you want to clear ALL data from the database? (yes/no): ")
    if user_input.lower() == 'yes':
        clear_database_content(DB_SETTINGS)
    else:
        print("Database clear operation cancelled.")

    print("\nRun this script directly: python your_clear_script_name.py")