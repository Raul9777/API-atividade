import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciamento de Produtos")

st.title("Gerenciamento de Produtos")

menu = st.sidebar.radio("Menu", ["Produtos"])

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
