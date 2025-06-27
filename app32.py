# app.py (Final Version with Bug Fix & Delete Template Feature) - Lexus version
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table, Input, Output, State, callback, ctx, ALL
import psycopg2
import pandas as pd
from datetime import datetime, date, timedelta
from typing import List, Dict, Any, Optional, Tuple
import calendar
from sqlalchemy import text
import os
import uuid
import base64

from utils.performance import calculate_case_performance, calculate_task_performance


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
    db_update_case_dates_from_tasks,
    db_calculate_and_set_task_due_dates,
    db_update_case_status_and_start_date,
    db_check_and_complete_case,
    db_update_task_details,
    db_fetch_tasks_for_date,
    db_fetch_tasks_for_month,
    db_fetch_template_types,
    db_add_template_type,
    db_delete_template_type,
    db_fetch_tasks_for_template,
    db_add_task_to_template,
    db_update_task_template,
    db_delete_task_from_template,
    db_add_remark,
    db_fetch_remarks_for_case,
    db_fetch_affected_cases_report,
    db_fetch_affected_tasks_report,
    _fetch_dashboard_data
)


# Using Dash Mantine Components for a modern, reliable UI
import dash_mantine_components as dmc

# Import Plotly Express for charting
import plotly.express as px
import plotly.io as pio

# Import user authentication and management functions
from auth import (
    db_add_user, db_get_user, db_get_all_users,
    db_update_user_password, db_delete_user, check_password
)

# Database connection (moved out of auth into its own module)
from db.connection import get_db_connection


# Import Flask server for download handling
from flask import send_from_directory

# =============================================================================
# DARK MODE THEME CONFIGURATION
# =============================================================================
# 1. Define the custom dark theme for MantineProvider
DARK_THEME = {
    "colorScheme": "dark",
    "primaryColor": "blue",
    "colors": {
        "dark": [
            "#C1C2C5", "#A6A7AB", "#909296", "#5C5F66", "#373A40", "#2C2E33", "#25262B", "#1A1B1E", "#141517",
            "#101113",
        ],
        "blue": [
            "#E7F5FF", "#D0EBFF", "#A5D8FF", "#74C0FC", "#4DABF7", "#339AF0", "#228BE6", "#1C7ED6", "#1971C2",
            "#1864AB",
        ],
        "red": [
            "#FFF5F5", "#FFE3E3", "#FFC9C9", "#FFA8A8", "#FF8787", "#FF6B6B", "#FA5252", "#F03E3E", "#E03131",
            "#C92A2A"
        ],
    },
    "fontFamily": "'Inter', sans-serif",
    "headings": {"fontFamily": "'Inter', sans-serif", "fontWeight": 600},
}

# 2. Set the default Plotly template for dark mode charts
pio.templates["custom_dark"] = pio.templates["plotly_dark"]
pio.templates["custom_dark"].layout.paper_bgcolor = 'rgba(0,0,0,0)'
pio.templates["custom_dark"].layout.plot_bgcolor = 'rgba(0,0,0,0)'
pio.templates["custom_dark"].layout.font.color = DARK_THEME["colors"]["dark"][0]
pio.templates["custom_dark"].layout.title.font.color = DARK_THEME["colors"]["dark"][0]
pio.templates.default = "custom_dark"

# 3. Define DataTable styles for dark mode
DATATABLE_STYLE_DARK = {
    'style_table': {'overflowX': 'auto'},
    'style_header': {
        'backgroundColor': DARK_THEME["colors"]["dark"][6],
        'color': 'white',
        'fontWeight': 'bold',
        'border': '1px solid ' + DARK_THEME["colors"]["dark"][4],
    },
    'style_cell': {
        'backgroundColor': DARK_THEME["colors"]["dark"][7],
        'color': 'white',
        'border': '1px solid ' + DARK_THEME["colors"]["dark"][4],
        'padding': '10px',
        'textAlign': 'left'
    },
    'style_data_conditional': [
        {'if': {'row_index': 'odd'}, 'backgroundColor': DARK_THEME["colors"]["dark"][6]},
        {'if': {'state': 'active'}, 'backgroundColor': DARK_THEME["colors"]["blue"][8],
         'border': '1px solid ' + DARK_THEME["colors"]["blue"][5]},
        {'if': {'state': 'selected'}, 'backgroundColor': DARK_THEME["colors"]["blue"][9],
         'border': '1px solid ' + DARK_THEME["colors"]["blue"][5]},
        # Performance coloring
        {'if': {'filter_query': '{performance} = "Completed On Time"'}, 'backgroundColor': '#1F4B2D',
         'color': '#E6F4EA'},
        {'if': {'filter_query': '{performance} = "On Time"'}, 'backgroundColor': '#1F4B2D', 'color': '#E6F4EA'},
        {'if': {'filter_query': '{performance} = "Completed Late"'}, 'backgroundColor': '#663C00', 'color': '#FFECB3'},
        {'if': {'filter_query': '{performance} = "Overdue"'}, 'backgroundColor': '#5C2223', 'color': '#FEEBEE'},
        {'if': {'filter_query': '{performance} = "Pending"'}, 'backgroundColor': '#373A40', 'color': '#A6A7AB'},
    ]
}

# =============================================================================
# GLOBAL HELPER FUNCTIONS
# =============================================================================
# Directory to store uploaded files
UPLOAD_DIRECTORY = "uploads"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# =============================================================================
# ATTACHMENT FUNCTIONS
# =============================================================================
def db_add_attachment(task_id: int, original_filename: str, stored_filename: str, uploaded_by: str):
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


def db_fetch_attachments_for_task(task_id: int) -> pd.DataFrame:
    sql = text("""
        SELECT attachment_id, original_filename, stored_filename
        FROM task_attachments WHERE task_id = :task_id ORDER BY upload_timestamp DESC
    """)
    with get_db_connection() as conn:
        return pd.read_sql(sql, conn, params={"task_id": task_id})


