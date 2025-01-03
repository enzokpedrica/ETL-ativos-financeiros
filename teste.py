import streamlit as st
import yfinance as yf

def carregar_dados (empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_ano = dados_acao.history(period="1d", start = "2001-01-01", end = "2024-12-30")
    cotacoes_ano = cotacoes_ano[["Close"]]
    return cotacoes_ano

dados = carregar_dados("ITUB4.SA")

st.write("teste")
st.line_chart(dados)
st.write("fim")

