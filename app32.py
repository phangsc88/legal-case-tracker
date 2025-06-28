import os

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table, Input, Output, State, callback, ctx, ALL
import dash_mantine_components as dmc
import plotly.express as px
import plotly.io as pio
from flask import send_from_directory
import uuid
import base64
import pandas as pd
import calendar
from datetime import date, datetime, timedelta
from db.connection import engine
from models import Base

# --- TEMPORARY: Drop and recreate all tables ---
if os.environ.get("RESET_DB") == "1":
    Base.metadata.drop_all(engine)
    print("All tables dropped!")
    Base.metadata.create_all(engine)
    print("All tables recreated!")
else:
    print("RESET_DB not set. No action taken.")

from auth import db_add_user
from db.connection import get_db_connection
from sqlalchemy import text

Base.metadata.create_all(engine)


# =============================================================================
# Shared theme & DataTable styles for dark mode
# =============================================================================
from utils.styles import DARK_THEME, DATATABLE_STYLE_DARK

# =============================================================================
# Shared performance calculators
# =============================================================================
from utils.performance import calculate_case_performance, calculate_task_performance

# =============================================================================
# Page‐layout factories
# =============================================================================
from layouts.login           import build_login_layout
from layouts.user_management import build_user_management_layout
from layouts.homepage        import build_homepage_layout
from layouts.templates       import build_templates_layout, build_template_tasks_container
from layouts.calendar        import build_calendar_layout, build_calendar_tasks_table_component
from layouts.dashboard       import build_dashboard_layout
from layouts.reports         import build_date_report_layout
from layouts.case_detail     import build_case_detail_layout

# =============================================================================
# Auth helpers
# =============================================================================
from auth import (
    db_add_user, db_get_user, db_get_all_users,
    db_update_user_password, db_delete_user, check_password
)

# =============================================================================
# DB connection & query APIs used in callbacks
# =============================================================================
from db.connection import get_db_connection
from db.queries import (
    db_fetch_all_cases,
    db_add_case,
    db_populate_tasks_from_template,
    db_update_case,
    db_delete_case,
    db_fetch_single_case,
    db_fetch_case_due_date,
    db_fetch_tasks_for_case,
    db_fetch_attachments_for_task,
    db_fetch_remarks_for_case,
    db_update_case_status_and_start_date,
    db_update_task_details,
    db_add_remark,
    db_fetch_tasks_for_date,
    db_fetch_tasks_for_month,
    db_fetch_template_types,
    db_add_template_type,
    db_delete_template_type,
    db_add_task_to_template,
    db_delete_task_from_template,
    db_fetch_affected_cases_report,
    db_fetch_affected_tasks_report,
    _fetch_dashboard_data
)

def ensure_default_admin():
    """Create an initial admin if no users exist yet."""
    with get_db_connection() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM users"))
        count = result.scalar()
        if count == 0:
            # Only create if the table is empty!
            created = db_add_user(
                username="admin",
                password="1234",  # Change to something strong later!
                privilege="Admin"
            )
            if created:
                print(f"Default admin created: username='admin' password='1234'")
                print("**CHANGE THIS PASSWORD IMMEDIATELY AFTER FIRST LOGIN!**")
            else:
                print("Failed to create default admin (user may already exist or error occurred)")

ensure_default_admin()

# =============================================================================
# Attachment helper functions
# =============================================================================
UPLOAD_DIRECTORY = "uploads"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def db_add_attachment(task_id: int, original_filename: str, stored_filename: str, uploaded_by: str):
    from sqlalchemy import text
    sql = text("""
        INSERT INTO task_attachments (task_id, original_filename, stored_filename, uploaded_by)
        VALUES (:task_id, :original_filename, :stored_filename, :uploaded_by)
    """)
    with get_db_connection() as conn:
        conn.execute(sql, {
            "task_id": task_id,
            "original_filename": original_filename,
            "stored_filename": stored_filename,
            "uploaded_by": uploaded_by
        })
        conn.commit()

def db_get_attachment_info(attachment_id: int):
    from sqlalchemy import text
    sql = text("SELECT stored_filename FROM task_attachments WHERE attachment_id = :attachment_id")
    with get_db_connection() as conn:
        row = conn.execute(sql, {"attachment_id": attachment_id}).fetchone()
        return dict(row) if row else None

def db_delete_attachment(attachment_id: int):
    info = db_get_attachment_info(attachment_id)
    if info:
        path = os.path.join(UPLOAD_DIRECTORY, info["stored_filename"])
        if os.path.exists(path):
            os.remove(path)
    from sqlalchemy import text
    sql = text("DELETE FROM task_attachments WHERE attachment_id = :attachment_id")
    with get_db_connection() as conn:
        conn.execute(sql, {"attachment_id": attachment_id})
        conn.commit()

