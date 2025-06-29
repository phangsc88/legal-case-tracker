# app.py — FINAL, COMPLETE VERSION
# (UPDATED: DB Initialization and Admin Creation)

import os
import uuid
import base64
import calendar
from datetime import date, datetime, timedelta
from typing import List, Dict, Any, Optional, Tuple

import pandas as pd
import dash
from dash import dcc, html, dash_table, Input, Output, State, ctx, ALL
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.express as px
from flask import send_from_directory
from sqlalchemy import text
from layouts.templates import build_template_tasks_container

# --- Database & Auth Helpers ---
from db.connection import get_db_connection, engine
from models import Base
from auth import (
    db_add_user, db_get_user, db_get_all_users,
    db_update_user_password, db_delete_user, check_password
)
from db.queries import (
    db_fetch_all_cases, db_add_case, db_populate_tasks_from_template,
    db_update_case, db_delete_case, db_fetch_single_case,
    db_fetch_case_due_date, db_fetch_tasks_for_case,
    db_fetch_tasks_for_date, db_fetch_tasks_for_month,
    db_add_remark, db_update_task_details, db_update_case_status_and_start_date,
    db_fetch_template_types, db_add_template_type, db_delete_template_type,
    db_fetch_tasks_for_template,
    db_add_task_to_template, db_delete_task_from_template, db_update_task_template,
    db_fetch_affected_cases_report, db_fetch_affected_tasks_report,
    _fetch_dashboard_data, db_fetch_remarks_for_case,
    db_add_attachment, db_delete_attachment, db_fetch_attachments_for_task
)

# --- Styling & Layout Components ---
from utils.styles import DARK_THEME, DATATABLE_STYLE_DARK
from layouts.login import build_login_layout
# from layouts.user_management import build_user_management_layout <-- Defining locally
from layouts.homepage import build_homepage_layout, build_cases_list_component
# from layouts.templates import build_templates_layout <-- Defining locally
from layouts.calendar import build_calendar_layout, build_calendar_tasks_table_component
from layouts.dashboard import build_dashboard_layout
from layouts.reports import build_date_report_layout
from layouts.case_detail import build_attachments_list


# =============================================================================
# --- START: NEW DB INITIALIZATION & ADMIN CREATION (FROM RENDERS VERSION) ---
# =============================================================================
Base.metadata.create_all(engine)

# DANGEROUS: This feature allows for a full database reset for development purposes.
# To use, set an environment variable: RESET_DB=1
if os.environ.get("RESET_DB") == "1":
    print("⚠️ WARNING: RESET_DB environment variable is set.")
    print("Dropping and recreating the 'public' schema...")
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE"))
        conn.execute(text("CREATE SCHEMA public"))
        conn.commit()
    print("✅ Schema dropped and recreated successfully.")
    # Recreate tables in the new schema
    Base.metadata.create_all(engine)
    print("✅ All tables recreated.")

def ensure_default_admin():
    """Creates a default administrator user if no users exist in the database."""
    with get_db_connection() as conn:
        user_count = conn.execute(text("SELECT COUNT(*) FROM users")).scalar()
        if user_count == 0:
            print("No users found. Creating default admin...")
            created = db_add_user(
                username="admin",
                password="1234",
                privilege="Admin"
            )
            if created:
                print("✅ Default admin created successfully:")
                print("   - Username: 'admin'")
                print("   - Password: '1234'")
                print("\n**SECURITY WARNING: Change this password immediately after first login!**\n")
            else:
                print("❌ Failed to create default admin. An error occurred or the user already exists.")

# Run the function to ensure the admin exists on startup
ensure_default_admin()
# =============================================================================
# --- END: NEW DB INITIALIZATION & ADMIN CREATION ---
# =============================================================================


# --- Dash App Setup ---
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server
UPLOAD_DIRECTORY = "uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


# --- File Serving Endpoints ---
@server.route('/files/view/<filename>')
def serve_view(filename):
    return send_from_directory(UPLOAD_DIRECTORY, filename)


@server.route('/files/download/<filename>')
def serve_download(filename):
    return send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True)


# =============================================================================
# LAYOUT FUNCTIONS (Defined locally for a self-contained script)
# =============================================================================
def build_user_management_layout(privilege: str):
    if privilege != 'Admin': return dbc.Alert("You do not have permission to access this page.", color="danger")
    users_df = pd.DataFrame(db_get_all_users())
    users_df['actions'] = "Reset Password / Delete" if not users_df.empty else ""
    return html.Div([
        html.H2("User Management"), html.Div(id='user-management-alert'),
        dbc.Card(dbc.CardBody([
            html.H4("Add New User"),
            dbc.Row([
                dbc.Col(dmc.TextInput(placeholder='Username', id='add-user-username'), md=3),
                dbc.Col(dmc.PasswordInput(placeholder='Password', id='add-user-password'), md=3),
                dbc.Col(dmc.Select(data=['Admin', 'User'], value='User', id='add-user-privilege'), md=3),
                dbc.Col(dmc.Button('Add User', id='add-user-button'), md=3, className="align-self-end")
            ])
        ]), className='mb-4'),
        html.H4("Existing Users"),
        dash_table.DataTable(id='users-table',
                             columns=[{'name': c.replace('_', ' ').title(), 'id': c} for c in ['username', 'privilege', 'created_at', 'actions']],
                             data=users_df.to_dict('records'), **DATATABLE_STYLE_DARK,
                             style_cell_conditional=[{'if': {'column_id': 'actions'}, 'cursor': 'pointer', 'textDecoration': 'underline', 'color': DARK_THEME["colors"]["blue"][5]}]),
        dbc.Modal([dbc.ModalHeader(dbc.ModalTitle("Reset User Password")),
                   dbc.ModalBody([dcc.Store(id='reset-user-id-store'), html.P(id='reset-password-username-text'), dmc.PasswordInput(id='reset-password-input')]),
                   dbc.ModalFooter(dmc.Group([dmc.Button("Cancel", id='reset-password-cancel-button', variant="outline"), dmc.Button("Save New Password", id='reset-password-save-button')]))
                   ], id='reset-password-modal', is_open=False, centered=True),
        dbc.Modal([dbc.ModalHeader(dbc.ModalTitle("Confirm Deletion")),
                   dbc.ModalBody([dcc.Store(id='delete-user-id-store'), html.P(id='delete-user-confirm-text')]),
                   dbc.ModalFooter(dmc.Group([dmc.Button("Cancel", id='delete-user-cancel-button', variant="outline"), dmc.Button("DELETE USER", id='delete-user-confirm-button', color='red')]))
                   ], id='delete-user-modal', is_open=False, centered=True)
    ])

