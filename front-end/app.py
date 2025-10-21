import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciamento de Produtos")

st.title("Gerenciamento de Produtos")

menu = st.sidebar.radio("Menu", ["Produtos", "Adicionar Produto"])

if menu == "Produtos":
    st.subheader("Todos os produtos disponíveis")
    response = requests.get(f"{API_URL}/estoque")
    
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            for produto in produtos:
                st.write(f"**{produto['nome']}** ({produto['categoria']}) - {produto['preco']} - {produto['quantidade']}")
        else:
            st.info("Nenhum produto encontrado")
    else:
        st.error("Erro ao obter produtos")

elif menu == "Adicionar Produto":
    st.subheader("Adicionar Produto")
    
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria do produto")
    preco = st.number_input("Preço do produto", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=0, step=1)
    
    if st.button("Salvar Produto"):
        params = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produtos", json=params)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso")
        else:
            st.error("Erro ao adicionar o produto")
