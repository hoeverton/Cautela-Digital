import mysql.connector
from mysql.connector import Error

import sys
print(sys.path)
print("------------------")

sys.path.append('C:\cautela virtual\banco')

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Et@drummer1',
        database='cautelavirtual'
    )

    if conexao.is_connected():
        print("Conexão ao banco de dados MySQL foi estabelecida.")

        # Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        #SQL CREATE
        def include(policial):
            comando = f'INSERT INTO policial (nome_policial, nome_guerra,rg,post_grad,email,senha,conf_senha) VALUES (?,?,?,?,?,?,?)',
            valores = (
                policial.nome_policial,
                policial.nome_guerra,
                policial.rg,
                policial.post_grad,
                policial.email,
                policial.senha,
                policial.conf_senha
            )
            cursor.execute(comando, valores)
            conexao.commit()
            print("Inserção bem-sucedida")
        #SQL UPDATE
        def update(self,novo_nome,id_policial):
            novo_nome = novo_nome
            id_policial = id_policial
            comando = f'UPDATE policial SET nome_policial = "{novo_nome}" WHERE idpolicial = {id_policial}'

            # Executar o comando SQL
            cursor.execute(comando)

            # Confirmar a atualização no banco de dados
            conexao.commit()
            print(f"Atualização bem-sucedida para o registro com idpolicial {id_policial}")


        
except Error as e:
    print(f"Erro ao conectar ao banco de dados MySQL: {e}")

finally:
    # Certifique-se de sempre fechar o cursor e a conexão, mesmo em caso de erro
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão ao banco de dados MySQL foi fechada.")
        
novoPolicia =  Policial("João Silva", "João", "123456789", "Sd", "joao@email.com", "senha123", "senha123")
include(novo_policial)