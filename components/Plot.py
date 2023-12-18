import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from components.Summary import giveSummary
import matplotlib.pyplot as plt


def makePlot():
    """
    Make plots for various uses cases.
    """

    st.title("Here, you can find some visualizations on the dataset")

    st.title("Parking Meter Density Bubble Map")

    st.write("Each point on the plot represents a specific location in a 2-dimensional space defined by X and Y coordinates. \
             The plot visually showcases the distribution of these locations.")


    data = pd.read_csv('dataset/Parking_Meters.csv')

    meter_density = data.groupby(['LATITUDE', 'LONGITUDE']).size().reset_index(name='meter_count')
    
    m = folium.Map(location=[meter_density['LATITUDE'].mean(), meter_density['LONGITUDE'].mean()], zoom_start=12)

    for index, row in meter_density.iterrows():
        folium.CircleMarker(location=[row['LATITUDE'], row['LONGITUDE']],
                            radius=row['meter_count'] / 1000,  # Adjust the radius as needed
                            color='blue',
                            fill=True,
                            fill_color='blue').add_to(m)

    folium_static(m)

    data['INSTALLED_ON'] = pd.to_datetime(data['INSTALLED_ON'])

    installations_over_time = data['INSTALLED_ON'].value_counts().reset_index()
    installations_over_time.columns = ['Date', 'Installations']

    installations_over_time = installations_over_time.sort_values(by='Date')

    st.title('Meter Installations Over Time')
    st.write("Installations are increasing every month/year. This is a good sign. More space is properly utilised.")
    st.line_chart(installations_over_time.set_index('Date'))

    st.title("In which direction are the most vehicles parked?")
    st.write("Hmmm, West seems to be answer.And less vechicles have been parked in East direction. Tada!!" )
    st.bar_chart(data['DIR'].value_counts())

    # Display Payment Method Distribution
    st.subheader("What is the top pay policy by the public?")
    payment_methods = data['PAY_POLICY'].value_counts()
    st.bar_chart(payment_methods)



    # Using a spinner to show user that its loading.
    st.title("Dataset Summary Report")
    st.write("A detailed summary report loaded with statistics and visualizations will be opened in a new tab. \
             If you love statistics, you will definitely love this report.")
    with st.spinner('Generating Summary Report...'):
        if st.button('Generate and Open Summary'):
            giveSummary()
    
    

    
