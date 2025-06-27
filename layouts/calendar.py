import pandas as pd
from datetime import date
import calendar

from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from db.queries import db_fetch_tasks_for_date, db_fetch_tasks_for_month



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

