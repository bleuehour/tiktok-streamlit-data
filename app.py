import streamlit as st
import pandas as pd
from subprocess import call
import plotly.express as px

st.set_page_config(layout='wide')


hashtag = st.text_input('Search for a hashtag here', value="")

if st.button('Get Data'):
    call(['python', 'tiktok.py', hashtag])
    df = pd.read_csv('tiktokdata.csv')

    fig = px.histogram(df, x='desc', hover_data=[
                       'desc'], y='stats_diggCount', height=300)
    st.plotly_chart(fig, use_container_width=True)

    left_col, right_col = st.columns(2)

    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=[
                          'desc'], size='stats_playCount', color='stats_playCount')
    left_col.plotly_chart(scatter1, use_container_width=True)

    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=[
                          'author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right_col.plotly_chart(scatter2, use_container_width=True)

    df
