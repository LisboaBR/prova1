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
st.title(":bar_chart: Dashboard análise diabetes")
# st.subheader("🔔 Análise Descritiva com Python e Streamlit")

alt.themes.enable("dark")
# theme_plotly = None

# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/LisboaBR/prova1/master/dados_diabetes.csv"

# read csv from a URL
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url, sep =';')

df = get_data()
df['Diabetes'] = df['diabetes'].map({1: 'Sim', 0: 'Não'})
df[['glicose','pressao_sangue','espessura_pele','insulina','IMC']] = df[['glicose','pressao_sangue','espessura_pele','insulina','IMC']].replace(0,np.NaN)


st.sidebar.image("img/ufsj-logo.png",caption="UFSJ")
st.sidebar.markdown("Desenvolvido por Janos - [Contato](janos.esteves@aluno.com.br)")

# top-level filters
# job_filter = st.selectbox("Selecione um variável para estudo", pd.unique(df.columns))

# creating a single-element container


# dataframe filter
# df = df[df["job"] == job_filter]

# near real-time / live feed simulation
# for seconds in range(200):

# df["age_new"] = df["age"] * np.random.choice(range(1, 5))
# df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

# creating KPIs
numero_total_pacientes = len(df)

numero_saudaveis, numero_doentes = df['diabetes'].value_counts().values.tolist() 
# count_married = int(
#     df[(df["marital"] == "married")]["marital"].count()
#     + np.random.choice(range(1, 30))
# )


def configura_kpis():
    container_kpis = st.container(border=True)
    with container_kpis:
        # create three columns
        kpi1Col, kpi2Col, kpi3Col, kpi4Col = st.columns(4)

        # fill in those three columns with respective metrics or KPIs
        kpi1Col.metric(
            label="Pacientes Totais 📌",
            value=round(numero_total_pacientes),
            # delta=round(numero_pacientes) - 10,
        )
        
        kpi2Col.metric(
            label="Positivo para diabetes ",
            value=int(numero_saudaveis),
            # delta=-10 + count_married,
        )
        
        kpi3Col.metric(
            label="Pacientes Saudáveis ",
            value=int(numero_doentes),
            # delta=-round(balance / count_married) * 100,
        )

        kpi4Col.metric(
            label="Outros ",
            value=int(0),
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

configura_kpis()

# st.markdown("""---""")

# # Now insert some more in the container
# container_kpis.write("This is inside too")

placeholder = st.empty()
with placeholder.container(border=True):

    # create two columns for charts
    fig_col1, fig_col2, fig_col3 = st.columns(3)
    with fig_col1:
        st.markdown("### Primeiro Grafico")
        fig1=px.bar( 
            df, 
            x = ['Saudável','Diabético' ], 
            y = df['diabetes'].value_counts().values.tolist(), 
            orientation = 'v',
            color=['Saudável','Diabético'],
            text_auto=True,
            height=400,
            width=400
            )
        fig1.update_layout(
                title={'text':'Contagem de diabéticos',
                    #    'y':1.0,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top', 
                    })
        fig1.update_xaxes(title='Condição de saúde')
        fig1.update_yaxes(title='Quantidade de pacientes')
        st.write(fig1)
        
    with fig_col2:
        st.markdown("### Segundo Grafico")
        fig2=px.scatter(df, 
               x='glicose', 
               y='pressao_sangue',
               color="Diabetes",
            #    hover_name="diabetes",
               color_discrete_sequence=["yellow", "blue"],
               log_x=False,
               height=400,
               width=400
               );
        fig2.update_traces(marker=dict(size=5,line=dict(width=1)),selector=dict(mode='markers'))
        fig2.update_layout(
            title={'text':'Glicose x Pressão sanguínea',
                #    'y':1.0,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top', 
                })
        fig2.update_xaxes(title='Glicose')
        fig2.update_yaxes(title='Pressão sanguínea')
        st.write(fig2)
    
    with fig_col3:
        st.markdown("### Terceiro Grafico")
        fig3=px.imshow(df.corr().round(2),
                aspect="auto",
                text_auto=True,
                height=400,
                width=400,
                color_continuous_scale='Viridis'
              )
        fig3.update_layout(
            title={'text':'Matriz de correlação entre as variáveis',
                #    'y':1.0,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top', 
                })
        # fig.update_xaxes(title='Condição de saúde')
        # fig.update_yaxes(title='Quantidade de pacientes')
        st.write(fig3)

st.markdown("### Visão detalhada dos graficos")
st.dataframe(df)
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
with st.expander('About', expanded=True):
    st.write('''
        - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
        - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
        - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
        ''')