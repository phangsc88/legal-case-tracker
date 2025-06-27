import pandas as pd
from sqlalchemy import text
from .connection import get_db_connection
from typing import Optional, Dict, Any, Tuple
from datetime import date
from utils.performance import calculate_case_performance as _calculate_case_performance
from utils.performance import calculate_task_performance as _calculate_task_performance



# Database Functions (WITH DYNAMIC LOGIC)
# =============================================================================
def db_fetch_all_cases() -> pd.DataFrame:
    with get_db_connection() as conn:
        sql = text("""
        SELECT c.case_id, c.case_name, c.status, c.case_type,
            to_char(c.start_date, 'YYYY-MM-DD') as start_date,
            to_char(c.completed_date, 'YYYY-MM-DD') as completed_date,
            (SELECT MAX(t_sub.due_date) FROM tasks t_sub WHERE t_sub.case_id = c.case_id) as case_due_date,
            COUNT(t.task_id) FILTER (WHERE t.due_date < CURRENT_DATE AND t.status != 'Completed') as overdue_tasks_count
        FROM cases c
        LEFT JOIN tasks t ON c.case_id = t.case_id
        GROUP BY c.case_id, c.case_name, c.status, c.case_type, c.start_date, c.completed_date
        ORDER BY c.case_id ASC
        """)
        df = pd.read_sql(sql, conn)
        if not df.empty:
            df['case_due_date'] = pd.to_datetime(df['case_due_date']).dt.strftime('%Y-%m-%d').replace({pd.NaT: None})
            df['performance'] = df.apply(
                lambda row: _calculate_case_performance(row['status'], row['case_due_date'], row['completed_date'],
                                                        row['overdue_tasks_count']), axis=1)
        else:
            df = df.assign(performance=[])
        return df


def db_add_case(name: str, status: str, case_type: str) -> int:
    sql = text("INSERT INTO cases (case_name, status, case_type) VALUES (:name, :status, :case_type) RETURNING case_id")
    with get_db_connection() as conn:
        result = conn.execute(sql, {"name": name, "status": status, "case_type": case_type}).scalar_one()
        conn.commit()
        return result


def db_populate_tasks_from_template(case_id: int, case_type: str):
    if not case_type: return
    with get_db_connection() as conn:
        sql_select = text("""
            SELECT tt.task_name, tt.default_status, tt.day_offset, tt.documents_required 
            FROM task_templates tt 
            JOIN template_types tty ON tt.template_type_id = tty.template_type_id 
            WHERE tty.type_name = :case_type 
            ORDER BY tt.task_sequence
        """)
        template_tasks_df = pd.read_sql(sql_select, conn, params={"case_type": case_type})

        if template_tasks_df.empty: return

        tasks_to_insert = [
            {
                "case_id": case_id,
                "task_name": row['task_name'],
                "status": row['default_status'],
                "day_offset": row['day_offset'],
                "documents_required": row['documents_required']
            } for _, row in template_tasks_df.iterrows()
        ]

        if tasks_to_insert:
            sql_insert = text("""
                INSERT INTO tasks (case_id, task_name, status, day_offset, documents_required) 
                VALUES (:case_id, :task_name, :status, :day_offset, :documents_required)
            """)
            conn.execute(sql_insert, tasks_to_insert)
            conn.commit()


def db_update_case(case_id: int, name: str, status: str, case_type: str):
    sql = text("UPDATE cases SET case_name = :name, status = :status, case_type = :type WHERE case_id = :id")
    with get_db_connection() as conn:
        conn.execute(sql, {"name": name, "status": status, "type": case_type, "id": case_id})
        conn.commit()


def db_delete_case(case_id: int):
    with get_db_connection() as conn:
        sql_delete_tasks = text("DELETE FROM tasks WHERE case_id = :case_id")
        conn.execute(sql_delete_tasks, {"case_id": case_id})

        sql_delete_case = text("DELETE FROM cases WHERE case_id = :case_id")
        conn.execute(sql_delete_case, {"case_id": case_id})

        conn.commit()


def db_fetch_single_case(case_id: int) -> Optional[Dict[str, Any]]:
    if not case_id: return None
    sql = text(
        "SELECT case_id, case_name, status, case_type, start_date, completed_date FROM cases WHERE case_id = :case_id")
    with get_db_connection() as conn:
        result = conn.execute(sql, {"case_id": case_id}).fetchone()
        if result:
            try:
                return result._asdict()
            except AttributeError:
                return dict(result)
        return None


