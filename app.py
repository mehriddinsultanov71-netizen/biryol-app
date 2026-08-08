import streamlit as st
from services.rag_service import get_ai_answer

# Sahifa sozlamalari
st.set_page_config(
    page_title="1YO'L - Transport Ekotizimi",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Zamonaviy Yandex uslubidagi CSS stillar
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    [data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }
    .main-title {
        font-size: 2rem;
        font-weight: 800;
        color: #ffffff;
    }
    .sub-title {
        font-size: 1rem;
        color: #94a3b8;
        margin-bottom: 20px;
    }
    .stTextInput input, .stTextArea textarea {
        color: #ffffff !important;
        background-color: #1e293b !important;
        border: 1px solid #475569 !important;
        border-radius: 10px !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1e293b !important;
        color: white !important;
        border-radius: 10px !important;
    }
    .stButton>button {
        width: 100%;
        background-color: #facc15;
        color: #0f172a;
        font-weight: 700;
        border-radius: 10px;
        padding: 0.6rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #eab308;
        color: #0f172a;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar menyu (1YO'L logotipi va nomi bilan)
with st.sidebar:
    st.markdown("### 🚘 **1YO'L**")
    st.caption("Yagona transport ekotizimi")
    st.markdown("---")
    
    selected_tab = st.radio(
        "Bo'limlar",
        ["💬 Qanday yordam kerak?", "📝 Murojaat uchun", "📊 Monitoring", "ℹ️ Tizim haqida"]
    )
    
    st.markdown("---")
    st.markdown("🟢 **Status:** Onlayn")
    st.markdown("🌐 **Tarmoq:** Toshkent shahar")

# 1-BO'LIM: Qanday yordam kerak? (AI Maslahatchi)
if selected_tab == "💬 Qanday yordam kerak?":
    st.markdown('<p class="main-title">🚘 1YO\'L — Qanday yordam kerak?</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Yo\'nalishlar, bekatlar, jadvallar yoki to\'lovlar bo\'yicha sun\'iy intellektdan darhol javob oling.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        device_id = st.text_input("Mobile ID / Qurilma ID", value="user_toshkent_01")
    with col2:
        category = st.selectbox(
            "Mavzu yo'nalishi:",
            ["Jamoat transporti", "Toshkent metro", "Tariflar va to'lovlar", "Bekatlar va jadval"]
        )

    query_help = st.text_area("Savolingizni yozing:", placeholder="Masalan: Chilonzor yo'li bekatlari qaysilar yoki 94-sonli avtobus qayerdan o'tadi?")

    if st.button("🚀 Yordam olish"):
        if not query_help.strip():
            st.warning("Iltimos, savolingizni kiriting!")
        else:
            with st.spinner("Sun'iy intellekt javob tayyorlamoqda..."):
                answer = get_ai_answer(query_help, category)
            st.success("Muvaffaqiyatli bajarildi!")
            st.markdown("### 🤖 1YO'L AI Maslahati:")
            st.info(answer)

# 2-BO'LIM: Murojaat uchun
elif selected_tab == "📝 Murojaat uchun":
    st.markdown('<p class="main-title">📝 Murojaat yuborish</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Transport tizimidagi kamchiliklar bo\'yicha shikoyat yoki yangi takliflaringizni qoldiring.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        app_type = st.selectbox("Murojaat turi:", ["Shikoyat", "Taklif", "Minnatdorchilik", "Texnik muammo"])
    with col2:
        transport_type = st.selectbox("Transport turi:", ["Avtobus", "Metro", "Elektrpoyezd", "Boshqa"])

    appeal_text = st.text_area("Murojaat matni:", placeholder="Muammo yoki taklifingizni batafsil yozib qoldiring...")

    if st.button("📤 Murojaatni yuborish"):
        if not appeal_text.strip():
            st.warning("Iltimos, murojaat matnini yozing!")
        else:
            ai_response = get_ai_answer(f"Murojaat turi: {app_type}. Transport: {transport_type}. Mazmuni: {appeal_text}", "Rasmiy murojaat")
            st.success("Murojaatingiz 1YO'L transport boshqarmasiga muvaffaqiyatli yuborildi!")
            st.markdown("### 📋 Murojaatni qayta ishlash natijasi:")
            st.info(ai_response)

# 3-BO'LIM: Monitoring
elif selected_tab == "📊 Monitoring":
    st.markdown('<p class="main-title">📊 Transport Monitoringi</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Ekotizimning joriy ko\'rsatkichlari.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Faol transportlar", "1,245 ta", "+18 ta")
    col2.metric("Kunlik yo'lovchilar", "420 ming", "+5.4%")
    col3.metric("AI Javob tezligi", "0.3 s", "Tezkor")

# 4-BO'LIM: Tizim haqida
elif selected_tab == "ℹ️ Tizim haqida":
    st.markdown('<p class="main-title">ℹ️ 1YO\'L Platformasi haqida</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Shahar infratuzilmasini raqamlashtirish loyihasi.</p>', unsafe_allow_html=True)
    
    st.write("""
    **1YO'L** — zamonaviy shahar transport ekotizimi bo'lib, quyidagi imkoniyatlarni taqdim etadi:
    * **💬 Qanday yordam kerak?:** Har qanday transport yo'nalishlari va qoidalar bo'yicha sun'iy intellektdan tezkor maslahat olish.
    * **📝 Murojaat uchun:** Haydovchilar, bekatlar yoki jamoat transportidagi holatlar yuzasidan shikoyat va takliflarni qoldirish.
    """)