def db_get_attachment_info(attachment_id: int) -> Optional[Dict[str, Any]]:
    sql = text("SELECT stored_filename FROM task_attachments WHERE attachment_id = :attachment_id")
    with get_db_connection() as conn:
        result = conn.execute(sql, {"attachment_id": attachment_id}).fetchone()
        if result:
            try:
                return result._asdict()
            except AttributeError:
                return dict(result)
        return None


def db_delete_attachment(attachment_id: int):
    attachment_info = db_get_attachment_info(attachment_id)
    if attachment_info:
        file_path = os.path.join(UPLOAD_DIRECTORY, attachment_info['stored_filename'])
        if os.path.exists(file_path):
            os.remove(file_path)

    sql = text("DELETE FROM task_attachments WHERE attachment_id = :attachment_id")
    with get_db_connection() as conn:
        conn.execute(sql, {"attachment_id": attachment_id})
        conn.commit()


# =============================================================================
# App Layout Building Functions
# =============================================================================
def build_cases_list_component(privilege: str):
    cases_df = db_fetch_all_cases()
    is_admin = (privilege == 'Admin')

    header = dbc.ListGroupItem(
        dbc.Row([
            dbc.Col(html.B("Case Name"), width=4), dbc.Col(html.B("Status"), width=2),
            dbc.Col(html.B("Performance"), width=2), dbc.Col(html.B("Case Type"), width=2),
            dbc.Col(html.B("Action"), width=2),
        ], align="center"),
        className="list-group-item-dark"
    )

    def get_performance_color(p):
        return {"Completed On Time": "green", "On Time": "green", "Overdue": "red",
                "Pending": "gray", "Completed Late": "orange"}.get(p, "blue")

    if cases_df.empty:
        return dbc.ListGroup([header, dbc.ListGroupItem("No cases found.")], flush=True)

    case_items = [header]
    for _, row in cases_df.iterrows():
        action_buttons = [
            dmc.Button("View", id={'type': 'view-case-btn', 'index': row['case_id']}, size="xs", variant="subtle")
        ]
        if is_admin:
            action_buttons.extend([
                dmc.Button("Edit", id={'type': 'edit-case-btn', 'index': row['case_id']}, size="xs", color="yellow",
                           variant="subtle", ml=5),
                dmc.Button("Delete", id={'type': 'delete-case-btn', 'index': row['case_id']}, size="xs", color="red",
                           variant="subtle", ml=5)
            ])

        item = dbc.ListGroupItem(
            dbc.Row([
                dbc.Col(row['case_name'], width=4, className="d-flex align-items-center"),
                dbc.Col(row['status'], width=2, className="d-flex align-items-center"),
                dbc.Col(
                    dmc.Badge(row['performance'], color=get_performance_color(row['performance']), variant="light") if
                    row['performance'] else "N/A",
                    width=2, className="d-flex align-items-center"),
                dbc.Col(row['case_type'], width=2, className="d-flex align-items-center"),
                dbc.Col(dmc.Group(action_buttons, gap='xs'), width=2),
            ], align="center", className="py-2")
        )
        case_items.append(item)

    return dbc.ListGroup(case_items, flush=True)


def build_homepage_layout(privilege: str):
    template_types_df = db_fetch_template_types()
    template_types = template_types_df['type_name'].tolist() if not template_types_df.empty else []

    return html.Div([
        dcc.Store(id='edit-case-id-store'),
        dcc.Store(id='delete-case-id-store'),
        html.Div(id='home-alert-container'),

        dbc.Card(dbc.CardBody([
            html.H4("Add a New Case", className="card-title"),
            dbc.Row([
                dbc.Col(dmc.TextInput(id='home-new-case-name', placeholder="Enter Case Name..."), md=4),
                dbc.Col(dmc.Select(id='home-new-case-status', data=['Not Started', 'In Progress', 'On Hold'],
                                   value='Not Started', placeholder="Select Status"), md=3),
                dbc.Col(dmc.Select(id='home-new-case-type', data=template_types, placeholder="Select Case Type"), md=3),
                dbc.Col(dmc.Button("Add Case", id='home-add-case-button'), md=2, className="align-self-end"),
            ])
        ])),
        html.H2("All Cases", className="text-center my-4"),
        html.Div(id='case-list-container', children=build_cases_list_component(privilege)),

        dbc.Modal([
            dbc.ModalHeader("Edit Case"),
            dbc.ModalBody([
                html.Div([dmc.Text("Case Name:", size="sm"), dmc.TextInput(id='modal-edit-case-name')]),
                html.Div([dmc.Text("Status:", size="sm", mt="sm"), dmc.Select(id='modal-edit-case-status',
                                                                              data=['Not Started', 'In Progress',
                                                                                    'On Hold', 'Completed'])]),
                html.Div([dmc.Text("Case Type:", size="sm", mt="sm"),
                          dmc.Select(id='modal-edit-case-type', data=template_types)]),
            ]),
            dbc.ModalFooter(dmc.Group([
                dmc.Button("Cancel", id="cancel-edit-case-button", variant="outline"),
                dmc.Button("Save Changes", id="save-edit-case-button")
            ]))
        ], id='edit-case-modal', is_open=False, centered=True),

        dbc.Modal([
            dbc.ModalHeader("Confirm Deletion"),
            dbc.ModalBody(id='delete-case-confirm-text'),
            dbc.ModalFooter(dmc.Group([
                dmc.Button("Cancel", id='cancel-delete-case-button', variant="outline"),
                dmc.Button("DELETE", id='confirm-delete-case-button', color='red')
            ]))
        ], id='delete-case-modal', is_open=False, centered=True),
    ])


