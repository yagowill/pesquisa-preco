# Pesquisa de Preços - Dados Abertos (Compras Governamentais)

⚡ Ferramenta para agilizar a pesquisa de preços de mercado usando a API de Dados Abertos de Compras do Governo Federal.

🔗 **Acesse a aplicação online:** [https://pesquisa-preco.streamlit.app/](https://pesquisa-preco.streamlit.app/)

> **Nota sobre o Fork:** Este projeto é um fork de uma ferramenta anterior. Aqui, o resultado é exibido na tela e também exportável como CSV, com métricas estatísticas úteis para compor mapas de preços.

## 🎯 Funcionalidades

- Consulta por **Material** ou **Serviço** (selectbox de tipo de item).
- Integração via iframe com o [Catálogo de Materiais e Serviços do Governo Federal](https://catalogo.compras.gov.br/cnbs-web/busca).
- Parâmetros de consulta:
  - `Código do Item de Catálogo` (obrigatório)
  - `Página` (mín 1, padrão 1)
  - `Itens por página` (mín 10, padrão 500)
- Requisição com timeout de 30 segundos (`requests.Timeout`).
- Tratamento de erros:
  - timeout
  - erros HTTP (4xx/5xx)
  - requisições inválidas
- Estatísticas calculadas (a partir de `precoUnitario`):
  - Média
  - Mediana
  - Desvio Padrão
  - Coeficiente de Variação
- Exibição de resultados em tabela (`st.dataframe`) com colunas renomeadas em português.
- Download de CSV com `;` como separador e codificação `utf-8-sig` para Excel.

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Requests

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.8+
- Conexão com internet (API pública do Compras.gov.br)

### Instalação

```bash
pip install -r requirements.txt
```

### Execução

```bash
streamlit run streamlit_app.py
```

A app abrirá em `http://localhost:8501`.

## 📖 Uso da Aplicação

1. Acesse a área de busca do catálogo no iframe e encontre o código do item (`CATMAT` ou `CATSER`).
2. Selecione `Tipo de item` (Material/Serviço).
3. Cole o `Código do Item de Catálogo`.
4. Ajuste `Página` e `Itens por página`, se necessário.
5. Clique em `Consultar`.

### Comportamento esperado

- Se o campo código estiver vazio, aparece aviso de preenchimento obrigatório.
- Ao realizar a consulta, serão exibidos:
  - total de páginas na API
  - páginas restantes
  - estatísticas de preço unitário
  - tabela detalhada de resultados
- Botão para exportar CSV fica disponível quando há resultados.

## 📡 Endpoints

- `https://dadosabertos.compras.gov.br/modulo-pesquisa-preco/1_consultarMaterial`
- `https://dadosabertos.compras.gov.br/modulo-pesquisa-preco/3_consultarServico`

## 🧩 Formato CSV gerado

- Delimitador: `;`
- Codificação: `utf-8-sig` (BOM)
- Colunas renomeadas em português, conforme mapeamento em `streamlit_app.py`.

## 🛠️ Observações de implementação

- Campos `precoUnitario` formatados para exibição em real brasileiro (`R$ xx.xxx,xx`).
- Erros de API são mostrados no app via `st.error`.
- Caso nenhum item seja encontrado, mensagem orienta para verificar o código.
