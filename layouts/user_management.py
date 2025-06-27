from dash import html
import dash_bootstrap_components as dbc
import dash_table
import dash_mantine_components as dmc

import pandas as pd
from db.queries import (
    db_get_all_users,
    db_add_user,
    db_update_user_password,
    db_delete_user
)


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