def build_template_type_list_items(privilege: str):
    template_types_df = db_fetch_template_types()
    template_types = template_types_df.to_dict('records') if not template_types_df.empty else []
    is_admin = (privilege == 'Admin')
    items = []
    for tt in template_types:
        item_row = dbc.Row([
            dbc.Col(dbc.ListGroupItem(tt['type_name'], id={'type': 'template-type-item', 'index': tt['template_type_id']}, action=True, className="border-0")),
            dbc.Col(dmc.Button("Delete", id={'type': 'delete-template-type-btn', 'index': tt['template_type_id']}, color="red", variant="subtle", size="xs", className="float-end"), width="auto", className="d-flex align-items-center") if is_admin else None,
        ], align="center", justify="between")
        items.append(item_row)
    return items

def build_templates_layout(privilege: str):
    is_admin = (privilege == 'Admin')
    return html.Div([
        dcc.Store(id='selected-template-type-id-store'), dcc.Store(id='template-to-delete-store'),
        html.H2("Manage Task Templates"), html.Div(id='templates-alert-container'),
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody([
                html.H4("Template Types"),
                dbc.ListGroup(id='template-type-list', children=build_template_type_list_items(privilege)),
                html.Hr(),
                dbc.InputGroup([dbc.Input(id='new-template-type-name', placeholder="New Template Name...", disabled=not is_admin), dbc.Button("Add Type", id='add-template-type-button', color="success", disabled=not is_admin)])
            ])), width=4),
            dbc.Col(html.Div(id='template-tasks-container', children=html.P("Select a template type to see its tasks.")), width=8)
        ]),
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Confirm Deletion")), dbc.ModalBody("Are you sure you want to delete this template and ALL of its associated tasks? This action cannot be undone."),
            dbc.ModalFooter(dmc.Group([dmc.Button("Cancel", id="cancel-delete-template-btn", variant="outline"), dmc.Button("DELETE TEMPLATE", id="confirm-delete-template-btn", color="red")]))
        ], id='delete-template-confirm-modal', is_open=False, centered=True)
    ])

def build_tasks_table_component(case_id: int, privilege: str):
    tasks_df = db_fetch_tasks_for_case(case_id)
    if not tasks_df.empty:
        attachment_counts = [len(db_fetch_attachments_for_task(task_id)) for task_id in tasks_df['task_id']]
        tasks_df['attachments'] = [f"{count} file(s)" for count in attachment_counts]
        tasks_df['action'] = "Edit"
    else:
        tasks_df = tasks_df.assign(attachments=[], action=[])
    columns_to_display = [{"name": "Task Name", "id": "task_name"}, {"name": "Status", "id": "status"}, {"name": "Performance", "id": "performance"}, {"name": "Attachments", "id": "attachments"}, {"name": "Documents Required", "id": "documents_required"}, {"name": "Due Date", "id": "due_date_display"}, {"name": "Start Date", "id": "task_start_date"}, {"name": "Completed Date", "id": "task_completed_date"}, {"name": "Last Updated By", "id": "last_updated_by"}, {"name": "Action", "id": "action"}]
    style_cell_conditional=[{'if': {'column_id': 'action'}, 'cursor': 'pointer', 'textDecoration': 'underline', 'color': DARK_THEME["colors"]["blue"][5]}, {'if': {'column_id': 'attachments'}, 'cursor': 'pointer', 'textDecoration': 'underline', 'color': DARK_THEME["colors"]["blue"][3]}]
    return dash_table.DataTable(id='detail-tasks-table', columns=columns_to_display, data=tasks_df.to_dict('records'), **DATATABLE_STYLE_DARK, style_cell_conditional=style_cell_conditional)

def build_remarks_display_component(case_id: int):
    remarks_df = db_fetch_remarks_for_case(case_id)
    if remarks_df.empty: return html.P("No remarks yet.", className="text-muted")
    return [dbc.Card(dbc.CardBody([dmc.Text(f"By {row['user_name']} on {row['timestamp']}", size="xs", c="dimmed"), dmc.Text(row['message'], c="dark.0")]), className="mb-2", style={"backgroundColor": DARK_THEME['colors']['dark'][6]}) for _, row in remarks_df.iterrows()]

