# utils/styles.py
import plotly.io as pio

# =============================================================================
# DARK MODE THEME CONFIGURATION
# =============================================================================
DARK_THEME = {
    "colorScheme": "dark",
    "primaryColor": "blue",
    "colors": {
        "dark": [
            "#C1C2C5", "#A6A7AB", "#909296", "#5C5F66",
            "#373A40", "#2C2E33", "#25262B", "#1A1B1E",
            "#141517", "#101113",
        ],
        "blue": [
            "#E7F5FF", "#D0EBFF", "#A5D8FF", "#74C0FC",
            "#4DABF7", "#339AF0", "#228BE6", "#1C7ED6",
            "#1971C2", "#1864AB",
        ],
        "red": [
            "#FFF5F5", "#FFE3E3", "#FFC9C9", "#FFA8A8",
            "#FF8787", "#FF6B6B", "#FA5252", "#F03E3E",
            "#E03131", "#C92A2A"
        ],
    },
    "fontFamily": "'Inter', sans-serif",
    "headings": {"fontFamily": "'Inter', sans-serif", "fontWeight": 600},
}

# Apply custom Plotly template for dark mode
pio.templates["custom_dark"] = pio.templates["plotly_dark"]
pio.templates["custom_dark"].layout.paper_bgcolor = "rgba(0,0,0,0)"
pio.templates["custom_dark"].layout.plot_bgcolor  = "rgba(0,0,0,0)"
pio.templates["custom_dark"].layout.font.color    = DARK_THEME["colors"]["dark"][0]
pio.templates["custom_dark"].layout.title.font.color = DARK_THEME["colors"]["dark"][0]
pio.templates.default = "custom_dark"

# DataTable styles for dark mode
DATATABLE_STYLE_DARK = {
    "style_table": {"overflowX": "auto"},
    "style_header": {
        "backgroundColor": DARK_THEME["colors"]["dark"][6],
        "color": "white",
        "fontWeight": "bold",
        "border": "1px solid " + DARK_THEME["colors"]["dark"][4],
    },
    "style_cell": {
        "backgroundColor": DARK_THEME["colors"]["dark"][7],
        "color": "white",
        "border": "1px solid " + DARK_THEME["colors"]["dark"][4],
        "padding": "10px",
        "textAlign": "left",
    },
    "style_data_conditional": [
        {"if": {"row_index": "odd"}, "backgroundColor": DARK_THEME["colors"]["dark"][6]},
        {"if": {"state": "active"},
         "backgroundColor": DARK_THEME["colors"]["blue"][8],
         "border": "1px solid " + DARK_THEME["colors"]["blue"][5]},
        {"if": {"state": "selected"},
         "backgroundColor": DARK_THEME["colors"]["blue"][9],
         "border": "1px solid " + DARK_THEME["colors"]["blue"][5]},
        # Performance coloring
        {"if": {"filter_query": '{performance} = "Completed On Time"'},
         "backgroundColor": "#1F4B2D", "color": "#E6F4EA"},
        {"if": {"filter_query": '{performance} = "On Time"'},
         "backgroundColor": "#1F4B2D", "color": "#E6F4EA"},
        {"if": {"filter_query": '{performance} = "Completed Late"'},
         "backgroundColor": "#663C00", "color": "#FFECB3"},
        {"if": {"filter_query": '{performance} = "Overdue"'},
         "backgroundColor": "#5C2223", "color": "#FEEBEE"},
        {"if": {"filter_query": '{performance} = "Pending"'},
         "backgroundColor": "#373A40", "color": "#A6A7AB"},
    ],
}
