import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# carregando os dados
df_trabalho_rendimento = pd.read_csv('trabalho_rendimento_atualizado.csv')
df_economia = pd.read_csv('economia_atualizada.csv')

# titulo da aplicação
st.title('Análises de Vulnerabilidade Socioeconômica e Potencial de Consumo')

# 1
st.header("1. Comparação: Taxa de Desemprego vs. Renda Média")
fig, ax = plt.subplots()
df_vulnerabilidade = df_trabalho_rendimento[df_trabalho_rendimento['Indicadores'].isin(['Taxa de Desemprego', 'Renda Média'])]
df_vulnerabilidade.set_index('Indicadores', inplace=True)
df_vulnerabilidade.T.plot(kind='bar', ax=ax)
ax.set_ylabel('Valores')
st.pyplot(fig)

# 2
st.header("2. Relação: Benefícios Sociais vs. Crescimento do PIB")
fig, ax = plt.subplots()
df_beneficios = df_trabalho_rendimento[df_trabalho_rendimento['Indicadores'] == 'Benefícios Sociais']
df_pib = df_economia[df_economia['Indicadores'] == 'PIB Crescimento (%)']

# aqui é realizada a combinação de dados para plotagem
df_combinado = pd.concat([df_beneficios.set_index('Indicadores').T, df_pib.set_index('Indicadores').T], axis=1)
df_combinado.columns = ['Benefícios Sociais', 'PIB Crescimento (%)']
df_combinado.plot(kind='bar', ax=ax)
ax.set_ylabel('Valores (%)')
st.pyplot(fig)

# 3
st.header("3. Renda per Capita vs. Oportunidades de Consumo")
fig, ax = plt.subplots()
df_renda_consumo = df_economia[df_economia['Indicadores'] == 'Renda per Capita']
df_renda_consumo.set_index('Indicadores', inplace=True)
df_renda_consumo.T.plot(kind='bar', ax=ax)
ax.set_ylabel('Renda per Capita')
st.pyplot(fig)

# 4
st.header("4. Crescimento da Renda Média vs. Taxa de Emprego")
fig, ax = plt.subplots()
df_renda_emprego = df_trabalho_rendimento[df_trabalho_rendimento['Indicadores'].isin(['Renda Média', 'Taxa de Emprego'])]
df_renda_emprego.set_index('Indicadores', inplace=True)
df_renda_emprego.T.plot(kind='bar', ax=ax)
ax.set_ylabel('Valores')
st.pyplot(fig)