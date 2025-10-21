readme_content = """
# 📦 Sistema de Gerenciamento de Estoque (Fullstack Python)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Este é um sistema completo para **gerenciamento de estoque**, composto por uma **interface gráfica intuitiva** construída com **Streamlit** e um **backend robusto** baseado em **FastAPI** e **PostgreSQL**.

A aplicação permite a listagem, adição, atualização de preço e remoção de produtos do estoque.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python** | Linguagem principal do projeto. |
| **Streamlit** | Utilizado para criar a interface gráfica (frontend) (`app.py`). |
| **FastAPI** | Framework para criação da API que serve como intermediário entre o frontend e o banco de dados (`api.py`). |
| **PostgreSQL** | Sistema de Gerenciamento de Banco de Dados (SGBD) para armazenamento dos produtos. |
| `psycopg2` | Driver Python para conexão com o PostgreSQL. |
| `python-dotenv` | Para gerenciar variáveis de ambiente e a conexão segura com o DB. |

---

## ⚙️ Funcionalidades

A interface Streamlit oferece as seguintes opções através do menu lateral:

* **Listar Produtos**: Exibe todos os itens cadastrados na tabela `estoque` do PostgreSQL.
* **Adicionar Produto**: Formulário para inserção de um novo produto (nome, categoria, preço e quantidade).
* **Atualizar Preço do Produto**: Permite alterar o preço de um produto existente usando seu ID.
* **Deletar Produto**: Remove um produto do banco de dados utilizando seu ID.

---

## 🚀 Como Rodar o Projeto

Para colocar o projeto no ar, você precisará de **dois processos rodando** simultaneamente: o servidor da API (FastAPI) e a interface gráfica (Streamlit).

### 1. Pré-requisitos

* **Python 3.x** instalado.
* Um servidor **PostgreSQL** rodando (localmente ou em nuvem).

### 2. Configuração do Ambiente

#### 2.1. Variáveis de Ambiente (`.env`)

Crie um arquivo na raiz do projeto chamado `.env` e configure os dados de acesso ao seu banco de dados PostgreSQL:

```env
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432