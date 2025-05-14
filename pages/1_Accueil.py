import streamlit as st
import base64
import pathlib

def set_background(image_path: str) -> None:
    encoded = base64.b64encode(pathlib.Path(image_path).read_bytes()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{encoded}") center/cover fixed;
            overflow: hidden !important;
        }}
        .overlay {{
            position: fixed; inset: 0;
            background: rgba(15,23,42,0.75);
            z-index: -1;
        }}
        .content-box {{
            background: rgb(193, 39, 45);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-bottom: 2rem;
        }}
        .feature-card {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-left: 4px solid #E74C3C;
        }}
        .main-title {{
            font-size: 3.5rem;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}
        h2 {{
            color: #2C3E50 !important;
        }}
        p {{
            color: black !important;
        }}
        .stButton>button {{
            background-color: rgb(193, 39, 45);
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }}
        </style>
        <div class="overlay"></div>
    """, unsafe_allow_html=True)

set_background("cars11.png")

st.markdown('<div class="main-title">🏠 MOROCCAN CAR PRICE</div>', unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class="content-box">
        <h2>Plateforme d'Estimation des Prix des Voitures d'Occasion au Maroc</h2>
<p style="font-size:1.1rem;">
    Notre application utilise des algorithmes avancés de Machine Learning pour estimer le prix des véhicules avec précision. Basée sur des données réelles du marché marocain, elle prend en compte les caractéristiques clés comme le kilométrage, l'année du modèle, la marque et l'état du véhicule.
</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#E74C3C;">🔍 Estimation Précise</h3>
        <p>Algorithmes avancés spécialement adaptés pour le marché automobile marocain.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#E74C3C;">📊 Données Fiables</h3>
        <p>Analyse basée sur des milliers d'annonces vérifiées pour une estimation réaliste.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3 style="color:#E74C3C;">🚀 Facile à Utiliser</h3>
        <p>Interface intuitive avec sélection dynamique des modèles et marques.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Prêt à estimer le prix de votre voiture?")
if st.button("Commencer la prédiction →"):
    st.switch_page("pages/2_Prediction.py")
    
st.markdown("""
<div style="text-align: center; color: white; margin-top: 3rem;">
    <p style="color: white;">Projet Machine Learning- Licence d'Excellence en IA - Faculté des Sciences Ben M'Sik 2025</p>
</div>
""", unsafe_allow_html=True)