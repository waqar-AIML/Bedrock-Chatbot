import streamlit as st
import requests

API_URL = "https://49pgmyhuz3.execute-api.ap-south-1.amazonaws.com/Dev"

st.title("🤖 Bedrock Chatbot")

user_input = st.text_input("Ask something:")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                API_URL,
                json={"prompt": user_input}
            )

            if response.status_code == 200:
                ai_reply = response.json()["response"]
                st.write("AI:", ai_reply)
            else:
                st.error(f"API Error: {response.status_code}")

        except Exception as e:
            st.error(f"Error: {str(e)}")
