import streamlit as st
import spacy

# Load the spaCy model (small English model)
nlp = spacy.load("en_core_web_sm")

# Set the title and page icon
st.set_page_config(page_title="TeleHealth-Ease Chatbot", page_icon="🌡️")

# Add a title
st.title("TeleHealth-Ease Chatbot")

# Introduction
st.write("I'm here to assist you with any medical questions you may have.")

# User input
user_input = st.text_input("You: ")

# Process user input and provide a response
if user_input:
    # Process the user's input using spaCy
    doc = nlp(user_input)

    # Example responses based on user input
    if "name" in [token.text.lower() for token in doc]:
        st.write("TeleHealth-Ease: My name is TeleHealth-Ease.")
    elif "stay" in [token.text.lower() for token in doc]:
        st.write("TeleHealth-Ease: I'm a virtual assistant, so I don't have a physical location.")
    else:
        st.write("TeleHealth-Ease: I'm here to help with your medical questions.")

# Provide instructions to the user
st.write("Feel free to ask me any medical-related questions or share your symptoms.")

