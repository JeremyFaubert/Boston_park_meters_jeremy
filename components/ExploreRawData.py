import streamlit as st 
import pandas as pd


@st.cache_data
def load_data(DATA_URL = "dataset/Parking_Meters.csv", DATE_COLUMN = "installed_on" ,nrows=6000):
    """ 
    Load data from a dataset into a pandas dataframe. Rename the header to lower_case
    args : 
        - DATA_URL : path to dataset, default :"dataset/Parking_Meters.csv"
        - DATE_COLUMN : data column in the dataset, which is used to convert to datetime object from text. default : installed_on
        - nrows : number of rows to load from the dataset. default = 60000
    """
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


def toggleRawData():
    """
    Toggles the dataset after loaded.
    """
    st.title("If you want to take a look at the dataset, this is for you!")
    st.write("Please check the checkbox. Nice rhyming ha! Yes, yes, you can un-view it as it is a checkbox.")
    data_load_state = st.text('Loading data...')
    data = load_data()
    data_load_state.text("Done! (using st.cache_data)")
    checkbox_data = st.checkbox('Show Raw Data')

    if checkbox_data:
        st.subheader('Raw data')
        st.write(data)