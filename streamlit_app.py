import streamlit as st
import requests
import pandas as pd
import streamlit.components.v1 as components

# Função para formatar preço em reais
def formatar_preco_reais(valor):
    if valor is None:
        return 'Preço não disponível'
    else:
        return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

# URLs atualizadas
consultarItemMaterial_base_url = 'https://dadosabertos.compras.gov.br/modulo-pesquisa-preco/1_consultarMaterial'
consultarItemServico_base_url = 'https://dadosabertos.compras.gov.br/modulo-pesquisa-preco/3_consultarServico'

def obter_itens(tipo_item, codigo_item_catalogo, pagina, tamanho_pagina):
    url = consultarItemMaterial_base_url if tipo_item == 'Material' else consultarItemServico_base_url
    params = {
        'pagina': pagina,   
        'tamanhoPagina':tamanho_pagina,  # Ajuste para 500 itens por página
        'codigoItemCatalogo': codigo_item_catalogo
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            json_response = response.json()
            itens = json_response.get('resultado', [])
            paginas_restantes = json_response.get('paginasRestantes', 0)
            total_paginas = json_response.get('totalPaginas', 0)
            return itens, paginas_restantes, total_paginas
        else:
            st.error(f"Erro na consulta: {response.status_code}")
            return [], 0
    except Exception as e:
        st.error(f"Erro ao realizar a requisição: {str(e)}")
        return [], 0

# Streamlit UI
st.title("PESQUISA DE PREÇOS DE MATERIAIS E/OU SERVIÇOS")    

# Disclaimer
st.markdown("Utilize o catálogo de materiais e serviços do Governo Federal para encontrar o código desejado.")

components.iframe("https://catalogo.compras.gov.br/cnbs-web/busca", height=450, width=720, scrolling=True)

tipo_item = st.selectbox("Selecione o tipo de item para consulta", ['Material', 'Serviço'], key='tipo_item')
codigo_item_catalogo = st.text_input("Código do Item de Catálogo", value="", key='codigo_item_catalogo')
pagina = 1
tamanho_pagina = 500  # Definido para 500 itens por página

if st.button('Consultar'):
    if codigo_item_catalogo:  # Verifica se o código do item de catálogo não está vazio
        itens, paginas_restantes, total_paginas = obter_itens(tipo_item, codigo_item_catalogo, pagina, tamanho_pagina)
        if itens:  # Ensure 'itens' is not empty before proceeding
            st.session_state['itens'] = itens      
        else:
            st.error("Nenhum item encontrado. Por favor, tente com um código diferente ou verifique a conexão com a API.")
    else:
        st.warning("Por favor, informe o código do item de catálogo para realizar a consulta.")

    if st.session_state.get('itens'):
        try:
            # Ensure 'itens' is in the expected format before normalization
            if isinstance(st.session_state['itens'], list) and all(isinstance(item, dict) for item in st.session_state['itens']):
                df_completo = pd.json_normalize(st.session_state['itens'])
                # Apply formatting
                dataframe = df_completo
                mean = dataframe['precoUnitario'].mean()
                median = dataframe['precoUnitario'].median()
                std = dataframe['precoUnitario'].std()
                cv = ((std / mean) * 100)
                st.markdown(
                    f"""
                        |Preço Unitário Médio|Preço Unitário Mediano|Desvio Padrão|Coeficiente de Variação|
                        |:------------------:|:--------------------:|:-----------:|:---------------------:|
                        |**{formatar_preco_reais(mean)}**|**{formatar_preco_reais(median)}**|**{std}**|**{cv}**|
                    """
                )
                df_completo['precoUnitario'] = df_completo['precoUnitario'].apply(formatar_preco_reais)
                st.write(df_completo)
                
                              
                         
            else:
                st.error("Formato dos itens inválido para normalização.")
        except Exception as e:
            st.error(f"Erro ao processar os itens: {str(e)}")
