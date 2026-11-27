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
            "Cadastrar Usuário",
            "Consultar Usuário"
        ]
    )
    #==============================
    # Botão Sair
    #==============================
    st.sidebar.divider()
    if st.sidebar.button(
        "🚪Sair"
    ):
        st.session_state.logado=False
        st.session_state.usuario=""
        st.rerun()
    #================================
    # Opção 1 - Dashboard
    #================================

    if menu == "Dashboard":
        st.subheader("Visão Geral do Sistema")
        conexao=conectar()
        cursor=conexao.cursor()
        cursor.execute(
            "SELECT COUNT(*) FROM usuarios"
        )
        total_usuarios=cursor.fetchone()[0]
        cursor.close()
        conexao.close()
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total de Usuários",
                total_usuarios
            )
        with col2:
            st.metric(
                "Nome do Usuário Conectado",
                st.session_state.usuario
            )
        st.info(
            "Utilize o menu lateral para acessar as funcionalidade"
        )

    #=============================
    # Opção 2 - Cadastrar Usuario
    #=============================

    elif menu == "Cadastrar Usuário":
        st.subheader("Cadastrar Novo Usuário")
        novo_usuario=st.text_input(
            "Nome do Usuario"
        )
        nova_senha=st.text_input(
            "Nova Senha",
            type="password"
        )

        if st.button("Salvar"):
            if novo_usuario and nova_senha:
                conexao=None
                cursor=None

                try:
                    conexao = conectar()
                    cursor=conexao.cursor()

                    sql="""
                        INSERT INTO usuarios
                        (usuario, senha)
                        values(%s,%s)
                    """

                    cursor.execute(
                        sql,
                        (novo_usuario,nova_senha)
                    )

                    conexao.commit()

                    st.success(
                        "Usuário Cadastrado com Sucesso!"
                    )

                except Exception as erro:
                    if conexao:
                        conexao.rollback()
                    st.error(
                        f"Erro ao cadastrar usuario:{erro}"
                    )
                finally:
                    if cursor:
                        cursor.close()
                    if conexao and conexao.is_connected():
                        conexao.close()

        else:
            st.warning("Preencha todos os campos!")

    #============================
    # Opção 3 - Consultar Usuario
    #============================

    elif menu == "Consultar Usuário":
        st.subheader("Usuarios Cadastrados")
        conexao=None
        cursor=None

        try:
            conexao = conectar()
            cursor =  conexao.cursor()

            cursor.execute(
                "SELECT id, usuario FROM usuarios ORDER BY id"
            )

            usuarios=cursor.fetchall()
            if usuarios:
                st.dataframe(
                    usuarios,
                    column_config={
                        0:"ID",
                        1:"Usuário"
                    },
                    # Erro crasso
                    user_container_width=True,
                    hide_index=True
                )

                st.success(
                    f"Total de registros:{len(usuarios)}"
                )
            else:
                st.warning(
                    "Não existem usuários cadastrados"
                )

        except Exception as erro:
            st.error(
                f"Erro ao consultar usuários: {erro}"
            )

        finally:
            if cursor:
                cursor.close()
            if conexao and conexao.is_connected():
                conexao.close()