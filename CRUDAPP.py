# crudApp


import streamlit as st
import pandas as pd

# Aba da aplicação

st.set_page_config(
    page_title="Controle de Estoque",
    page_icon=":shopping_trolley:"
)


def cadastra_produto():
    produto_id = st.text_input('ID')
    produto_nome = st.text_input('Nome')
    produto_preco = st.number_input('Preço', min_value=0.0)
    produto_estoque = st.number_input('Estoque', min_value=0, step=1)

    if st.button('Cadastrar Produto'):
        # Cria um novo dataFrame
        novo_produto = pd.DataFrame({
            'ID': [produto_id],
            'Nome': [produto_nome],
            'Preco': [produto_preco],
            'Estoque': [produto_estoque]
        })

        st.session_state['produtos'] = pd.concat([st.session_state['produtos'], novo_produto], ignore_index=True)
        st.dataframe(st.session_state['produtos'])
        st.success('Produto cadastrado com sucesso!')


# Função para mostrar todos os produtos
def listar_produtos():
    st.subheader("Todos os produtos do Sistema")
    st.dataframe(st.session_state['produtos'])


def apagar_produto():
    lista_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox('Selecione o ID do produto para apagar', lista_produtos)
    if produto_id and st.button('Apagar Produto'):
        # Remove produto pelo ID
        st.session_state['produtos'] = st.session_state['produtos'][st.session_state['produtos']['ID'] != produto_id]
        st.success('Produto apagado com sucesso!')


def alterar_produto():
    lista_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox('Selecione o ID do produto para alterar', lista_produtos)
    if produto_id:
        #localiza o produto pelo iad
        produto = st.session_state['produtos'][st.session_state['produtos']['ID'] == produto_id].iloc[0]
        #Entrada de dados para atualizar produto

        novo_nome=st.text_input('Nome', value=produto['Nome'])
        novo_preco=st.number_input('Preço',min_value=0.0,value=produto['Preco'])
        novo_estoque=st.number_input('Estoque',min_value=0,value=int(produto['Estoque']))

    if st.button('Atualizar Produto'):
        st.session_state['produtos'].loc[
            st.session_state['produtos']['ID']==produto_id, ['Nome','Preco','Estoque']]=[novo_nome,novo_preco,novo_estoque]

        st.success('Produto atualizado com sucesso!')
if __name__ == "__main__":
    st.title('Controle de Estoque')

    # inicializa o DataFrame e salva na sessão
    if 'produtos' not in st.session_state:
        st.session_state['produtos'] = pd.DataFrame(columns=['ID', 'Nome', 'Preco', 'Estoque'])

    # Controle da Ação através de barra lateral

    opcao = st.sidebar.selectbox('Escolha uma opção', [
        'Cadastrar Produto', 'Alterar Produto', 'Apagar Produto', 'Listar todos os Produtos'
    ])
    if opcao == 'Cadastrar Produto':

        cadastra_produto()
    elif opcao == 'Alterar Produto':
        alterar_produto()
    elif opcao == 'Apagar Produto':
        apagar_produto()
    elif opcao == 'Listar todos os Produtos':
        listar_produtos()
