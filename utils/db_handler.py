import sqlite3

DB_NAME = "bakery.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price REAL NOT NULL
        )
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password, role)
        VALUES ('admin', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 'admin')
    ''')

    default_items = [
        ('Cake', 120.0),
        ('Bread', 40.0),
        ('Donut', 30.0),
        ('Cookie', 20.0)
    ]
    cursor.executemany('''
        INSERT OR IGNORE INTO menu (name, price) VALUES (?, ?)
    ''', default_items)

    conn.commit()
    conn.close()