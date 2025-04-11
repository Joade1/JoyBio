import tkinter as tk
from tkinter import messagebox
import sqlite3

def save_data():
    username = entry_name.get()
    measured = float(entry_measured.get())
    magnification = float(entry_magnification.get())
    real = measured / magnification

    conn = sqlite3.connect("specimen_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (username, measured_size, magnification, real_size) VALUES (?, ?, ?, ?)",
                   (username, measured, magnification, real))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Result", f"{username}, real size is {real:.2f} µm")

app = tk.Tk()
app.title("Specimen Size Calculator")

tk.Label(app, text="Name").pack()
entry_name = tk.Entry(app)
entry_name.pack()

tk.Label(app, text="Measured Size (µm)").pack()
entry_measured = tk.Entry(app)
entry_measured.pack()

tk.Label(app, text="Magnification").pack()
entry_magnification = tk.Entry(app)
entry_magnification.pack()

tk.Button(app, text="Calculate & Save", command=save_data).pack()

app.mainloop()