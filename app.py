import streamlit as st

# --- SAHIFA KONFIGURATSIYASI ---
st.set_page_config(
    page_title="BirYol - Transportda bir yo'l!",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (Xatoliklarni to'g'rilovchi toza dizayn) ---
st.markdown("""
<style>
    /* Umumiy fon va matnlar */
    .stApp {
        background-color: #f8f9fc;
    }
    
    /* Sarlavhalardagi g'alati ko'k fonni olib tashlash */
    h1, h2, h3, h4, h5, h6, p, span {
        background-color: transparent !important; 
        color: #1e3a8a;
    }

    /* Asosiy Sarlavha */
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    
    .sub-title {
        font-size: 1.2rem;
        color: #4b5563;
        margin-bottom: 20px;
    }

    /* Transport Kartochkalari */
    .transport-card {
        background-color: white;
        padding: 15px;
        border-radius: 16px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e5e7eb;
        text-align: center;
        transition: transform 0.2s;
        margin-bottom: 15px;
    }
    .transport-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
    }

    /* Rasm joylashuvi */
    .img-container {
        width: 100%;
        height: 120px;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 10px;
    }
    .img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .icon-text {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1f2937;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- CHAP PANEL (SIDEBAR) ---
st.sidebar.title("BirYol")
menu = ["Bosh sahifa", "AI Yordamchi", "Murojaat yuborish", "Statistika", "Sozlamalar"]
choice = st.sidebar.radio("Menyu", menu)

st.sidebar.markdown("---")
st.sidebar.markdown("📞 **Call markaz: 1242**")
st.sidebar.caption("24/7 qo'llab-quvvatlash")

# --- ASOSIY SAHIFA MAZMUNI ---
if choice == "Bosh sahifa":
    
    # Sarlavha qismi
    st.markdown('<p class="main-title">Transportda bir yo\'l!</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Murojaatingizni yuboring, yechimini topamiz</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.button("📝 Murojaat yuborish", type="primary", use_container_width=True)
    with col2:
        st.button("💬 AI yordamchidan so'rash", use_container_width=True)

    st.markdown("---")
    st.markdown("### Transport turlarini tanlang")
    
    # 6 ta ustun
    t1, t2, t3, t4, t5, t6 = st.columns(6)

    # 100% ishlaydigan rasm havolalari
    transports = [
        {"col": t1, "name": "Avtobuslar", "icon": "🚌", "img": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=400&q=80"},
        {"col": t2, "name": "Metro", "icon": "🚇", "img": "https://images.unsplash.com/photo-1512411961421-2e624c965e64?w=400&q=80"},
        {"col": t3, "name": "Elektrobuslar", "icon": "🚎", "img": "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=400&q=80"},
        {"col": t4, "name": "Poyezdlar", "icon": "🚆", "img": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?w=400&q=80"},
        {"col": t5, "name": "Taksi", "icon": "🚕", "img": "https://images.unsplash.com/photo-1494976388531-d105809059f3?w=400&q=80"},
        {"col": t6, "name": "Barchasi", "icon": "🔳", "img": "https://images.unsplash.com/photo-1511316712398-3f5f3e433f48?w=400&q=80"}
    ]

    for item in transports:
        with item["col"]:
            st.markdown(f"""
                <div class="transport-card">
                    <div class="img-container">
                        <img src="{item['img']}" alt="{item['name']}">
                    </div>
                    <div class="icon-text">{item['icon']} {item['name']}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Tanlash", key=item["name"], use_container_width=True):
                st.success(f"{item['name']} tanlandi!")

else:
    st.title(choice)
    st.write("Bu sahifa ulanish jarayonida...")