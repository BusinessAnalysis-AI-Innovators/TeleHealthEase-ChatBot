import streamlit as st

# Set the title and page icon
st.set_page_config(page_title="TeleHealth-Ease Chatbot", page_icon="🌡️")

# Add a title
st.title("TeleHealth-Ease Chatbot")

# Introduction
st.write("I'm here to assist you with any medical questions you may have.")

# User input
user_input = st.text_input("You: ")

# Simple responses based on user input
if user_input:
    # Check for common questions and provide predefined answers
    if "name" in user_input.lower():
        st.write("TeleHealth-Ease: My name is TeleHealth-Ease.")
    elif "location" in user_input.lower() or "stay" in user_input.lower():
        st.write("TeleHealth-Ease: I'm a virtual assistant, so I don't have a physical location.")
    else:
        st.write("TeleHealth-Ease: I'm here to help with your medical questions.")

# Provide instructions to the user
st.write("Feel free to ask me any medical-related questions or share your symptoms.")
