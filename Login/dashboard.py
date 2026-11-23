import streamlit as st
from conexao import conectar

#==============================
# Função Principal da Dashboard
#==============================

def exibir():
    st.title("📊Dashboard Administração")
    st.write(
        f"Bem-vindo(a), {st.session_state.usuario}!"
    )
    # <hr>
    st.divider()

    #========================
    # Menu Lateral
    #========================
    st.sidebar.title("Menu Principal")
    menu = st.sidebar.selectbox(
        "Selecione uma opção",
        [
            "Dashboard",
            "Cadastro de Ussuários",
            "Consultar Usuário"
        ]
    )
    #==============================
    # Botão Sair
    #==============================
    st.sidebar.divider()
    if st.sidebar.button(
        "🚪Sair"
    )
