import streamlit as st

def displayAboutMe():
    """
    Display information about Jeremy Faubert.
    """
    st.title("Yo!! 你好")
    st.write("It means \"Hi\" in mandarin.😜")

    # List Comprehension
    #  Creating a list using list comprehension
    # Dictionary
    info_dict = {
        "NAME": "Jeremy",
        "AGE": 19,
        "LOCATION": "Boston",
        "GOAL": "To obtain an internship at a leading financial institution this summer.✌🏽😅"
    }

    # Displaying the list created with list comprehension
    # Displaying information from the dictionary
    st.title("User Information:")
    for key, value in info_dict.items():
        st.write(f"{key}: {value}")

    skills = ["Accounting", "Excel", "Bloomberg Software", "Python", "Streamlit"]

    # Setting Arial font
    st.write(
        "<style>div.Widget.row-widget.stRadio > div{flex-direction: column;} p {font-family: Arial, text-align: center; color : #FFF0F5; sans-serif;}</style>",
        unsafe_allow_html=True,
    )
    st.write("SKILLS")
    # LIST COMPREHENSION
    [st.write(f"{skill}") for skill in skills]
    # Create an empty space
    placeholder = st.empty()

    # Display your initial profile picture
    profile_pic_path = "assets/jeremy_pic.jpeg"  # Replace with your image path
    profile_pic = placeholder.image(profile_pic_path, width=800, caption='Jeremy Faubert ✌🏽')

    # Introductory text
    st.write("Hello! I'm Jeremy Faubert.  I am a geography-nerd !! With a keen interest in the ever-evolving field of finance, I am eager to leverage my education and passion to make a meaningful impact. I am particularly drawn to areas such as investment management, financial analysis, and risk management. \
            During my time at Bentley University , I am focused on developing a strong foundation in financial principles, \
            investment strategies, and financial modeling. I am also actively involved in extracurricular activities, such as participating in finance, consulting, and investment clubs, where I am able to apply my classroom knowledge to practical real-world scenarios.")

    st.markdown("[Visit my LinkedIn profile](https://www.linkedin.com/in/jeremy-faubert/)")

    st.markdown(
        f"""
        <style>
            img {{ height: 800px; }}
        </style>
        """, unsafe_allow_html=True
    )


    st.title("Random Facts and Jokes")
    display_facts_and_jokes()

# using import here, to showcase, that it is allowed by Python as a feature.😁
import random


# A function that returns 2 values.
def get_random_facts():
    """
    Picks a random fact from list of facts and returns it and a default joke. 
    """
    facts = [
        "Bananas are berries, but strawberries aren't.",
        "Polar bears could eat as many as 86 penguins in a single sitting.",
        "A group of flamingos is called a 'flamboyance'.",
        "Octopuses have three hearts.",
        "The shortest war in history lasted only 38 minutes between Britain and Zanzibar in 1896."
    ]
    
    return random.choice(facts), "Why don't skeletons fight each other? They don't have the guts!"

# Function to display facts and jokes
# Function used at 2 differnt places of the program.
def display_facts_and_jokes():
    """
    Display facts and default joke.
    """
    fact, joke = get_random_facts()
    st.markdown(
        f"""
        <div style='margin: 10px; padding: 10px;'>
            <h4 style='margin-bottom: 5px;'>Random Fact:</h4>
            <p style='margin-top: 0; padding-left: 10px;'>{fact}</p>
            <h4 style='margin-bottom: 5px;'>Joke:</h4>
            <p style='margin-top: 0; padding-left: 10px;'>{joke}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


