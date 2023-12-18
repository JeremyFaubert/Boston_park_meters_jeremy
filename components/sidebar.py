import streamlit as st
from components.AboutApp import displayAppData
from components.ExploreRawData import toggleRawData
from components.Plot import makePlot
from components.AboutMe import displayAboutMe

def displaySideBar():
    """
    Display side bar for navigating multiple pages.
    """
    st.set_page_config(page_title='Boston Parking Meters')
    st.sidebar.title('Menu')
    # Add options to the menu using selectbox
    menu_option = st.sidebar.selectbox(
        'Select an option',
        ('Overview', 'Dataset', "Visualizations",'About Me')
    )

    # Display content based on the selected option
    if menu_option == 'Overview':
        displayAppData()
    elif menu_option == 'Dataset':
        toggleRawData()
    elif menu_option == 'Visualizations':
        makePlot()
    elif menu_option == 'About Me':
        displayAboutMe()


