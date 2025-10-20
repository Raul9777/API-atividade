from fastapi import FastAPI
import funcao  

app = FastAPI(title="Gerenciador de Produtos")

@app.get("/")
def home():
    return {
        "Mensagem": "Bem-vindo ao gerenciador de produtos"
    }

@app.get("/produtos")
def catalogo():
    produtos = funcao.listar_produtos() 
    lista = []
    for produto in produtos:  
        lista.append({
            "id": produto[0], 
            "nome": produto[1],  
            "categoria": produto[2],
            "preco": produto[3], 
            "quantidade": produto[4]  
        })
    return {"produtos": lista}
