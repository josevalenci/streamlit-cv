# chatbot.py

import streamlit as st
from openai import OpenAI

def run_chatbot():
    st.title("🤖 ChatBot Mentor")
    st.write("Hazle preguntas a tu asistente de datos personalizado.")

    #openai.api_key = st.secrets["OPENAI_API_KEY"]
    st.write("📡 Intentando cargar la clave OpenAI...")
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        st.write("✅ Clave cargada correctamente.")
    except Exception as e:
        st.error(f"❌ Error cargando clave OpenAI: {e}")
        return


    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "Eres un mentor amable y experto en ciencia de datos."}
        ]

    user_input = st.text_input("Tu pregunta")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Pensando..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )

            reply = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": reply})

    for msg in st.session_state.messages[1:]:
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
'''

import streamlit as st
from openai import OpenAI, RateLimitError, AuthenticationError

def run_chatbot():
    st.title("🤖 ChatBot Mentor (modo demo si no hay saldo)")
    st.write("Hazle preguntas a tu asistente de datos personalizado.")

    # Intenta cargar la API Key
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        openai_available = True
    except Exception as e:
        st.warning("⚠️ Modo demo activado: sin acceso a la API de OpenAI.")
        openai_available = False

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "Eres un mentor amable y experto en ciencia de datos."}
        ]

    user_input = st.text_input("Tu pregunta")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        if openai_available:
            with st.spinner("Pensando..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=st.session_state.messages
                    )
                    reply = response.choices[0].message.content
                except (RateLimitError, AuthenticationError):
                    reply = "⚠️ Parece que no hay saldo disponible en la API. Estoy en modo demo."
                    openai_available = False
        else:
            # 🔁 Modo demo: responde con frases fijas
            demo_responses = {
                "hola": "¡Hola! ¿En qué te puedo ayudar?",
                "data science": "La ciencia de datos combina programación, estadística y curiosidad.",
                "cv": "Puedo ayudarte a mejorar tu CV para roles de datos.",
                "default": "Estoy en modo demo. Intenta preguntarme sobre ciencia de datos o CV."
            }

            key = next((k for k in demo_responses if k in user_input.lower()), "default")
            reply = demo_responses[key]

        st.session_state.messages.append({"role": "assistant", "content": reply})

    # Mostrar historial
    for msg in st.session_state.messages[1:]:
        st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
'''