def build_attachments_list(task_id):
    attachments_df = db_fetch_attachments_for_task(task_id)
    if attachments_df.empty:
        return dbc.Alert("No attachments for this task.", color="info")

    items = []
    for _, row in attachments_df.iterrows():
        item = dbc.ListGroupItem(
            dbc.Row([
                dbc.Col(row['original_filename'], width=7, className="d-flex align-items-center"),
                dbc.Col(
                    dmc.Group([
                        dmc.Anchor(
                            dmc.Button("View", variant="subtle", size="sm"),
                            href=f"/files/view/{row['stored_filename']}",
                            target="_blank"
                        ),
                        dmc.Anchor(
                            dmc.Button("Download", variant="subtle", size="sm"),
                            href=f"/files/download/{row['stored_filename']}",
                            target="_blank"
                        ),
                        dmc.Button("Delete", id={'type': 'delete-attachment-btn', 'index': row['attachment_id']},
                                   color="red", variant="subtle", size="sm"),
                    ], gap="xs"),
                    width=5, className="d-flex justify-content-end")
            ], align="center")
        )
        items.append(item)
    return dbc.ListGroup(items, flush=True)

# =============================================================================
# App initialization & layout
# =============================================================================
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server

# file serving endpoints
@server.route('/files/view/<filename>')
def serve_view(filename):
    return send_from_directory(UPLOAD_DIRECTORY, filename)

@server.route('/files/download/<filename>')
def serve_download(filename):
    return send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True)

# main layout
app.layout = dmc.MantineProvider(
    theme=DARK_THEME,
    withGlobalClasses=True,
    children=[
        dcc.Store(id='session-store', storage_type='session'),
        dcc.Location(id='url', refresh=False),
        dmc.NotificationProvider(),
        html.Div(id='navbar-container'),
        html.Div(id='page-content', className="p-4")
    ]
)

# =============================================================================
# Main Router and Navbar Callback
# =============================================================================
@callback(Output('page-content', 'children'), Output('navbar-container', 'children'), Input('url', 'pathname'),
          State('session-store', 'data'))
def main_router_and_navbar(pathname: str, session_data: dict):
    session_data = session_data or {}
    is_authenticated = session_data.get('is_authenticated', False)
    privilege = session_data.get('privilege')
    username = session_data.get('username')

    nav_links_data = [{"href": "/", "label": "Home (Cases)"}, {"href": "/templates", "label": "Manage Templates"},
                      {"href": "/calendar", "label": "Calendar"},
                      {"href": "/dashboard", "label": "Dashboard"},
                      {"href": "/date-report", "label": "Date Range Report"}]
    if privilege == 'Admin': nav_links_data.append({"href": "/user-management", "label": "User Management"})
    nav_links = [dbc.NavItem(dbc.NavLink(link["label"], href=link["href"], active="exact")) for link in nav_links_data]

    user_menu = dmc.Menu([dmc.MenuTarget(dmc.Button(f"Welcome, {username} ({privilege})", variant="outline")),
                          dmc.MenuDropdown([dmc.MenuItem("Logout", href="/logout")])]) if is_authenticated else None

    navbar = dbc.Navbar(dbc.Container(
        [dbc.NavbarBrand("Legal Case Progress Tracker", href="/"), dbc.Nav(nav_links, navbar=True, className="ms-auto"),
         html.Div(user_menu, className="ms-3") if user_menu else None], fluid=True),
        color=DARK_THEME["colors"]["dark"][7], dark=True, className="mb-4 shadow-sm")

    if not is_authenticated:
        return build_login_layout(), navbar

    if pathname == '/logout':
        return dcc.Location(pathname="/", id="redirect-logout"), navbar
    elif pathname == '/user-management':
        return build_user_management_layout(privilege), navbar
    elif pathname == '/templates':
        return build_templates_layout(privilege), navbar
    elif pathname == '/calendar':
        return build_calendar_layout(), navbar
    elif pathname == '/dashboard':
        return build_dashboard_layout(), navbar
    elif pathname == '/date-report':
        return build_date_report_layout(), navbar
    elif pathname and pathname.startswith('/case/'):
        try:
            case_id = int(pathname.split('/')[-1])
            return build_case_detail_layout(case_id, username, privilege), navbar
        except (ValueError, IndexError):
            return dbc.Alert("Invalid case ID in URL.", color="danger"), navbar
    elif pathname == "/":
        return build_homepage_layout(privilege), navbar
    return dbc.Alert("404: Page not found.", color="danger"), navbar


# =============================================================================
# Callbacks
# =============================================================================
@callback(Output('session-store', 'data', allow_duplicate=True), Output('url', 'pathname', allow_duplicate=True),
          Output('login-alert', 'children'),
          Input('login-button', 'n_clicks'), State('login-username', 'value'), State('login-password', 'value'),
          prevent_initial_call=True)
