import streamlit as st
from conexao import conectar
import dashboard

#=========================
# Configurações da Página
#=========================
st.set_page_config(
    page_title="Sistema de Login",
    page_icon="🔐",
    # o parametro Layout é com letra minuscula
    # Layout="centered"
    layout="centered"
)

#========================
# Controle da Sessão
#========================
if "logado" not in st.session_state:
    # Faltou a variável
    # st.session_state=False
    st.session_state.logado=False
if "usuario" not in st.session_state:
    # Faltou a variável usuario
    # st.session_state=""
    st.session_state.usuario=""

#=================================
# Função para verificação do login
#=================================

def verificar_login(usuario, senha):
    conexao=conectar()

    cursor = conexao.cursor()

    sql="""
        select id, usuario
        from usuarios
        where usuario=%s
        and senha=%s
        """

    cursor.execute(sql, (usuario,senha))

    resultado = cursor.fetchone()

    cursor.close()

    conexao.close()

    return resultado

#======================
# Tela de Login
#======================
# Erro crasso -> if not st.session.state.logado: -> no lugar do ponto é o underline
if not st.session_state.logado:
    st.title("🔐Sistema de Login")
    st.write("Informe suas credenciais para acessar o sistema.")
    st.divider()
    # Erro crasso -> usuario=st.text.input -> underline e não ponto
    usuario=st.text_input(
        "Usuario"
    )
    # Erro crasso -> senha=st.text_input -> underline e não ponto
    
    senha=st.text_input(
        "Senha"
        )

    if st.button("Entrar", use_container_width=True):
        if usuario and senha:
            try:
                resultado=verificar_login(
                    usuario,
                    senha
                )
                if resultado:
                    st.session_state.logado=True
                    st.session_state.usuario = resultado[1]
                    st.success("Acesso autorizado!")
                    # esta instrução não pertence à biblioteca STREAMLIT
                    # st.return -> Código errado
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos")
            except Exception as erro:
                st.error("Erro ao acessar o banco:{erro}")
        else:
            st.warning("Preencha o usuario e a senha!")
#===================================================
# Redirencionando o usuário para o arquivo Dashboard
#===================================================
else:
    dashboard.exibir()