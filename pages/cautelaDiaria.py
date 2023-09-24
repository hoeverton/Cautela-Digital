import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Cautela Diária")

# Criar um dataframe para armazenar os dados da cautela
cautela = pd.DataFrame(columns=["Data", "Furriel", "Material", "Patrimonio", "Policial", "Assinatura", "Data entrega", "Assinatura Furriel","Em Aberto"])

# Função para adicionar uma nova cautela
def adicionar_cautela(data, furriel, material, patrimonio, policial, assinatura, data_entrega, assinatura_furriel):
    global cautela
    nova_cautela = {"Data": data, "Furriel": furriel, "Material": material, "Patrimonio": patrimonio, 
                    "Policial": policial, "Assinatura": assinatura, "Data entrega": data_entrega, 
                    "Assinatura Furriel": assinatura_furriel}
    cautela = cautela.append(nova_cautela, ignore_index=True)

# Sidebar com opções
st.sidebar.header("Opções")
opcao = st.sidebar.selectbox("Escolha uma opção", ["Visualizar Cautelas", "Adicionar Cautela","Finalizar Cautela"])

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
    materiais = sorted(["Chave VTR", "Chave Seção", "Cal.12", "IA2", "SMT", "HT", "Outros"])
    materiais.remove("Outros")  # Remove "Outros" da lista
    materiais.append("Outros")  # Adiciona "Outros"
    material = st.selectbox("Material", materiais)

    def bando():
      op_bando = ["C/ Bandoleira","S/Bandoleira"]
      bando = st.selectbox("Opção",op_bando  )
    def patrimonio(material):
         if material == "IA2":
            ia2_patrimonios = ["601", "602", "603"]  # Lista de patrimônios para IA2
            patrimonio = st.selectbox("Patrimônio (IA2)", ia2_patrimonios)
            bando()
         else:
            patrimonio = None

         if material == "Chave VTR":
            chave_vtr_patrimonios = ["16165", "1452", "16169"]  # Lista de patrimônios Chave vtr's
            patrimonio = st.selectbox("Patrimônio (Chave VTR)",chave_vtr_patrimonios)
         else:
            patrimonio = None 

         if material == "Chave Seção":
            chave_secao_patrimonios = ["CMDO", "SUb-CMDO", "P1","P3","P4","P5","Furrielação"]  # Lista de patrimônios Seção
            patrimonio = st.selectbox("Patrimônio (Chave SEÇÃO)",chave_secao_patrimonios)
         else:
            patrimonio = None 
         if material == "Cal.12":
            cal12_patrimonios = ["319", "145"]  # Lista de patrimônios para Cal12
            patrimonio = st.selectbox("Patrimônio (Cal.12)",cal12_patrimonios)
            bando()
         else:
            patrimonio = None  
         if material == "SMT":
            smt_patrimonios = ["356", "357"]  # Lista de patrimônios para SMT
            patrimonio = st.selectbox("Patrimônio (SMT)", smt_patrimonios)
            bando()
         else:
            patrimonio = None  
         if material == "Outros":
            patrimonio = st.text_input("Patrimônio")            
            descri = st.text_input("Descrição") 
         else:
            patrimonio = None
         if material == "HT":
            ht_patrimonios = ["335687", "335699"]  # Lista de patrimônios para HT
            patrimonio = st.selectbox("Patrimônio (SMT)", ht_patrimonios)
            ht_acessorio = st.multiselect("Selecione a opção",["Bandoleira","Presilha","SEM"])
         else:
            patrimonio = None    
               
     
     

    patrimonio(material)

    
    
    
    policial = st.text_input("Policial")
    if st.button("Assinatura"):
        pass
    #assinatura = st.text_input("Assinatura")
   # data_entrega = st.date_input("Data de Entrega")     
    
    
    if st.button("Adicionar Cautela"):
        adicionar_cautela(data, furriel, material, patrimonio, policial, assinatura, data_entrega, assinatura_furriel)
        st.success("Cautela adicionada com sucesso!")

# Nota: Você pode adicionar mais recursos, como edição e exclusão de cautelas, validação de entrada, etc.

