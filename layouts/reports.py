from datetime import date, timedelta
from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


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