def db_fetch_case_due_date(case_id: int) -> Optional[date]:
    if not case_id: return None
    sql = text("SELECT MAX(due_date) FROM tasks WHERE case_id = :case_id")
    with get_db_connection() as conn:
        due_date = conn.execute(sql, {"case_id": case_id}).scalar_one_or_none()
    return due_date


def db_fetch_tasks_for_case(case_id: int) -> pd.DataFrame:
    if not case_id: return pd.DataFrame()
    with get_db_connection() as conn:
        sql = text("""
            SELECT task_id, task_name, status, due_date, day_offset, documents_required,
                to_char(task_start_date, 'YYYY-MM-DD') as task_start_date,
                to_char(task_completed_date, 'YYYY-MM-DD') as task_completed_date,
                last_updated_by,
                to_char(last_updated_at, 'YYYY-MM-DD HH24:MI:SS') as last_updated_at_display
            FROM tasks WHERE case_id = :case_id ORDER BY task_id ASC
        """)
        df = pd.read_sql(sql, conn, params={"case_id": case_id})
        if not df.empty:
            df['due_date'] = pd.to_datetime(df['due_date']).dt.strftime('%Y-%m-%d').replace({pd.NaT: None})
            df['due_date_display'] = df.apply(
                lambda row: row['due_date'] if pd.notnull(row['due_date']) else (
                    f"+ {int(row['day_offset'])} Days" if pd.notnull(row['day_offset']) else "N/A"), axis=1)
            df['performance'] = df.apply(
                lambda row: _calculate_task_performance(row['status'], row['due_date'], row['task_completed_date']),
                axis=1)
        return df


def db_update_case_dates_from_tasks(case_id: int):
    with get_db_connection() as conn:
        sql_get_current_start = text("SELECT start_date FROM cases WHERE case_id = :case_id")
        current_case_start_date = conn.execute(sql_get_current_start, {"case_id": case_id}).scalar_one_or_none()

        sql_min_task_start = text(
            "SELECT MIN(task_start_date) FROM tasks WHERE case_id = :case_id AND status IN ('In Progress', 'Completed')")
        min_task_start_date = conn.execute(sql_min_task_start, {"case_id": case_id}).scalar_one_or_none()

        new_case_start_date = min_task_start_date if min_task_start_date else current_case_start_date

        if new_case_start_date and new_case_start_date != current_case_start_date:
            db_calculate_and_set_task_due_dates(case_id, new_case_start_date)

        sql_incomplete_count = text("SELECT COUNT(*) FROM tasks WHERE case_id = :case_id AND status != 'Completed'")
        incomplete_tasks_count = conn.execute(sql_incomplete_count, {"case_id": case_id}).scalar_one()

        new_case_completed_date = None
        if incomplete_tasks_count == 0:
            sql_max_task_complete = text(
                "SELECT MAX(task_completed_date) FROM tasks WHERE case_id = :case_id AND status = 'Completed'")
            max_task_completed_date = conn.execute(sql_max_task_complete, {"case_id": case_id}).scalar_one_or_none()
            new_case_completed_date = max_task_completed_date if max_task_completed_date else date.today()

        sql_update_case = text(
            "UPDATE cases SET start_date = :start_date, completed_date = :completed_date WHERE case_id = :case_id")
        conn.execute(sql_update_case,
                     {"start_date": new_case_start_date, "completed_date": new_case_completed_date, "case_id": case_id})
        conn.commit()


def db_calculate_and_set_task_due_dates(case_id: int, start_date: date):
    with get_db_connection() as conn:
        sql_select = text("SELECT task_id, day_offset FROM tasks WHERE case_id = :case_id AND day_offset IS NOT NULL")
        tasks_to_update_df = pd.read_sql(sql_select, conn, params={"case_id": case_id})

        if tasks_to_update_df.empty:
            return

        updates = [
            {'task_id': int(row['task_id']), 'due_date': start_date + timedelta(days=int(row['day_offset']))}
            for _, row in tasks_to_update_df.iterrows()
        ]

        if updates:
            sql_update = text("UPDATE tasks SET due_date = :due_date WHERE task_id = :task_id")
            conn.execute(sql_update, updates)
            conn.commit()


