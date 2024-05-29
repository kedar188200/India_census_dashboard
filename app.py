import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

final_df = pd.read_csv('India.csv')

state_list = list(final_df['State'].unique())
state_list.sort()
state_list.insert(0, 'All')

columns = list(final_df.columns[[2,3,4,5,6,7,8,9,13,14]])
columns.sort()

st.sidebar.title('India map stats')
selected_state = st.sidebar.selectbox('Select a state', state_list)

primary = st.sidebar.selectbox('Select primary parameter', columns)

secondary = st.sidebar.selectbox('Select secondary parameter', columns)

plot = st.sidebar.button('Plot graph')

if plot:
    st.text('Size represents the primary parameter')
    st.text('Color represents the secondary parameter')

    if selected_state == 'All':
        fig = px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude", zoom=5,
                                size = primary, color=secondary, mapbox_style="carto-positron", size_max=15, width=1200,
                                height=700, hover_name='District name')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = final_df[final_df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", zoom=5,
                                size=primary, color=secondary, mapbox_style="carto-positron", size_max=15, width=1200,
                                height=700, hover_name='District name')
        st.plotly_chart(fig, use_container_width=True)