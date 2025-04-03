# chatbot.py
import streamlit as st
import openai

def run_chatbot():
    st.title("🤖 ChatBot Mentor")
    st.write("Hazle preguntas a tu asistente de datos personalizado.")

    openai.api_key = st.secrets["OPENAI_API_KEY"]

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "Eres un mentor amable y experto en ciencia de datos."}
        ]

    user_input = st.text_input("Tu pregunta")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Pensando..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            reply = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": reply})

    for msg in st.session_state.messages[1:]:
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
