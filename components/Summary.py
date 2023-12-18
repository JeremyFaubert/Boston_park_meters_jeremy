

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

import sweetviz as sv

def generate_summary():
    """
    Generate summary report on dataset and return the path of report which is in html format.
    """
    data = pd.read_csv('dataset/Parking_Meters.csv')
    report = sv.analyze(data)

    # Save the Sweetviz report as an HTML file
    report_path = "sweetviz_report.html"
    report.show_html(report_path)

    return report_path

def giveSummary():
    """
    Display the generate summary report.
    """
    report_path = generate_summary()
    st.write("The summary report is opened in new tab/IF tab was not opened, download from here.")
    report_file = open('sweetviz_report.html','r')
    report = report_file.read()
    st.components.v1.html(report, width=800, height=600, scrolling=True)


