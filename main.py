import requests
import pandas as pd
import streamlit as st
from PIL import Image
import urllib.request
#import plotly.express as px

url = 'https://apiv3.apifootball.com/?action=get_standings&league_id=99&APIkey=31fa144160de5317859a67c5937c70fc1186eba8721d6339118ce307e7b876ec'

brasileirao = requests.get(url)
brasileirao = brasileirao.json()
brasileirao = pd.DataFrame(brasileirao)

#dados = pd.read_csv(open('Teste.csv'))

st.set_page_config(layout="wide")

brasileirao.drop(columns=['home_league_position',
                          'home_promotion',
                          'home_league_payed',
                          "home_league_W",
                          "home_league_D",
                          "home_league_L",
                          "home_league_GF",
                          "home_league_GA",
                          "home_league_PTS",
                          "away_league_position",
                          "away_promotion",
                          "away_league_payed",
                          "away_league_W",
                          "away_league_D",
                          "away_league_L",
                          "away_league_GF",
                          "away_league_GA",
                          "away_league_PTS",
                          'country_name',
                          'league_id',
                          'league_name',
                          'league_round',
                          'fk_stage_key',
                          'stage_name',
                          'team_badge'], inplace = True)

brasileirao.rename(columns={'team_id':'ID',
                            'team_name':'Nome',
                            'overall_promotion':'Zona de classificação',
                            'overall_league_position':'Posição',
                            'overall_league_payed':'Partidas jogadas',
                            'overall_league_W':'Vitórias',
                            'overall_league_D':'Empates',
                            'overall_league_L':'Derrotas',
                            'overall_league_GF':'Gols marcados',
                            'overall_league_GA':'Gols sofridos',
                            'overall_league_PTS':'Pontos'
                            }, inplace = True)

logos = {'America' : 'https://logodetimes.com/times/america-mineiro/logo-america-mineiro-256.png',
          'Atletico' : 'https://logodetimes.com/times/atletico-mineiro/logo-atletico-mineiro-256.png',
          'Athletico' : 'https://logodetimes.com/times/atletico-paranaense/logo-atletico-paranaense-256.png',
          'Bahia' : 'https://logodetimes.com/times/bahia/logo-bahia-256.png',
          'Botafogo' : 'https://logodetimes.com/times/botafogo/logo-botafogo-256.png',
          'Corinthians' : 'https://logodetimes.com/times/corinthians/logo-corinthians-256.png',
          'Coritiba' : 'https://logodetimes.com/times/coritiba/logo-coritiba-256.png',
          'Cruzeiro' : 'https://logodetimes.com/times/cruzeiro/logo-cruzeiro-256.png',
          'Cuiaba' : 'https://logodetimes.com/times/cuiaba/logo-cuiaba-256.png',
          'Flamengo' : 'https://logodetimes.com/times/flamengo/logo-flamengo-256.png',
          'Fluminense' : 'https://logodetimes.com/times/fluminense/logo-fluminense-256.png',
          'Fortaleza' : 'https://logodetimes.com/times/fortaleza/logo-fortaleza-256.png',
          'Goias' : 'https://logodetimes.com/times/goias/logo-goias-256.png',
          'Gremio' : 'https://logodetimes.com/times/gremio/logo-gremio-256.png',
          'Internacional' : 'https://logodetimes.com/times/internacional/logo-internacional-256.png',
          'Palmeiras' : 'https://logodetimes.com/times/palmeiras/logo-palmeiras-256.png',
          'RB' : 'https://logodetimes.com/times/red-bull-bragantino/logo-red-bull-bragantino-256.png',
          'Santos' : 'https://logodetimes.com/times/santos/logo-santos-256.png',
          'Sao' : 'https://logodetimes.com/times/sao-paulo/logo-sao-paulo-256.png',
          'Vasco' : 'https://logodetimes.com/times/vasco-da-gama/logo-vasco-da-gama-256.png'}

times = st.sidebar.selectbox("Times", brasileirao["Nome"].unique())
dados = brasileirao[brasileirao["Nome"] == times]

def nome_img(dados):
    imagem = str(dados["Nome"])
    x = imagem.split()
    return str(x[1])
def infos(dados):
    vitoria = int(dados["Vitórias"])
    empate = int(dados["Empates"])
    derrota = int(dados["Derrotas"])
    return vitoria, empate, derrota

col1, col2, col3 =  st.columns(3)

with col1:
# def aproveitamento(dados):
    dados = brasileirao[brasileirao["Nome"] == times]
    t = infos(dados)
    partidas_jogadas = int(dados['Partidas jogadas'])
    pontos_possiveis = partidas_jogadas * 3
    pontos = int(dados['Pontos'])
    aproveitamento = (pontos/pontos_possiveis) * 100

    st.markdown("<h2 style='text-align: center; color: white;'>"+(f'Aproveitamento: {aproveitamento:,.2f}')+"</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>"+(f'Vitórias: {t[0]}')+"</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>"+(f'Empates: {t[1]}')+"</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>"+(f'Derrotas: {t[2]}')+"</h2>", unsafe_allow_html=True)

with col2:
    st.dataframe(brasileirao)

with col3:
    imagem = nome_img(dados)
    #print(logos[imagem])
    imagem = str(logos[imagem])
    st.image(imagem)