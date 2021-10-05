from fastapi import FastAPI
from pydantic import BaseModel
from tools_pay import *

app = FastAPI()

class Bilhete(BaseModel):
    numeros:str
    email:str

# Rota Raiz
@app.get("/")
def raiz():
    return "OLA MUNDO!"


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
