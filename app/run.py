import threading
from app import run_flask_app
from fyp import app as dash_app
from flask import Flask

def run_dash_and_flask():
    # Function to run Dash app
    def run_dash():
        dash_app.run_server(debug=False)

    # Start Dash app in a separate thread
    dash_thread = threading.Thread(target=run_dash)
    dash_thread.start()

    # Run Flask app
    run_flask_app()

    # Wait for Dash thread to finish
    dash_thread.join()

if __name__ == '__main__':
    run_dash_and_flask()
