import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Aircraft Distance Traveled Calculator in SID with multiple PDG", 
    page_icon="✈️", 
    layout="centered" # Ideal para celular e PC
)

# --- CSS CUSTOMIZADO PARA ESTÉTICA PREMIUM E CENTRALIZAÇÃO ---
st.markdown("""
    <style>
    /* Centralizar títulos e textos principais */
    h1, h2, h3 {
        text-align: center;
        color: #1E3A8A; /* Azul marinho elegante */
        font-family: 'Inter', sans-serif;
    }
    .subtitle {
        text-align: center;
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Centralizar Métricas (Resultados) */
    div[data-testid="stMetricValue"] {
        text-align: center;
        color: #1E3A8A;
        font-size: 28px !important;
        font-weight: bold;
    }
    div[data-testid="stMetricLabel"] {
        text-align: center;
        font-size: 16px;
    }

    /* Estilizar o botão principal */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2563EB;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNÇÕES DE CÁLCULO ---
NM_PARA_FT = 6076.12

def ft_para_nm(ft):
    return ft / NM_PARA_FT

# --- CABEÇALHO ---
st.markdown("<h1>✈️ Calculadora de Distância por PDG</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Calculadora de Distância Percorrida por Aeronave em SID com múltiplos PDG(s)</div>", unsafe_allow_html=True)

st.divider()

# --- CONFIGURAÇÃO INICIAL ---
st.markdown("### ⚙️ Configuração Geral")
col_geral1, col_geral2 = st.columns(2)

with col_geral1:
    num_segs = st.number_input("Quantidade de segmentos", min_value=1, max_value=10, value=2)
with col_geral2:
    alt_inicial_primeiro = st.number_input("Altitude inicial (ft)", value=0, step=100)

st.write("") # Espaçamento

# --- SEGMENTOS DE SUBIDA ---
st.markdown("### 📍 Configuração dos Segmentos")

segmentos = []

# Uso de expanders deixa a interface limpa, excelente para celular
for i in range(num_segs):
    with st.expander(f"Configurar Segmento {i + 1}", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            if i == 0:
                alt_i = alt_inicial_primeiro
                st.info(f"Altitude Inicial: **{alt_i} ft**")
            else:
                # Pega a altitude final do segmento anterior
                alt_i = segmentos[-1][1] 
                st.info(f"Alt. Inicial (Auto): **{alt_i} ft**")
                
        with col2:
            alt_f = st.number_input(f"Altitude Final (ft)", value=int(alt_i + 500), step=100, key=f"alt_f_{i}")
            grad = st.number_input(f"Gradiente (%)", value=3.3, step=0.1, format="%.1f", key=f"grad_{i}")
            
        segmentos.append((alt_i, alt_f, grad))

st.write("") # Espaçamento

# --- PROCESSAMENTO E RESULTADOS ---
if st.button("Calcular", type="primary"):
    st.divider()
    
    resultados_ft = []
    erro = False
    
    # Validação e Cálculo
    for i, (alt_i, alt_f, grad) in enumerate(segmentos, 1):
        if grad <= 0:
            st.error(f"Erro no Segmento {i}: O gradiente deve ser maior que 0%.")
            erro = True
        elif alt_f <= alt_i:
            st.error(f"Erro no Segmento {i}: A altitude final deve ser maior que a inicial.")
            erro = True
        else:
            resultados_ft.append((alt_f - alt_i) / (grad / 100))
            
    if not erro:
        total_ft = sum(resultados_ft)
        total_nm = ft_para_nm(total_ft)
        
        st.markdown("### 📊 Resultado")
        
        # Exibição dos resultados em cards centralizados
        col_res1, col_res2, col_res3 = st.columns(3)
        col_res1.metric("Segmentos", num_segs)
        col_res2.metric("Dist. Total (ft)", f"{round(total_ft):,} ft".replace(",", "."))
        col_res3.metric("Dist. Total (NM)", f"{total_nm:.2f} NM")
        
        st.write("")
        st.markdown("### Resumo por Trecho")
        
        # Tabela de Resultados Otimizada
        dados_tabela = []
        for i, ((alt_i, alt_f, grad), dist_ft) in enumerate(zip(segmentos, resultados_ft)):
            dados_tabela.append({
                "Seg.": f"#{i + 1}",
                "Trecho (ft)": f"{int(alt_i)} → {int(alt_f)}",
                "Grad (%)": f"{grad:.1f}%",
                "Dist. (ft)": f"{round(dist_ft):,}".replace(",", "."),
                "Dist. (NM)": f"{ft_para_nm(dist_ft):.2f}"
            })
            
        df = pd.DataFrame(dados_tabela)
        
        # Tabela expansível na largura correta
        st.dataframe(df, use_container_width=True, hide_index=True)