def db_update_case_status_and_start_date(case_id: int, status: str):
    case_info = db_fetch_single_case(case_id)
    if not case_info: return

    today = date.today()
    should_set_initial_start_date = (status == 'In Progress' and case_info.get('start_date') is None)

    with get_db_connection() as conn:
        if should_set_initial_start_date:
            sql = text("UPDATE cases SET status = :status, start_date = :start_date WHERE case_id = :case_id")
            conn.execute(sql, {"status": status, "start_date": today, "case_id": case_id})
            db_calculate_and_set_task_due_dates(case_id, today)
        else:
            sql = text("UPDATE cases SET status = :status WHERE case_id = :case_id")
            conn.execute(sql, {"status": status, "case_id": case_id})
        conn.commit()

    db_update_case_dates_from_tasks(case_id)


def db_check_and_complete_case(case_id: int) -> bool:
    with get_db_connection() as conn:
        sql_incomplete = text("SELECT COUNT(*) FROM tasks WHERE case_id = :case_id AND status != 'Completed'")
        incomplete_count = conn.execute(sql_incomplete, {"case_id": int(case_id)}).scalar_one()

        if incomplete_count == 0:
            sql_update_case = text("UPDATE cases SET status = 'Completed' WHERE case_id = :case_id")
            conn.execute(sql_update_case, {"case_id": int(case_id)})
            conn.commit()
            db_update_case_dates_from_tasks(case_id)
            return True
    return False


def db_update_task_details(task_id: int, name: str, status: str, start_date_input: Optional[str],
                           completed_date_input: Optional[str], new_due_date_input_str: Optional[str],
                           updated_by_user: str) -> Tuple[str, bool]:
    today = date.today()
    case_was_started_automatically = False

    start_date_for_db = date.fromisoformat(start_date_input) if start_date_input else None
    completed_date_for_db = date.fromisoformat(completed_date_input) if completed_date_input else None
    due_date_for_db_str = new_due_date_input_str

    with get_db_connection() as conn:
        sql_select = text(
            "SELECT case_id, status, task_start_date, task_completed_date, due_date FROM tasks WHERE task_id = :task_id")
        result = conn.execute(sql_select, {"task_id": int(task_id)}).fetchone()
        if not result: return status, False

        task_data = result._asdict()
        case_id = task_data['case_id']

        final_status = status
        if completed_date_for_db:
            final_status = 'Completed'
        elif start_date_for_db and final_status != 'Completed':
            final_status = 'In Progress'

        if not start_date_for_db and final_status == 'In Progress':
            start_date_for_db = today

        if final_status == 'Completed' and not completed_date_for_db:
            completed_date_for_db = task_data['task_completed_date'] or today

        if final_status != 'Completed':
            completed_date_for_db = None

        sql_update = text("""UPDATE tasks SET task_name=:name, status=:status, task_start_date=:start, 
                             task_completed_date=:completed, due_date=:due, last_updated_by=:user, 
                             last_updated_at=:now WHERE task_id=:task_id""")
        conn.execute(sql_update, {"name": name, "status": final_status, "start": start_date_for_db,
                                  "completed": completed_date_for_db, "due": due_date_for_db_str,
                                  "user": updated_by_user, "now": datetime.now(), "task_id": int(task_id)})
        conn.commit()

    db_update_case_dates_from_tasks(case_id)

    final_case_info = db_fetch_single_case(case_id)
    if final_case_info and final_case_info.get('status') == 'Not Started' and final_case_info.get(
            'start_date') is not None:
        db_update_case_status_and_start_date(case_id, 'In Progress')
        case_was_started_automatically = True

    db_check_and_complete_case(case_id)

    with get_db_connection() as conn:
        sql_get_status = text("SELECT status FROM tasks WHERE task_id = :task_id")
        final_task_status = conn.execute(sql_get_status, {"task_id": int(task_id)}).scalar_one()

    return final_task_status, case_was_started_automatically


def db_fetch_tasks_for_date(target_date: date) -> pd.DataFrame:
    with get_db_connection() as conn:
        sql = text(
            "SELECT t.task_name, c.case_name, c.case_id FROM tasks t JOIN cases c ON t.case_id = c.case_id WHERE t.due_date = :target_date AND t.status != 'Completed'")
        return pd.read_sql(sql, conn, params={"target_date": target_date})