def build_case_detail_layout(case_id: int, username: str, privilege: str):
    case_info = db_fetch_single_case(case_id)
    if not case_info: return dbc.Alert(f"Case with ID {case_id} not found.", color="danger")
    due_date, start_date_text = db_fetch_case_due_date(case_id), f"Started: {case_info['start_date']}" if case_info.get('start_date') else "Not Started Yet"
    completed_date_text, case_due_date_text = f"Completed: {case_info['completed_date']}" if case_info.get('completed_date') else "", f"Case Due: {due_date}" if due_date else ""
    is_user_role = (privilege == 'User')
    return html.Div([
        dcc.Store(id='detail-case-id-store', data=case_id), dcc.Store(id='detail-task-id-store'), dcc.Store(id='attachment-task-id-store'),
        html.Div(id='detail-alert-container'),
        dbc.Card(dbc.CardBody([
            dbc.Row([
                dbc.Col([html.H2(case_info['case_name'], id="detail-case-name"), html.H5(f"Type: {case_info['case_type']}", className="text-muted"), html.H5(start_date_text, className="text-info", id='start-date-display'), html.H5(case_due_date_text, className="text-warning", id='case-due-date-display'), html.H5(completed_date_text, className="text-success", id='case-completed-date-display')], width=8),
                dbc.Col([dmc.Text("Change Case Status:", size="sm"), dmc.Select(id='detail-case-status-dropdown', data=['Not Started', 'In Progress', 'On Hold', 'Completed'], value=case_info['status']), dmc.Button("Update Status", id='update-status-button', fullWidth=True, mt="md")], width=4)
            ])
        ])),
        html.H3("Tasks", className="text-center my-4"), html.Div(id='detail-tasks-table-container', children=build_tasks_table_component(case_id, privilege)),
        dbc.Modal([
            dbc.ModalHeader("Edit Task"),
            dbc.ModalBody([
                dmc.TextInput(label="Task Name:", id='edit-task-name'),
                dmc.Select(label="Status:", id='edit-task-status', data=['Not Started', 'In Progress', 'On Hold', 'Completed'], mt="sm"),
                dmc.TextInput(label="Documents Required:", id='edit-task-documents', disabled=True, mt="sm"),
                html.Div([
                    dmc.Text("Task Start Date:", size="sm"),
                    dmc.DatePicker(id='edit-task-start-date', style={"width": "100%"})
                ], className="mt-2"),
                html.Div([
                    dmc.Text("Task Completed Date:", size="sm"),
                    dmc.DatePicker(id='edit-task-completed-date', style={"width": "100%"})
                ], className="mt-2"),
                html.Div([
                    dmc.Text("Due Date:", size="sm", mt="sm"),
                    dmc.DatePicker(id='edit-task-due-date', style={"width": "100%", "display": "none" if is_user_role else "block"}),
                    dmc.TextInput(id='edit-task-due-date-display', disabled=True, style={"width": "100%", "display": "block" if is_user_role else "none"}),
                    dmc.Text("Due dates can only be changed by Admins.", size="xs", c="dimmed") if is_user_role else None
                ]),
            ]),
            dbc.ModalFooter(dmc.Group([dmc.Button("Cancel", id="cancel-edit-task-button", variant="outline"), dmc.Button("Save Changes", id="save-edit-task-button")]))
        ], id='edit-task-modal', is_open=False, centered=True),
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle(id="attachment-modal-title")),
            dbc.ModalBody([
                dbc.Card(dbc.CardBody([html.H5("Upload New File"), dcc.Upload(id='upload-attachment', children=html.Div(['Drag and Drop or ', html.A('Select Files')]), style={'width': '100%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px 0'}, multiple=True)])),
                html.Hr(), html.H5("Existing Attachments"), html.Div(id='attachment-list-container')
            ]),
            dbc.ModalFooter(dmc.Button("Close", id="close-attachment-modal", variant="outline"))
        ], id='attachment-modal', is_open=False, centered=True, size="lg"),
        html.Hr(className="my-4"),
        dbc.Card(dbc.CardBody([
            html.H4("Case Remarks", className="card-title mb-3"),
            dbc.Row([
                dbc.Col(dmc.TextInput(value=username, disabled=True, id='remark-user-name'), md=3),
                dbc.Col(dmc.Textarea(placeholder="Enter remark...", autosize=True, minRows=2, id='remark-message-textarea'), md=7),
                dbc.Col(dmc.Button("Add Remark", id='add-remark-button', fullWidth=True), md=2, className="align-self-end")
            ]),
            html.Div(id='remarks-display-area', className="mt-3", children=build_remarks_display_component(case_id))
        ]))
    ])

# =============================================================================
# MAIN APP AND CALLBACKS
# =============================================================================

app.layout = dmc.MantineProvider(theme=DARK_THEME, withGlobalClasses=True, children=[
    dcc.Store(id='session-store', storage_type='session'), dcc.Location(id='url', refresh=False),
    dmc.NotificationProvider(), html.Div(id='navbar-container'), html.Div(id='page-content', className='p-4'),
])

# ... (The rest of the callbacks remain exactly the same as the original working version) ...

