import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import joblib
import mysql.connector
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import Flask, request  # Correct import statement
from datetime import datetime
from flask import redirect, url_for
from flask import Flask, render_template



db_connection = {}

# Initialize the Dash app
app = dash.Dash(__name__)


# Configure MySQL connection
mysql_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'api'
}

# Establish MySQL connection
connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()





    
if __name__ == '__main__':
    app.run_server(debug=False)
    db_connection.close()
    