import dash
from .layout import layout  # Import the layout from layout.py
from .callbacks import register_callbacks  # Import the callbacks from callbacks.py
import dash_bootstrap_components as dbc

def main():
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = layout
    register_callbacks(app)
    app.run_server(debug=True)

if __name__ == "__main__":
    main()
