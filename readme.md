# Pesquisa de Preços - Dados Abertos (Compras Governamentais)

Este projeto é uma ferramenta desenvolvida em Python com [Streamlit](https://streamlit.io/) que permite realizar pesquisas de preços de materiais e serviços utilizando a API de Dados Abertos do Governo Federal (`compras.gov.br`).

> **Nota sobre o Fork:** Este projeto é um *fork* de uma ferramenta anterior que realizava a consulta e gerava apenas um arquivo CSV para download. Nesta versão, o código foi refatorado para exibir os resultados **diretamente na tela**, incluindo o cálculo automático da **Média** e da **Mediana** dos preços unitários encontrados, facilitando a análise rápida de preços de referência.

## 🎯 Funcionalidades

  - **Consulta Flexível:** Permite pesquisar tanto por **Materiais** quanto por **Serviços**.
  - **Busca de Códigos:** Integração via *iframe* com o [Catálogo de Materiais e Serviços do Governo Federal](https://catalogo.compras.gov.br/cnbs-web/busca) para facilitar a localização do `Código do Item`.
  - **Análise Estatística Rápida:** Exibe instantaneamente o **Preço Unitário Médio** e o **Preço Unitário Mediano** dos itens retornados pela API.
  - **Visualização de Dados:** Apresenta a tabela completa de resultados (Dataframe) diretamente na interface do usuário, formatada com valores em Reais (R$).

## 🛠️ Tecnologias Utilizadas

  - [Streamlit](https://streamlit.io/)
  - [Pandas](https://pandas.pydata.org/)
  - [Requests](https://pypi.org/project/requests/)

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual.

1.  Clone este repositório ou baixe os arquivos.
2.  Instale as dependências listadas no arquivo `requirements.txt` executando o seguinte comando no terminal:

<!-- end list -->

```bash
pip install -r requirements.txt
```

### Rodando a Aplicação

Após instalar as dependências, navegue até a pasta do projeto e execute:

```bash
streamlit run streamlit_app.py
```

A aplicação será aberta automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).

## 📖 Como Usar

1.  **Identifique o Código:** Utilize a janela do catálogo (iframe) exibida na tela para buscar o material ou serviço desejado e copiar o seu código (CATMAT ou CATSER).
2.  **Selecione o Tipo:** Escolha entre "Material" ou "Serviço" no menu de seleção.
3.  **Insira o Código:** Cole o código numérico no campo "Código do Item de Catálogo".
4.  **Consultar:** Clique no botão `Consultar`.
5.  **Analise os Resultados:**
      * Veja os indicadores de **Preço Médio** e **Mediana** no topo.
      * Explore a tabela detalhada com todas as compras encontradas logo abaixo.

## 📡 API Utilizada

O sistema consome dados dos seguintes *endpoints* do Portal de Dados Abertos de Compras Governamentais:

  * `modulo-pesquisa-preco/1_consultarMaterial`
  * `modulo-pesquisa-preco/3_consultarServico`