@app.callback(Output('page-content', 'children'), Output('navbar-container', 'children'), Input('url', 'pathname'), State('session-store', 'data'))
def main_router_and_navbar(pathname, session_data):
    session_data = session_data or {}; is_authenticated = session_data.get('is_authenticated', False)
    privilege = session_data.get('privilege'); username = session_data.get('username')
    links = [{"href": "/", "label": "Home"}, {"href": "/templates", "label": "Manage Templates"}, {"href": "/calendar", "label": "Calendar"}, {"href": "/dashboard", "label": "Dashboard"}, {"href": "/date-report", "label": "Reports"}]
    if privilege == 'Admin': links.append({"href": "/user-management", "label": "Users"})
    nav_items = [dbc.NavItem(dbc.NavLink(link["label"], href=link["href"], active="exact")) for link in links]
    user_menu = dmc.Menu([dmc.MenuTarget(dmc.Button(f"{username} ({privilege})", variant="outline")), dmc.MenuDropdown([dmc.MenuItem("Logout", href="/logout")])]) if is_authenticated else None
    navbar = dbc.Navbar(dbc.Container([dbc.NavbarBrand("Legal Case Tracker", href="/"), dbc.Nav(nav_items, navbar=True, className="ms-auto"), html.Div(user_menu, className="ms-3") if user_menu else None]), color=DARK_THEME["colors"]["dark"][7], dark=True, className="mb-4")
    if not is_authenticated: return build_login_layout(), navbar
    if pathname == '/logout': return dcc.Location(pathname="/", id="redirect-logout"), navbar
    route_map = {'/user-management': lambda: build_user_management_layout(privilege), '/templates': lambda: build_templates_layout(privilege), '/calendar': build_calendar_layout, '/dashboard': build_dashboard_layout, '/date-report': build_date_report_layout}
    if pathname in route_map: return route_map[pathname](), navbar
    if pathname and pathname.startswith('/case/'):
        try: case_id = int(pathname.split('/')[-1]); return build_case_detail_layout(case_id, username, privilege), navbar
        except (ValueError, IndexError): return dbc.Alert("Invalid case ID in URL.", color="danger"), navbar
    return build_homepage_layout(privilege), navbar

# ─── Authentication, Navigation, and Login Callbacks ────────────────────────
@app.callback(Output('session-store', 'data', allow_duplicate=True), Output('url', 'pathname', allow_duplicate=True), Output('login-alert', 'children'), Input('login-button', 'n_clicks'), State('login-username', 'value'), State('login-password', 'value'), prevent_initial_call=True)
def handle_login(n_clicks, username, password):
    if not username or not password: return dash.no_update, dash.no_update, dbc.Alert("Please enter username and password", color="warning")
    user_data = db_get_user(username)
    if user_data and check_password(user_data['password_hash'], password): return {'is_authenticated': True, 'username': username, 'privilege': user_data['privilege']}, '/', None
    return dash.no_update, dash.no_update, dbc.Alert("Invalid username or password", color="danger")

@app.callback(Output('session-store', 'data', allow_duplicate=True), Input('url', 'pathname'), State('session-store', 'data'), prevent_initial_call=True)
def handle_logout(pathname, session_data):
    if pathname == '/logout' and (session_data or {}).get('is_authenticated'): return {'is_authenticated': False, 'username': None, 'privilege': None}
    raise PreventUpdate

@app.callback(Output("forgot-password-modal", "is_open"), Input("forgot-password-link", "n_clicks"), Input("close-forgot-password-modal", "n_clicks"), State("forgot-password-modal", "is_open"), prevent_initial_call=True)
def toggle_forgot_password_modal(n1, n2, is_open):
    if n1 or n2: return not is_open
    return is_open

@app.callback(Output('url', 'pathname', allow_duplicate=True), Input({'type': 'view-case-btn', 'index': ALL}, 'n_clicks'), prevent_initial_call=True)
def navigate_to_case_detail(n_clicks):
    if not any(n_clicks): raise PreventUpdate
    return f"/case/{ctx.triggered_id['index']}"

@app.callback(Output('url', 'pathname', allow_duplicate=True), Input({'type': 'calendar-view-case-btn', 'index': ALL}, 'n_clicks'), prevent_initial_call=True)
def calendar_monthly_navigation(n_clicks):
    if not any(n_clicks): raise PreventUpdate
    return f"/case/{ctx.triggered_id['index']}"

@app.callback(Output('url', 'pathname', allow_duplicate=True), Input({'type': 'calendar-daily-view-btn', 'index': ALL}, 'n_clicks'), prevent_initial_call=True)
def calendar_daily_navigation(n_clicks):
    if not any(n_clicks): raise PreventUpdate
    return f"/case/{ctx.triggered_id['index']}"

@app.callback(Output('url', 'pathname', allow_duplicate=True), Input('report-table', 'active_cell'), State('report-table', 'data'), prevent_initial_call=True)
def navigate_from_report(active_cell, table_data):
    if not active_cell or active_cell['column_id'] != 'action': raise PreventUpdate
    return f"/case/{table_data[active_cell['row']]['case_id']}"

# ─── User Management Callbacks ──────────────────────────────────────────────
@app.callback(Output('user-management-alert', 'children', allow_duplicate=True), Output('users-table', 'data', allow_duplicate=True), Input('add-user-button', 'n_clicks'), State('add-user-username', 'value'), State('add-user-password', 'value'), State('add-user-privilege', 'value'), prevent_initial_call=True)
def add_user(n_clicks, username, password, privilege):
    if not all([username, password, privilege]): return dbc.Alert("All fields are required.", color="warning"), dash.no_update
    if db_add_user(username, password, privilege):
        updated_users_df = pd.DataFrame(db_get_all_users())
        if not updated_users_df.empty: updated_users_df['actions'] = "Reset Password / Delete"
        return dbc.Alert(f"User '{username}' added.", color="success"), updated_users_df.to_dict('records')
    return dbc.Alert(f"Username '{username}' may already exist.", color="danger"), dash.no_update

@app.callback(Output('reset-password-modal', 'is_open'), Output('reset-user-id-store', 'data'), Output('reset-password-username-text', 'children'), Output('delete-user-modal', 'is_open'), Output('delete-user-id-store', 'data'), Output('delete-user-confirm-text', 'children'), Input('users-table', 'active_cell'), State('users-table', 'data'), prevent_initial_call=True)
def open_user_action_modals(active_cell, data):
    if not active_cell or active_cell.get('row') is None or active_cell.get('column_id') != 'actions': raise PreventUpdate
    row_data = data[active_cell['row']]; user_id, username = row_data['user_id'], row_data['username']
    return True, user_id, f"Enter new password for user: {username}", False, dash.no_update, dash.no_update

