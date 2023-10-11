import streamlit as st
import pandas as pd
import numpy as np



def carregar_dados(file):
    dados = pd.read_csv(file)
    return dados

def exibir_estatisticas(dados):
    # Calcula as medidas descritivas da variável 'val'
    col1, col2 = st.columns(2)
    with col1:
        # measure =  st.selectbox('Selecione a medida',dados['measure'].unique())
        metric =  st.selectbox('Selecione a métrica',dados['metric'].unique())
        #Inserir condicional a partir de metric
        cause =  st.selectbox('Selecione a causa',dados['cause'].unique())

    with col2:
        location =  st.selectbox('Selecione o local',dados['location'].unique())
        # sex =  dados['sex'].unique()
        # age = st.selectbox('Selecione a faixa etária',dados['age'].unique())
        # year = st.selectbox('Selecione o ano de análise',dados['year'].unique())
        
    dados = dados[(dados['location']==location) & (dados['cause']== cause)]    
    # dados_filtrados = dados[(dados['measure'] == measure) & (dados['metric'] == metric) & (dados['cause'] == cause)
    #                          & (dados['location'] == location) & (dados['sex'] == sex) & (dados['age'] == age) 
    #                          & (dados['year'] == year)]                                                                                      
                             

    # media = dados_filtrados['val'].mean().round(1)
    # soma = dados_filtrados['val'].sum().round(0)
    
    # st.write('**Medidas Descritivas**')
    # if (metric=='Number'):
    #     st.write(f'O número de casos é {soma} casos')
    # else:
    #     st.write(f'A mortalidade é {media} casos a cada 100 mil habitantes')
    # st.data_editor(dados_filtrados)
    # def analise(dados):
    #     st.write('Dados para todos os anos do banco de dados')
    #     dados =  dados.groupby(['cause','sex', 'age'])['val'].sum().reset_index().round(0)
    #     st.write(dados)

    # dadosFiltrados = dados[(dados['location'] == location) & (dados['cause'] == cause)]
    # analise(dadosFiltrados)
    # dados['val'] = dados['val'].apply(lambda x: locale.format_string('%.2f', x))
    #Número de casos por sexo
       


    #Somente óbitos sem Both e sem all ages
    dadosN = dados[(dados['metric'] == 'Number') & (dados['age'] != 'All ages') & (dados['sex'] !='Both')]
    total= dadosN['val'].sum()
    dfSex = dadosN.groupby(['sex'])['val'].sum().reset_index().round()
    dfSex['percentual'] = dfSex['val'] / total * 100
    dfSex['percentual'] = dfSex['percentual'].round(2)
    st.subheader('Sexo')
    st.dataframe(dfSex,hide_index=True)
    # dadosM= dados[(dados['metric'] == 'Rate') & (dados['age'] != 'All ages') & (dados['sex'] !='Both')]
    # mort = dadosM.groupby(['sex'])['val'].mean().reset_index().round(1)
    # st.dataframe(mort,hide_index=True)


    #Dados por faixas etárias
    dadosI = dados[(dados['metric'] == 'Number') & (dados['age'] != 'All ages')  & (dados['sex'] == 'Both')]
    dfIdades = dadosI.groupby(['age'])['val'].sum().reset_index().round(0)
    total= dadosI['val'].sum()
    dfIdades['percentual'] = dfIdades['val'] / total * 100
    dfIdades['percentual'] = dfIdades['percentual'].round(2)
    # arredondar(dfIdades)
    st.subheader('Faixas etárias')
    st.dataframe(dfIdades,hide_index=True)

    #Dados por anos
    dadosAnos = dados[(dados['metric'] == 'Number') & (dados['age'] == 'All ages') & (dados['cause'] == cause) & (dados['sex'] == 'Both')]
    total= dadosAnos['val'].sum()
    dflocais= dadosAnos.groupby(['location'])['val'].sum().reset_index().round(0)
    dflocais['percentual'] = dflocais['val'] / total * 100
    dflocais['percentual'] = dflocais['percentual'].round(1)
    st.subheader('Local')
    st.dataframe(dflocais,hide_index=True)

    #Locais
    dadosLocais = dados[(dados['metric'] == 'Number') & (dados['age'] == 'All ages') & (dados['cause'] == cause) & (dados['sex'] == 'Both')]
    total= dadosLocais['val'].sum()
    dfLocal= dadosLocais.groupby(['year'])['val'].sum().reset_index().round(0)
    dfLocal['percentual'] = dfLocal['val'] / total * 100
    dfLocal['percentual'] = dfLocal['percentual'].round(1)
    st.subheader('Ano(s)')
    st.dataframe(dfLocal,hide_index=True)


 
    
    


def main():
    st.title('Dashboard Interativo de Análise de Dados')
    file = st.file_uploader('Faça o upload do seu arquivo CSV aqui', type='csv')
    
    if file is not None:
        dados = carregar_dados(file)
        exibir_estatisticas(dados)
       
        
        

if __name__ == '__main__':
    main()
