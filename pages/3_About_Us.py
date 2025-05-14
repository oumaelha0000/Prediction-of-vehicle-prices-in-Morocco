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
        .stButton>button {{
            background-color: rgb(193, 39, 45);
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }}
        .overlay {{
            position: fixed; inset: 0;
            background: rgba(15,23,42,0.75);
            z-index: -1;
        }}
        .content-box {{
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-bottom: 2rem;
            border: 2px solid white;
        }}
         .content-box2 {{
            background: rgb(231 76 60 / 49%);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            margin-bottom: 2rem;
        }}
        .team-card {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-left: 4px solid #C1272D;
        }}
        .main-title {{
            font-size: 3rem;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}
        h2 {{
            color: #2C3E50 !important;
            margin-bottom: 1.5rem !important;
            position: relative;
            padding-bottom: 0.5rem;
        }}
        h2::after {{
            content: "";
            position: absolute;
            bottom: 0;
            left: 0;
            width: 60px;
            height: 2px;
            background: #C1272D;
        }}
        h3 {{
            color: #C1272D !important;
            margin-bottom: 1rem !important;
        }}
        p {{
            color: #333333 !important;
            margin-bottom: 0.8rem !important;
        }}
        strong {{
            color: #2C3E50 !important;
        }}
        ul {{
            margin-top: 1rem !important;
            padding-left: 1.5rem !important;
        }}
        li {{
            margin-bottom: 0.5rem !important;
        }}
        .mission-box {{
            background: rgba(193, 39, 45, 0.1);
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border-left: 4px solid #C1272D;
        }}
        </style>
        <div class="overlay"></div>
    """, unsafe_allow_html=True)

set_background("cars11.png")

st.markdown('<div class="main-title">ℹ️ À Propos de Nous</div>', unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class="content-box">
        <div class="mission-box">
            <h2>Notre Mission</h2>
    <p>
        Développer une plateforme fiable d'estimation des prix des voitures d'occasion au Maroc, en combinant <strong>analyse de données</strong>, <strong>nettoyage de données</strong>, et <strong>modélisation avancée</strong>. Notre objectif est de fournir des estimations précises et transparentes pour aider les acheteurs et vendeurs.
    </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class="content-box">
        <h2>👥 Notre Équipe</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="team-card">
            <h3>Experts en Data Science</h3>
            <p><strong>Spécialistes en analyse de données</strong></p>
            <p>Notre équipe technique possède une expertise approfondie en machine learning et analyse de données.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="team-card">
            <h3>Conseillers Automobiles</h3>
            <p><strong>Professionnels du secteur automobile</strong></p>
            <p>Nos conseillers apportent leur connaissance du marché pour valider nos modèles et estimations.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class="content-box">
            <h2>📚 Notre Approche</h2>
            <p>Nous combinons technologie et expertise sectorielle pour fournir des estimations fiables et actualisées du marché automobile marocain.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="content-box2">
            <h2>Technologies utilisées :</h2>
            <ul>
    <li><strong>Collecte de données :</strong> Analyse de milliers d'annonces du marché marocain</li>
    <li><strong>Prétraitement :</strong> Nettoyage et normalisation des données</li>
    <li><strong>Modélisation :</strong> Algorithmes de machine learning avancés</li>
    <li><strong>Interface :</strong> Plateforme conviviale et intuitive</li>
</ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
if st.button("← Retour à l'accueil"):
    st.switch_page("pages/1_Accueil.py")

st.markdown("""
<div style="text-align: center; color: white; margin-top: 3rem;">
    <p style="color: white;">Projet Machine Learning - Licence d'Excellence en IA - Faculté des Sciences Ben M'Sik 2025</p>
</div>
""", unsafe_allow_html=True)