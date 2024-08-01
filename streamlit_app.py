

# //////////////////////////////////////////////////////////////////////////////////////////////////


import os
import requests
import tempfile
import cv2
import numpy as np
from PIL import Image, ImageOps
import streamlit as st
from time import sleep
import speech_recognition as sr
from googletrans import Translator
import random
import string

# Function to recognize speech and convert it to text
def recognize_speech(language):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Please say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=language)
            st.success(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Could not understand the audio")
            return ""
        except sr.RequestError:
            st.error("Could not request results; check your network connection")
            return ""

# Function to translate text to English
def translate_text(text, src_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest='en')
    return translation.text

# Function to display the sign language animation for each letter or specific phrase
def display_animation_or_video(text):
    text = text.upper()  # Convert text to uppercase
    image_size = (270, 450)  # Define a consistent size for images

    video_phrases = {
        "GOOD MORNING": "good_morning.mp4",
        "GOOD NIGHT": "good_night.mp4",
        "YES": "yes.mp4",
        "MONDAY": "monday.mp4",
        "FRIDAY": "friday.mp4",
        "FUN": "fun.mp4"
    }

    # Check if the text matches any specific video phrase
    if text in video_phrases:
        video_path = os.path.join('hand_signs', video_phrases[text])
        if os.path.exists(video_path):
            st.video(video_path)
            return

    # If not a specific phrase, display the hand signs for each letter
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

# Function to handle face filters on videos
def add_face_filter(video_path, filter_type):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if filter_type == "Girl":
        filter_image = cv2.imread('filters/girl_face.png', cv2.IMREAD_UNCHANGED)
    elif filter_type == "Boy":
        filter_image = cv2.imread('filters/boy_face.png', cv2.IMREAD_UNCHANGED)
    else:
        return video_path  # No filter applied
    
    if filter_image is None:
        raise FileNotFoundError(f"Filter image for {filter_type} not found or couldn't be loaded.")
    
    # Ensure filter image has an alpha channel
    if filter_image.shape[2] == 3:
        filter_image = cv2.cvtColor(filter_image, cv2.COLOR_BGR2BGRA)
    
    cap = cv2.VideoCapture(video_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    temp_video_path = tempfile.mktemp(suffix='.mp4')
    out = cv2.VideoWriter(temp_video_path, cv2.VideoWriter_fourcc(*'mp4v'), 20, (frame_width, frame_height))
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x, y, w, h) in faces:
            filter_resized = cv2.resize(filter_image, (w, h), interpolation=cv2.INTER_AREA)
            for c in range(0, 3):
                frame[y:y+h, x:x+w, c] = filter_resized[:, :, c] * (filter_resized[:, :, 3] / 255.0) + frame[y:y+h, x:x+w, c] * (1.0 - filter_resized[:, :, 3] / 255.0)
        
        out.write(frame)
    
    cap.release()
    out.release()
    return temp_video_path

# Function to handle the community discussion forum
def community_discussion_forum():
    st.title("Community Discussion Forum")
    st.markdown("<h3>Upload a video and view posts from others</h3>", unsafe_allow_html=True)
    
    username = st.text_input("Enter your username")
    st.image('click_here_gif.webp', width=100)
    if username:
        video_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "avi", "mkv"])
        description = st.text_input("Description")
        filter_option = st.selectbox("Choose a face filter", ["None", "Girl", "Boy"])

        if st.button("Upload Video"):
            st.image('click_here_gif.webp', caption='Uploading...', use_column_width=True)
            if video_file is not None and description:
                with tempfile.NamedTemporaryFile(delete=False) as tmp:
                    tmp.write(video_file.read())
                    tmp_path = tmp.name

                if filter_option != "None":
                    tmp_path = add_face_filter(tmp_path, filter_option)
                
                with open(tmp_path, "rb") as f:
                    files = {"file": f}
                    data = {"username": username, "description": description}
                    response = requests.post("http://localhost:5000/upload", files=files, data=data)
                    if response.status_code == 200:
                        st.success("Video uploaded successfully")
                    else:
                        st.error(f"Failed to upload video: {response.text}")

        st.markdown("---")

        st.title("Posts")
        st.markdown("<h3>View and manage your posts</h3>", unsafe_allow_html=True)

        response = requests.get("http://localhost:5000/videos")
        if response.status_code == 200:
            videos = response.json()
            if not videos:
                st.info("No posts available.")
            for video in videos:
                if 'username' in video and 'description' in video and 'videoPath' in video:
                    st.markdown(f"### {video['description']}")
                    video_url = f"http://localhost:5000{video['videoPath']}"
                    st.markdown(f'<div class="video-container"><video controls><source src="{video_url}" type="video/mp4"></video></div>', unsafe_allow_html=True)
                    if video['username'] == username:
                        if st.button("Delete Post", key=video['_id']):
                            delete_response = requests.delete(f"http://localhost:5000/videos/{video['_id']}")
                            if delete_response.status_code == 200:
                                st.success("Post deleted successfully")
                            else:
                                st.error("Failed to delete post")
        else:
            st.error("Failed to retrieve posts")

