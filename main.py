from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel
from tools_pay import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Bilhete(BaseModel):
    numeros: List[int]
    email: str

# Rota Raiz
@app.get("/", response_class=HTMLResponse)
def raiz():
    return """
    <html>
        <head>
            <title>Lightning Lottery</title>
        </head>
        <body>
            <h1>Lightning Lottery!</h1>
            <p>
            Esse é um serviço em fase Beta!<br>
            Lighting Lottery é uma loteria que usa a rede lightning do Bitcoin.<br>
            </p>
        </body>
    </html>"""



@app.post("/apostar")
def apostar(bilhete:Bilhete):
    """
    Envie um json(Bilhete) contendo uma Lista de Numeros e um Email!
    Retorna uma tupla com uma invoice e um qrcode em base64!
    """
    return get_invoice(memo=str(bilhete.numeros)+" , "+bilhete.email)

@app.get("/transacoes")
def transacoes():
    return get_transactions()

@app.get("/info")
def info():
    return get_info()
