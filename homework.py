import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        group_name TEXT
    )
''')

students_data = [
    ('Иван', 'Иванов', 20, 'Группа 1'),
    ('Петр', 'Петров', 21, 'Группа 2'),
    ('Мария', 'Сидорова', 19, 'Группа 1')
]

cursor.executemany('''
    INSERT INTO Students (first_name, last_name, age, group_name)
    VALUES (?, ?, ?, ?)
''', students_data)

conn.commit()
conn.close()
