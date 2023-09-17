import streamlit as st
import pandas as pd 

st.header('Weather Forecast for the Next Days')
placeval = st.text_input(label='Place', key='userplace')
sliderval = st.slider(label='Forecast Days', min_value=1, max_value=5, key='userdays', help='Select the number of forecasted days')
dropval = st.selectbox(options=('Temperature', 'Sky'), label='Select data to view:')
st.subheader(f'{dropval} for the next {sliderval} days in {placeval}')


