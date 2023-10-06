import sqlite3

# SQLite database connection
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Insert sample data into the `attendreport` table
attendreport_data = [
    (101, 'John', 'P', 'A', 'W', 'P', 'A', 'P', 'P', 'W', 'A', 'P'),
    (102, 'Alice', 'P', 'A', 'W', 'W', 'P', 'A', 'A', 'P', 'W', 'A'),
    (103, 'Bob', 'A', 'P', 'P', 'P', 'W', 'P', 'A', 'W', 'A', 'P'),
    (104, 'Eve', 'P', 'P', 'P', 'A', 'W', 'A', 'A', 'P', 'W', 'P'),
    (105, 'Charlie', 'A', 'A', 'A', 'W', 'W', 'W', 'P', 'P', 'A', 'A'),
    (106, 'David', 'P', 'A', 'P', 'P', 'P', 'P', 'W', 'A', 'A', 'W'),
    (107, 'Grace', 'W', 'W', 'W', 'P', 'P', 'P', 'P', 'A', 'A', 'P'),
]

cursor.executemany('INSERT INTO attendreport (tid, name, d01, d02, d03, d04, d05, d06, d07, d08, d09, d10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', attendreport_data)

# Insert sample data into the `book` table
book_data = [
    (1, 'Book 1', 'Author 1', '123456789'),
    (2, 'Book 2', 'Author 2', '987654321'),
    (3, 'Book 3', 'Author 3', '111111111'),
    (4, 'Book 4', 'Author 4', '222222222'),
    (5, 'Book 5', 'Author 5', '333333333'),
    (6, 'Book 6', 'Author 6', '444444444'),
    (7, 'Book 7', 'Author 7', '555555555'),
]

cursor.executemany('INSERT INTO book (book_id, title, author, isbn) VALUES (?, ?, ?, ?)', book_data)

# Insert sample data into the `admin` table
admin_data = [
    (4, 'newuser1', 'password4'),
    (5, 'newuser2', 'password5'),
    (6, 'newuser3', 'password6'),
    # Add more sample data here
]

cursor.executemany('INSERT INTO admin (admin_id, username, password) VALUES (?, ?, ?)', admin_data)

# Insert sample data into the `readers` table
readers_data = [
    (1, 'Kimeu', 'Math', 'teacher', '1234567890', 'kimeu@example.com'),
    (2, 'Mugecha ', 'Science', 'student', '9876543210', 'mugecha@example.com'),
    (3, 'Kamunya', 'English', 'teacher', '5555555555', 'kamunya@example.com'),
    (4, 'Nelson', 'History', 'student', '1111111111', 'nelsonk2@example.com'),
    (5, 'Mute', 'Physics', 'teacher', '9999999999', 'mute@example.com'),
    (6, 'Sally', 'Chemistry', 'student', '8888888888', 'sally3@example.com'),
    (7, 'Gatimu', 'Biology', 'teacher', '7777777777', 'gatimu@example.com'),
]

cursor.executemany('INSERT INTO readers (id, name, department, role, number, email) VALUES (?, ?, ?, ?, ?, ?)', readers_data)

# Insert sample data into the `issue_book` table
issue_book_data = [
    (1, '2023-10-10', 1),
    (2, '2023-10-15', 2),
    (3, '2023-10-20', 3),
    (4, '2023-10-25', 4),
    (5, '2023-10-30', 5),
    (6, '2023-11-05', 6),
    (7, '2023-11-10', 7),
]

cursor.executemany('INSERT INTO issue_book (issue_id, return_date, readers_id) VALUES (?, ?, ?)', issue_book_data)

# Commit the changes and close the connection
conn.commit()
conn.close()
