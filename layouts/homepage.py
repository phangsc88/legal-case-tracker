from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

import pandas as pd
from db.queries import (
    db_fetch_all_cases,
    db_fetch_template_types,
    db_add_case,
    db_populate_tasks_from_template,
)

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