def db_fetch_tasks_for_month(start_of_month: date, end_of_month: date) -> pd.DataFrame:
    with get_db_connection() as conn:
        sql = text(
            "SELECT t.task_id, t.task_name, t.status, t.due_date, c.case_name, c.case_id FROM tasks t JOIN cases c ON t.case_id = c.case_id WHERE t.due_date BETWEEN :start AND :end ORDER BY t.due_date ASC, c.case_name, t.task_name")
        df = pd.read_sql(sql, conn, params={"start": start_of_month, "end": end_of_month})
        if not df.empty:
            df['due_date'] = pd.to_datetime(df['due_date'])
            df['due_date_display'] = df['due_date'].dt.strftime('%Y-%m-%d')
            df['performance'] = df.apply(lambda row: _calculate_task_performance(row['status'], row['due_date'], None),
                                         axis=1)
        return df


def db_fetch_template_types() -> pd.DataFrame:
    with get_db_connection() as conn:
        return pd.read_sql(text("SELECT template_type_id, type_name FROM template_types ORDER BY type_name"), conn)


def db_add_template_type(type_name: str):
    sql = text("INSERT INTO template_types (type_name) VALUES (:type_name) ON CONFLICT (type_name) DO NOTHING")
    with get_db_connection() as conn:
        conn.execute(sql, {"type_name": type_name})
        conn.commit()


# NEW
def db_delete_template_type(template_type_id: int):
    """
    Deletes a template type and all of its associated task templates.
    """
    with get_db_connection() as conn:
        # First, delete all task templates associated with this type
        sql_delete_tasks = text("DELETE FROM task_templates WHERE template_type_id = :tt_id")
        conn.execute(sql_delete_tasks, {"tt_id": template_type_id})

        # Then, delete the template type itself
        sql_delete_type = text("DELETE FROM template_types WHERE template_type_id = :tt_id")
        conn.execute(sql_delete_type, {"tt_id": template_type_id})

        conn.commit()


def db_fetch_tasks_for_template(template_type_id: int) -> pd.DataFrame:
    if not template_type_id: return pd.DataFrame()
    with get_db_connection() as conn:
        sql = text("""
            SELECT task_template_id, task_sequence, task_name, default_status, day_offset, documents_required
            FROM task_templates 
            WHERE template_type_id = :template_type_id 
            ORDER BY task_sequence
        """)
        return pd.read_sql(sql, conn, params={"template_type_id": template_type_id})


def db_add_task_to_template(template_type_id: int, seq: int, name: str, status: str, offset: Optional[int],
                            documents: Optional[str]):
    sql = text("""
        INSERT INTO task_templates (template_type_id, task_sequence, task_name, default_status, day_offset, documents_required) 
        VALUES (:tt_id, :seq, :name, :status, :offset, :documents)
    """)
    with get_db_connection() as conn:
        conn.execute(sql, {
            "tt_id": template_type_id,
            "seq": seq,
            "name": name,
            "status": status,
            "offset": offset,
            "documents": documents
        })
        conn.commit()


def db_update_task_template(task_template_id: int, column: str, value: Any):
    allowed_columns = {
        "task_sequence": "task_sequence",
        "task_name": "task_name",
        "default_status": "default_status",
        "day_offset": "day_offset",
        "documents_required": "documents_required"
    }

    if column not in allowed_columns:
        print(f"Error: Attempted to update a non-whitelisted column: {column}")
        return

    sql = text(f"UPDATE task_templates SET {allowed_columns[column]} = :value WHERE task_template_id = :tt_id")
    with get_db_connection() as conn:
        conn.execute(sql, {"value": value, "tt_id": task_template_id})
        conn.commit()


def db_delete_task_from_template(task_template_id: int):
    sql = text("DELETE FROM task_templates WHERE task_template_id = :tt_id")
    with get_db_connection() as conn:
        conn.execute(sql, {"tt_id": int(task_template_id)})
        conn.commit()


def db_add_remark(case_id: int, user_name: str, message: str):
    sql = text("INSERT INTO case_remarks (case_id, user_name, message) VALUES (:case_id, :user_name, :message)")
    with get_db_connection() as conn:
        conn.execute(sql, {"case_id": case_id, "user_name": user_name, "message": message})
        conn.commit()


def db_fetch_remarks_for_case(case_id: int) -> pd.DataFrame:
    with get_db_connection() as conn:
        sql = text(
            "SELECT remark_id, user_name, timestamp, message FROM case_remarks WHERE case_id = :case_id ORDER BY timestamp DESC")
        df = pd.read_sql(sql, conn, params={"case_id": case_id})
        if not df.empty:
            df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
        return df


