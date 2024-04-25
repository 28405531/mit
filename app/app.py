from flask import Flask, render_template, request, redirect, url_for, flash
from models import User, create_user, get_user_by_email
from werkzeug.security import check_password_hash
import secrets
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from fyp import app as dash_app
import mysql.connector 
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Flask-Login setup
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing_user = get_user_by_email(email)
        if existing_user:
            flash('Email already exists. Please choose another one.')
        else:
            create_user(email, password)
            flash('Registration successful. Please log in.')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = get_user_by_email(email)

        if user and check_password_hash(user.password, password):
            # Use Flask-Login to log in the user
            login_user(user)

            flash('Login successful.')
            # Redirect to the 'http://127.0.0.1:8050/' URL
            # return redirect('http://127.0.0.1:8050/')
        else:
            flash('Login failed. Check your email and password.')

    return render_template('login.html')

# Function to check if admin login is valid
def is_valid_admin(email, password):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='#Nawu#*13',
        database='api'
    )

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM admin WHERE email = %s"
    values = (email,)

    cursor.execute(query, values)

    admin_data = cursor.fetchone()

    cursor.close()
    connection.close()

    if admin_data and admin_data['password'] == password:
        return True
    else:
        return False

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Simulate admin login
        if is_valid_admin(email,password):
            
            
            flash('Login successful.')
            return redirect(url_for('admin_login'))
        else:
            flash('Login failed. Check your email and password.')

    return render_template('admin.html')
# Database configuration (replace with your actual database configuration)
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '#Nawu#*13',
    'database': 'api'
}



# Function to fetch data from the users table (replace with your actual query)
def fetch_users_data_from_database():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM users"
    cursor.execute(query)

    users_data = cursor.fetchall()

    cursor.close()
    connection.close()

    return users_data





@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    
    users_data = fetch_users_data_from_database()
    
    # user_history_data = fetch_user_history_data_from_database()

    return render_template(
        'admin_login.html',
        
        users_data=users_data,
        
       
    )

def run_flask_app():
    app.run(debug=False)

if __name__ == '__main__':
    app.run(debug=False)
    
    
    
    
    
    
    