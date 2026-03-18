# app.py
import os
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

# Set your API key
os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY_HERE"

# Initialize the model
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# Streamlit UI
st.title("🌐 LangChain + Google Gemini Multi-language Chat")

# Input: user message
user_input = st.text_area("Enter your message:", "")

# Language selection
languages = ["None", "Hindi", "Spanish", "French", "German","Telugu", "Chinese"]
target_lang = st.selectbox("Translate to (optional):", languages)

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a message first!")
    else:
        # Prepare messages for translation if a language is selected
        if target_lang != "None":
            messages = [
                SystemMessage(f"Translate the following English text to {target_lang}"),
                HumanMessage(user_input)
            ]
            response = model.invoke(messages)
        else:
            # Just regular chat
            response = model.invoke(user_input)
        
        st.markdown("**Response:**")
        st.write(response)