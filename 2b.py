import sqlite3

conn = sqlite3.connect("specimen_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        username TEXT,
        measured_size REAL,
        magnification REAL,
        real_size REAL
    )
''')

username = input("Enter your name: ")
measured_size = float(input("Enter measured size under microscope (in µm): "))
magnification = float(input("Enter magnification: "))
real_size = measured_size / magnification

cursor.execute('''
    INSERT INTO records (username, measured_size, magnification, real_size)
    VALUES (?, ?, ?, ?)
''', (username, measured_size, magnification, real_size))

conn.commit()
conn.close()

print(f"{username}, your specimen's real-life size is {real_size} µm")