def build_case_detail_layout(case_id: int, username: str, privilege: str):
    case_info = db_fetch_single_case(case_id)
    if not case_info: return dbc.Alert(f"Case with ID {case_id} not found.", color="danger")

    due_date = db_fetch_case_due_date(case_id)
    start_date_text = f"Started: {case_info['start_date'].strftime('%Y-%m-%d')}" if case_info.get(
        'start_date') else "Not Started Yet"
    completed_date_text = f"Completed: {case_info['completed_date'].strftime('%Y-%m-%d')}" if case_info.get(
        'completed_date') else ""
    case_due_date_text = f"Case Due: {due_date.strftime('%Y-%m-%d')}" if due_date else ""
    is_user_role = (privilege == 'User')

    return html.Div([
        dcc.Store(id='detail-case-id-store', data=case_id),
        dcc.Store(id='detail-task-id-store'),
        dcc.Store(id='attachment-task-id-store'),
        html.Div(id='detail-alert-container'),
        dbc.Card(dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H2(case_info['case_name'], id="detail-case-name"),
                    html.H5(f"Type: {case_info['case_type']}", className="text-muted"),
                    html.H5(start_date_text, className="text-info", id='start-date-display'),
                    html.H5(case_due_date_text, className="text-warning", id='case-due-date-display'),
                    html.H5(completed_date_text, className="text-success", id='case-completed-date-display')
                ], width=8),
                dbc.Col([
                    dmc.Text("Change Case Status:", size="sm"),
                    dmc.Select(id='detail-case-status-dropdown',
                               data=['Not Started', 'In Progress', 'On Hold', 'Completed'], value=case_info['status']),
                    dmc.Button("Update Status", id='update-status-button', fullWidth=True, mt="md")
                ], width=4)
            ])
        ])),
        html.H3("Tasks", className="text-center my-4"),
        html.Div(id='detail-tasks-table-container', children=build_tasks_table_component(case_id)),

        dbc.Modal([
            dbc.ModalHeader("Edit Task"),
            dbc.ModalBody([
                html.Div([dmc.Text("Task Name:", size="sm"), dmc.TextInput(id='edit-task-name')]),
                html.Div([
                    dmc.Text("Status:", size="sm", mt="sm"),
                    dmc.Select(id='edit-task-status',
                               data=['Not Started', 'In Progress', 'On Hold', 'Completed'])
                ]),
                html.Div([dmc.Text("Task Start Date:", size="sm", mt="sm"),
                          dmc.DatePicker(id='edit-task-start-date', style={"width": "100%"})]),
                html.Div([dmc.Text("Task Completed Date:", size="sm", mt="sm"),
                          dmc.DatePicker(id='edit-task-completed-date', style={"width": "100%"})]),
                html.Div([
                    dmc.Text("Due Date:", size="sm", mt="sm"),
                    dmc.DatePicker(
                        id='edit-task-due-date',
                        style={"width": "100%", "display": "none" if is_user_role else "block"}
                    ),
                    dmc.TextInput(
                        id='edit-task-due-date-display',
                        disabled=True,
                        style={"width": "100%", "display": "block" if is_user_role else "none"}
                    ),
                    dmc.Text("Due dates can only be changed by Admins.", size="xs",
                             c="dimmed") if is_user_role else None
                ]),
            ]),
            dbc.ModalFooter(dmc.Group([
                dmc.Button("Cancel", id="cancel-edit-task-button", variant="outline"),
                dmc.Button("Save Changes", id="save-edit-task-button")
            ]))
        ], id='edit-task-modal', is_open=False, centered=True),

        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle(id="attachment-modal-title")),
            dbc.ModalBody([
                dbc.Card(dbc.CardBody([
                    html.H5("Upload New File"),
                    dcc.Upload(
                        id='upload-attachment',
                        className='uploader-area',
                        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
                        style={
                            'width': '100%', 'height': '60px', 'lineHeight': '60px',
                            'borderWidth': '1px', 'borderStyle': 'dashed',
                            'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px 0'
                        },
                        multiple=True
                    ),
                ])),
                html.Hr(),
                html.H5("Existing Attachments"),
                html.Div(id='attachment-list-container')
            ]),
            dbc.ModalFooter(
                dmc.Button("Close", id="close-attachment-modal", variant="outline")
            )
        ], id='attachment-modal', is_open=False, centered=True, size="lg"),

        html.Hr(className="my-4"),
        dbc.Card(dbc.CardBody([
            html.H4("Case Remarks", className="card-title mb-3"),
            dbc.Row([
                dbc.Col(dmc.TextInput(value=username, disabled=True, id='remark-user-name'), md=3),
                dbc.Col(
                    dmc.Textarea(placeholder="Enter remark...", autosize=True, minRows=2, id='remark-message-textarea'),
                    md=7),
                dbc.Col(dmc.Button("Add Remark", id='add-remark-button', fullWidth=True), md=2,
                        className="align-self-end")
            ]),
            html.Div(id='remarks-display-area', className="mt-3", children=build_remarks_display_component(case_id))
        ]))
    ])


# =============================================================================
# REPLACEMENT for build_tasks_table_component (Bug Fix)
# =============================================================================
def build_tasks_table_component(case_id: int):
    tasks_df = db_fetch_tasks_for_case(case_id)
    if not tasks_df.empty:
        attachment_counts = []
        for task_id in tasks_df['task_id']:
            attachments_df = db_fetch_attachments_for_task(task_id)
            count = len(attachments_df)
            attachment_counts.append(f"{count} file(s)")
        tasks_df['attachments'] = attachment_counts
        tasks_df['edit'] = "Edit"
    else:
        tasks_df = tasks_df.assign(attachments=[], edit=[])

    table_columns = [
        {"name": "Task Name", "id": "task_name"},
        {"name": "Status", "id": "status"},
        {"name": "Performance", "id": "performance"},
        {"name": "Documents Required", "id": "documents_required"},
        {"name": "Attachments", "id": "attachments"},
        {"name": "Due Date", "id": "due_date_display"},
        {"name": "Start Date", "id": "task_start_date"},
        {"name": "Completed Date", "id": "task_completed_date"},
        {"name": "Last Updated By", "id": "last_updated_by"},
        {"name": "Last Update Date", "id": "last_updated_at_display"},
        {"name": "Action", "id": "edit"}
    ]

    # --- BUG FIX IS HERE ---
    # 1. Create a local copy of the styles to avoid modifying the global dict
    table_styles = DATATABLE_STYLE_DARK.copy()
    # 2. Update the style_cell property in the local copy with our new styles
    table_styles['style_cell'] = {
        **DATATABLE_STYLE_DARK['style_cell'],
        'whiteSpace': 'pre-line',
        'height': 'auto',
    }
    # --- END OF BUG FIX ---

    return dash_table.DataTable(
        id='detail-tasks-table',
        columns=table_columns,
        data=tasks_df.to_dict('records'),
        **table_styles,  # 3. Use the fully combined and corrected styles dictionary
        style_cell_conditional=[
            {'if': {'column_id': 'edit'}, 'color': DARK_THEME["colors"]["blue"][5],
             'textDecoration': 'underline', 'cursor': 'pointer'},
            {'if': {'column_id': 'attachments'}, 'color': DARK_THEME["colors"]["blue"][3],
             'textDecoration': 'underline', 'cursor': 'pointer'}
        ]
    )


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


