from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import sqlite3
from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("templates"))

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        template = env.get_template("index.html")
        response = template.render(name=None, size=None)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode())

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = self.rfile.read(length).decode()
        data = parse_qs(body)

        username = data.get("username", [""])[0]
        measured = float(data.get("measured", ["0"])[0])
        magnification = float(data.get("magnification", ["1"])[0])
        size = round(measured / magnification, 2)

        conn = sqlite3.connect("/tmp/specimen.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS records (username TEXT, measured_size REAL, magnification REAL, real_size REAL)")
        cursor.execute("INSERT INTO records VALUES (?, ?, ?, ?)", (username, measured, magnification, size))
        conn.commit()
        conn.close()

        template = env.get_template("index.html")
        response = template.render(name=username, size=size)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode())
