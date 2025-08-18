import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    assistant TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)""")

def save_interaction(user, assistant):
    cursor.execute("INSERT INTO history (user, assistant) VALUES (?, ?)", (user, assistant))
    conn.commit()

def get_last_interactions(limit=5):
    cursor.execute("SELECT user, assistant FROM history ORDER BY id DESC LIMIT ?", (limit,))
    return cursor.fetchall()