def build_remarks_display_component(case_id: int):
    remarks_df = db_fetch_remarks_for_case(case_id)
    if remarks_df.empty: return html.P("No remarks yet.", className="text-muted")
    return [
        dbc.Card(
            dbc.CardBody([
                dmc.Text(f"By {row['user_name']} on {row['timestamp']}", size="xs", c="dimmed"),
                dmc.Text(row['message'], c="dark.0")
            ]),
            className="mb-2",
            style={"backgroundColor": DARK_THEME['colors']['dark'][6]}
        ) for _, row in remarks_df.iterrows()
    ]


def build_calendar_layout():
    today = date.today()
    start_of_current_month = today.replace(day=1)
    _, end_day = calendar.monthrange(today.year, today.month)
    end_of_current_month = today.replace(day=end_day)
    initial_tasks_df = db_fetch_tasks_for_month(start_of_current_month, end_of_current_month)
    return html.Div([
        dmc.Grid(children=[
            dmc.GridCol([dmc.Text("Select a Date to View Daily Tasks", size="sm"),
                         dmc.DatePicker(id='interactive-calendar', value=today.isoformat(), style={"width": "100%"})],
                        span={"base": 12, "md": 6, "lg": 5}),
            dmc.GridCol(
                [html.H4("Tasks for Selected Date", id="selected-date-header"), html.Div(id="tasks-for-selected-date")],
                span={"base": 12, "md": 6, "lg": 7})
        ], gutter="xl"),
        html.Hr(className="my-4"),
        html.H3(id='upcoming-overdue-tasks-header', className="text-center"),
        html.Div(id='upcoming-overdue-tasks-table-container',
                 children=build_calendar_tasks_table_component(initial_tasks_df))
    ])


def build_calendar_tasks_table_component(tasks_df: pd.DataFrame):
    if tasks_df.empty: return dbc.Alert("No upcoming or overdue tasks for this month.", color="info", className="mt-3")
    header = dbc.ListGroupItem(dbc.Row(
        [dbc.Col(html.B("Due Date"), width=2), dbc.Col(html.B("Case"), width=4), dbc.Col(html.B("Task"), width=4),
         dbc.Col(html.B("Action"), width=2)], align="center"), className="list-group-item-dark")
    task_list_items = [header]
    for _, row in tasks_df.iterrows():
        item = dbc.ListGroupItem(dbc.Row([
            dbc.Col(row['due_date_display'], width=2, className="d-flex align-items-center"),
            dbc.Col(row['case_name'], width=4, className="d-flex align-items-center"),
            dbc.Col(row['task_name'], width=4, className="d-flex align-items-center"),
            dbc.Col(dmc.Button("View Case", id={'type': 'calendar-view-case-btn', 'index': row['case_id']}), width=2)
        ], align="center", className="py-2"))
        task_list_items.append(item)
    return dbc.ListGroup(task_list_items, flush=True)


# UPDATED
def build_templates_layout(privilege: str):
    template_types_df = db_fetch_template_types()
    template_types = template_types_df.to_dict('records') if not template_types_df.empty else []
    is_admin = (privilege == 'Admin')

    def create_template_item(tt):
        # Create an item with a delete button for admins
        if is_admin:
            return dbc.ListGroupItem(
                dbc.Row([
                    dbc.Col(tt['type_name'], width=9, className="d-flex align-items-center"),
                    dbc.Col(
                        dmc.Button(
                            "Delete",
                            id={'type': 'delete-template-btn', 'index': tt['template_type_id']},
                            color="red",
                            variant="subtle",
                            size="xs"
                        ),
                        width=3, className="d-flex justify-content-end"
                    )
                ], align="center"),
                id={'type': 'template-type-item', 'index': tt['template_type_id']},
                action=True
            )
        # Non-admins just see the name
        return dbc.ListGroupItem(
            tt['type_name'],
            id={'type': 'template-type-item', 'index': tt['template_type_id']},
            action=True
        )

    return html.Div([
        dcc.Store(id='selected-template-type-id-store'),
        dcc.Store(id='delete-template-id-store'),  # Store for the ID to delete
        html.H2("Manage Task Templates"),
        html.Div(id='templates-alert-container'),
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody([
                html.H4("Template Types"),
                dbc.ListGroup(
                    [create_template_item(tt) for tt in template_types],
                    id='template-type-list'
                ),
                html.Hr(),
                dbc.InputGroup(
                    [dbc.Input(id='new-template-type-name', placeholder="New Template Name...", disabled=not is_admin),
                     dbc.Button("Add Type", id='add-template-type-button', color="success", disabled=not is_admin)])
            ])), width=4),
            dbc.Col(
                html.Div(id='template-tasks-container', children=html.P("Select a template type to see its tasks.")),
                width=8)
        ]),
        # Confirmation Modal for deleting a template type
        dbc.Modal([
            dbc.ModalHeader("Confirm Template Deletion"),
            dbc.ModalBody(id='delete-template-confirm-text'),
            dbc.ModalFooter(dmc.Group([
                dmc.Button("Cancel", id='cancel-delete-template-button', variant="outline"),
                dmc.Button("DELETE TEMPLATE", id='confirm-delete-template-button', color='red')
            ]))
        ], id='delete-template-modal', is_open=False, centered=True),
    ])


