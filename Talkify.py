from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Google API Key
GOOGLE_API_KEY = "AIzaSyDyK0KcVnlV7sfBrI0v1QVFErrflh5wkxE"

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=GOOGLE_API_KEY
)

# Streamlit Page
st.set_page_config(page_title="Talkify")
st.title("🤖 Talk With Baba – AI QnA Bot")
st.markdown("My QnA Bot")

# Store Chat History
if "history" not in st.session_state:
    st.session_state.history = []

# Display Previous Messages
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
query = st.chat_input("Ask anything...")

if query:
    # Save User Message
    st.session_state.history.append({
        "role": "user",
        "content": query
    })

    # Show User Message
    with st.chat_message("user"):
        st.markdown(query)

    # Send Full History to Model
    res = llm.invoke(st.session_state.history)

    # Show AI Response
    with st.chat_message("assistant"):
        st.markdown(res.content)

    # Save AI Response
    st.session_state.history.append({
        "role": "assistant",
        "content": res.content
    })