@app.callback(Output('user-management-alert', 'children'), Output('reset-password-modal', 'is_open', allow_duplicate=True), Output('reset-password-input', 'value'), Input('reset-password-save-button', 'n_clicks'), State('reset-user-id-store', 'data'), State('reset-password-input', 'value'), prevent_initial_call=True)
def handle_reset_password(n_clicks, user_id, new_password):
    if not new_password: return dbc.Alert("Password cannot be empty.", color="warning"), True, ""
    if db_update_user_password(user_id, new_password): return dbc.Alert("Password reset successfully.", color="success"), False, ""
    return dbc.Alert("Failed to reset password.", color="danger"), False, ""

@app.callback(Output('reset-password-modal', 'is_open', allow_duplicate=True), Input('reset-password-cancel-button', 'n_clicks'), prevent_initial_call=True)
def cancel_reset_password(n_clicks): return False

# ─── Homepage & Case CRUD Callbacks ─────────────────────────────────────────
@app.callback(Output('case-list-container', 'children', allow_duplicate=True), Output('home-alert-container', 'children', allow_duplicate=True), Input('home-add-case-button', 'n_clicks'), State('session-store', 'data'), State('home-new-case-name', 'value'), State('home-new-case-status', 'value'), State('home-new-case-type', 'value'), prevent_initial_call=True)
def home_add_case(n_clicks, session_data, name, status, case_type):
    if not all([name, status, case_type]): return dash.no_update, dbc.Alert("All fields are required to add a case.", color="warning")
    new_case_id = db_add_case(name, status, case_type); db_populate_tasks_from_template(new_case_id, case_type)
    return build_cases_list_component(session_data.get('privilege')), dbc.Alert(f"Case '{name}' added successfully.", color="success")

@app.callback(Output('edit-case-modal', 'is_open'), Output('delete-case-modal', 'is_open'), Output('edit-case-id-store', 'data'), Output('delete-case-id-store', 'data'), Output('modal-edit-case-name', 'value'), Output('modal-edit-case-status', 'value'), Output('modal-edit-case-type', 'value'), Output('delete-case-confirm-text', 'children'), Input({'type': 'edit-case-btn', 'index': ALL}, 'n_clicks'), Input({'type': 'delete-case-btn', 'index': ALL}, 'n_clicks'), prevent_initial_call=True)
def open_case_modals(edit_clicks, delete_clicks):
    if not ctx.triggered_id or (not any(edit_clicks) and not any(delete_clicks)): raise PreventUpdate
    case_id = ctx.triggered_id['index']; case_info = db_fetch_single_case(case_id)
    if 'edit-case-btn' in ctx.triggered_id['type'] and case_info: return True, False, case_id, dash.no_update, case_info['case_name'], case_info['status'], case_info['case_type'], dash.no_update
    elif 'delete-case-btn' in ctx.triggered_id['type'] and case_info: return False, True, dash.no_update, case_id, dash.no_update, dash.no_update, dash.no_update, f"Delete '{case_info['case_name']}'? This will delete all associated tasks."
    return False, False, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

@app.callback(Output('case-list-container', 'children', allow_duplicate=True), Output('home-alert-container', 'children', allow_duplicate=True), Output('edit-case-modal', 'is_open', allow_duplicate=True), Input('save-edit-case-button', 'n_clicks'), State('session-store', 'data'), State('edit-case-id-store', 'data'), State('modal-edit-case-name', 'value'), State('modal-edit-case-status', 'value'), State('modal-edit-case-type', 'value'), prevent_initial_call=True)
def save_case_edit(n_clicks, session_data, case_id, name, status, case_type):
    if not all([name, status, case_type]): return dash.no_update, dbc.Alert("All fields are required.", color="warning"), True
    db_update_case(case_id, name, status, case_type)
    return build_cases_list_component(session_data.get('privilege')), dbc.Alert(f"Case '{name}' updated.", color="success"), False

@app.callback(Output('case-list-container', 'children', allow_duplicate=True), Output('home-alert-container', 'children', allow_duplicate=True), Output('delete-case-modal', 'is_open', allow_duplicate=True), Input('confirm-delete-case-button', 'n_clicks'), State('session-store', 'data'), State('delete-case-id-store', 'data'), prevent_initial_call=True)
def confirm_case_delete(n_clicks, session_data, case_id):
    db_delete_case(case_id)
    return build_cases_list_component(session_data.get('privilege')), dbc.Alert("Case has been deleted.", color="danger"), False

@app.callback(Output('edit-case-modal', 'is_open', allow_duplicate=True), Output('delete-case-modal', 'is_open', allow_duplicate=True), Input('cancel-edit-case-button', 'n_clicks'), Input('cancel-delete-case-button', 'n_clicks'), prevent_initial_call=True)
def cancel_case_modals(edit_cancel, delete_cancel):
    if ctx.triggered_id == 'cancel-edit-case-button': return False, dash.no_update
    if ctx.triggered_id == 'cancel-delete-case-button': return dash.no_update, False
    raise PreventUpdate

