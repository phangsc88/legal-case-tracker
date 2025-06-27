from dash import dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from db.queries import db_fetch_tasks_for_case, db_fetch_attachments_for_task
from utils.performance import calculate_task_performance
from app32 import DATATABLE_STYLE_DARK


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
