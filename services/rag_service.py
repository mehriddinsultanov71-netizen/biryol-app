import streamlit as st
import os
from groq import Groq

def get_ai_answer(query: str, category: str):
    # Streamlit secrets yoki muhit o'zgaruvchisidan kalitni olish
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    
    # Groq mijozini yaratish
    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": f"Siz WayUz transport ekotizimining aqlli yordamchisisiz. Murojaat yo'nalishi: {category}"
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )
    return completion.choices[0].message.content