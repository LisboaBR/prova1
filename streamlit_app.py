# import bibliotecas
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import altair as alt
from streamlit_extras.metric_cards import style_metric_cards
########################
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

# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/LisboaBR/prova1/master/dados_diabetes.csv"

# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url, sep =';')

df = get_data()
df['Diabetes'] = df['diabetes'].map({1: 'Sim', 0: 'Não'})
df[['glicose','pressao_sangue','espessura_pele','insulina','IMC']] = df[['glicose','pressao_sangue','espessura_pele','insulina','IMC']].replace(0,np.NaN)

with st.sidebar:
    st.title("Prova 1",)
    st.subheader("Análise de dados com python ")
    st.markdown("Professor: Heber Tormentino")
    st.image("img/ufsj-logo.png",caption="UFSJ")
    st.markdown(":black[**Desenvolvido por:**]")
    st.markdown("Aluno: Janos Almeida")
    st.markdown("Matricula: 204400042")
    st.markdown('<a href="mailto:janos.esteves@aluno.ufsj.edu.br">Contato</a>', unsafe_allow_html=True)
    # st.markdown("[Contato](janos.esteves@aluno.ufsj.edu.br)")
#
# top-level filters
# job_filter = st.selectbox("Selecione um variável para estudo", pd.unique(df.columns))
# dataframe filter
# df = df[df["job"] == job_filter]


# creating KPIs
numero_total_pacientes = len(df)

numero_saudaveis, numero_doentes = df['diabetes'].value_counts().values.tolist() 
media_glicose = df['glicose'].mean()


