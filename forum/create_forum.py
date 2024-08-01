import streamlit as st
import sqlite3

# Connect to database
conn = sqlite3.connect('forum/database.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS posts
             (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)''')
conn.commit()

# Streamlit UI
st.title("Community Discussion Forum")

content = st.text_area("Post your content")

if st.button("Post"):
    c.execute("INSERT INTO posts (content) VALUES (?)", (content,))
    conn.commit()
    st.success("Content posted successfully")

conn.close()
