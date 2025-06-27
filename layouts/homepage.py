from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from db.queries import db_fetch_template_types
from db.queries import db_fetch_all_cases, db_add_case, db_populate_tasks_from_template

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
