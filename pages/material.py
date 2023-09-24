import streamlit as st
import pandas as pd

# Título da página
st.title("Cadastro de Matérias")

# Criar um dataframe vazio para armazenar as matérias cadastradas
df = pd.DataFrame(columns=["Matéria", "Patrimonio"])

patrimonio = ""

# Sidebar com opções
st.sidebar.header("Opções")
opcao = st.sidebar.selectbox("Escolha uma opção", ["Adicionar", "Alterar","Remover"])


# Entrada de dados para o nome da matéria

materiais = sorted(["Chave VTR", "Chave Seção", "Cal.12", "IA2", "SMT", "HT", "Outros","Carregadores","Munição","Celular","Carregadore Celular"])
materiais.remove("Outros")  # Remove "Outros" da lista
materiais.append("Outros")  # Adiciona "Outros"
material = st.selectbox("Material", materiais)
inf_but_patrimoio = True  # Acesso botão de cadastro de patrimonio

#opçao carregadores 
if material == "Carregadores":
    carregadores =sorted(["IA2","SMT","Beretta","Outros"])
    carregadores.remove("Outros")
    carregadores.append("Outros")
    carregador =st.selectbox("Modelo",carregadores) 
    inf_but_patrimoio = False
   
#opçao Munições    
if material == "Munição":
    lote_muni = st.text_input("Lote")
    cal_muni = st.text_input("Calibre")
    inf_but_patrimoio = False

if material == "Outros":
    material_outros = st.text_input("Digite Material")
    materiais.append(material_outros)
    inf_but_patrimoio = True    

  

# funão butão patrimonio
def butun_patrimonio(inf_but_patrimoio):
    #butun_patrimonio = st.button("Patrimonio")
    if inf_but_patrimoio == True:

        patrimonio = st.text_input("Patrimonio")
butun_patrimonio(inf_but_patrimoio)        


# Entrada de dados para o número de créditos
#creditos = st.number_input("Créditos", min_value=0)

# Menu suspenso para selecionar a categoria
#categorias = ["IA", "Cal12", "SMT","HT","Chaves","Carregador Celular",]
#categoria_selecionada = st.selectbox("Categoria", categorias)

# Botão para cadastrar a matéria
if st.button("Cadastrar"):
    if material != "" : #and codigo_materia != "" and creditos > 0
        # Adicionar os dados da matéria ao dataframe
        df = df.append({"Matéria": material, "Patrimonio": patrimonio}, ignore_index=True)
        st.success("Matéria cadastrada com sucesso!")
        
            

# Exibir as matérias cadastradas
#st.subheader("Matérias Cadastradas")
#st.write(df)
