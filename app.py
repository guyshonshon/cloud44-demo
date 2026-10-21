"""Cloud44 demo: a small notes board on Flask and PostgreSQL.

It reads its database from DATABASE_URL and listens where gunicorn binds it (see the Dockerfile).
"""

import os

import psycopg
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://demo:demo@localhost:5432/demo")


def db():
    return psycopg.connect(DATABASE_URL, autocommit=True)


def init_db():
    with db() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS notes ("
            " id serial PRIMARY KEY,"
            " body text NOT NULL CHECK (length(body) BETWEEN 1 AND 280),"
            " created_at timestamptz NOT NULL DEFAULT now())"
        )


@app.get("/")
def index():
    with db() as conn:
        notes = conn.execute("SELECT body, created_at FROM notes ORDER BY id DESC LIMIT 50").fetchall()
    return render_template("index.html", notes=notes)


@app.post("/notes")
def add_note():
    body = request.form.get("body", "").strip()[:280]
    if body:
        with db() as conn:
            conn.execute("INSERT INTO notes (body) VALUES (%s)", (body,))
    return redirect(url_for("index"))


@app.get("/healthz")
def healthz():
    with db() as conn:
        conn.execute("SELECT 1")
    return {"status": "ok"}


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0")
