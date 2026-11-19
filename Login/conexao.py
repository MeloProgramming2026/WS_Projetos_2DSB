import mysql.connector

# ==============================
# CONEXÃO COM MYSQL
# ==============================

def conectar():

    conexao = mysql.connector.connect(

        host="localhost",
        user="root",
        password="",
        database="sistema_login"

    )

    return conexao