# ─── Task Editing & Automation ──────────────────────────────────────────────
@app.callback(Output('edit-task-modal', 'is_open', allow_duplicate=True), Output('detail-task-id-store', 'data'), Output('edit-task-name', 'value'), Output('edit-task-status', 'value'), Output('edit-task-due-date', 'value'), Output('edit-task-due-date-display', 'value'), Output('edit-task-start-date', 'value'), Output('edit-task-completed-date', 'value'), Output('edit-task-documents', 'value'), Input('detail-tasks-table', 'active_cell'), State('detail-tasks-table', 'data'), prevent_initial_call=True)
def open_edit_task_modal(active_cell, data):
    if not active_cell or active_cell.get('row') is None or active_cell.get('column_id') != 'action': raise PreventUpdate
    task_data = data[active_cell['row']]
    return (True, task_data['task_id'], task_data['task_name'], task_data['status'], task_data.get('due_date'), task_data.get('due_date_display'), task_data.get('task_start_date'), task_data.get('task_completed_date'), task_data.get('documents_required'))

@app.callback(Output('edit-task-modal', 'is_open', allow_duplicate=True), Output('detail-alert-container', 'children'), Output('detail-tasks-table-container', 'children'), Output('detail-case-status-dropdown', 'value'), Output('case-completed-date-display', 'children'), Output('start-date-display', 'children'), Output('case-due-date-display', 'children'), Input('save-edit-task-button', 'n_clicks'), State('session-store', 'data'), State('detail-task-id-store', 'data'), State('detail-case-id-store', 'data'), State('edit-task-name', 'value'), State('edit-task-status', 'value'), State('edit-task-due-date', 'value'), State('edit-task-start-date', 'value'), State('edit-task-completed-date', 'value'), State('detail-tasks-table', 'data'), prevent_initial_call=True)
def handle_edit_task_modal_actions(save_clicks, session_data, task_id, case_id, name, status, new_due_date, start_date, completed_date, tasks_table_data):
    if not all([task_id, case_id, name, status]): return True, dbc.Alert("Task Name and Status cannot be empty.", color="warning"), *([dash.no_update] * 6)
    username, privilege = (session_data or {}).get('username', 'System'), (session_data or {}).get('privilege')
    original_task = next((row for row in tasks_table_data if row["task_id"] == task_id), {}); original_task_status = original_task.get("status", "N/A")
    due_date_to_pass = new_due_date if privilege == 'Admin' else None
    _, case_started = db_update_task_details(task_id, name, status, start_date, completed_date, due_date_to_pass, username)
    updated_case_info = db_fetch_single_case(case_id); case_due_date_obj = db_fetch_case_due_date(case_id)
    alert_msg = "Task updated successfully!"
    if case_started: alert_msg = "Task started! Case status automatically updated to 'In Progress' and all due dates have been set."
    elif updated_case_info.get('status') == 'Completed' and original_task_status != 'Completed': alert_msg = "All tasks completed! Case has been marked as completed."
    new_start_text = f"Started: {updated_case_info.get('start_date')}" if updated_case_info.get('start_date') else "Not Started Yet"
    new_complete_text = f"Completed: {updated_case_info.get('completed_date')}" if updated_case_info.get('completed_date') else ""
    new_due_text = f"Case Due: {case_due_date_obj}" if case_due_date_obj else ""
    refreshed_table = build_tasks_table_component(case_id, privilege)
    return False, dbc.Alert(alert_msg, color="success", duration=5000), refreshed_table, updated_case_info.get('status'), new_complete_text, new_start_text, new_due_text

@app.callback(Output('edit-task-modal', 'is_open', allow_duplicate=True), Input('cancel-edit-task-button', 'n_clicks'), prevent_initial_call=True)
def cancel_edit_task(n_clicks):
    if not n_clicks: raise PreventUpdate
    return False

# ─── File Attachments Callbacks ─────────────────────────────────────────────
@app.callback(Output('attachment-modal', 'is_open'), Output('attachment-task-id-store', 'data'), Output('attachment-modal-title', 'children'), Output('attachment-list-container', 'children'), Input('detail-tasks-table', 'active_cell'), Input('close-attachment-modal', 'n_clicks'), State('detail-tasks-table', 'data'), State('attachment-modal', 'is_open'), prevent_initial_call=True)
def handle_attachment_modal_visibility(active_cell, n_clicks, data, is_open):
    if ctx.triggered_id == 'close-attachment-modal': return False, dash.no_update, dash.no_update, dash.no_update
    if active_cell and active_cell.get('column_id') == 'attachments':
        task_data = data[active_cell['row']]; task_id = task_data['task_id']
        return True, task_id, f"Attachments for: {task_data['task_name']}", build_attachments_list(task_id)
    return is_open, dash.no_update, dash.no_update, dash.no_update

@app.callback(Output('attachment-list-container', 'children', allow_duplicate=True), Output('detail-tasks-table-container', 'children', allow_duplicate=True), Output('detail-alert-container', 'children', allow_duplicate=True), Input('upload-attachment', 'contents'), State('upload-attachment', 'filename'), State('attachment-task-id-store', 'data'), State('detail-case-id-store', 'data'), State('session-store', 'data'), prevent_initial_call=True)
def handle_file_upload(list_of_contents, list_of_names, task_id, case_id, session_data):
    if list_of_contents is None: raise PreventUpdate
    username = (session_data or {}).get('username', 'System'); privilege = (session_data or {}).get('privilege')
    for content, name in zip(list_of_contents, list_of_names):
        content_type, content_string = content.split(','); decoded = base64.b64decode(content_string)
        stored_filename = f"{uuid.uuid4()}{os.path.splitext(name)[1]}"
        with open(os.path.join(UPLOAD_DIRECTORY, stored_filename), "wb") as fp: fp.write(decoded)
        db_add_attachment(task_id, name, stored_filename, username)
    return build_attachments_list(task_id), build_tasks_table_component(case_id, privilege), dbc.Alert(f"{len(list_of_names)} file(s) uploaded!", color="success")