def handle_login(n_clicks, username, password):
    if not username or not password: return dash.no_update, dash.no_update, dbc.Alert(
        "Please enter username and password", color="warning", duration=3000)
    user_data = db_get_user(username)
    if user_data and check_password(user_data['password_hash'], password):
        return {'is_authenticated': True, 'username': username, 'privilege': user_data['privilege']}, '/', None
    return dash.no_update, dash.no_update, dbc.Alert("Invalid username or password", color="danger", duration=3000)


@callback(Output('session-store', 'data', allow_duplicate=True), Input('url', 'pathname'),
          State('session-store', 'data'), prevent_initial_call=True)
def handle_logout(pathname, session_data):
    if pathname == '/logout' and (session_data or {}).get('is_authenticated'):
        return {'is_authenticated': False, 'username': None, 'privilege': None}
    raise dash.exceptions.PreventUpdate


@callback(Output("forgot-password-modal", "is_open"), Input("forgot-password-link", "n_clicks"),
          Input("close-forgot-password-modal", "n_clicks"), State("forgot-password-modal", "is_open"),
          prevent_initial_call=True)
def toggle_forgot_password_modal(n1, n2, is_open):
    if n1 or n2: return not is_open
    return is_open


@callback(Output('user-management-alert', 'children', allow_duplicate=True),
          Output('users-table', 'data', allow_duplicate=True),
          Input('add-user-button', 'n_clicks'), State('add-user-username', 'value'),
          State('add-user-password', 'value'), State('add-user-privilege', 'value'), prevent_initial_call=True)
def add_user(n_clicks, username, password, privilege):
    if not all([username, password, privilege]): return dbc.Alert("All fields are required.",
                                                                  color="warning"), dash.no_update
    if db_add_user(username, password, privilege):
        updated_users_df = pd.DataFrame(db_get_all_users())
        if not updated_users_df.empty: updated_users_df['actions'] = "Reset Password / Delete"
        return dbc.Alert(f"User '{username}' added.", color="success"), updated_users_df.to_dict('records')
    return dbc.Alert(f"Username '{username}' may already exist.", color="danger"), dash.no_update


@callback(Output('reset-password-modal', 'is_open', allow_duplicate=True),
          Output('reset-user-id-store', 'data', allow_duplicate=True),
          Output('reset-password-username-text', 'children', allow_duplicate=True),
          Output('delete-user-modal', 'is_open', allow_duplicate=True),
          Output('delete-user-id-store', 'data', allow_duplicate=True),
          Output('delete-user-confirm-text', 'children', allow_duplicate=True),
          Input('users-table', 'active_cell'),
          State('users-table', 'data'),
          prevent_initial_call=True)
def open_user_action_modals(active_cell, data):
    if not active_cell or active_cell.get('row') is None or active_cell.get(
            'column_id') != 'actions': raise dash.exceptions.PreventUpdate
    row_data = data[active_cell['row']]
    user_id, username = row_data['user_id'], row_data['username']
    return True, user_id, f"Enter new password for user: {username}", False, dash.no_update, dash.no_update


@callback(Output('user-management-alert', 'children'), Output('reset-password-modal', 'is_open', allow_duplicate=True),
          Output('reset-password-input', 'value', allow_duplicate=True), # Added allow_duplicate=True here
          Input('reset-password-save-button', 'n_clicks'), State('reset-user-id-store', 'data'),
          State('reset-password-input', 'value'), prevent_initial_call=True)
def handle_reset_password(n_clicks, user_id, new_password):
    if not new_password: return dbc.Alert("Password cannot be empty.", color="warning"), True, ""
    if db_update_user_password(user_id, new_password):
        return dbc.Alert("Password reset successfully.", color="success"), False, ""
    return dbc.Alert("Failed to reset password.", color="danger"), False, ""


@callback(Output('reset-password-modal', 'is_open', allow_duplicate=True),
          Input('reset-password-cancel-button', 'n_clicks'), prevent_initial_call=True)
def cancel_reset_password(n_clicks): return False


@callback(Output('case-list-container', 'children', allow_duplicate=True),
          Output('home-alert-container', 'children', allow_duplicate=True),
          Input('home-add-case-button', 'n_clicks'),
          State('session-store', 'data'),
          State('home-new-case-name', 'value'),
          State('home-new-case-status', 'value'),
          State('home-new-case-type', 'value'),
          prevent_initial_call=True)
def home_add_case(n_clicks, session_data, name, status, case_type):
    if not all([name, status, case_type]):
        return dash.no_update, dbc.Alert("All fields are required to add a case.", color="warning", duration=3000)

    privilege = (session_data or {}).get('privilege')
    new_case_id = db_add_case(name, status, case_type)
    db_populate_tasks_from_template(new_case_id, case_type)

    alert = dbc.Alert(f"Case '{name}' added successfully.", color="success", duration=3000)
    # Assuming build_cases_list_component is defined elsewhere in your project
    from layouts.homepage import build_cases_list_component # Added this import for context
    return build_cases_list_component(privilege), alert


