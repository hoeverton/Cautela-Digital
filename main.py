import streamlit as st;
import pandas as pd;
#from banco import database as db
import sys




st.title("Cadastro")
st.sidebar.title("Menu")
st.sidebar.selectbox('Policial',['Incluir','Alterar','Excluir','Consultar'])
st.sidebar.selectbox('Cautela diaria',['Incluir','Alterar','Finalizar','Consultar'])

with st.form(key="include_policial"):
    input_nome = st.text_input("Digite Seu Nome")
    input_nomeGuerra = st.text_input("Digite Seu Nome de Guerra")
    input_rg = st.text_input("Digite RG somente numeros")
    input_post_grad = st.selectbox("Selecione Posto ou Graduação",["Ten.Cel","Maj","Cap","1 Ten","2 Ten","Asp","Sub. Ten","1 Sgt","2 Sgt","3 Sgt","Cb","Sd"])
    input_email = st.text_input("Digite seu endereço de e-mail")
    input_senha = st.text_input("Digite sua senha", type="password")
    input_conf_senha = st.text_input("Confirme a  senha", type="password")

    input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        policial.nome_policial = input_nome
        policial.nome_guerra = input_nomeGuerra
        policial.rg = input_rg
        policial.post_grad = input_post_grad
        policial.email = input_email
        policial.senha =input_senha
        policial.confSenha =input_conf_senha
        st.succes("Policial incluido com sucesso!")

    # Valide as senhas
        if input_senha == input_conf_senha:
            # As senhas coincidem, execute a ação desejada aqui
            st.write("Formulário enviado com sucesso!")
        else:
            # As senhas não coincidem, exiba uma mensagem de erro
            st.write("Senha deve ser igual à confirmação de senha!")

#db.update("Eto",1)            