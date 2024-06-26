from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import bleach  # Import the bleach library for sanitization

app = Flask(__name__)

# Configure the database connection
db_config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'form'
}

# Sanitization function using bleach
def sanitize_input(input_data):
    return bleach.clean(input_data, tags=[], attributes={}, strip=True)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Collecting form data and sanitizing
    first_name = sanitize_input(request.form.get('firstName'))
    last_name = sanitize_input(request.form.get('lastName'))
    email = sanitize_input(request.form.get('email'))
    country = sanitize_input(request.form.get('country'))
    message = sanitize_input(request.form.get('message'))
    gender = sanitize_input(request.form.get('gender'))
    subjects = ','.join(request.form.getlist('subject'))  # Joining multiple subjects with a comma

    # Insert data into the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO user (first_name, last_name, email, country, message, gender, subjects)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (first_name, last_name, email, country, message, gender, subjects))
    conn.commit()
    cursor.close()
    conn.close()

    # Redirecting to the thank you page with the form data
    return redirect(url_for('thank_you', first_name=first_name))

@app.route('/thank_you')
def thank_you():
    first_name = request.args.get('first_name', 'Guest')
    return render_template('thank_you.html', first_name=first_name)

if __name__ == '__main__':
    # Ensure the table exists
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        country VARCHAR(100) NOT NULL,
        message TEXT NOT NULL,
        gender CHAR(1) NOT NULL,
        subjects VARCHAR(255) NOT NULL
    )
    """)
    conn.close()
    app.run(debug=True)
