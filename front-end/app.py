import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Estoques", page_icon="🗄")

st.header("**Gerenciador de Estoque 📦**")

st.subheader("Bem-vindo ao sistema de gerenciamento de Estoque!")

menu = st.sidebar.radio("Opções", ["Listar Produtos", "Adicionar Produto", "Atualizar Preço do Produto", "Deletar Produto"])
if menu == "Listar Produtos":
    st.subheader("Todos Produtos do estoque")
    response = requests.get(f"{API_URL}/estoque")
    
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])  
        
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado")
    else:
        st.error("Erro ao conectar com a API")

elif menu == "Adicionar Produto":
    st.subheader("➕ Adicionar produto")

    nome = st.text_input("Digite o **Nome do Produto**: ")
    categoria = st.text_input("Digite a **Categoria do Produto**: ")
    preco = st.number_input("Digite o **Preço do Produto**: ", step=0.01)
    quantidade = st.number_input("Digite a **Quantidade** :", step=1)

    if st.button("Salvar Produto 📂"):
        params = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        }

        response = requests.post(f"{API_URL}/estoque", params=params)
        if response.status_code == 200:
            st.success("Produto Adicionado com Sucesso!")
        else:
            st.error("Erro ao Adicionar o Produto")

elif menu == "Atualizar Preço do Produto":
    st.subheader("Atualizar dados de um Produto 📁")

    id_produto = st.number_input("ID do Produto que deseja atualizar", min_value=1, step=1)
    novo_preco = st.number_input("Novo Preço: ", )
    if st.button("Atualizar"):
        dados = {"novo_preco": novo_preco}
        response = requests.put(f"{API_URL}/estoque/{id_produto}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                st.warning(data["erro"])
            else:
                 st.success("Preço atualizado com sucesso")
        else:
             st.error("Erro ao atualizar o preço do produto")


elif menu == "Deletar Produto":
    st.subheader("Deletar um Produto")

    id = st.number_input("Digite o ID do produto que deseja deletar: ", min_value=1, step=1)

    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/estoque/{id}")
        
        if response.status_code == 200:
            data = response.json()

            if "error" in data and data["error"] == "Produto não encontrado":
                st.warning("Produto com esse ID não existe.")
            elif "mensagem" in data:
                st.success(data["mensagem"])
            else:
                st.warning("Resposta inesperada da API.")
        else:
            st.error(f"Erro ao deletar o produto. Código: {response.status_code}")