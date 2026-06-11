from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("Bildatabase.db", check_same_thread=False)

c = conn.cursor()



c.execute("""
CREATE TABLE IF NOT EXISTS Bildatabase(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    merke TEXT NOT NULL,
    modell REAL,
    km REAL,
    dristoff TEXT NOT NULL,
    pris REAL
          
)
""")

conn.commit()

def PUS():
    c.execute( "INSERT INTO Bildatabase (merke, modell, km, dristoff, pris) VALUES (?,?,?,?,?)",
              ("NIO", 2014, 1400, "BN", 500000))
    conn.commit()

print("------------------------")

def get_id():
    c.execute("SELECT * FROM Bildatabase WHERE id = ?", (3,))
    res = c.fetchall()
    return jsonify(res)

def update():
    c.execute("UPDATE Bildatabase SET pris = ? WHERE id = ?", (200000, 2))
    conn.commit()

def delite():
    c.execute("DELETE FROM Bildatabase WHERE id = ?", (6, ))
    conn.commit()


@app.route("/bil") #har brukt ai fra denn elinjen til neste linje
def bil():
    c.execute("SELECT * FROM Bildatabase")
    data = c.fetchall()

    return jsonify(data)

app.run(debug=True) #har brukt ai til hit