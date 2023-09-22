import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Cautela Diária")

# Criar um dataframe para armazenar os dados da cautela
cautela = pd.DataFrame(columns=["Data", "Furriel", "Material", "Patrimonio", "Policial", "Assinatura", "Data entrega", "Assinatura Furriel"])

# Função para adicionar uma nova cautela
def adicionar_cautela(data, furriel, material, patrimonio, policial, assinatura, data_entrega, assinatura_furriel):
    global cautela
    nova_cautela = {"Data": data, "Furriel": furriel, "Material": material, "Patrimonio": patrimonio, 
                    "Policial": policial, "Assinatura": assinatura, "Data entrega": data_entrega, 
                    "Assinatura Furriel": assinatura_furriel}
    cautela = cautela.append(nova_cautela, ignore_index=True)

# Sidebar com opções
st.sidebar.header("Opções")
opcao = st.sidebar.selectbox("Escolha uma opção", ["Visualizar Cautelas", "Adicionar Cautela"])

# Páginas do aplicativo
if opcao == "Visualizar Cautelas":
    st.subheader("Cautelas Cadastradas")
    st.dataframe(cautela)

elif opcao == "Adicionar Cautela":
    st.subheader("Adicionar Nova Cautela")
    data = st.date_input("Data")
    furriel = st.text_input("Furriel")
    if st.button("Assinatura Furriel"):
        pass
    material = st.selectbox("Material",["Chave VTR","Chave Seção","Cal.12","IA2","SMT","HT"])
    patrimonio = st.text_input("Patrimônio")
    policial = st.text_input("Policial")
    if st.button("Assinatura"):
        pass
    #assinatura = st.text_input("Assinatura")
   # data_entrega = st.date_input("Data de Entrega")     
    
    
    if st.button("Adicionar Cautela"):
        adicionar_cautela(data, furriel, material, patrimonio, policial, assinatura, data_entrega, assinatura_furriel)
        st.success("Cautela adicionada com sucesso!")

# Nota: Você pode adicionar mais recursos, como edição e exclusão de cautelas, validação de entrada, etc.