# UPDATED (Bug Fix)
def build_template_tasks_container(template_type_id: int, privilege: str):
    tasks_df = db_fetch_tasks_for_template(template_type_id)
    is_admin = (privilege == 'Admin')
    if not tasks_df.empty:
        tasks_df['delete'] = "X"

    table_columns = [
        {"name": "Seq", "id": "task_sequence", "type": "numeric"},
        {"name": "Task Name", "id": "task_name", "type": "text"},
        {"name": "Default Status", "id": "default_status", "type": "text"},
        {"name": "Documents Required", "id": "documents_required", "type": "text"},
        {"name": "Due Days Offset", "id": "day_offset", "type": "numeric"},
    ]
    if is_admin:
        table_columns.append({"name": "Delete", "id": "delete"})

    # --- BUG FIX IS HERE ---
    table_styles = DATATABLE_STYLE_DARK.copy()
    table_styles['style_cell'] = {
        **DATATABLE_STYLE_DARK['style_cell'],
        'whiteSpace': 'pre-line',
        'height': 'auto',
    }
    # --- END OF BUG FIX ---

    return html.Div([
        html.H4("Checklist for selected template"),
        dash_table.DataTable(
            id='template-tasks-table',
            columns=table_columns,
            data=tasks_df.to_dict('records'),
            editable=is_admin,
            **table_styles,
            style_cell_conditional=[
                {'if': {'column_id': 'delete'}, 'color': DARK_THEME["colors"]["red"][5], 'fontWeight': 'bold',
                 'cursor': 'pointer'}
            ] if is_admin else []
        ),
        html.Hr(),
        html.Div([
            html.H5("Add New Task to Template"),
            dmc.Grid([
                dmc.GridCol(dmc.NumberInput(label="Seq #", id='new-task-seq'), span=2),
                dmc.GridCol(dmc.TextInput(label="Task Name", id='new-task-name'), span=4),
                dmc.GridCol(
                    dmc.Select(label="Default Status", id='new-task-status', data=['Not Started', 'In Progress', 'On Hold'],
                               value='Not Started'), span=3),
                dmc.GridCol(dmc.NumberInput(label="Days Offset", id='new-task-offset'), span=3),
                dmc.GridCol(dmc.Textarea(label="Documents Required", id='new-task-documents',
                                         placeholder="List required documents...", autosize=True, minRows=2), span=12),
            ], gutter="md"),
            dmc.Button("Add Task", id='add-task-to-template-button', mt="md")
        ], style={'display': 'block' if is_admin else 'none'})
    ])


def build_date_report_layout():
    return html.Div([
        html.H2("Date Range Report", className="mb-4"),
        dbc.Card(dbc.CardBody([
            dbc.Row([
                dbc.Col([dmc.Text("Report Type", size="sm"),
                         dmc.Select(id='report-type-dropdown', data=['Cases', 'Tasks'], value='Cases')], md=2),
                dbc.Col([dmc.Text("From Date", size="sm"),
                         dmc.DatePicker(id='report-from-date', value=date.today() - timedelta(days=30),
                                        style={"width": "100%"})], md=3),
                dbc.Col([dmc.Text("To Date", size="sm"),
                         dmc.DatePicker(id='report-to-date', value=date.today(), style={"width": "100%"})], md=3),
                dbc.Col(dmc.Button("Generate Report", id='report-generate-button', fullWidth=True), md=4,
                        className="align-self-end")
            ])
        ])),
        html.Div(id='report-output-container', className="mt-4")
    ])


def build_dashboard_layout():
    today, start_of_year = date.today(), date(date.today().year, 1, 1)
    return html.Div([
        html.H2("Legal Case Dashboard", className="text-center mb-4"),
        dbc.Card(dbc.CardBody([
            html.H4("Filter by Date Range", className="card-title"),
            dbc.Row([
                dbc.Col([dmc.Text("From Date", size="sm"),
                         dmc.DatePicker(id='dashboard-from-date', value=start_of_year.isoformat(),
                                        style={"width": "100%"})], md=4),
                dbc.Col([dmc.Text("To Date", size="sm"),
                         dmc.DatePicker(id='dashboard-to-date', value=today.isoformat(), style={"width": "100%"})],
                        md=4),
                dbc.Col(dmc.Button("Generate Charts", id='dashboard-generate-button', fullWidth=True), md=4,
                        className="align-self-end")
            ])
        ]), className="mb-4"),
        dbc.Row([
            dbc.Col(
                dbc.Card(dbc.CardBody([html.H4("Case Status Distribution"), dcc.Graph(id='case-status-pie-chart')])),
                lg=6, className="mb-4"),
            dbc.Col(dbc.Card(
                dbc.CardBody([html.H4("Overall Case Performance"), dcc.Graph(id='case-performance-pie-chart')])), lg=6,
                className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody([html.H4("Task Status by Period"), dcc.Graph(id='task-status-bar-chart')])),
                    lg=6, className="mb-4"),
            dbc.Col(dbc.Card(
                dbc.CardBody([html.H4("Task Performance by Period"), dcc.Graph(id='task-performance-bar-chart')])),
                lg=6, className="mb-4")
        ]),
        dbc.Row([dbc.Col(dbc.Card(dbc.CardBody(
            [html.H4("Case Performance by Case Type"), dcc.Graph(id='case-performance-by-type-bar-chart')])),
            className="mb-4")])
    ])


