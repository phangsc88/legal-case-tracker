from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import pandas as pd # <--- ADDED THIS IMPORT for pd.DataFrame and pd.notnull

# bring in all four DB functions you actually use here
from db.queries import (
    db_fetch_single_case,
    db_fetch_case_due_date,
    db_fetch_tasks_for_case,
    db_fetch_attachments_for_task,
    db_fetch_remarks_for_case,
)

# your shared theme & styles
from utils.styles import DARK_THEME, DATATABLE_STYLE_DARK

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


# =============================================================================
# REPLACEMENT for build_tasks_table_component (Now in layouts/case_detail.py)
# =============================================================================
# --- CORRECTED FUNCTION SIGNATURE: MUST ACCEPT 'privilege' ---

# In layouts/case_detail.py

def build_tasks_table_component(case_id: int, privilege: str):
    tasks_df = db_fetch_tasks_for_case(case_id)
    is_editor_or_admin = (privilege in ['Admin', 'Editor'])

    if tasks_df.empty:
        return dbc.Alert("No tasks for this case.", color="info", className="mt-3")

    table_data = tasks_df.to_dict('records')

    if is_editor_or_admin:
        for row in table_data:
            row['action'] = 'Edit'

    table_columns = [
        {"name": "Task Name", "id": "task_name"},
        {"name": "Status", "id": "status"},
        {"name": "Performance", "id": "performance"},
        {"name": "Due Date", "id": "due_date_display"},
        {"name": "Start Date", "id": "task_start_date"},
        {"name": "Completed Date", "id": "task_completed_date"},
        {"name": "Last Updated By", "id": "last_updated_by"},
        {"name": "Last Update Date", "id": "last_updated_at_display"},
    ]

    if is_editor_or_admin:
        table_columns.append({"name": "Action", "id": "action"})

    # --- THIS IS THE FIX ---

    # 1. Start with your base styles
    table_styles = DATATABLE_STYLE_DARK.copy()

    # 2. Define the new conditional styles for performance
    performance_styles = [
        {'if': {'filter_query': '{performance} = "Completed On Time"'}, 'backgroundColor': '#1F4B2D',
         'color': '#E6F4EA'},
        {'if': {'filter_query': '{performance} = "On Time"'}, 'backgroundColor': '#1F4B2D', 'color': '#E6F4EA'},
        {'if': {'filter_query': '{performance} = "Completed Late"'}, 'backgroundColor': '#663C00', 'color': '#FFECB3'},
        {'if': {'filter_query': '{performance} = "Overdue"'}, 'backgroundColor': '#5C2223', 'color': '#FEEBEE'},
        {'if': {'filter_query': '{performance} = "Pending"'}, 'backgroundColor': '#373A40', 'color': '#A6A7AB'},
    ]

    # 3. Combine the new styles with any existing styles
    #    This ensures we don't pass the same argument twice.
    if 'style_data_conditional' in table_styles:
        table_styles['style_data_conditional'].extend(performance_styles)
    else:
        table_styles['style_data_conditional'] = performance_styles

    # Add the action column style to the cell conditional styles
    action_style = {'if': {'column_id': 'action'},
                    'width': '80px', 'textAlign': 'center',
                    'color': DARK_THEME["colors"]["blue"][3],
                    'textDecoration': 'underline', 'cursor': 'pointer'}

    if 'style_cell_conditional' in table_styles:
        table_styles['style_cell_conditional'].append(action_style)
    else:
        table_styles['style_cell_conditional'] = [action_style]

    # 4. Create the DataTable, passing the combined styles dictionary
    return dash_table.DataTable(
        id='detail-tasks-table',
        columns=table_columns,
        data=table_data,
        markdown_options={"html": True},
        **table_styles  # Unpack all the combined styles here
    )

# --- build_case_detail_layout (itself) ---
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
        html.Div(id='detail-tasks-table-container', children=build_tasks_table_component(case_id, privilege)), # <--- ADDED COMMA HERE

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
