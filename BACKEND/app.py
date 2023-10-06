from flask import Flask, request, jsonify, g
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'library.db'  # Set the path to your SQLite database
CORS(app)

# Define a function to create a new SQLite connection and cursor
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
    cursor = g.db.cursor()
    return g.db, cursor

# Define routes and functions

@app.route('/api/attendreport', methods=['GET'])
def get_attendreport():
    conn, cursor = get_db()  # Create a new connection and cursor
    cursor.execute('SELECT tid, name, d01, d02, d03, d04, d05, d06, d07, d08, d09, d10 FROM attendreport')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            'tid': row[0],
            'name': row[1],
            'd01': row[2],
            'd02': row[3],
            'd03': row[4],
            'd04': row[5],
            'd05': row[6],
            'd06': row[7],
            'd07': row[8],
            'd08': row[9],
            'd09': row[10],
            'd10': row[11]
        })
    conn.close()  # Close the connection
    return jsonify(result)



@app.route('/admin', methods=['GET'])
def get_admins():
    conn, cursor = get_db()  # Create a new connection and cursor
    cursor.execute('SELECT * FROM admin')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            'admin_id': row[0],
            'username': row[1],
            'password': row[2]
        })
    conn.close()  # Close the connection
    return jsonify(result)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Get the JSON data from the request body
    username = data.get('username')
    password = data.get('password')

    # Connect to the SQLite database
    conn, cursor = get_db()

    # Check if the provided username and password match an admin in the 'admin' table
    cursor.execute('SELECT * FROM admin WHERE username = ? AND password = ?', (username, password))
    admin = cursor.fetchone()

    conn.close()  # Close the database connection

    if admin:
        # Authentication successful
        # You may generate a token and return it here if needed
        return jsonify({'success': True, 'message': 'Authentication successful'})
    else:
        # Authentication failed
        return jsonify({'success': False, 'message': 'Authentication failed'})

@app.route('/readers', methods=['GET'])
def get_readers():
    conn, cursor = get_db()  # Create a new connection and cursor
    cursor.execute('SELECT id, name, department, role, number, email FROM readers')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            'id': row[0],
            'name': row[1],
            'department': row[2],
            'role': row[3],
            'number': row[4],
            'email': row[5]
        })
    conn.close()  # Close the connection
    return jsonify(result)

@app.route('/api/tregpost', methods=['POST'])
def issue_book():
    data = request.get_json()  # Get the JSON data from the request body
    isbn = data.get('isbn')
    reader_id = data.get('reader_id')

    # Connect to the SQLite database
    conn, cursor = get_db()

    # Check if the ISBN and reader_id are valid (you can add your validation logic here)

    # Perform the book issuing logic (e.g., update the database)

    # Close the database connection
    conn.close()

    # Return a response (you can customize the response message as needed)
    return jsonify({'message': 'Book issued successfully'})

@app.route('/sreg', methods=['POST'])
def register_student():
    data = request.get_json()  # Get the JSON data from the request body
    tid = data.get('tid')
    tname = data.get('tname')
    depart = data.get('depart')
    mno = data.get('mno')
    email = data.get('email')

    # Connect to the SQLite database
    conn, cursor = get_db()

    # Insert the student data into the 'students' table
    cursor.execute('INSERT INTO students (student_id, student_full_name, department, student_number, email_address) VALUES (?, ?, ?, ?, ?)',
                   (tid, tname, depart, mno, email))

    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the database connection

    # Return a response indicating the successful registration
    return jsonify({'message': 'Student registered successfully'})

@app.route('/treg', methods=['POST'])
def register_teacher():
    try:
        data = request.get_json()
        tid = data.get('tid')
        tname = data.get('tname')
        depart = data.get('depart')
        mno = data.get('mno')
        email = data.get('email')

        # Connect to the SQLite database
        conn, cursor = get_db()

        # Insert data into the 'teachers' table
        cursor.execute(
            "INSERT INTO teachers (teacher_id, teacher_full_name, department, teacher_number, email_address) VALUES (?, ?, ?, ?, ?)",
            (tid, tname, depart, mno, email)
        )

        conn.commit()  # Commit the changes to the database
        conn.close()   # Close the database connection

        response = {
            'message': 'Teacher registered successfully',
            'status': 200
        }

    except Exception as e:
        response = {
            'message': str(e),
            'status': 500
        }

    return jsonify(response)

@app.route('/api/books', methods=['GET'])
def get_books():
    conn, cursor = get_db()
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            'Serial': row[0],
            'Name': row[1],
            'Category': row[2],
            'Author': row[3],
            'ISBN': row[4]
        })
    conn.close()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
