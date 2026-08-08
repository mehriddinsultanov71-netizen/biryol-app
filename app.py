import streamlit as st
from groq import Groq

# --- API SOZLAMASI (Streamlit Secrets orqali) ---
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
    ai_enabled = True
except Exception as e:
    ai_enabled = False

# --- SAHIFA KONFIGURATSIYASI ---
st.set_page_config(
    page_title="BirYol - Transportda bir yo'l!",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .stApp {
        background-color: #f8f9fc;
    }
    h1, h2, h3, h4, h5, h6, p, span {
        background-color: transparent !important; 
        color: #1e3a8a;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #4b5563;
        margin-bottom: 20px;
    }
    .transport-card {
        background-color: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e5e7eb;
        text-align: center;
        margin-bottom: 10px;
    }
    .transport-icon {
        font-size: 3.5rem;
        margin-bottom: 10px;
    }
    .transport-name {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1f2937;
    }
</style>
""", unsafe_allow_html=True)

# --- CHAP PANEL ---
st.sidebar.title("BirYol")
menu = ["Bosh sahifa", "AI Yordamchi", "Murojaat yuborish", "Statistika", "Sozlamalar"]
choice = st.sidebar.radio("Menyu", menu)

st.sidebar.markdown("---")
st.sidebar.markdown("📞 **Call markaz: 1242**")
st.sidebar.caption("24/7 qo'llab-quvvatlash")

# --- SAHIFALAR MANTIQIY QISMI ---

if choice == "Bosh sahifa":
    st.markdown('<p class="main-title">Transportda bir yo\'l!</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Murojaatingizni yuboring, yechimini topamiz</p>', unsafe_allow_html=True)
    
    col1, col2, _ = st.columns([1, 1, 2])
    with col1:
        if st.button("📝 Murojaat yuborish", type="primary", use_container_width=True):
            st.session_state['menu_choice'] = "Murojaat yuborish"
            st.rerun()
    with col2:
        if st.button("💬 AI yordamchidan so'rash", use_container_width=True):
            st.session_state['menu_choice'] = "AI Yordamchi"
            st.rerun()

    st.markdown("---")
    st.markdown("### Transport turlarini tanlang")
    
    t1, t2, t3, t4, t5, t6 = st.columns(6)

    transports = [
        {"col": t1, "name": "Avtobuslar", "icon": "🚌"},
        {"col": t2, "name": "Metro", "icon": "🚇"},
        {"col": t3, "name": "Elektrobuslar", "icon": "🚎"},
        {"col": t4, "name": "Poyezdlar", "icon": "🚆"},
        {"col": t5, "name": "Taksi", "icon": "🚕"},
        {"col": t6, "name": "Barchasi", "icon": "🌐"}
    ]

    for item in transports:
        with item["col"]:
            st.markdown(f"""
                <div class="transport-card">
                    <div class="transport-icon">{item['icon']}</div>
                    <div class="transport-name">{item['name']}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Tanlash", key=item["name"], use_container_width=True):
                st.success(f"{item['name']} tanlandi!")

elif choice == "AI Yordamchi":
    st.title("🤖 AI Yordamchi (Haqiqiy Sun'iy Intellekt)")
    st.write("Toshkent shahridagi transport va yo'nalishlar bo'yicha savollaringizni bevosita AIga bering.")
    
    # Chat tarixini saqlash
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Oldingi xabarlarni chiqarish
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Foydalanuvchidan xabar olish
    if user_query := st.chat_input("Savolingizni yozing..."):
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):
            if ai_enabled:
                with st.spinner("Sun'iy intellekt javob tayyorlamoqda..."):
                    try:
                        chat_completion = client.chat.completions.create(
                            messages=[
                                {
                                    "role": "system",
                                    "content": "Sen O'zbekiston transport tizimi va Toshkent shahri yo'nalishlari bo'yicha mutaxassis bo'lgan sun'iy intellekt yordamchisan ('BirYol' loyihasi). Foydalanuvchi savollariga faqat o'zbek tilida aniq, ishonchli va foydali javob ber."
                                },
                                {
                                    "role": "user",
                                    "content": user_query,
                                }
                            ],
                            model="llama-3.3-70b-versatile",
                        )
                        ai_response = chat_completion.choices[0].message.content
                        st.markdown(ai_response)
                        st.session_state.messages.append({"role": "assistant", "content": ai_response})
                    except Exception as e:
                        error_msg = f"API bilan bog'lanishda xatolik yuz berdi: {e}"
                        st.error(error_msg)
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
            else:
                warning_msg = "Streamlit Cloud'da GEMINI_API_KEY (yoki GROQ_API_KEY) Secrets bo'limida sozlanmagan."
                st.warning(warning_msg)
                st.session_state.messages.append({"role": "assistant", "content": warning_msg})

elif choice == "Murojaat yuborish":
    st.title("📝 Murojaat yuborish")
    st.write("Transport yo'nalishidagi muammo yoki takliflaringizni qoldiring.")
    
    with st.form("appeal_form"):
        name = st.text_input("Ism va familiyangiz")
        phone = st.text_input("Telefon raqamingiz (+998...)")
        transport_type = st.selectbox("Transport turi", ["Avtobus", "Metro", "Elektrobus", "Poyezd", "Taksi", "Boshqa"])
        message = st.text_area("Murojaat matni")
        
        submitted = st.form_submit_button("Murojaatni jo'natish", type="primary")
        if submitted:
            if name and message:
                st.success("Murojaatingiz muvaffaqiyatli qabul qilindi! Tez orada ko'rib chiqiladi.")
            else:
                st.error("Iltimos, majburiy maydonlarni to'ldiring.")

elif choice == "Statistika":
    st.title("📊 Statistika va Tahlillar")
    st.write("Hududiy transport oqimi va kelib tushgan murojaatlar statistikasi.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Jami murojaatlar", "1,248", "+12%")
    col2.metric("Hal etilganlar", "1,120", "+18%")
    col3.metric("Jarayondagilar", "128", "-4%")
    
    st.info("Tez kunda interaktiv grafiklar qo'shiladi.")

elif choice == "Sozlamalar":
    st.title("⚙️ Sozlamalar")
    st.write("Ilova parametrlarini o'zgartirish.")
    
    st.selectbox("Tilni tanlang", ["O'zbekcha", "Русский", "English"])
    st.toggle("Tungi rejim (Dark Mode)", value=False)
    st.button("Saqlash", type="primary")