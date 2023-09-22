import streamlit as st
import pandas as pd

# Título da página
st.title("Cadastro de Matérias")

# Criar um dataframe vazio para armazenar as matérias cadastradas
df = pd.DataFrame(columns=["Nome da Matéria", "Código da Matéria", "Créditos", "Categoria"])

# Entrada de dados para o nome da matéria
nome_materia = st.text_input("Nome da Matéria")

# Entrada de dados para o código da matéria
codigo_materia = st.text_input("Código da Matéria")

# Entrada de dados para o número de créditos
creditos = st.number_input("Créditos", min_value=0)

# Menu suspenso para selecionar a categoria
categorias = ["IA", "Cal12", "SMT"]
categoria_selecionada = st.selectbox("Categoria", categorias)

# Botão para cadastrar a matéria
if st.button("Cadastrar"):
    if nome_materia != "" and codigo_materia != "" and creditos > 0:
        # Adicionar os dados da matéria ao dataframe
        df = df.append({"Nome da Matéria": nome_materia, "Código da Matéria": codigo_materia, "Créditos": creditos, "Categoria": categoria_selecionada}, ignore_index=True)
        st.success("Matéria cadastrada com sucesso!")

# Exibir as matérias cadastradas
st.subheader("Matérias Cadastradas")
st.write(df)
