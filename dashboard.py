import streamlit as st
import pandas as pd
import plotly.express as px
#sd, pd, e px são todos ALIAS, eles NÃO SÃO palavras reservadas

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
#casas decimais separadas por virgula e separações por ;

df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")
#corrigindo os formatos das datas

df["Month"] = df["Date"].apply(lambda x: str(x.year)+ "-" + str(x.month))
month =st.sidebar.selectbox("Mês", df["Month"].unique())
# a 1° linha identifica, traduz e ordena ano e mes, alem de aplicar uma a outro para serem mostrados juntos
#a 2° linha cria a selectbox ao lado esquerdo em uma sidebar


df_filtered = df[df["Month"] == month]


c1,c2 = st.columns(2)
c3,c4,c5 = st.columns(3)
#divide as partes da pagina em colunas ja organizadas DE ACORDO 
#COM A ORDEM DE COMO O CODIGO ESTÁ ESCRITO

graph_day = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
c1.plotly_chart(graph_day, use_container_width=True)

graph_product = px.bar(df_filtered, orientation="h",  x="Date", y="Product line", color="City", title="Faturamento por tipo de produto")
c2.plotly_chart(graph_product, use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
graph_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
c3.plotly_chart(graph_city, use_container_width=True)

graph_tipo = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
c4.plotly_chart(graph_tipo, use_container_width=True)

city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
graph_ava = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")
c5.plotly_chart(graph_ava, use_container_width=True)

df_filtered = df[df["Month"] == month]
df_filtered
