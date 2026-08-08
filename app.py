import streamlit as st

# --- SAHIFA KONFIGURATSIYASI ---
st.set_page_config(
    page_title="BirYol - Transportda bir yo'l!",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (ZAMONAVIY DIZAYN UCHUN) ---
def local_css():
    st.markdown("""
    <style>
    /* Umumiy shrift va fon */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #f8f9fc;
    }

    /* Asosiy konteyner */
    .stApp > header {
        background-color: transparent;
    }
    .stApp {
        margin-top: 0px;
    }

    /* Sarlavhalar */
    h1, h2, h3 {
        color: #1e3a8a;
        font-weight: 600 !important;
    }

    /* Professional Card uslubi */
    .transport-card {
        background-color: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .transport-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
    }

    /* Banner Card uslubi */
    .banner-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e5e7eb;
        margin-bottom: 30px;
    }

    /* Tugmalar uslubi (Streamlit tugmalarini o'zgartirish) */
    .stButton > button {
        border-radius: 12px;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        border-color: #1e3a8a;
        color: #1e3a8a;
    }

    /* Ikonka uslubi */
    .transport-icon {
        font-size: 40px;
        margin-bottom: 15px;
        display: block;
    }

    /* Realistik rasm uslubi */
    .transport-image-container {
        width: 100%;
        height: 120px;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 15px;
    }
    .transport-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

local_css()

# --- CHAP PANEL (SIDEBAR) ---
st.sidebar.title("BirYol")
st.sidebar.image("https://raw.githubusercontent.com/mehriddinsultanov71-netizen/biryol-app/main/app/logo.png", width=100)

menu = ["Bosh sahifa", "AI Yordamchi", "Murojaat yuborish", "Statistika", "Sozlamalar"]
choice = st.sidebar.radio("Menyu", menu)

st.sidebar.markdown("---")
st.sidebar.markdown("📞 **Call markaz:**")
st.sidebar.markdown("### 1242")
st.sidebar.caption("24/7 qo'llab-quvvatlash")

# --- ASOSIY SAHIFA MAZMUNI ---

if choice == "Bosh sahifa":
    # 1. Professional Banner va Realistik Rasmlar
    st.markdown('<div class="banner-card">', unsafe_allow_html=True)
    
    col_b1, col_b2 = st.columns([2, 1])
    with col_b1:
        st.markdown("# Transportda bir yo'l!")
        st.markdown("##### Murojaatingizni yuboring, yechimini topamiz")
        
        c1, c2 = st.columns(2)
        with c1:
            # Xatolik to'g'irlandi: kind o'rniga type ishlatildi
            st.button("📝 Murojaat yuborish", type="primary", use_container_width=True)
        with c2:
            st.button("💬 AI yordamchidan so'rash", use_container_width=True)

    with col_b2:
        bus_img = "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?q=80&w=400&auto=format&fit=crop"
        metro_img = "https://images.unsplash.com/photo-1512411961421-2e624c965e64?q=80&w=400&auto=format&fit=crop"
        car_img = "https://images.unsplash.com/photo-1494976388531-d105809059f3?q=80&w=400&auto=format&fit=crop"
        
        st.markdown(f"""
            <div style="display: flex; gap: 10px; height: 180px;">
                <img src="{bus_img}" style="width: 30%; height: 100%; object-fit: cover; border-radius: 12px;"/>
                <img src="{metro_img}" style="width: 40%; height: 100%; object-fit: cover; border-radius: 12px;"/>
                <img src="{car_img}" style="width: 30%; height: 100%; object-fit: cover; border-radius: 12px;"/>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Transport turlari (Realistik rasmlar bilan)
    st.markdown("### Transport turlarini tanlang")
    
    t_col1, t_col2, t_col3, t_col4, t_col5, t_col6 = st.columns(6)

    transports = [
        {"name": "Avtobuslar", "icon": "🚌", "image": "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?q=80&w=400&auto=format&fit=crop"},
        {"name": "Metro", "icon": "🚇", "image": "https://images.unsplash.com/photo-1512411961421-2e624c965e64?q=80&w=400&auto=format&fit=crop"},
        {"name": "Elektrobuslar", "icon": "🚎", "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=400&auto=format&fit=crop"},
        {"name": "Poyezdlar", "icon": "🚆", "image": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?q=80&w=400&auto=format&fit=crop"},
        {"name": "Taksi", "icon": "🚕", "image": "https://images.unsplash.com/photo-1556108154-150cc3d37a78?q=80&w=400&auto=format&fit=crop"},
        {"name": "Barchasi", "icon": "🔳", "image": "https://images.unsplash.com/photo-1511316712398-3f5f3e433f48?q=80&w=400&auto=format&fit=crop"}
    ]

    cols = [t_col1, t_col2, t_col3, t_col4, t_col5, t_col6]

    for i, transport in enumerate(transports):
        with cols[i]:
            st.markdown(f"""
                <div class="transport-card">
                    <div class="transport-image-container">
                        <img src="{transport['image']}" class="transport-image"/>
                    </div>
                    <span class="transport-icon">{transport['icon']}</span>
                    <h4>{transport['name']}</h4>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Tanlash", key=f"btn_{i}", use_container_width=True):
                st.info(f"{transport['name']} bo'limi tanlandi!")

    # 3. Statistika qismi
    st.markdown("---")
    st.markdown("### Statistika (bugun)")
    stat1, stat2, stat3, stat4 = st.columns(4)

    with stat1:
        st.metric(label="Yangi murojaatlar", value="1 248", delta="12.5%")
    with stat2:
        st.metric(label="Yechilgan", value="1 002")
    with stat3:
        st.metric(label="Ko'rib chiqilmoqda", value="246")
    with stat4:
        st.metric(label="Rad etilgan", value="98", delta="-2.1%", delta_color="inverse")

else:
    st.title(choice)
    st.write(f"{choice} sahifasi hozircha tayyor emas.")