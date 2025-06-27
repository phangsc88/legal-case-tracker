from datetime import date
import pandas as pd


def calculate_case_performance(status, case_due_date_str, completed_date_str, overdue_tasks_count):
    overdue_tasks_count = overdue_tasks_count or 0
    case_due_date_obj = pd.to_datetime(case_due_date_str).date() if pd.notnull(case_due_date_str) else None
    completed_date_obj = pd.to_datetime(completed_date_str).date() if pd.notnull(completed_date_str) else None
    if status == 'Completed':
        if case_due_date_obj and completed_date_obj:
            return 'Completed On Time' if completed_date_obj <= case_due_date_obj else 'Completed Late'
        return 'Completed On Time'
    elif status in ['Not Started', 'On Hold']:
        return 'Pending'
    elif status == 'In Progress':
        return 'Overdue' if overdue_tasks_count > 0 else 'On Time'
    return 'Pending'


def calculate_task_performance(status, due_date_str, task_completed_date_str):
    today = date.today()
    due_date_obj = pd.to_datetime(due_date_str).date() if pd.notnull(due_date_str) else None
    completed_date_obj = pd.to_datetime(task_completed_date_str).date() if pd.notnull(task_completed_date_str) else None
    if status == 'Completed':
        if due_date_obj and completed_date_obj:
            return 'Completed On Time' if completed_date_obj <= due_date_obj else 'Completed Late'
        return 'Completed On Time'
    elif status in ['Not Started', 'On Hold']:
        if due_date_obj:
            return 'Overdue' if due_date_obj < today else 'Pending'
        return 'Pending'
    elif status == 'In Progress':
        if due_date_obj:
            return 'Overdue' if due_date_obj < today else 'On Time'
        return 'On Time'
    return 'Pending'
