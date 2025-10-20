from fastapi import FastAPI
import funcao

app = FastAPI(title = "Gerenciador de Produtos")

@app.get("/")
def home():
    return {
        "Mensage": "Bem-vindo ao gerenciador de produtos"
    }

@app.get("/produtos")
def catalogo():
    filmes = funcao.listar_produtos()
    lista = []
    for produto in 