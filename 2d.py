from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = size = None
    if request.method == "POST":
        name = request.form["username"]
        measured = float(request.form["measured"])
        magnification = float(request.form["magnification"])
        size = round(measured / magnification, 2)

        conn = sqlite3.connect("specimen_data.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO records (username, measured_size, magnification, real_size) VALUES (?, ?, ?, ?)",
                       (name, measured, magnification, size))
        conn.commit()
        conn.close()

    return render_template("index.html", name=name, size=size)

if __name__ == "__main__":
    app.run(debug=True)
