import streamlit as st
import plotly.express as px
from backend import get_data

st.header('Weather Forecast for the Next Days')
placeval = st.text_input(label='Place', key='userplace')
sliderval = st.slider(label='Forecast Days', min_value=1, max_value=5, key='userdays', help='Select the number of forecasted days')
dropval = st.selectbox(options=('Temperature', 'Sky'), label='Select data to view:')
st.subheader(f'{dropval} for the next {sliderval} days in {placeval}')

if placeval:
    filtered_data = get_data(placeval, sliderval)

    try:
        if dropval =='Temperature':
            temperatures = [temps['main']['temp'] for temps in filtered_data]
            temperatures = [temperature-273.15 for temperature in temperatures]
            date = [dates['dt_txt'] for dates in filtered_data]
            fig = px.line(x=date, y=temperatures, labels={'x':'Dates', 'y': 'Temperatures'})
            st.plotly_chart(fig)

        if dropval == 'Sky':
            skycondi = [sky['weather'][0]['main'] for sky in filtered_data]
            images = {'Clear': 'https://github.com/Amaruq0703/Weather-Visualiser/blob/main/images/clear.png?raw=true', 'Clouds':'https://github.com/Amaruq0703/Weather-Visualiser/blob/main/images/cloud.png?raw=true',
                        'Rain': 'https://github.com/Amaruq0703/Weather-Visualiser/blob/main/images/rain.png?raw=true', 'Snow': 'https://github.com/Amaruq0703/Weather-Visualiser/blob/main/images/snow.png?raw=true'}
            imagepaths = [images[sky] for sky in skycondi]
            date = [dates['dt_txt'] for dates in filtered_data]
            st.image(imagepaths, width=100, caption= date)

    except KeyError:
        st.info('Please enter a valid city')


        
        
        