@callback(
    Output('edit-case-modal', 'is_open'),
    Output('delete-case-modal', 'is_open'),
    Output('edit-case-id-store', 'data'),
    Output('delete-case-id-store', 'data'),
    Output('modal-edit-case-name', 'value'),
    Output('modal-edit-case-status', 'value'),
    Output('modal-edit-case-type', 'value'),
    Output('delete-case-confirm-text', 'children'),
    Input({'type': 'edit-case-btn', 'index': ALL}, 'n_clicks'),
    Input({'type': 'delete-case-btn', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def open_case_modals(edit_clicks, delete_clicks):
    triggered_id = ctx.triggered_id
    if not triggered_id or not any(edit_clicks) and not any(delete_clicks):
        raise dash.exceptions.PreventUpdate

    case_id = triggered_id['index']

    if 'edit-case-btn' in triggered_id['type']:
        case_info = db_fetch_single_case(case_id)
        if case_info:
            return True, False, case_id, dash.no_update, case_info['case_name'], case_info['status'], case_info[
                'case_type'], dash.no_update

    elif 'delete-case-btn' in triggered_id['type']:
        case_info = db_fetch_single_case(case_id)
        if case_info:
            text = f"Are you sure you want to delete the case '{case_info['case_name']}'? This action cannot be undone and will delete all associated tasks."
            return False, True, dash.no_update, case_id, dash.no_update, dash.no_update, dash.no_update, text

    return False, False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update


@callback(
    Output('case-list-container', 'children', allow_duplicate=True),
    Output('home-alert-container', 'children', allow_duplicate=True),
    Output('edit-case-modal', 'is_open', allow_duplicate=True),
    Input('save-edit-case-button', 'n_clicks'),
    State('session-store', 'data'),
    State('edit-case-id-store', 'data'),
    State('modal-edit-case-name', 'value'),
    State('modal-edit-case-status', 'value'),
    State('modal-edit-case-type', 'value'),
    prevent_initial_call=True
)
def save_case_edit(n_clicks, session_data, case_id, name, status, case_type):
    if not n_clicks: raise dash.exceptions.PreventUpdate
    if not all([name, status, case_type]):
        return dash.no_update, dbc.Alert("All fields are required.", color="warning"), True

    db_update_case(case_id, name, status, case_type)
    privilege = (session_data or {}).get('privilege')
    alert = dbc.Alert(f"Case '{name}' updated successfully.", color="success", duration=3000)
    # Assuming build_cases_list_component is defined elsewhere in your project
    from layouts.homepage import build_cases_list_component # Added this import for context
    return build_cases_list_component(privilege), alert, False


@callback(
    Output('case-list-container', 'children', allow_duplicate=True),
    Output('home-alert-container', 'children', allow_duplicate=True),
    Output('delete-case-modal', 'is_open', allow_duplicate=True),
    Input('confirm-delete-case-button', 'n_clicks'),
    State('session-store', 'data'),
    State('delete-case-id-store', 'data'),
    prevent_initial_call=True
)
def confirm_case_delete(n_clicks, session_data, case_id):
    if not n_clicks: raise dash.exceptions.PreventUpdate

    db_delete_case(case_id)
    privilege = (session_data or {}).get('privilege')
    alert = dbc.Alert(f"Case has been deleted.", color="danger", duration=3000)
    # Assuming build_cases_list_component is defined elsewhere in your project
    from layouts.homepage import build_cases_list_component # Added this import for context
    return build_cases_list_component(privilege), alert, False


@callback(
    Output('edit-case-modal', 'is_open', allow_duplicate=True),
    Output('delete-case-modal', 'is_open', allow_duplicate=True),
    Input('cancel-edit-case-button', 'n_clicks'),
    Input('cancel-delete-case-button', 'n_clicks'),
    prevent_initial_call=True
)
def cancel_case_modals(edit_cancel, delete_cancel):
    triggered_id = ctx.triggered_id
    if triggered_id == 'cancel-edit-case-button':
        return False, dash.no_update
    if triggered_id == 'cancel-delete-case-button':
        return dash.no_update, False
    raise dash.exceptions.PreventUpdate


@callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input({'type': 'view-case-btn', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def homepage_view_navigation(n_clicks):
    if not any(n_clicks):
        raise dash.exceptions.PreventUpdate

    case_id = ctx.triggered_id['index']
    return f"/case/{case_id}"


@callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input({'type': 'calendar-view-case-btn', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def calendar_monthly_navigation(n_clicks):
    if not any(n_clicks):
        raise dash.exceptions.PreventUpdate

    case_id = ctx.triggered_id['index']
    return f"/case/{case_id}"


@callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input({'type': 'calendar-daily-view-btn', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def calendar_daily_navigation(n_clicks):
    if not any(n_clicks):
        raise dash.exceptions.PreventUpdate

    case_id = ctx.triggered_id['index']
    return f"/case/{case_id}"


@callback(Output('url', 'pathname', allow_duplicate=True), Input('report-table', 'active_cell'),
          State('report-table', 'data'), prevent_initial_call=True)
def report_table_navigation(active_cell, table_data):
    if not active_cell or active_cell.get('row') is None or active_cell[
        'column_id'] != 'action': raise dash.exceptions.PreventUpdate
    return f"/case/{table_data[active_cell['row']]['case_id']}"


@callback(Output('detail-alert-container', 'children', allow_duplicate=True),
          Output('detail-tasks-table-container', 'children'), Output('start-date-display', 'children'),
          Output('case-due-date-display', 'children'), Output('case-completed-date-display', 'children'),
          Output('detail-case-status-dropdown', 'value'),
          Input('update-status-button', 'n_clicks'), State('detail-case-id-store', 'data'),
          State('detail-case-status-dropdown', 'value'), prevent_initial_call=True)
def update_case_status(n_clicks, case_id, new_status):
    if not new_status: return dbc.Alert("Please select a status.",
                                        color="warning"), dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    db_update_case_status_and_start_date(case_id, new_status)
    updated_case_info = db_fetch_single_case(case_id)
    new_due_date = db_fetch_case_due_date(case_id)
    # Assuming build_tasks_table_component is defined elsewhere in your project
    from layouts.case_detail import build_tasks_table_component # Added this import for context
    return (dbc.Alert("Case status updated! Dates may have been recalculated.", color="info", duration=4000),
            build_tasks_table_component(case_id),
            f"Started: {updated_case_info['start_date'].strftime('%Y-%m-%d')}" if updated_case_info.get(
                'start_date') else "Not Started Yet",
            f"Case Due: {new_due_date.strftime('%Y-%m-%d')}" if new_due_date else "",
            f"Completed: {updated_case_info['completed_date'].strftime('%Y-%m-%d')}" if updated_case_info.get(
                'completed_date') else "",
            updated_case_info['status'])


@callback(Output('edit-task-modal', 'is_open'), Output('detail-task-id-store', 'data'),
          Output('edit-task-name', 'value'), Output('edit-task-status', 'value'),
          Output('edit-task-due-date', 'value'),
          Output('edit-task-due-date-display', 'value'),
          Output('edit-task-start-date', 'value'),
          Output('edit-task-completed-date', 'value'),
          Input('detail-tasks-table', 'active_cell'), State('detail-tasks-table', 'data'), prevent_initial_call=True)
def open_edit_task_modal(active_cell, data):
    if not active_cell or active_cell.get('row') is None or active_cell.get(
            'column_id') != 'edit': raise dash.exceptions.PreventUpdate
    task_data = data[active_cell['row']]

    due_date_str = task_data.get('due_date')
    due_date_obj = date.fromisoformat(due_date_str[:10]) if due_date_str and isinstance(due_date_str, str) else None

    start_date_str = task_data.get('task_start_date')
    start_date_obj = date.fromisoformat(start_date_str[:10]) if start_date_str and isinstance(start_date_str,
                                                                                              str) else None

    completed_date_str = task_data.get('task_completed_date')
    completed_date_obj = date.fromisoformat(completed_date_str[:10]) if completed_date_str and isinstance(
        completed_date_str, str) else None

    return (True, task_data['task_id'], task_data['task_name'], task_data['status'],
            due_date_obj,
            due_date_str,
            start_date_obj,
            completed_date_obj)


@callback(Output('edit-task-modal', 'is_open', allow_duplicate=True),
          Output('detail-alert-container', 'children', allow_duplicate=True),
          Output('detail-tasks-table-container', 'children', allow_duplicate=True),
          Output('detail-case-status-dropdown', 'value', allow_duplicate=True),
          Output('case-completed-date-display', 'children', allow_duplicate=True),
          Output('start-date-display', 'children', allow_duplicate=True),
          Output('case-due-date-display', 'children', allow_duplicate=True),
          Input('save-edit-task-button', 'n_clicks'), State('session-store', 'data'),
          State('detail-task-id-store', 'data'), State('detail-case-id-store', 'data'),
          State('edit-task-name', 'value'), State('edit-task-status', 'value'), State('edit-task-due-date', 'value'),
          State('edit-task-start-date', 'value'),
          State('edit-task-completed-date', 'value'), State('detail-tasks-table', 'data'), prevent_initial_call=True)
def handle_edit_task_modal_actions(save_clicks, session_data, task_id, case_id, name, status, new_due_date, start_date,
                                   completed_date, tasks_table_data):
    if not save_clicks: raise dash.exceptions.PreventUpdate

    if not all([task_id, case_id, name, status]): return True, dbc.Alert("Task Name and Status cannot be empty.",
                                                                         color="warning"), *([dash.no_update] * 6)

    username, privilege = (session_data or {}).get('username', 'System'), (session_data or {}).get('privilege')
    original_task = next((row for row in tasks_table_data if row["task_id"] == task_id), {})
    original_task_status = original_task.get("status", "N/A")

    due_date_to_pass = new_due_date if privilege == 'Admin' else None

    final_task_status, case_started = db_update_task_details(task_id, name, status, start_date, completed_date,
                                                             due_date_to_pass, username)

    updated_case_info = db_fetch_single_case(case_id)
    case_due_date_obj = db_fetch_case_due_date(case_id)

    alert_msg = "Task updated successfully!"
    if case_started:
        alert_msg = "Task started! Case status automatically updated to 'In Progress' and all due dates have been set."
    elif updated_case_info.get('status') == 'Completed' and original_task_status != 'Completed':
        alert_msg = "All tasks completed! Case has been marked as completed."

    new_start_text = f"Started: {updated_case_info.get('start_date').strftime('%Y-%m-%d')}" if updated_case_info.get(
        'start_date') else "Not Started Yet"
    new_complete_text = f"Completed: {updated_case_info.get('completed_date').strftime('%Y-%m-%d')}" if updated_case_info.get(
        'completed_date') else ""
    new_due_text = f"Case Due: {case_due_date_obj.strftime('%Y-%m-%d')}" if case_due_date_obj else ""

    # Assuming build_tasks_table_component is defined elsewhere in your project
    from layouts.case_detail import build_tasks_table_component # Added this import for context
    return (False, dbc.Alert(alert_msg, color="success", duration=5000), build_tasks_table_component(case_id),
            updated_case_info.get('status'), new_complete_text, new_start_text, new_due_text)


@callback(Output('edit-task-modal', 'is_open', allow_duplicate=True), Input('cancel-edit-task-button', 'n_clicks'),
          prevent_initial_call=True)
def cancel_edit_task(n_clicks):
    if not n_clicks: raise dash.exceptions.PreventUpdate
    return False


@callback(Output('remarks-display-area', 'children'), Output('remark-message-textarea', 'value'),
          Output('detail-alert-container', 'children', allow_duplicate=True),
          Input('add-remark-button', 'n_clicks'), State('detail-case-id-store', 'data'),
          State('remark-user-name', 'value'), State('remark-message-textarea', 'value'), prevent_initial_call=True)
def add_remark_to_case(n_clicks, case_id, user_name, message):
    if not message or not message.strip(): return dash.no_update, "", dbc.Alert("Remark message cannot be empty.",
                                                                                color="warning", duration=3000)
    db_add_remark(case_id, user_name, message)
    # Assuming build_remarks_display_component is defined elsewhere in your project
    from layouts.case_detail import build_remarks_display_component # Added this import for context
    return build_remarks_display_component(case_id), "", dbc.Alert("Remark added.", color="success", duration=3000)


@callback(Output('tasks-for-selected-date', 'children'), Output('selected-date-header', 'children'),
          Input('interactive-calendar', 'value'))
def update_tasks_for_date(selected_date_str):
    if not selected_date_str: return [dbc.Alert("Select a date.", color="info")], "Tasks for Selected Date"
    selected_date = date.fromisoformat(selected_date_str)
    tasks_df = db_fetch_tasks_for_date(selected_date)
    header_text = f"Tasks for {selected_date.strftime('%B %d, %Y')}"
    if tasks_df.empty: return [dbc.Alert("No tasks due on this date.", color="info")], header_text
    return [dbc.Alert([html.Strong(f"{row['case_name']}: "), html.Span(row['task_name']),
                       dmc.Button("View", id={'type': 'calendar-daily-view-btn', 'index': row['case_id']},
                                  variant="subtle", size="sm", className="float-end")],
                      color="primary", className="mb-2") for _, row in tasks_df.iterrows()], header_text


@callback(Output('upcoming-overdue-tasks-table-container', 'children'),
          Output('upcoming-overdue-tasks-header', 'children'), Input('interactive-calendar', 'value'))
def update_calendar_month_table(selected_date_str):
    target_date = date.fromisoformat(selected_date_str) if selected_date_str else date.today()
    start_of_month = target_date.replace(day=1)
    end_of_month = start_of_month.replace(day=calendar.monthrange(start_of_month.year, start_of_month.month)[1])
    tasks_df = db_fetch_tasks_for_month(start_of_month, end_of_month)
    return build_calendar_tasks_table_component(tasks_df), f"Tasks for {start_of_month.strftime('%B %Y')}"


# UPDATED
@callback(Output('templates-alert-container', 'children', allow_duplicate=True),
          Output('template-type-list', 'children'),
          Output('new-template-type-name', 'value'),
          Input('add-template-type-button', 'n_clicks'),
          State('session-store', 'data'),
          State('new-template-type-name', 'value'),
          prevent_initial_call=True)
def add_template_type(n_clicks, session_data, type_name):
    if not type_name or not type_name.strip():
        return dbc.Alert("Template name cannot be empty.", color="warning"), dash.no_update, dash.no_update

    db_add_template_type(type_name)
    updated_types_df = db_fetch_template_types()
    updated_types = updated_types_df.to_dict('records') if not updated_types_df.empty else []

    privilege = (session_data or {}).get('privilege')
    is_admin = (privilege == 'Admin')

    def create_template_item(tt):
        if is_admin:
            return dbc.ListGroupItem(
                dbc.Row([
                    dbc.Col(tt['type_name'], width=9, className="d-flex align-items-center"),
                    dbc.Col(dmc.Button("Delete", id={'type': 'delete-template-btn', 'index': tt['template_type_id']},
                                       color="red", variant="subtle", size="xs"), width=3,
                            className="d-flex justify-content-end")
                ], align="center"),
                id={'type': 'template-type-item', 'index': tt['template_type_id']}, action=True
            )
        return dbc.ListGroupItem(tt['type_name'], id={'type': 'template-type-item', 'index': tt['template_type_id']},
                                 action=True)

    new_list = [create_template_item(tt) for tt in updated_types]

    return dbc.Alert(f"Template '{type_name}' added!", color="success", duration=3000), new_list, ""


@callback(Output('template-tasks-container', 'children'), Input('selected-template-type-id-store', 'data'),
          State('session-store', 'data'))
def display_template_tasks(template_id, session_data): # Added session_data as an argument here
    privilege = (session_data or {}).get('privilege')
    return build_template_tasks_container(template_id, privilege) # Assuming this function exists and takes privilege

@callback(
    Output('selected-template-type-id-store', 'data'),
    Input({'type': 'template-type-item', 'index': ALL}, 'n_clicks'),
    State({'type': 'template-type-item', 'index': ALL}, 'id'),
    prevent_initial_call=True
)
def update_selected_template(n_clicks, ids):
    if not ctx.triggered_id:
        raise dash.exceptions.PreventUpdate

    selected_template_id = ctx.triggered_id['index']
    return selected_template_id

# ===================== DASHBOARD CHART CALLBACK =====================

from dash import callback, Output, Input, State
import plotly.express as px

@callback(
    Output('case-status-pie-chart', 'figure'),
    Output('case-performance-pie-chart', 'figure'),
    Output('task-status-bar-chart', 'figure'),
    Output('task-performance-bar-chart', 'figure'),
    Output('case-performance-by-type-bar-chart', 'figure'),
    Input('dashboard-generate-button', 'n_clicks'),
    State('dashboard-from-date', 'value'),
    State('dashboard-to-date', 'value'),
    prevent_initial_call=True
)
def update_dashboard_charts(n_clicks, from_date, to_date):
    import pandas as pd
    empty_fig = px.scatter()  # fallback if no data

    # Validate input
    if not n_clicks or not from_date or not to_date:
        return [empty_fig] * 5

    # Use your dashboard data fetcher (returns cases_df, tasks_df)
    cases_df, tasks_df = _fetch_dashboard_data(
        pd.to_datetime(from_date).date(),
        pd.to_datetime(to_date).date()
    )

    # 1. Case Status Pie
    case_status_fig = (px.pie(cases_df, names='status', title='') if not cases_df.empty else empty_fig)

    # 2. Case Performance Pie
    case_perf_fig = (px.pie(cases_df, names='performance', title='') if not cases_df.empty else empty_fig)

    # 3. Task Status Bar
    task_status_fig = (px.histogram(tasks_df, x='status', title='') if not tasks_df.empty else empty_fig)

    # 4. Task Performance Bar
    task_perf_fig = (px.histogram(tasks_df, x='performance', title='') if not tasks_df.empty else empty_fig)

    # 5. Case Performance by Type Bar
    if not cases_df.empty and 'case_type' in cases_df and 'performance' in cases_df:
        grouped = cases_df.groupby(['case_type', 'performance']).size().reset_index(name='count')
        bytype_fig = px.bar(grouped, x='case_type', y='count', color='performance', barmode='group', title='')
    else:
        bytype_fig = empty_fig

    return case_status_fig, case_perf_fig, task_status_fig, task_perf_fig, bytype_fig

#Date Range Report Callback

from dash import callback, Output, Input, State, dash_table, html
import pandas as pd
from utils.styles import DATATABLE_STYLE_DARK  # Use your dark style

@callback(
    Output('report-output-container', 'children'),
    Input('report-generate-button', 'n_clicks'),
    State('report-type-dropdown', 'value'),
    State('report-from-date', 'value'),
    State('report-to-date', 'value'),
    prevent_initial_call=True
)
def generate_date_range_report(n_clicks, report_type, from_date, to_date):
    if not n_clicks or not report_type or not from_date or not to_date:
        return html.Div("Please select report type and date range.", style={"color": "orange"})

    from db.queries import db_fetch_affected_cases_report, db_fetch_affected_tasks_report

    from_date = pd.to_datetime(from_date).date()
    to_date = pd.to_datetime(to_date).date()

    if report_type == "Cases":
        df = db_fetch_affected_cases_report(from_date, to_date)
    else:
        df = db_fetch_affected_tasks_report(from_date, to_date)

    if df.empty:
        return html.Div("No data found for this period.", style={"color": "orange"})

    # Add action column if available
    if "case_id" in df.columns:
        df["action"] = "View"

    columns = [{"name": c.replace("_", " ").title(), "id": c} for c in df.columns]

    # Make a local copy of the dark style, and add the underline for 'action'
    datatable_style = DATATABLE_STYLE_DARK.copy()
    datatable_style['style_cell_conditional'] = datatable_style.get('style_cell_conditional', []) + [
        {"if": {"column_id": "action"}, "color": "#58a6ff", "textDecoration": "underline", "cursor": "pointer"},
    ]

    return dash_table.DataTable(
        id='report-table',
        columns=columns,
        data=df.to_dict("records"),
        page_size=20,
        **datatable_style
    )
# ===================== ATTACHMENTS MODAL CALLBACKS (FULL SECTION) =====================

from dash import callback, Output, Input, State, ctx, ALL, no_update
import os
import base64
import uuid

# Make sure this import path matches your project!
from layouts.case_detail import build_attachments_list

UPLOAD_DIRECTORY = "uploads"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# 1. Open the modal when Attachments cell is clicked
@callback(
    Output("attachment-modal", "is_open"),
    Output("attachment-task-id-store", "data"),
    Input("detail-tasks-table", "active_cell"),
    State("detail-tasks-table", "data"),
    prevent_initial_call=True,
)
def open_attachments_modal(active_cell, data):
    if not active_cell or not data or active_cell.get('row') is None or active_cell.get('column_id') != 'attachments':
        raise dash.exceptions.PreventUpdate
    task_id = data[active_cell['row']]['task_id']
    return True, task_id

# 2. Close the modal when Close button is clicked
@callback(
    Output("attachment-modal", "is_open", allow_duplicate=True),
    Input("close-attachment-modal", "n_clicks"),
    prevent_initial_call=True
)
def close_attachment_modal(n_clicks):
    if n_clicks:
        return False
    raise dash.exceptions.PreventUpdate

# 3. Handle BOTH:
#    - Showing current attachments on open
#    - Uploading files, then showing updated list
@callback(
    Output('existing-attachments-area', 'children', allow_duplicate=True),
    Input('attachment-modal', 'is_open'),
    Input('upload-attachment', 'contents'),
    State('upload-attachment', 'filename'),
    State('attachment-task-id-store', 'data'),
    State('session-store', 'data'),
    prevent_initial_call=True
)
def update_attachments_area(modal_open, upload_contents, upload_filenames, task_id, session_data):
    # 1. Handle file upload if triggered by upload
    if ctx.triggered_id == 'upload-attachment' and upload_contents and upload_filenames:
        if not isinstance(upload_filenames, list):
            upload_contents = [upload_contents]
            upload_filenames = [upload_filenames]
        uploaded_by = (session_data or {}).get('username', 'System')
        for content, filename in zip(upload_contents, upload_filenames):
            content_type, content_string = content.split(',')
            decoded = base64.b64decode(content_string)
            ext = filename.split('.')[-1]
            stored_filename = f"{uuid.uuid4().hex}.{ext}"
            file_path = os.path.join(UPLOAD_DIRECTORY, stored_filename)
            with open(file_path, "wb") as f:
                f.write(decoded)
            # Assumes db_add_attachment is in your app file or imported!
            db_add_attachment(task_id, filename, stored_filename, uploaded_by)

    # 2. Always refresh list if modal open and task_id present
    if modal_open and task_id:
        return build_attachments_list(task_id)
    return no_update

# 4. Handle deleting an attachment, then refresh the list
@callback(
    Output("existing-attachments-area", "children", allow_duplicate=True),
    Input({'type': 'delete-attachment-btn', 'index': ALL}, 'n_clicks'),
    State("attachment-task-id-store", "data"),
    prevent_initial_call=True,
)
def handle_delete_attachment(n_clicks_list, task_id):
    if not any(n_clicks_list):
        raise dash.exceptions.PreventUpdate
    triggered = ctx.triggered_id
    if triggered and isinstance(triggered, dict) and 'index' in triggered:
        attachment_id = triggered['index']
        db_delete_attachment(attachment_id)
    return build_attachments_list(task_id)



if __name__ == '__main__':
    app.run(debug=True, port=8050)
