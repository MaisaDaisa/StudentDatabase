import sqlite3
from Student import Student


class StudentDatabase:

    def __init__(self, name):
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                last_name TEXT,
                gpa REAL,
                faculty TEXT
            )
        """)

    def add_student(self, student):
        self.cursor.execute("""
            INSERT INTO students VALUES 
            (?, ?, ?, ?, ?)
        """, (self.get_last_id()+1, student.name, student.last_name, student.gpa, student.faculty))
        self.conn.commit()

    def update_student(self, last_name, student):
        self.cursor.execute("""
        UPDATE students SET name=?, last_name=?, gpa=?, faculty=?
        WHERE last_name=?
        """, (student.name, student.last_name, student.gpa, student.faculty, last_name))
        self.conn.commit()

    def get_student(self, id):
        self.cursor.execute("""
            SELECT * FROM students WHERE id=?
        """, (id, ))
        row = self.cursor.fetchone()
        return Student(*row[1:])

    def delete_student(self, id):
        self.cursor.execute("""
            DELETE FROM students
            WHERE id=?
        """, (id,))
        self.conn.commit()

    def get_last_id(self):
        self.cursor.execute("""
            SELECT id FROM students ORDER BY id DESC LIMIT 1
        """)
        row = self.cursor.fetchone()
        if row is None:
            return 0
        return row[0]