def build_login_layout():
    return dbc.Container([
        dbc.Row(dbc.Col(html.Div(id='login-alert'), md=6), justify="center"),
        dbc.Row(dbc.Col(dbc.Card([
            dbc.CardHeader(html.H4("Login", className="text-center")),
            dbc.CardBody([
                dmc.Text("Username", size="sm"), dmc.TextInput(id='login-username', required=True),
                dmc.Text("Password", size="sm", mt="sm"), dmc.PasswordInput(id='login-password', required=True),
                dmc.Button("Login", id='login-button', fullWidth=True, mt="xl"),
                dmc.Button("Forgot Password?", id="forgot-password-link", variant="subtle", size="xs", mt="xs",
                           fullWidth=True)
            ])
        ]), md=5), justify="center", className="mt-5"),
        dbc.Modal([dbc.ModalHeader(dbc.ModalTitle("Password Reset")),
                   dbc.ModalBody(
                       "To reset your password, please contact an administrator who can set a temporary password for you."),
                   dbc.ModalFooter(dmc.Button("Close", id="close-forgot-password-modal"))],
                  id="forgot-password-modal", is_open=False, centered=True)
    ], fluid=True)


def build_user_management_layout(privilege: str):
    if privilege != 'Admin': return dbc.Alert("You do not have permission to access this page.", color="danger")

    users_df = pd.DataFrame(db_get_all_users())
    if not users_df.empty:
        users_df['actions'] = "Reset Password / Delete"
    else:
        users_df = pd.DataFrame(columns=['user_id', 'username', 'privilege', 'created_at', 'actions'])

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
                             columns=[{'name': c.replace('_', ' ').title(), 'id': c} for c in
                                      ['username', 'privilege', 'created_at', 'actions']],
                             data=users_df.to_dict('records'), **DATATABLE_STYLE_DARK,
                             style_cell_conditional=[
                                 {'if': {'column_id': 'actions'}, 'color': DARK_THEME["colors"]["blue"][5],
                                  'textDecoration': 'underline', 'cursor': 'pointer'}]),
        dbc.Modal([dbc.ModalHeader(dbc.ModalTitle("Reset User Password")),
                   dbc.ModalBody([dcc.Store(id='reset-user-id-store'), html.P(id='reset-password-username-text'),
                                  dmc.PasswordInput(id='reset-password-input')]),
                   dbc.ModalFooter(dmc.Group([
                       dmc.Button("Cancel", id='reset-password-cancel-button', variant="outline"),
                       dmc.Button("Save New Password", id='reset-password-save-button')]))
                   ], id='reset-password-modal', is_open=False, centered=True),
        dbc.Modal([dbc.ModalHeader(dbc.ModalTitle("Confirm Deletion")),
                   dbc.ModalBody([dcc.Store(id='delete-user-id-store'), html.P(id='delete-user-confirm-text')]),
                   dbc.ModalFooter(dmc.Group([dmc.Button("Cancel", id='delete-user-cancel-button', variant="outline"),
                                              dmc.Button("DELETE USER", id='delete-user-confirm-button', color='red')]))
                   ], id='delete-user-modal', is_open=False, centered=True)
    ])


# =============================================================================
# App Initialization and Main Layout
# =============================================================================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server


@server.route('/files/view/<filename>')
def serve_viewable_file(filename):
    return send_from_directory(UPLOAD_DIRECTORY, filename)


@server.route('/files/download/<filename>')
def serve_downloadable_file(filename):
    return send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True)


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


@callback(Output('reset-password-modal', 'is_open'), Output('reset-user-id-store', 'data'),
          Output('reset-password-username-text', 'children'),
          Output('delete-user-modal', 'is_open'), Output('delete-user-id-store', 'data'),
          Output('delete-user-confirm-text', 'children'),
          Input('users-table', 'active_cell'), State('users-table', 'data'), prevent_initial_call=True)
def open_user_action_modals(active_cell, data):
    if not active_cell or active_cell.get('row') is None or active_cell.get(
            'column_id') != 'actions': raise dash.exceptions.PreventUpdate
    row_data = data[active_cell['row']]
    user_id, username = row_data['user_id'], row_data['username']
    return True, user_id, f"Enter new password for user: {username}", False, dash.no_update, dash.no_update


