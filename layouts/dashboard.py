from datetime import date
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


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

