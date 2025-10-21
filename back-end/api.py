from fastapi import FastAPI
import funcao  

app = FastAPI(title="Gerenciador de Produtos")

@app.get("/estoque")
def home():
    return {"Mensagem": "Bem-vindo ao gerenciador de produtos"}

@app.get("/estoque/catalogo")
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
    return {"estoque": lista}

@app.post("/estoque")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.criar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso"}

@app.put("/produtos/{id_produto}")
def atualizar_produto(id_produto: int, novo_preco: float):
    funcao.atualizar_preco(id_produto, novo_preco)
    produto = funcao.atualizar_produto(id_produto)
    if produto:
        return {"mensagem": "Produto atualizado com sucesso"}
    return {"erro": "Produto não encontrado"}

@app.delete("/estoque/{id_produto}")
def deletar_produto(id_produto: int):
    deletar = funcao.deletar_produto(id_produto)
    if deletar:
        funcao.deletar_produto(id_produto)
        return {"mensagem": "Produto excluído com sucesso"}
    return {"erro": "Produto não encontrado"}