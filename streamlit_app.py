import streamlit as st
import spacy

# Load the spaCy model for text classification
nlp = spacy.load("en_core_web_sm")

# Set the title and page icon
st.set_page_config(page_title="TeleHealth-Ease Chatbot", page_icon="🌡️")

# Add custom CSS for chat bubbles
st.markdown(
    """
    <style>
    .chat-bubble {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
        display: inline-block;
    }
    .user-bubble {
        background-color: #0074e4;
        color: white;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Chatbot
st.title("Welcome to TeleHealth-Ease Chatbot")

# User information
name = st.text_input("What's your name?")
location = st.text_input("Where are you located?")
symptoms = st.text_area("What are you experiencing?")

# Chatbot responses
if name:
    st.markdown(f'<div class="chat-bubble user-bubble">{name}</div>', unsafe_allow_html=True)

if location:
    st.markdown(f'<div class="chat-bubble user-bubble">{location}</div>', unsafe_allow_html=True)

if symptoms:
    st.markdown(f'<div class="chat-bubble user-bubble">{symptoms}</div>', unsafe_allow_html=True)

    # Use spaCy for symptom classification
    doc = nlp(symptoms)
    symptom_keywords = ["fever", "cough", "headache", "nausea", "fatigue"]

    detected_symptoms = [ent.text for ent in doc if ent.text.lower() in symptom_keywords]

    if detected_symptoms:
        st.write("Based on your symptoms, it seems you may be experiencing:")
        for symptom in detected_symptoms:
            st.markdown(f'<div class="chat-bubble">{symptom.capitalize()}</div>', unsafe_allow_html=True)

# End the conversation
st.balloons()


