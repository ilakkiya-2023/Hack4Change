import streamlit as st
import sqlite3

# Connect to database
conn = sqlite3.connect('forum/database.db')
c = conn.cursor()

# Streamlit UI
st.title("Community Discussion Forum")

# Display posts
c.execute("SELECT * FROM posts ORDER BY id DESC")
posts = c.fetchall()

for post in posts:
    st.write(post[1])

conn.close()