@app.callback(Output('attachment-list-container', 'children', allow_duplicate=True), Output('detail-tasks-table-container', 'children', allow_duplicate=True), Output('detail-alert-container', 'children', allow_duplicate=True), Input({'type': 'delete-attachment-btn', 'index': ALL}, 'n_clicks'), State('attachment-task-id-store', 'data'), State('detail-case-id-store', 'data'), State('session-store', 'data'), prevent_initial_call=True)
def handle_file_delete(n_clicks, task_id, case_id, session_data):
    if not any(n_clicks): raise PreventUpdate
    privilege = (session_data or {}).get('privilege')
    db_delete_attachment(ctx.triggered_id['index'])
    return build_attachments_list(task_id), build_tasks_table_component(case_id, privilege), dbc.Alert("Attachment deleted.", color="danger")

# ─── Manage Templates Callbacks (FIXED) ──────────────────────────────────
@app.callback(Output('templates-alert-container', 'children', allow_duplicate=True), Output('template-type-list', 'children'), Input('add-template-type-button', 'n_clicks'), State('session-store', 'data'), State('new-template-type-name', 'value'), prevent_initial_call=True)
def add_template_type(n_clicks, session_data, type_name):
    if not type_name or not type_name.strip(): return dbc.Alert("Template name cannot be empty.", color="warning"), dash.no_update
    privilege = (session_data or {}).get('privilege')
    db_add_template_type(type_name)
    return dbc.Alert(f"Template '{type_name}' added!", color="success"), build_template_type_list_items(privilege)

@app.callback(Output('template-tasks-container', 'children'), Input('selected-template-type-id-store', 'data'), State('session-store', 'data'))
def display_template_tasks(template_id, session_data):
    if template_id is None: return html.P("Select a template type to see its tasks.")
    return build_template_tasks_container(template_id, (session_data or {}).get('privilege'))

@app.callback(
    Output('template-tasks-container', 'children', allow_duplicate=True),
    Output('templates-alert-container', 'children', allow_duplicate=True),
    Output('new-task-seq', 'value'), Output('new-task-name', 'value'),
    Output('new-task-status', 'value'), Output('new-task-offset', 'value'),
    Output('new-task-documents', 'value'),
    [Input('add-task-to-template-button', 'n_clicks'), Input('template-tasks-table', 'active_cell')],
    [State('session-store', 'data'), State('selected-template-type-id-store', 'data'), State('new-task-seq', 'value'), State('new-task-name', 'value'), State('new-task-status', 'value'), State('new-task-offset', 'value'), State('new-task-documents', 'value'), State('template-tasks-table', 'data')],
    prevent_initial_call=True
)
def handle_template_task_actions(add_clicks, active_cell, session_data, template_id, seq, name, status, offset, documents, table_data):
    privilege = (session_data or {}).get('privilege')
    if privilege != 'Admin': return dash.no_update, dbc.Alert("You do not have permission to perform this action.", color="danger"), dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    triggered_id = ctx.triggered_id; alert = dash.no_update
    seq_out, name_out, status_out, offset_out, documents_out = seq, name, status, offset, documents
    if triggered_id == 'add-task-to-template-button':
        if not all([template_id, seq, name, status]):
            alert = dbc.Alert("Seq, Name, and Status are required.", color="warning")
        else:
            db_add_task_to_template(template_id, seq, name, status, offset, documents)
            alert = dbc.Alert("Task added!", color="success", duration=3000)
            seq_out, name_out, status_out, offset_out, documents_out = None, '', 'Not Started', None, ''
    elif triggered_id == 'template-tasks-table' and active_cell and active_cell['column_id'] == 'delete':
        task_template_id = table_data[active_cell['row']]['task_template_id']
        db_delete_task_from_template(task_template_id)
        alert = dbc.Alert("Task removed!", color="success", duration=3000)
    else: raise PreventUpdate
    return build_template_tasks_container(template_id, privilege), alert, seq_out, name_out, status_out, offset_out, documents_out

@app.callback(Output('selected-template-type-id-store', 'data'), Input({'type': 'template-type-item', 'index': ALL}, 'n_clicks'), prevent_initial_call=True)
def update_selected_template_id_store(n_clicks_list):
    if not any(n_clicks_list): raise PreventUpdate
    return ctx.triggered_id['index']

@app.callback(Output('delete-template-confirm-modal', 'is_open'), Output('template-to-delete-store', 'data'), Input({'type': 'delete-template-type-btn', 'index': ALL}, 'n_clicks'), State('delete-template-confirm-modal', 'is_open'), prevent_initial_call=True)
def open_delete_template_modal(n_clicks, is_open):
    if not any(n_clicks): raise PreventUpdate
    return not is_open, ctx.triggered_id['index']

@app.callback(Output('delete-template-confirm-modal', 'is_open', allow_duplicate=True), Output('template-type-list', 'children', allow_duplicate=True), Output('templates-alert-container', 'children', allow_duplicate=True), Input('confirm-delete-template-btn', 'n_clicks'), Input('cancel-delete-template-btn', 'n_clicks'), State('template-to-delete-store', 'data'), State('session-store', 'data'), prevent_initial_call=True)
def handle_template_deletion(confirm_clicks, cancel_clicks, template_id, session_data):
    triggered_id = ctx.triggered_id; privilege = (session_data or {}).get('privilege')
    if triggered_id == 'cancel-delete-template-btn': return False, dash.no_update, dash.no_update
    if triggered_id == 'confirm-delete-template-btn' and template_id:
        db_delete_template_type(template_id)
        updated_list_items = build_template_type_list_items(privilege)
        alert = dbc.Alert("Template and all its tasks have been deleted.", color="success", duration=4000)
        return False, updated_list_items, alert
    raise PreventUpdate

