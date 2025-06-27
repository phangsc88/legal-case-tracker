from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from db.queries import (
    db_fetch_template_types,
    db_add_template_type,
    db_delete_template_type,
    db_fetch_tasks_for_template,
    db_add_task_to_template,
    db_delete_task_from_template,
    db_update_task_template,
)
from utils.performance import calculate_task_performance  # if used
# bring in your shared DataTable‐style and theme
from utils.styles import DATATABLE_STYLE_DARK, DARK_THEME


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
