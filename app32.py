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
from sqlalchemy import text

if os.environ.get("RESET_DB") == "1":
    # DANGEROUS: Drops all tables, constraints, everything in schema "public"
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE"))
        conn.execute(text("CREATE SCHEMA public"))
        conn.commit()
    print("All tables dropped (CASCADE) and recreated schema!")
    Base.metadata.create_all(engine)

from auth import db_add_user
from db.connection import get_db_connection
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
# (All your other callbacks: login/logout, home, cases, tasks, attachments, dashboard, report, etc. — keep as is)
# =============================================================================

# --------------------------------------------------------------------------
# ======================== TEMPLATES CALLBACK SECTION =======================
# --------------------------------------------------------------------------

@callback(
    Output('templates-alert-container', 'children', allow_duplicate=True),
    Output('template-type-list', 'children'),
    Output('new-template-type-name', 'value'),
    Input('add-template-type-button', 'n_clicks'),
    State('session-store', 'data'),
    State('new-template-type-name', 'value'),
    prevent_initial_call=True
)
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

# ----------- UNIFIED template-tasks-container CALLBACK! -----------

@callback(
    Output('template-tasks-container', 'children'),
    Output('templates-alert-container', 'children',allow_duplicate=True),
    Output('new-task-seq', 'value'),
    Output('new-task-name', 'value'),
    Output('new-task-status', 'value'),
    Output('new-task-offset', 'value'),
    Output('new-task-documents', 'value'),
    Input('add-task-to-template-button', 'n_clicks'),
    Input('selected-template-type-id-store', 'data'),
    Input('template-tasks-table', 'active_cell'),
    State('template-tasks-table', 'data'),
    State('new-task-seq', 'value'),
    State('new-task-name', 'value'),
    State('new-task-status', 'value'),
    State('new-task-offset', 'value'),
    State('new-task-documents', 'value'),
    State('session-store', 'data'),
    prevent_initial_call=True
)
def unified_template_tasks_callback(
    add_task_n_clicks,
    selected_template_id,
    active_cell,
    tasks_data,
    seq, name, status, offset, documents,
    session_data
):
    # Default return values
    default = (dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update)
    privilege = (session_data or {}).get('privilege')
    alert = None
    triggered_id = ctx.triggered_id

    # --- 1. Handle ADD TASK ---
    if triggered_id == 'add-task-to-template-button':
        if not all([selected_template_id, seq, name, status]):
            return (
                dash.no_update,
                dbc.Alert("Please fill in all required fields.", color="warning"),
                dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
            )
        db_add_task_to_template(selected_template_id, seq, name, status, offset, documents)
        alert = dbc.Alert(f"Task '{name}' added to template.", color="success", duration=2500)
        # Reset input fields
        return (
            build_template_tasks_container(selected_template_id, privilege),
            alert,
            None, "", "Not Started", None, ""
        )

    # --- 2. Handle DELETE TASK (in table) ---
    if triggered_id == 'template-tasks-table' and active_cell and active_cell.get('row') is not None and active_cell.get('column_id') == 'delete':
        task_row = tasks_data[active_cell['row']]
        task_id = task_row.get('task_id')
        if task_id:
            db_delete_task_from_template(task_id)
            alert = dbc.Alert("Task deleted from template.", color="danger", duration=2000)
        return (
            build_template_tasks_container(selected_template_id, privilege),
            alert,
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
        )

    # --- 3. Handle TEMPLATE TYPE SELECTION (just viewing) ---
    if triggered_id == 'selected-template-type-id-store':
        return (
            build_template_tasks_container(selected_template_id, privilege),
            None,
            dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
        )

    # Fallback: Do nothing
    return default

# --------------------------------------------------------------------------
# ======================== END TEMPLATES CALLBACK SECTION ===================
# --------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=8050)
