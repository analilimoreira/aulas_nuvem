from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import mysql.connector

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Conexão com o MySQL (container 'db')
def get_db():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="senha",
        database="meubanco"
    )

# Rota para a interface web
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT nome FROM usuarios")
    usuarios = [row[0] for row in cursor.fetchall()]
    cursor.close()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "usuarios": usuarios})

# Rota para adicionar usuário (POST)
@app.post("/add_user")
async def add_user(nome: str = Form(...)):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (%s)", (nome,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Usuário adicionado!"}