# ─── Other Callbacks ────────────────────────────────────────────────────────
@app.callback(Output('detail-alert-container', 'children', allow_duplicate=True), Input('update-status-button', 'n_clicks'), State('detail-case-id-store', 'data'), State('detail-case-status-dropdown', 'value'), State('session-store', 'data'), prevent_initial_call=True)
def update_case_status(n_clicks, case_id, status, session):
    if not n_clicks: raise PreventUpdate
    db_update_case_status_and_start_date(case_id, status)
    return dbc.Alert(f"Case status updated to '{status}'.", color='success', dismissable=True)

@app.callback(Output('remarks-display-area', 'children', allow_duplicate=True), Output('remark-message-textarea', 'value'), Output('detail-alert-container', 'children', allow_duplicate=True), Input('add-remark-button', 'n_clicks'), State('detail-case-id-store', 'data'), State('remark-user-name', 'value'), State('remark-message-textarea', 'value'), prevent_initial_call=True)
def add_remark_to_case(n, case_id, user_name, message):
    if not message or not message.strip(): return dash.no_update, dash.no_update, dbc.Alert('Remark cannot be empty.', color='warning')
    db_add_remark(case_id, user_name, message)
    return build_remarks_display_component(case_id), '', dbc.Alert('Remark added.', color='success')

@app.callback(Output('tasks-for-selected-date', 'children'), Output('selected-date-header', 'children'), Input('interactive-calendar', 'value'))
def update_tasks_for_date(selected_date_str):
    if not selected_date_str: return [dbc.Alert('Select a date.', color='info')], 'Tasks for Selected Date'
    sel = date.fromisoformat(selected_date_str); df = db_fetch_tasks_for_date(sel)
    header = f"Tasks for {sel.strftime('%B %d, %Y')}"
    if df.empty: return [dbc.Alert('No tasks due on this date.', color='info')], header
    items = [dbc.Alert([html.Strong(f"{r['case_name']}: "), html.Span(r['task_name']), dmc.Button('View', id={'type': 'calendar-daily-view-btn', 'index': r['case_id']}, variant='subtle', size='sm', className='float-end')], color='primary', className='mb-2') for _, r in df.iterrows()]
    return items, header

@app.callback(Output('upcoming-overdue-tasks-table-container', 'children'), Output('upcoming-overdue-tasks-header', 'children'), Input('interactive-calendar', 'value'))
def update_calendar_month(selected_date_str):
    tgt = date.fromisoformat(selected_date_str) if selected_date_str else date.today()
    start = tgt.replace(day=1); _, last = calendar.monthrange(start.year, start.month); end = start.replace(day=last)
    df = db_fetch_tasks_for_month(start, end)
    header = f"Tasks for {start.strftime('%B %Y')}"
    return build_calendar_tasks_table_component(df), header

@app.callback(Output('case-status-pie-chart', 'figure'), Output('case-performance-pie-chart', 'figure'), Output('task-status-bar-chart', 'figure'), Output('task-performance-bar-chart', 'figure'), Output('case-performance-by-type-bar-chart', 'figure'), Input('dashboard-generate-button', 'n_clicks'), State('dashboard-from-date', 'value'), State('dashboard-to-date', 'value'), prevent_initial_call=True)
def update_dashboard_charts(n_clicks, from_date, to_date):
    if not n_clicks or not from_date or not to_date: return [px.scatter()] * 5
    cases_df, tasks_df = _fetch_dashboard_data(pd.to_datetime(from_date).date(), pd.to_datetime(to_date).date())
    figs = [px.pie(cases_df, names='status', title='Case Status'), px.pie(cases_df, names='performance', title='Case Performance'), px.histogram(tasks_df, x='status', title='Task Status'), px.histogram(tasks_df, x='performance', title='Task Performance'), px.bar(cases_df.groupby(['case_type', 'performance']).size().reset_index(name='count'), x='case_type', y='count', color='performance', barmode='group', title='Case Performance by Type')]
    for fig in figs: fig.update_layout(legend_title_text='')
    return figs

@app.callback(Output('report-output-container', 'children'), Input('report-generate-button', 'n_clicks'), State('report-type-dropdown', 'value'), State('report-from-date', 'value'), State('report-to-date', 'value'), prevent_initial_call=True)
def generate_date_report(n_clicks, report_type, from_date, to_date):
    if not all([report_type, from_date, to_date]): return dbc.Alert('Please select all filters.', color='warning')
    f, t = pd.to_datetime(from_date).date(), pd.to_datetime(to_date).date()
    df = db_fetch_affected_cases_report(f, t) if report_type == 'Cases' else db_fetch_affected_tasks_report(f, t)
    if df.empty: return dbc.Alert('No data found for this period.', color='info')
    if 'case_id' in df.columns: df['action'] = 'View'
    cols = [{'name': c.replace('_', ' ').title(), 'id': c} for c in df.columns]
    style = DATATABLE_STYLE_DARK.copy(); style['style_cell_conditional'] = style.get('style_cell_conditional', []) + [{'if': {'column_id': 'action'}, 'cursor': 'pointer', 'text-decoration': 'underline', 'color': DARK_THEME['colors']['blue'][5]}]
    return dash_table.DataTable(id='report-table', columns=cols, data=df.to_dict('records'), page_size=20, **style)


# --- Initial App Run ---
if __name__ == '__main__':
    app.run(debug=True)