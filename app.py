import requests
import json
import streamlit as st
import pydeck as pdk
import pandas as pd

# load data about people in space from API
space = requests.get('http://api.open-notify.org/astros.json')
space_data = json.loads(space.text)

# load data about location of the ISS
iss = requests.get('http://api.open-notify.org/iss-now.json')
iss_data = json.loads(iss.text)

# assign data about people that should be shown via streamlit app to variables
count = space_data['number']

names = []
for astronaut in space_data['people']:
    names.append(astronaut['name'])

# assign geolocation data to variables
lat = float(iss_data['iss_position']['latitude'])
long = float(iss_data['iss_position']['longitude'])
location = [[lat, long]]

# add title and short description to website
st.title('Humans currently in space')
st.markdown('This website gives a quick overview about people that are currently in space and the location of the '
            'ISS, which is where those astronauts are currently at.')

# add count of people to website
st.subheader('Number of people currently in space: ' + str(count))

# add names of people to website
st.subheader('Names of people currently in space:')
st.dataframe(names)

# add location map to website
st.subheader('Current Location of ISS')

df = pd.DataFrame(location,columns =['lat', 'lon'])

st.markdown('These are the current coordinates of the ISS:')
st.dataframe(df)
# st.map(df, zoom=1)

st.markdown('The red dot marks the live location of the ISS on the world map.')

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/seccoboi/ckor8662a5fsr17lezi2sf436',
    initial_view_state=pdk.ViewState(
        latitude=37.944,
        longitude=5.237,
        zoom=0,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            df,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=100,
            radius_min_pixels=1,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position='[lon, lat]',
            get_radius=2500,
            get_fill_color='[200, 30, 0, 160]',
        ),
    ],
))
