import sqlite3

conn = sqlite3.connect("Bildatabase.db")

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS Bildatabase(
    id INTEGER PRIMARY KEY AUTOINCREMENT
    merke TEXT NOT NULL,
    modell REAL,
    km REAL,
    dristoff TEXT NOT NULL,
    pris REAL
          
)
""")

conn.commit()