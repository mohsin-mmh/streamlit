from enum import auto
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import altair as alt

st.set_page_config(layout="wide", page_title='World GDP Data')

st.image("banner1.jpg", width=1200)

st.header('Countries GDP')

##...Load DataFrame
#excel_file = 'Labor Report Consolidated (Power Query) v2.0.xlsx'
#sheet_name = 'Raw Data'
csv_file = '3.1 GDP Data.csv'

#df = pd.read_excel(excel_file, sheet_name, usecols='A:F', header=1)
df = pd.read_csv(csv_file)

#Wealthy Countries
df_chart1 = df.loc[df['Country_Name'].isin(['United States', 'Australia', 'United Kingdom', 'Japan', 'Germany', 'Sweden'])]
df_chart1 = df_chart1[['Country_Name', '2014', '2015', '2016']].sort_values('2016', ascending=False)
df_chart1 = df_chart1.set_index('Country_Name')

#Central Asian Countries
df_chart2 = df.loc[df['Country_Name'].isin(['Malaysia', 'Thailand', 'Philippines', 'Indonesia', 'Vietnam'])]
df_chart2 = df_chart2[['Country_Name', '2014', '2015', '2016']].sort_values('2016', ascending=False)
df_chart2 = df_chart2.set_index('Country_Name')

#South Asian Countries
df_chart3 = df.loc[df['Country_Name'].isin(['India', 'Pakistan', 'Bangladesh', 'Nepal', 'Srilanka'])]
df_chart3 = df_chart3[['Country_Name', '2014', '2015', '2016']].sort_values('2016', ascending=False)
df_chart3 = df_chart3.set_index('Country_Name')

col1, col2 = st.columns(2)

with col1:
    
    #Creating Charts & Tables
    st.subheader('Comparison between High GDP Countries')
    st.line_chart(df_chart1)

    st.subheader('GDP Comparison between Central Asian Countries')
    st.bar_chart(df_chart2)

    st.subheader('Comparison between High GDP Countries')
    st.bar_chart(df_chart3)

with col2:
    st.subheader('List of High GDP Countries')
    st.table(df_chart1)

    st.subheader('List of Central Asian Countries')
    st.table(df_chart2)

    st.subheader('List of Central Asian Countries')
    st.table(df_chart3)


body = ("Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”")

st.markdown(body, unsafe_allow_html=False)