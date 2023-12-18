import streamlit as st 
import pandas as pd
from components.AboutMe import display_facts_and_jokes


def displayAppData():
    """
    Displays information about Boston Parking Meters App.
    """
    st.title('🌟 Boston Parking Meters')
    st.markdown(
        """
        <div style='background-color: black; padding: 32px; border-radius: 10px;'>
            <h3 style='color: #3366ff;'>Purpose</h3>
            <p style='font-size: 16px; color: #fff;'>Explore Boston's parking landscape effortlessly. 
            My app harnesses the Boston parking meters dataset to simplify parking insights, 
            helping you navigate the city hassle-free.</p>
            <p style='font-style: italic; color: #f9f9f9;'>By Jeremy Faubert</p>
        </div>

        <div style='background-color: black; padding: 32px; border-radius: 10px;'>
            <h3 style='color: #3366ff;'>Dataset</h3>
            <p style='font-size: 16px; color: #fff;'>Our dataset encompasses Boston's parking meters, offering details on locations, hours, rates, and more. 
            Access comprehensive information to plan your parking strategy efficiently.</p>
            <p style='font-style: italic; color: #f9f9f9;'>This dataset is public and given credit in references.</p>
        </div>

          <div style='background-color: black; padding: 32px; border-radius: 10px;'>
            <h3 style='color: #3366ff;'>App Features and Functionality</h3>
            <p style='font-size: 16px; color: #fff;'>Experience interactive data visualization and analysis. 
            Filter and explore parking data, uncover trends, and gain valuable insights for optimal parking decisions.
            </p>
            <ul style=" list-style-type : none; padding-left :0; ">
                <li> 📊   Charts </li> 
                <li> 📈   Graph </li> 
                <li> 🗺️   Map </li> 
                <li> 💿   Raw Dataset view </li>
                <li> 🧮   Some stats </li>
            </ul>
        </div>
    
        
        """,
        unsafe_allow_html=True
    )


    st.write()
    display_facts_and_jokes()