# Function to handle video calling feature
def video_calling():
    st.title("Video Calling")
    st.markdown("<h3>Generate an invite link and share it with others</h3>", unsafe_allow_html=True)
    if st.button("Generate Invite Link"):
        
        room_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        invite_link = f"https://meet.jit.si/{room_name}"
        st.success(f"Invite Link: {invite_link}")
        st.markdown(f"[Click here to start the call]({invite_link})", unsafe_allow_html=True)

# Function to handle learning materials
def learning_materials():
    st.title("Learning Materials")
    st.markdown("<h3>Upload and view learning materials</h3>", unsafe_allow_html=True)
    
    material_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "avi", "mkv"])
    if material_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(material_file.read())
            tmp_path = tmp.name

        st.video(tmp_path)
        st.success("Video uploaded and ready to view.")

    st.markdown("---")

    st.title("Materials")
    st.markdown("<h3>View uploaded materials</h3>", unsafe_allow_html=True)

    response = requests.get("http://localhost:5000/materials")
    if response.status_code == 200:
        materials = response.json()
        if not materials:
            st.info("No materials available.")
        for material in materials:
            if 'description' in material and 'videoPath' in material:
                st.markdown(f"### {material['description']}")
                material_url = f"http://localhost:5000{material['videoPath']}"
                st.markdown(f'<div class="video-container"><video controls><source src="{material_url}" type="video/mp4"></video></div>', unsafe_allow_html=True)
    else:
        st.error("Failed to retrieve materials")

# Streamlit application layout
st.set_page_config(page_title="Speech to Sign Language Converter", page_icon=":guardsman:", layout="wide")


st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the app mode", ["Home", "Speech Recognition", "Community Discussion Forum", "Video Calling", "Learning Materials"])

if app_mode == "Home":
    st.title("Welcome to the Learning Application")
    st.markdown("""
        <div class="main">
            <h2>About This App</h2>
            <p>This application is designed to aid individuals who are deaf or hard of hearing in learning and communication. It provides a variety of features including:</p>
            <ul>
                <li><strong>Speech Recognition:</strong> Convert spoken language into text to facilitate communication.</li>
                <li><strong>Sign Language Animations:</strong> View animations representing sign language for different letters and words.</li>
                <li><strong>Community Discussion Forum:</strong> Share and view videos related to learning and communication.</li>
                <li><strong>Video Calling:</strong> Generate invite links for video calls to connect with others.</li>
                <li><strong>Learning Materials:</strong> Upload and view educational videos to enhance learning.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


elif app_mode == "Speech Recognition":
    st.header("Speech Recognition")
    language = st.selectbox("Choose the language for speech recognition", ["English", "French", "Spanish", "German", "Chinese"])
    if st.button("Start Recognition"):
        recognized_text = recognize_speech(language)
        if recognized_text:
            if language != 'en':
                recognized_text = translate_text(recognized_text, language)
            st.markdown("### Sign Language Animation")
            display_animation_or_video(recognized_text)

elif app_mode == "Community Discussion Forum":
    community_discussion_forum()

elif app_mode == "Video Calling":
    video_calling()

elif app_mode == "Learning Materials":
    learning_materials()
elif app_mode == "Sign Language to text":
    learning_materials()