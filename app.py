import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Calculadora de Subida", page_icon="✈️", layout="centered")

NM_PARA_FT = 6076.12

def ft_para_nm(ft):
    return ft / NM_PARA_FT

# Título da aplicação
st.title("Calculadora de Subida por Gradiente")
st.write("Distância horizontal em pés e milhas náuticas")

# Seleção de quantidade de segmentos
num_segs = st.number_input("Quantos segmentos de subida?", min_value=1, max_value=10, value=2)

st.divider()

segmentos = []
alt_inicial_primeiro = st.number_input("Altitude inicial do 1º Segmento (ft)", value=0, step=100)

# Construção dos segmentos na tela
for i in range(num_segs):
    st.subheader(f"Segmento {i + 1}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if i == 0:
            alt_i = alt_inicial_primeiro
            st.info(f"Altitude inicial: **{alt_i} ft**")
        else:
            # Pega a altitude final do segmento anterior
            alt_i = segmentos[-1][1] 
            st.info(f"Altitude inicial (herdada): **{alt_i} ft**")
            
    with col2:
        alt_f = st.number_input(f"Altitude final (ft) - Seg {i+1}", value=int(alt_i + 500), step=100, key=f"alt_f_{i}")
        grad = st.number_input(f"Gradiente (%) - Seg {i+1}", value=3.3, step=0.1, format="%.1f", key=f"grad_{i}")
        
    segmentos.append((alt_i, alt_f, grad))
    st.write("") # Espaçamento

st.divider()

# Botão de Calcular
if st.button("Calcular Subida", type="primary"):
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
        
        # Exibição dos resultados em cards (Métricas)
        col1, col2, col3 = st.columns(3)
        col1.metric("Segmentos", num_segs)
        col2.metric("Distância Total (ft)", f"{round(total_ft):,} ft".replace(",", "."))
        col3.metric("Distância Total (NM)", f"{total_nm:.2f} NM")
        
        # Tabela de Resultados
        st.subheader("Resumo por Trecho")
        
        dados_tabela = []
        for i, ((alt_i, alt_f, grad), dist_ft) in enumerate(zip(segmentos, resultados_ft)):
            dados_tabela.append({
                "Seg.": i + 1,
                "Trecho (ft)": f"{int(alt_i)} → {int(alt_f)}",
                "Gradiente (%)": f"{grad:.1f}%",
                "Dist. (ft)": round(dist_ft),
                "Dist. (NM)": round(ft_para_nm(dist_ft), 2)
            })
            
        df = pd.DataFrame(dados_tabela)
        st.dataframe(df, use_container_width=True, hide_index=True)