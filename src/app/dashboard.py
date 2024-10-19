import dash
from .layout import layout  # Import the layout from layout.py
from .callbacks import register_callbacks  # Import the callbacks from callbacks.py
import dash_bootstrap_components as dbc

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Set the layout of the app
app.layout = layout

# Register the callbacks
register_callbacks(app)  # Call the function to register all callbacks

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
