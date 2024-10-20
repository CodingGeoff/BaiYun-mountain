from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                testimonial TEXT NOT NULL
            )''')
def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/submit_testimonial', methods=['POST'])
def submit_testimonial():
    name = request.form['name']
    email = request.form['email']
    testimonial = request.form['testimonial']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO testimonials (name, email, testimonial) VALUES (?, ?, ?)", (name, email, testimonial))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Testimonial submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)