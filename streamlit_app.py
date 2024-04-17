# import bibliotecas
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import altair as alt
from streamlit_extras.metric_cards import style_metric_cards
#____________________________________________________________________________________________________________________________________

# Configuração da pagina
st.set_page_config(
    page_title="Dashboard Diabetes",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("##") 
st.title("📊 Dashboard Análise Diabetes")


# st.subheader("🔔 Análise Descritiva com Python e Streamlit")

# alt.themes.enable("dark")
# theme_plotly = None
# with open('style.css')as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
#____________________________________________________________________________________________________________________________________

# Importamos os dados necessarios para analise
# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/LisboaBR/prova1/master/dados_diabetes.csv"

# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url, sep =';')

df = get_data()
df['Diabetes'] = df['diabetes'].map({1: 'Sim', 0: 'Não'})
df['Diabetes'] = df['diabetes'].map({1: 'Sim', 0: 'Não'})
df[['glicose','pressao_sangue','espessura_pele','insulina','IMC']] = df[['glicose','pressao_sangue','espessura_pele','insulina','IMC']].replace(0,np.NaN)

#____________________________________________________________________________________________________________________________________

# Configuramos o menu side bar
with st.sidebar:
    st.title("Prova 1",)
    st.subheader("Análise de dados com python ")
    st.markdown("Professor: Heber Tormentino")
    st.image("img/ufsj-logo.png",caption="UFSJ")
    st.markdown(":black[**Desenvolvido por:**]")
    st.markdown("Aluno: Janos Almeida")
    st.markdown("Matricula: 204400042")
    st.markdown('<a href="mailto:janos.esteves@aluno.ufsj.edu.br">Email contato</a>', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown("[Link notebook - Google Colab](https://colab.research.google.com/drive/11aNfVdSZ5LHvnvs8aPWDdHC3y9sRORX4)")
    st.markdown("[Link arquivos - Gdrive](https://drive.google.com/drive/folders/1-1cLCD04JDN5BkgAoB3ezBnYdvhbHVMo?usp=sharing)")
#
# top-level filters
# job_filter = st.selectbox("Selecione um variável para estudo", pd.unique(df.columns))
# dataframe filter
# df = df[df["job"] == job_filter]
#____________________________________________________________________________________________________________________________________

# Criamos os KPIs

numero_total_pacientes = len(df)

numero_saudaveis, numero_doentes = df['diabetes'].value_counts().values.tolist() 
media_glicose = df['glicose'].mean()
media_idades = df['idade'].mean()
media_pressao = df['pressao_sangue'].mean()
media_insulina = df['insulina'].mean()
media_imc = df['IMC'].mean()
media_risco_diabetes =df['predisposicao_diabetes'].mean()
media_gravidez = df['gravidez'].mean()
#____________________________________________________________________________________________________________________________________

# Criamos dados para graficos
# Criar dicionário com as variáveis
dados_dic = {
    'idade': df['idade'].sort_values().unique(),
    'pressao_media_por_idade': df.groupby('idade')['pressao_sangue'].mean(),
    'glicose_media_por_idade': df.groupby('idade')['glicose'].mean(),
    'insulina_media_por_idade': df.groupby('idade')['insulina'].mean(),
    'IMC_medio_por_idade': df.groupby('idade')['IMC'].mean(),
    'predisposicao_medio_por_idade': df.groupby('idade')['predisposicao_diabetes'].mean(),
    'gravidez_medio_por_idade':df.groupby('idade')['gravidez'].mean()
}

# Criar DataFrame
df_medias_por_idade = pd.DataFrame(dados_dic)

#____________________________________________________________________________________________________________________________________

# Posicionamos os KPIs na pagina:

with st.expander(label=":black[**KPIs**]", expanded=True):
    st.markdown("### Indicadores-Chave de Desempenho 🎯")
    # container_kpis = st.container(border=True)
    # with container_kpis:
    # create columns
    kpi1Col, kpi2Col, kpi3Col, kpi4Col = st.columns(4)
    # fill in those three columns with respective metrics or KPIs
    kpi1Col.metric(
        label=":black[**Pacientes Totais 📌**] ",
        value=round(numero_total_pacientes),
        # delta=round(numero_pacientes) - 10,
    )
    kpi2Col.metric(
        label=":black[**Número de Pacientes com Diabetes :red_circle:**] ",
        value=int(numero_saudaveis),
        # delta=-10 + count_married,
    )
    kpi3Col.metric(
        label=":black[**Glicose Média :syringe:**]",
        value=round(media_glicose,2),
        # delta=-round(balance / count_married) * 100,
    )
    kpi4Col.metric(
        label=":black[**Média de Idades :large_blue_circle:**] ",
        value=round(media_idades,1),
        # delta=-round(balance / count_married) * 100,
    )
    style_metric_cards(background_color="#FFFFFF",border_left_color="#686664",border_color="#000000",box_shadow="#F71938")
    #

    #lista_de_kpis_exibir = ["Pacientes totais","Positivo diabetes","Negativo diabetes","Idade média","Pressão média","Glicose média","Insulina média",
                        # "IMC médio","Risco diabetes médio","Gravidez média"]
    # with st.expander("Escolha os KPIs para exibir"):
    #     showData=st.multiselect('Filtros: ',lista_de_kpis_exibir,default=[],max_selections = 4)
    #     st.write(df[showData])
#
#____________________________________________________________________________________________________________________________________

# Criamos a primeira linha com 3 colunas de graficos
placeholder = st.empty()
with placeholder.container(border=True):
    # create two columns for charts
    fig_col1, fig_col2, fig_col3 = st.columns(3)
    with fig_col1:
        # st.markdown("### Porcentagem de diabéticos e não diabéticos")
        st.markdown("<h4 style='text-align: center;'>Porcentagem de diabéticos e não diabéticos</h4>", unsafe_allow_html=True)
        fig1=px.pie( 
            df, 
            values=df['diabetes'].value_counts().values.tolist(), 
            names= df['Diabetes'].unique(),
            # height=500,
            # width=500,
            hole=.5,
            )
        fig1.update_layout(
            # title={'text':'Porcentagem de diabéticos e não diabéticos',
            # 'x':0.5,
            # 'xanchor': 'center',
            # 'yanchor': 'top', 
            # },
            legend_title="Diabetes"
            )
        # fig1.show()
        st.plotly_chart(fig1,use_container_width=True)
        with st.expander(label="Explicação"):
            st.markdown("""
                        O gráfico acima nos informa que os dados estão desbalanceados. 
                        """)
    with fig_col2:
        # st.markdown("### Quantidade de positivos e negativos")
        st.markdown("<h4 style='text-align: center;'>Número de pacientes com e sem diabetes</h4>", unsafe_allow_html=True)
        fig2=px.bar( 
            df, 
            y = df['Diabetes'].unique(),
            x = df['diabetes'].value_counts().values.tolist(), 
            orientation = 'h',
            color=df['Diabetes'].unique(),
            text_auto=True,
            # height=400,
            # width=400
            )
        fig2.update_layout(
        #         title={'text':'Quantidade de positivos e negativos',
        #             'x':0.5,
        #             'xanchor': 'center',
        #             'yanchor': 'top',},
                    legend_title="Diabetes"
                    )
        fig2.update_yaxes(title='Positivo para diabetes')
        fig2.update_xaxes(title='Quantidade de pacientes')
        st.plotly_chart(fig2,use_container_width=True)
        # st.write(fig2)
        with st.expander(label="Explicação"):
            st.markdown("""
                        O gráfico acima nos informa os valores totais de pacientes com e sem diabetes.
                        """)
    with fig_col3:
        coluna = "glicose"
        # st.markdown(f"### Histograma {coluna}")
        st.markdown(f"<h4 style='text-align: center;'>Histograma {coluna}</h4>", unsafe_allow_html=True)
        fig3=px.histogram(
                        df,
                        x=coluna, 
                        color="Diabetes",
                        # histfunc='sum',
                        # color_discrete_sequence=["yellow", "blue"],
                        # text_auto=True,
                        # height=800,
                        # width=800,
                        # color_continuous_scale='Viridis'
                    )
        fig3.update_layout(
                # title={'text':f'Histograma {coluna}',
                # 'x':0.5,
                # 'xanchor': 'center',
                # 'yanchor': 'top', 
                # },
                # barmode='overlay',
                bargap=0.1,
                )
        fig3.update_xaxes(title=f'Valor {coluna}')
        fig3.update_yaxes(title='Frequência')
        st.plotly_chart(fig3,use_container_width=True)
        # st.write(fig3)
        with st.expander(label="Explicação"):
            st.markdown("""
                        O gráfico acima nos informa como esta a distribuição da variável glicose, que possui grande importancia para análise da diabetes.
                        """)
    #
#
#____________________________________________________________________________________________________________________________________

# Criamos a linha 2 na pagina com 2 colunas de graficos
placeholder2 = st.empty()
with placeholder2.container(border=True):
    fig_col4, fig_col5 = st.columns(2)
    with fig_col4:
        # st.markdown("### Matriz de correlação entre as variáveis")
        st.markdown(f"<h4 style='text-align: center;'>Matriz de correlação entre as variáveis</h4>", unsafe_allow_html=True)
        fig4=px.imshow(df.corr().round(2),
                aspect="auto",
                text_auto=True,
                # height=400,
                # width=400,
                # color_continuous_scale='Viridis'
              )
        # fig3.update_layout(
        #     title={'text':'Matriz de correlação entre as variáveis',
        #         #    'y':1.0,
        #         'x':0.5,
        #         'xanchor': 'center',
        #         'yanchor': 'top', 
        #         })
        # fig.update_xaxes(title='Condição de saúde')
        # fig.update_yaxes(title='Quantidade de pacientes')
        # st.write(fig4)
        st.plotly_chart(fig4,use_container_width=True)
        with st.expander(label="Explicação"):
            st.markdown(
                        """Pelo gráfico acima, as variáveis que apresentam maior correlação com a variável diabetes são:
                         \nglicose, insulina, IMC, espessura da pele e idade."""
                        )
    
    with fig_col5:
        # st.markdown("### Glicose x Pressão sanguínea")
        st.markdown(f"<h4 style='text-align: center;'>Glicose versus pressão sanguínea</h4>", unsafe_allow_html=True)
        fig5=px.scatter(df, 
               x='glicose', 
               y='pressao_sangue',
               color="Diabetes",
            #    hover_name="diabetes",
            #    color_discrete_sequence=["yellow", "blue"],
               log_x=False,
            #    height=400,
            #    width=400
               )
        fig5.update_traces(marker=dict(size=6,line=dict(width=1)),selector=dict(mode='markers'))
        # fig2.update_layout(
        #     title={'text':'Glicose x Pressão sanguínea',
        #         #    'y':1.0,
        #         'x':0.5,
        #         'xanchor': 'center',
        #         'yanchor': 'top', 
        #         })
        fig5.update_xaxes(title='Valor glicose')
        fig5.update_yaxes(title='Pressão sanguínea')
        # st.write(fig5)
        st.plotly_chart(fig5,use_container_width=True)
        with st.expander(label="Explicação"):
            st.markdown(
                        """Podemos concluir análisando o gráfico acima, que a maioria das pessoas
                          com níveis de glicose dentro da normalidade não tem diabetes.
                          """
                        )
    #
#
#____________________________________________________________________________________________________________________________________

# Criamos a linha 3 na pagina com 3 colunas de graficos

placeholder3 = st.empty()
with placeholder3.container(border=True):
    # create two columns for charts
    fig_col6, fig_col7, fig_col8 = st.columns(3)
    with fig_col6:
        st.markdown("<h4 style='text-align: center;'>Glicose média versus idade</h4>", unsafe_allow_html=True)
        fig6=px.line( 
            df_medias_por_idade,
            x=df_medias_por_idade["idade"],
            y="glicose_media_por_idade",
            # height=500,
            # width=500,
            markers=True
            )
        # fig6.update_layout(
        #         title={'text':'Quantidade de positivos e negativos',
        #             'x':0.5,
        #             'xanchor': 'center',
        #             'yanchor': 'top',},
        #             legend_title="Diabetes"
        #             )
        fig6.update_yaxes(title='Valor glicose média')
        fig6.update_xaxes(title='Idade')
        st.plotly_chart(fig6,use_container_width=True)
        # st.write(fig6)
        with st.expander(label="Explicação"):
            st.markdown(
                        """
                        A partir da análise do gráfico acima, podemos inferir que com avanço 
                        da idade, a glicose média das pacientes possuem uma tendência de aumento.
                          """
                        )
    with fig_col7:
        coluna = "IMC"
        # st.markdown(f"### Histograma {coluna}")
        st.markdown(f"<h4 style='text-align: center;'>Histograma {coluna}</h4>", unsafe_allow_html=True)
        fig7=px.histogram(
                        df,
                        x=coluna, 
                        color="Diabetes",
                        # color_discrete_sequence=["yellow", "blue"],
                        # text_auto=True,
                        # height=800,
                        # width=800,
                        # color_continuous_scale='Viridis'
                    )
        fig7.update_layout(
            # title={'text':f'Histograma {coluna}',
            #     #    'y':1.0,
            #     'x':0.5,
            #     'xanchor': 'center',
            #     'yanchor': 'top', 
            #     },
                bargap=0.1
                )
        fig7.update_xaxes(title=f'Valor {coluna}')
        fig7.update_yaxes(title='Frequência')
        st.plotly_chart(fig7,use_container_width=True)
        # st.write(fig7)
        with st.expander(label="Explicação"):
            st.markdown(
                        """
                        Depois da glicose, o IMC, é a segunda variável com maior correlação com a diabetes. O gráfico acima nos mostra como esta sua distribuição.
                          """
                        )
    with fig_col8:
        variavel = "pressao_media_por_idade"
        st.markdown(f"<h4 style='text-align: center;'>Pressão sanguínea média versus idade</h4>", unsafe_allow_html=True)
        fig8=px.line( 
            df_medias_por_idade,
            x=df_medias_por_idade["idade"],
            y="pressao_media_por_idade",
            # height=500,
            # width=500,
            markers=True
            )
        fig8.update_layout(
            # title={'text':'Porcentagem de diabéticos e não diabéticos',
            # 'x':0.5,
            # 'xanchor': 'center',
            # 'yanchor': 'top', 
            # },
            # legend_title="Diabetes",
            )
        fig8.update_yaxes(title='Valor pressão sanguínea média')
        fig8.update_xaxes(title='Idade')
        # fig8.show()
        st.plotly_chart(fig8,use_container_width=True)
        with st.expander(label="Explicação"):
            st.markdown(
                        """
                        A partir da análise do gráfico acima, podemos inferir que com avanço 
                        da idade, a pressão sanguínea média das pacientes possuem uma tendência de aumento.
                          """
                        )
    #
#

#____________________________________________________________________________________________________________________________________

# Criamos a linha 4 na pagina com 2 colunas de graficos
placeholder4 = st.empty()
with placeholder4.container(border=True):
    # create two columns for charts
    fig_col9, fig_col10 = st.columns(2)
    with fig_col9:
        # st.markdown("### Porcentagem de diabéticos e não diabéticos")
        st.markdown("<h4 style='text-align: center;'> Valor pressão sanguínea versus idade</h4>", unsafe_allow_html=True)
        fig9=px.area( 
            df, 
            x="idade", 
            y= "pressao_sangue",
            color="Diabetes"
            # height=500,
            # width=500,
            )
        fig9.update_layout(
            # title={'text':'Porcentagem de diabéticos e não diabéticos',
            # 'x':0.5,
            # 'xanchor': 'center',
            # 'yanchor': 'top', 
            # },
            legend_title="Diabetes"
            )
        fig9.update_yaxes(title='Valor pressão sanguínea')
        fig9.update_xaxes(title='Idade')
        # fig9.show()
        st.plotly_chart(fig9,use_container_width=True)
        with st.expander(label="Explicação"):
            st.markdown("""
                         O gráfico acima nos mostra as pressões sanguíneas das pacientes com e sem diabetes, 
                         e sua relação com a idade.
                        """)
    with fig_col10:
        # st.markdown("### Porcentagem de diabéticos e não diabéticos")
        st.markdown("<h4 style='text-align: center;'> Glicose versus idade</h4>", unsafe_allow_html=True)
        fig10=px.scatter( 
            df, 
            x="glicose", 
            y= "idade",
            color="Diabetes"
            # height=500,
            # width=500,
            )
        fig10.update_traces(marker=dict(size=6,line=dict(width=1)),selector=dict(mode='markers'))
        fig10.update_layout(
            # title={'text':'Porcentagem de diabéticos e não diabéticos',
            # 'x':0.5,
            # 'xanchor': 'center',
            # 'yanchor': 'top', 
            # },
            legend_title="Diabetes"
            )
        fig10.update_yaxes(title='Valor glicose')
        fig10.update_xaxes(title='Idade')
        # fig10.show()
        st.plotly_chart(fig10,use_container_width=True)
        with st.expander(label="Explicação"):
            st.markdown("""
                        Podemos concluir pelo gráfico acima que as pacientes jovens (≈21 a ≈40 anos)
                        e com uma concentração média de glicose, têm menos ocorrência de diabetes.
                        """)                
        #
    #
#
#____________________________________________________________________________________________________________________________________

# st.markdown("""---""")

# x = st.slider(label='x', 
#               )  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# st.markdown("""---""")
#____________________________________________________________________________________________________________________________________
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

#____________________________________________________________________________________________________________________________________
st.markdown("""---""")
if st.checkbox('Exibir base de dados'):
    df
st.markdown("""---""")
##____________________________________________________________________________________________________________________________________
# tab1, tab2 = st.tabs(["Aba 1","Aba 2"])
# with tab1:
#     with st.expander("Expandir"):
#         st.markdown("Oi")
# with tab2.caption("SALES BY PERCENTILES"):
#     c1,c2 = st.columns(2)
#     with c1:
#         st.markdown("ola1")
#     with c2:
#         st.markdown("ola2")
# st.markdown("""---""")
#____________________________________________________________________________________________________________________________________
with st.expander('Sobre'):
    st.write('''
        - Dashboard apresentado como Prova 1 para disciplina Análise de Dados com Python.
        ''')