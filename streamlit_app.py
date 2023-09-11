import streamlit as st

# Set the title and page icon
st.set_page_config(page_title="TeleHealth-Ease Chatbot", page_icon="🌡️")

# Add custom CSS to change the background color to blue
st.markdown(
    """
    <style>
    body {
        background-color: #0074e4; /* Blue color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a title
st.title("Welcome to TeleHealth-Ease Chatbot")

# Chatbot
st.write("I'm here to help with your medical questions.")

# User information
name = st.text_input("What's your name?")
location = st.text_input("Where are you located?")
symptoms = st.text_area("What are you experiencing?")

# Chatbot responses
if name:
    st.write(f"Hello, {name}!")

if location:
    st.write(f"Nice to know you're in {location}.")

if symptoms:
    st.write(f"I'm here to help with your symptoms. Let me provide some information.")

# Example medical answer (simplified)
if "fever" in symptoms.lower():
    st.write("Fever is often a sign of infection. It's essential to consult a doctor.")

# End the conversation
st.write("If you have more questions or need assistance, feel free to ask!")