@callback(Output('user-management-alert', 'children'), Output('reset-password-modal', 'is_open', allow_duplicate=True),
          Output('reset-password-input', 'value'),
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
def display_template_tasks(template_id, session_data):
    if template_id is None: return html.P("Select a template type to see its tasks.")
    return build_template_tasks_container(template_id, (session_data or {}).get('privilege'))


@callback(
    Output('template-tasks-container', 'children', allow_duplicate=True),
    Output('templates-alert-container', 'children', allow_duplicate=True),
    [Input('add-task-to-template-button', 'n_clicks'),
     Input('template-tasks-table', 'active_cell')],
    [State('session-store', 'data'),
     State('selected-template-type-id-store', 'data'),
     State('new-task-seq', 'value'),
     State('new-task-name', 'value'),
     State('new-task-status', 'value'),
     State('new-task-offset', 'value'),
     State('new-task-documents', 'value'),
     State('template-tasks-table', 'data')],
    prevent_initial_call=True
)
def handle_template_task_actions(add_clicks, active_cell, session_data, template_id, seq, name, status, offset,
                                 documents, table_data):
    privilege = (session_data or {}).get('privilege')
    if privilege != 'Admin':
        return dash.no_update, dbc.Alert("You do not have permission to perform this action.", color="danger")

    triggered_id = ctx.triggered_id
    alert = dash.no_update

    if triggered_id == 'add-task-to-template-button':
        if not all([template_id, seq, name, status]):
            alert = dbc.Alert("Seq, Name, and Status are required.", color="warning")
        else:
            db_add_task_to_template(template_id, seq, name, status, offset, documents)
            alert = dbc.Alert("Task added!", color="success", duration=3000)

    elif triggered_id == 'template-tasks-table' and active_cell and active_cell['column_id'] == 'delete':
        task_template_id = table_data[active_cell['row']]['task_template_id']
        db_delete_task_from_template(task_template_id)
        alert = dbc.Alert("Task removed!", color="success", duration=3000)
    else:
        raise dash.exceptions.PreventUpdate

    return build_template_tasks_container(template_id, privilege), alert


@callback(
    Output('templates-alert-container', 'children', allow_duplicate=True),
    Input('template-tasks-table', 'data'),
    State('template-tasks-table', 'data_previous'),
    prevent_initial_call=True
)
def handle_template_task_edit(data, data_previous):
    if data is None or data_previous is None:
        raise dash.exceptions.PreventUpdate

    for i, row in enumerate(data):
        if row != data_previous[i]:
            changed_row = row
            original_row = data_previous[i]

            for col_id in changed_row:
                if col_id in original_row and changed_row[col_id] != original_row[col_id]:
                    task_template_id = changed_row['task_template_id']
                    new_value = changed_row[col_id]

                    db_update_task_template(task_template_id, col_id, new_value)

                    return dbc.Alert(f"Updated '{col_id.replace('_', ' ').title()}' successfully.", color="info",
                                     duration=2000)

    raise dash.exceptions.PreventUpdate


# UPDATED
@callback(
    Output('selected-template-type-id-store', 'data'),
    Input({'type': 'template-type-item', 'index': ALL}, 'n_clicks'),
    State({'type': 'delete-template-btn', 'index': ALL}, 'n_clicks'),
    prevent_initial_call=True
)
def update_selected_template_id_store(item_clicks, delete_clicks):
    # This prevents the list item from being selected if the delete button inside it was the trigger
    if ctx.triggered_id and 'delete-template-btn' in ctx.triggered_id.get('type', ''):
        raise dash.exceptions.PreventUpdate

    if not any(item_clicks):
        raise dash.exceptions.PreventUpdate

    return ctx.triggered_id['index']


# NEW
@callback(
    Output('delete-template-modal', 'is_open'),
    Output('delete-template-id-store', 'data'),
    Output('delete-template-confirm-text', 'children'),
    Input({'type': 'delete-template-btn', 'index': ALL}, 'n_clicks'),
    State('template-type-list', 'children'),
    prevent_initial_call=True
)
def open_delete_template_modal(n_clicks, template_list_children):
    if not any(n_clicks):
        raise dash.exceptions.PreventUpdate

    template_id_to_delete = ctx.triggered_id['index']

    # Find the name of the template to show in the confirmation message
    template_name = "this template"
    try:
        for item in template_list_children:
            if item['props']['id']['index'] == template_id_to_delete:
                template_name = f"'{item['props']['children']['props']['children'][0]['props']['children']}'"
                break
    except (TypeError, KeyError):
        pass  # Fallback to the generic name if parsing fails

    text = f"Are you sure you want to delete the template {template_name}? This will delete all of its checklist tasks and cannot be undone."

    return True, template_id_to_delete, text


# NEW
@callback(
    Output('delete-template-modal', 'is_open', allow_duplicate=True),
    Output('templates-alert-container', 'children', allow_duplicate=True),
    Output('template-type-list', 'children', allow_duplicate=True),
    Output('template-tasks-container', 'children', allow_duplicate=True),
    Input('confirm-delete-template-button', 'n_clicks'),
    State('delete-template-id-store', 'data'),
    State('session-store', 'data'),
    prevent_initial_call=True
)
def confirm_template_delete(n_clicks, template_id, session_data):
    if not n_clicks:
        raise dash.exceptions.PreventUpdate

    db_delete_template_type(template_id)

    privilege = (session_data or {}).get('privilege', 'User')

    # Rebuild the list of templates after deletion
    template_types_df = db_fetch_template_types()
    template_types = template_types_df.to_dict('records') if not template_types_df.empty else []

    def create_template_item(tt):
        is_admin = (privilege == 'Admin')
        if is_admin:
            return dbc.ListGroupItem(
                dbc.Row([
                    dbc.Col(tt['type_name'], width=9, className="d-flex align-items-center"),
                    dbc.Col(
                        dmc.Button("Delete", id={'type': 'delete-template-btn', 'index': tt['template_type_id']},
                                   color="red", variant="subtle", size="xs"), width=3,
                        className="d-flex justify-content-end")
                ], align="center"),
                id={'type': 'template-type-item', 'index': tt['template_type_id']}, action=True
            )
        return dbc.ListGroupItem(tt['type_name'], id={'type': 'template-type-item', 'index': tt['template_type_id']},
                                 action=True)

    new_list_children = [create_template_item(tt) for tt in template_types]

    alert = dbc.Alert("Template and its tasks have been deleted.", color="danger", duration=3000)
    # Also clear the right-hand panel showing the tasks of the now-deleted template
    cleared_tasks_container = html.P("Select a template type to see its tasks.")

    return False, alert, new_list_children, cleared_tasks_container


# NEW
@callback(
    Output('delete-template-modal', 'is_open', allow_duplicate=True),
    Input('cancel-delete-template-button', 'n_clicks'),
    prevent_initial_call=True
)
def cancel_template_delete(n_clicks):
    if not n_clicks:
        raise dash.exceptions.PreventUpdate
    return False


@callback(Output('report-output-container', 'children'), Input('report-generate-button', 'n_clicks'),
          [State('report-type-dropdown', 'value'), State('report-from-date', 'value'),
           State('report-to-date', 'value')], prevent_initial_call=True)
def generate_date_range_report(n_clicks, report_type, from_date_str, to_date_str):
    if not from_date_str or not to_date_str: return dbc.Alert("Please select a valid date range.", color="warning")
    from_date_obj, to_date_obj = date.fromisoformat(from_date_str), date.fromisoformat(to_date_str)
    if from_date_obj > to_date_obj: return dbc.Alert("'From Date' cannot be after 'To Date'.", color="danger")

    df, cols = (db_fetch_affected_cases_report(from_date_obj, to_date_obj),
                ['case_name', 'status', 'performance', 'case_type', 'start_date',
                 'completed_date']) if report_type == 'Cases' \
        else (db_fetch_affected_tasks_report(from_date_obj, to_date_obj),
              ['case_name', 'task_name', 'status', 'performance', 'due_date'])

    if df.empty: return dbc.Alert(f"No affected {report_type.lower()} found for the selected period.", color="info")

    df['action'] = "View Case"
    table_cols = [{"name": col.replace('_', ' ').title(), "id": col} for col in cols] + [
        {"name": "Action", "id": "action"}]
    return dash_table.DataTable(id='report-table', columns=table_cols, data=df.to_dict('records'),
                                **DATATABLE_STYLE_DARK,
                                style_cell_conditional=[
                                    {'if': {'column_id': 'action'}, 'color': DARK_THEME["colors"]["blue"][5],
                                     'textDecoration': 'underline', 'cursor': 'pointer'}], page_size=20)


@callback(Output('case-status-pie-chart', 'figure'), Output('case-performance-pie-chart', 'figure'),
          Output('task-status-bar-chart', 'figure'),
          Output('task-performance-bar-chart', 'figure'), Output('case-performance-by-type-bar-chart', 'figure'),
          Input('dashboard-generate-button', 'n_clicks'), State('dashboard-from-date', 'value'),
          State('dashboard-to-date', 'value'), prevent_initial_call=True)
def update_dashboard_charts(n_clicks, from_date_str, to_date_str):
    if not from_date_str or not to_date_str: return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    from_date_obj, to_date_obj = date.fromisoformat(from_date_str), date.fromisoformat(to_date_str)
    cases_df, tasks_df = _fetch_dashboard_data(from_date_obj, to_date_obj)

    empty_fig = {"layout": {"xaxis": {"visible": False}, "yaxis": {"visible": False}, "annotations": [
        {"text": "No data for this period", "xref": "paper", "yref": "paper", "showarrow": False,
         "font": {"size": 16}}]}}

    case_status_fig = px.pie(cases_df, names='status', title='Case Status Distribution',
                             hole=.3) if not cases_df.empty else empty_fig
    case_perf_fig = px.pie(cases_df, names='performance', title='Overall Case Performance',
                           hole=.3) if not cases_df.empty else empty_fig
    task_status_fig = px.bar(tasks_df, x='status', title='Task Status by Period',
                             color='status') if not tasks_df.empty else empty_fig
    task_perf_fig = px.bar(tasks_df, x='performance', title='Task Performance by Period',
                           color='performance') if not tasks_df.empty else empty_fig
    case_perf_by_type_fig = px.bar(cases_df, x='case_type', color='performance', title='Case Performance by Case Type',
                                   barmode='group') if not cases_df.empty else empty_fig

    return case_status_fig, case_perf_fig, task_status_fig, task_perf_fig, case_perf_by_type_fig


# =============================================================================
# ATTACHMENT CALLBACKS
# =============================================================================
@callback(
    Output('attachment-modal', 'is_open'),
    Output('attachment-task-id-store', 'data'),
    Output('attachment-modal-title', 'children'),
    Output('attachment-list-container', 'children'),
    Input('detail-tasks-table', 'active_cell'),
    Input('close-attachment-modal', 'n_clicks'),
    State('detail-tasks-table', 'data'),
    State('attachment-modal', 'is_open'),
    prevent_initial_call=True
)
def handle_attachment_modal_visibility(active_cell, n_clicks, data, is_open):
    triggered_id = ctx.triggered_id

    if triggered_id == 'close-attachment-modal':
        return False, dash.no_update, dash.no_update, dash.no_update

    if active_cell and active_cell.get('column_id') == 'attachments':
        task_data = data[active_cell['row']]
        task_id = task_data['task_id']
        task_name = task_data['task_name']

        title = f"Attachments for: {task_name}"
        attachment_list = build_attachments_list(task_id)

        return True, task_id, title, attachment_list

    return is_open, dash.no_update, dash.no_update, dash.no_update


@callback(
    Output('attachment-list-container', 'children', allow_duplicate=True),
    Output('detail-tasks-table-container', 'children', allow_duplicate=True),
    Output('detail-alert-container', 'children', allow_duplicate=True),
    Input('upload-attachment', 'contents'),
    State('upload-attachment', 'filename'),
    State('attachment-task-id-store', 'data'),
    State('detail-case-id-store', 'data'),
    State('session-store', 'data'),
    prevent_initial_call=True
)
def handle_file_upload(list_of_contents, list_of_names, task_id, case_id, session_data):
    if list_of_contents is None:
        raise dash.exceptions.PreventUpdate

    username = (session_data or {}).get('username', 'System')

    for content, name in zip(list_of_contents, list_of_names):
        content_type, content_string = content.split(',')
        decoded = base64.b64decode(content_string)

        file_ext = os.path.splitext(name)[1]
        stored_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(UPLOAD_DIRECTORY, stored_filename)

        with open(file_path, "wb") as fp:
            fp.write(decoded)

        db_add_attachment(task_id, name, stored_filename, username)

    new_attachment_list = build_attachments_list(task_id)
    refreshed_table = build_tasks_table_component(case_id)
    alert = dbc.Alert(f"{len(list_of_names)} file(s) uploaded successfully!", color="success", duration=3000)

    return new_attachment_list, refreshed_table, alert


@callback(
    Output('attachment-list-container', 'children', allow_duplicate=True),
    Output('detail-tasks-table-container', 'children', allow_duplicate=True),
    Output('detail-alert-container', 'children', allow_duplicate=True),
    Input({'type': 'delete-attachment-btn', 'index': ALL}, 'n_clicks'),
    State('attachment-task-id-store', 'data'),
    State('detail-case-id-store', 'data'),
    prevent_initial_call=True
)
def handle_file_delete(n_clicks, task_id, case_id):
    if not any(n_clicks):
        raise dash.exceptions.PreventUpdate

    attachment_id_to_delete = ctx.triggered_id['index']
    db_delete_attachment(attachment_id_to_delete)

    new_attachment_list = build_attachments_list(task_id)
    refreshed_table = build_tasks_table_component(case_id)
    alert = dbc.Alert("Attachment deleted.", color="danger", duration=3000)

    return new_attachment_list, refreshed_table, alert


# =============================================================================
# Main Execution
# =============================================================================
if __name__ == '__main__':
    app.run(debug=True)