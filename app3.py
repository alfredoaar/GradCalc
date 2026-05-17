st.markdown("""
<style>

/* ===== FUNDO GLOBAL ===== */
.stApp {
    background: linear-gradient(135deg, #07111f, #0b1d35);
    color: #ffffff;
    font-family: 'Inter', sans-serif;
}

/* ===== TÍTULOS ===== */
h1 {
    text-align: center;
    color: #60A5FA;
    font-size: 3rem !important;
    font-weight: 800;
    animation: fadeInDown 1s ease;
    text-shadow: 0 0 15px rgba(96,165,250,0.5);
}

h2, h3 {
    color: #93C5FD;
    text-align: center;
}

/* ===== SUBTÍTULO ===== */
.subtitle {
    text-align: center;
    color: #CBD5E1;
    font-size: 1.1rem;
    margin-bottom: 2rem;
    animation: fadeIn 1.5s ease;
}

/* ===== CARDS ===== */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    transition: 0.3s;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-5px);
    border: 1px solid #60A5FA;
    box-shadow: 0 0 25px rgba(96,165,250,0.4);
}

/* ===== MÉTRICAS ===== */
div[data-testid="stMetricValue"] {
    text-align: center;
    color: #60A5FA;
    font-size: 32px !important;
    font-weight: bold;
}

div[data-testid="stMetricLabel"] {
    text-align: center;
    color: #E2E8F0;
    font-size: 15px;
}

/* ===== INPUTS ===== */
.stNumberInput {
    background: rgba(255,255,255,0.03);
    border-radius: 15px;
    padding: 10px;
}

/* ===== EXPANDERS ===== */
.streamlit-expanderHeader {
    background: rgba(255,255,255,0.04);
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.08);
    color: #93C5FD !important;
    font-weight: bold;
}

/* ===== BOTÃO ===== */
.stButton > button {
    width: 100%;
    border-radius: 15px;
    height: 3.5em;
    background: linear-gradient(90deg, #2563EB, #1D4ED8);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    transition: all 0.3s ease;
    box-shadow: 0 0 20px rgba(37,99,235,0.4);
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #3B82F6, #2563EB);
    box-shadow: 0 0 30px rgba(59,130,246,0.7);
}

/* ===== DATAFRAME ===== */
[data-testid="stDataFrame"] {
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
}

/* ===== LINHA DIVISÓRIA ===== */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #60A5FA, transparent);
    margin-top: 2rem;
    margin-bottom: 2rem;
}

/* ===== ANIMAÇÕES ===== */
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #0b1d35;
}

::-webkit-scrollbar-thumb {
    background: #2563EB;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)
