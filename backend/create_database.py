import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weight_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT NOT NULL,
    weight REAL NOT NULL,
    status TEXT CHECK(status IN ('Live', 'Recorded'))
)
''')

# Sample data
data = [
    ("2025-06-01 10:00", 50.2, "Live"),
    ("2025-06-01 10:30", 45.2, "Recorded"),
    ("2025-06-01 11:00", 10.2, "Live"),
    ("2025-06-01 11:30", 60.2, "Recorded"),
    ("2025-06-01 12:00", 57.2, "Live"),
    ("2025-06-01 12:30", 65.5, "Recorded"),
    ("2025-06-01 13:00", 20.0, "Live")
]

cursor.executemany("INSERT INTO weight_data (time, weight, status) VALUES (?, ?, ?)", data)

conn.commit()
conn.close()
