import mysql.connector

# ==============================
# CONEXÃO COM MYSQL
# ==============================

def conectar():

    conexao = mysql.connector.connect(

        host="localhost",
        user="bucefalo",
        password="123456",
        database="sistema_login"

    )

    return conexao