def db_fetch_affected_cases_report(from_date: date, to_date: date) -> pd.DataFrame:
    with get_db_connection() as conn:
        sql = text("""
            SELECT c.case_id, c.case_name, c.status, c.case_type,
                to_char(c.start_date, 'YYYY-MM-DD') as start_date,
                to_char(c.completed_date, 'YYYY-MM-DD') as completed_date,
                (SELECT MAX(t_sub.due_date) FROM tasks t_sub WHERE t_sub.case_id = c.case_id) as case_due_date,
                COUNT(t.task_id) FILTER (WHERE t.due_date < CURRENT_DATE AND t.status != 'Completed') as overdue_tasks_count
            FROM cases c
            LEFT JOIN tasks t ON c.case_id = t.case_id
            WHERE c.start_date BETWEEN :from_date AND :to_date
               OR c.completed_date BETWEEN :from_date AND :to_date
               OR (c.start_date < :from_date AND (c.completed_date > :to_date OR c.completed_date IS NULL))
            GROUP BY c.case_id
            ORDER BY c.case_id
        """)
        df = pd.read_sql(sql, conn, params={"from_date": from_date, "to_date": to_date})
        if not df.empty:
            df['performance'] = df.apply(
                lambda row: _calculate_case_performance(row['status'], row['case_due_date'], row['completed_date'],
                                                        row['overdue_tasks_count']), axis=1)
        return df


def db_fetch_affected_tasks_report(from_date: date, to_date: date) -> pd.DataFrame:
    with get_db_connection() as conn:
        sql = text("""
            SELECT t.task_id, t.task_name, t.status, c.case_name, c.case_id,
                   to_char(t.due_date, 'YYYY-MM-DD') as due_date,
                   t.task_completed_date
            FROM tasks t
            JOIN cases c ON t.case_id = c.case_id
            WHERE t.due_date BETWEEN :from_date AND :to_date
               OR t.task_start_date BETWEEN :from_date AND :to_date
               OR t.task_completed_date BETWEEN :from_date AND :to_date
            ORDER BY t.due_date
        """)
        df = pd.read_sql(sql, conn, params={"from_date": from_date, "to_date": to_date})
        if not df.empty:
            df['performance'] = df.apply(
                lambda row: _calculate_task_performance(row['status'], row['due_date'], row['task_completed_date']),
                axis=1)
        return df

def db_fetch_attachments_for_task(task_id: int) -> pd.DataFrame:
    sql = text("""
        SELECT attachment_id, original_filename, stored_filename
        FROM task_attachments WHERE task_id = :task_id ORDER BY upload_timestamp DESC
    """)
    with get_db_connection() as conn:
        return pd.read_sql(sql, conn, params={"task_id": task_id})


def _fetch_dashboard_data(from_date: date, to_date: date) -> Tuple[pd.DataFrame, pd.DataFrame]:
    with get_db_connection() as conn:
        sql_cases = text("""
            SELECT c.case_id, c.case_name, c.status, c.case_type, c.start_date, c.completed_date,
                   (SELECT MAX(t_sub.due_date) FROM tasks t_sub WHERE t_sub.case_id = c.case_id) as case_due_date,
                   COUNT(t.task_id) FILTER (WHERE t.due_date < CURRENT_DATE AND t.status != 'Completed') as overdue_tasks_count
            FROM cases c LEFT JOIN tasks t ON c.case_id = t.case_id
            WHERE c.status IN ('Not Started', 'On Hold') OR (c.start_date <= :to_date AND (c.completed_date >= :from_date OR c.completed_date IS NULL))
            GROUP BY c.case_id
        """)
        cases_df = pd.read_sql(sql_cases, conn, params={"from_date": from_date, "to_date": to_date})
        if not cases_df.empty:
            cases_df['performance'] = cases_df.apply(
                lambda row: _calculate_case_performance(row['status'], row['case_due_date'], row['completed_date'],
                                                        row['overdue_tasks_count']), axis=1)

        sql_tasks = text(
            "SELECT t.task_id, t.task_name, t.status, t.due_date, t.task_completed_date FROM tasks t WHERE t.due_date BETWEEN :from_date AND :to_date")
        tasks_df = pd.read_sql(sql_tasks, conn, params={"from_date": from_date, "to_date": to_date})
        if not tasks_df.empty:
            tasks_df['performance'] = tasks_df.apply(
                lambda row: _calculate_task_performance(row['status'], row['due_date'], row['task_completed_date']),
                axis=1)

    return cases_df, tasks_df