with st.expander(label=":black[**KPIs**]", expanded=True):
    st.markdown("### Indicadores-Chave de Desempenho")
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
        label=":black[**Número de pacientes com diabetes :red_circle:**] ",
        value=int(numero_saudaveis),
        # delta=-10 + count_married,
    )
    kpi3Col.metric(
        label=":black[**Glicose média :syringe:**]",
        value=round(media_glicose,2),
        # delta=-round(balance / count_married) * 100,
    )
    kpi4Col.metric(
        label=":black[**Pacientes Saudáveis :large_blue_circle:**] ",
        value=int(numero_doentes),
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

# tab1, tab2 = st.tabs(["Gráficos gerais","Graficos por Variável"])
# with tab1:#.caption("SALES BY PERCENTILES"):
#     c1,c2 = st.columns(2)
#     with c1:
#         st.markdown("ola1")
#     with c2:
#         st.markdown("ola2")
# with tab2:
#     with st.expander("Expandir"):
#         fig_col1teste, fig_col2teste, = st.columns(2)
#         with fig_col1teste:
#             st.markdown("### Contagem de diabéticos")
#             fig1teste=px.bar( 
#                 df, 
#                 x = ['Saudável','Diabético' ], 
#                 y = df['diabetes'].value_counts().values.tolist(), 
#                 orientation = 'v',
#                 color=['Saudável','Diabético'],
#                 text_auto=True,
#                 height=400,
#                 width=400
#                 )
#             # fig1.update_layout(
#             #         title={'text':'Contagem de diabéticos',
#             #             #    'y':1.0,
#             #             'x':0.5,
#             #             'xanchor': 'center',
#             #             'yanchor': 'top', 
#             #             })
#             fig1teste.update_xaxes(title='Condição de saúde')
#             fig1teste.update_yaxes(title='Quantidade de pacientes')
#             st.write(fig1teste)
            
#         with fig_col2teste:
#             st.markdown("### Glicose x Pressão sanguínea")
#             fig2teste=px.scatter(df, 
#                 x='glicose', 
#                 y='pressao_sangue',
#                 color="Diabetes",
#                 #    hover_name="diabetes",
#                 color_discrete_sequence=["yellow", "blue"],
#                 log_x=False,
#                 height=400,
#                 width=400
#                 );
#             fig2teste.update_traces(marker=dict(size=5,line=dict(width=1)),selector=dict(mode='markers'))
#             # fig2.update_layout(
#             #     title={'text':'Glicose x Pressão sanguínea',
#             #         #    'y':1.0,
#             #         'x':0.5,
#             #         'xanchor': 'center',
#             #         'yanchor': 'top', 
#             #         })
#             fig2teste.update_xaxes(title='Glicose')
#             fig2teste.update_yaxes(title='Pressão sanguínea')
#             st.write(fig2teste)


# st.markdown("""---""")

# # Now insert some more in the container
# container_kpis.write("This is inside too")

placeholder = st.empty()
with placeholder.container(border=True):
    # create two columns for charts
    fig_col1, fig_col2, fig_col3 = st.columns(3)
    with fig_col1:
        st.markdown("### Porcentagem de diabéticos e não diabéticos")
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
                        O gráfico acima nos informa que os dados estão desequilibrados. 
                        """)
    with fig_col2:
        st.markdown("### Contagem de diabéticos")
        fig2=px.bar( 
            df, 
            y = df['Diabetes'].unique(),
            x = df['diabetes'].value_counts().values.tolist(), 
            orientation = 'h',
            # color=df['Diabetes'].unique(),
            text_auto=True,
            # height=400,
            # width=400
            )
        fig2.update_layout(
                title={'text':'Contagem de diabéticos',
                    #    'y':1.0,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top',},
                    legend_title="Diabetes"
                    )
        fig2.update_yaxes(title='Condição de saúde')
        fig2.update_xaxes(title='Quantidade de pacientes')
        st.plotly_chart(fig2,use_container_width=True)
        # st.write(fig2)
        
    with fig_col3:
        coluna = "glicose"
        st.markdown(f"### Histograma {coluna}")
        fig3=px.histogram(
                        df[coluna],
                        x=coluna, 
                        # color="Diabetes",
                        # color_discrete_sequence=["yellow", "blue"],
                        # text_auto=True,
                        # height=800,
                        # width=800,
                        # color_continuous_scale='Viridis'
                    )
        # fig3.update_layout(
        #     title={'text':f'Histograma {coluna}',
        #         #    'y':1.0,
        #         'x':0.5,
        #         'xanchor': 'center',
        #         'yanchor': 'top', 
        #         })
        # fig.update_xaxes(title='Condição de saúde')
        fig3.update_yaxes(title='Frequência')
        st.plotly_chart(fig3,use_container_width=True)
        # st.write(fig3)
    
    
    fig_col4, fig_col5 = st.columns(2)
    with fig_col4:
        st.markdown("### Matriz de correlação entre as variáveis")
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
                        """As características que apresentam maior correlação com a variável alvo são glicose, 
                        insulina, IMC, espessura da pele e idade, conforme visto no gráfico acima."""
                        )
    
    with fig_col5:
        st.markdown("### Glicose x Pressão sanguínea")
        fig5=px.scatter(df, 
               x='glicose', 
               y='pressao_sangue',
               color="Diabetes",
            #    hover_name="diabetes",
            #    color_discrete_sequence=["yellow", "blue"],
               log_x=False,
            #    height=400,
            #    width=400
               );
        fig5.update_traces(marker=dict(size=6,line=dict(width=1)),selector=dict(mode='markers'))
        # fig2.update_layout(
        #     title={'text':'Glicose x Pressão sanguínea',
        #         #    'y':1.0,
        #         'x':0.5,
        #         'xanchor': 'center',
        #         'yanchor': 'top', 
        #         })
        fig5.update_xaxes(title='Glicose')
        fig5.update_yaxes(title='Pressão sanguínea')
        # st.write(fig5)
        st.plotly_chart(fig5,use_container_width=True)
    

# st.markdown("### Visão detalhada dos graficos")
# st.dataframe(df)
st.markdown("""---""")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.markdown("""---""")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

st.markdown("""---""")
if st.checkbox('Mostrar base de dados'):
    df
st.markdown("""---""")
tab1, tab2 = st.tabs(["Aba 1","Aba 2"])
with tab1:
    with st.expander("Expandir"):
        st.markdown("Oi")
with tab2.caption("SALES BY PERCENTILES"):
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("ola1")
    with c2:
        st.markdown("ola2")
st.markdown("""---""")
with st.expander('About', expanded=True):
    st.write('''
        - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
        - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
        - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
        ''')