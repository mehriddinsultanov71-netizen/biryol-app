import streamlit as st

# Sahifa kengaytmasi
st.set_page_config(page_title="BirYol - Transport Ekotizimi", layout="wide")

st.title("BirYol")
st.caption("Transportda bir yo'l!")

# Transport turlari uchun sarlavha
st.markdown("### Transport turlarini tanlang")

# 7 ta ustun hosil qilish (rasmdagidek ketma-ketlikda)
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("🚌 Avtobus", use_container_width=True):
        st.success("Avtobus yo'nalishlari tanlandi!")

with col2:
    if st.button("🚇 Metro", use_container_width=True):
        st.success("Metro bekati va yo'nalishlari tanlandi!")

with col3:
    if st.button("🚎 Elektrobus", use_container_width=True):
        st.success("Elektrobuslar tanlandi!")

with col4:
    if st.button("🚍 Trolleybus", use_container_width=True):
        st.success("Trolleybuslar tanlandi!")

with col5:
    if st.button("🚆 Poyezdlar", use_container_width=True):
        st.success("Poyezd qatnovlari tanlandi!")

with col6:
    if st.button("🚕 Taksi", use_container_width=True):
        st.success("Taksi xizmatlari tanlandi!")

with col7:
    if st.button("🔲 Barchasi", use_container_width=True):
        st.info("Barcha transport turlari ko'rsatilmoqda.")