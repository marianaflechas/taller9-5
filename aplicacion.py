import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('ANALISIS GPA')

tab1, tab2 = st.tabs(['ANALISIS UNIVARIADO','ANALISIS BIVARIADO'])

with tab1:
    st.header('ANALISIS UNIVARIADO')

    data =  pd.read_csv('datass.csv')

   

    fig_age = px.histogram(data, x="age", nbins=40, title="DISTRIBUCION DE EDADES")
    fig_gender = px.bar(data['gender'].value_counts().reset_index(), x='gender', y='count',title="DISTRIBUCION DE GENERO")
    fig_alcohol = px.bar(data['alcohol'].value_counts().reset_index(), x='alcohol', y='count',title="NUMERO DE DIAS DE CONSUMO DE ALCOHOL SEMANAL")
    fig_grades = px.histogram(data, x="grades", nbins=40, title="DISTRIBUCION DE NOTAS")

    st.plotly_chart(fig_age)
    st.plotly_chart(fig_gender)
    st.plotly_chart(fig_alcohol)
    st.plotly_chart(fig_grades)

with tab2:

    st.header('ANALISIS UNIVARIADO')

    fig_grades_age = px.scatter(data, x="grades", y="age", title="Notas vs. Edad")
    fig_grades_alcohol = px.scatter(data, x="grades", y="alcohol", title="Notas vs. Consumo de Alcohol")
    fig_boxplot = px.box(data, x="gender", y="grades", title="Boxplot de Notas por Género")

    st.plotly_chart(fig_grades_age)
    st.plotly_chart(fig_grades_alcohol)
    st.plotly_chart(fig_boxplot)