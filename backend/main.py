import sqlite3

from typing import Annotated
from fastapi import FastAPI
from typing import List, Dict
from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse

app = FastAPI()

# Функция для подключения к базе данных и создания таблицы
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        point INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Вызов функции для инициализации базы данных при запуске
init_db()

# Функция для получения всех данных из таблицы users
def get_users() -> List[Dict[str, any]]:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, point FROM users')
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "username": row[1], "point": row[2]} for row in rows]

@app.get("/user/api")
async def user():
    users = get_users()
    return {"users": users}

@app.post("/add/")
async def login(name: Annotated[str, Form()], points: Annotated[str, Form()]):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (username, point)
        VALUES (?, ?)
    ''', (name, points))
    conn.commit()
    conn.close()
    return RedirectResponse(url="http://localhost:4321/", status_code=302)

@app.get("/dell/{id}")
async def dell_user(id: int):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return RedirectResponse(url="http://localhost:4321/", status_code=302)
