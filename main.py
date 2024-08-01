import os
from PIL import Image, ImageOps
import streamlit as st
from time import sleep
import speech_recognition as sr

# Function to recognize speech and convert it to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Please say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Could not understand the audio")
            return ""
        except sr.RequestError:
            st.error("Could not request results; check your network connection")
            return ""

# Function to display the sign language animation for each letter
def display_animation(text):
    text = text.upper()  # Convert text to uppercase
    image_size = (270, 450)  # Define a consistent size for images
    for word in text.split():
        columns = st.columns(len(word))
        for i, letter in enumerate(word):
            image_path = os.path.join('hand_signs', f'{letter}.png.jpg')
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = ImageOps.fit(image, image_size, Image.LANCZOS)
                with columns[i]:
                    st.image(image, caption=letter)
            else:
                st.error(f"No image found for letter: {letter}")
        st.markdown("<br>", unsafe_allow_html=True)
        sleep(2)  # Pause between words

# Streamlit UI
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stButton button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .st-info, .st-success, .st-error {
        font-size: 18px;
        font-weight: bold;
        margin: 10px 0;
    }
    h1, h3 {
        text-align: center;
        color: #000000;  /* Change color to black */
    }
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('Audio to Sign Language Converter')
st.markdown("<h3>Convert your speech to sign language easily</h3>", unsafe_allow_html=True)

if st.button('Start'):
    recognized_text = recognize_speech()
    if recognized_text:
        display_animation(recognized_text)
