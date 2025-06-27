from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


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
