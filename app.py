import streamlit as st
import base64
import pathlib


st.set_page_config(
    page_title="Moroccan Car Price",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="auto"
)


def set_background(image_path: str) -> None:
    encoded = base64.b64encode(pathlib.Path(image_path).read_bytes()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{encoded}") center/cover fixed;
            background-size: cover;
        }}
        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(15, 23, 42, 0.85);
            z-index: -1;
        }}
        .content-box {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .nav-card {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #C1272D;
        }}
        </style>
        <div class="overlay"></div>
    """, unsafe_allow_html=True)

set_background("cars11.png")


st.markdown("""
<h1 style="color: white; text-align: center; font-size: 3rem; margin-bottom: 2rem;">
    🚗 MOROCCAN CAR PRICE
</h1>
""", unsafe_allow_html=True)


st.markdown("""
<div class="content-box">
    <h2 style="color: #2C3E50; margin-bottom: 1rem;">
        Système intelligent d'estimation des prix des voitures au Maroc
    </h2>
    <p style="color: #333;">
        Sélectionnez une section dans la barre latérale ou cliquez sur l'une des options ci-dessous
    </p>
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="nav-card">
        <h3 style="color: #C1272D;">🏠 Accueil</h3>
        <p style="color: #555;">Page d'accueil avec présentation de l'application</p>
        <a href="/Accueil" target="_self" style="
            display: block;
            text-align: center;
            background: #C1272D;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            width: 100%;
            cursor: pointer;
            font-weight: bold;
            margin-top: 0.5rem;
            text-decoration: none;
        ">Accéder</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-card">
        <h3 style="color: #C1272D;">💰 Prédiction</h3>
        <p style="color: #555;">Estimez le prix de votre voiture en quelques clics</p>
        <a href="/Prediction" target="_self" style="
            display: block;
            text-align: center;
            background: #C1272D;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            width: 100%;
            cursor: pointer;
            font-weight: bold;
            margin-top: 0.5rem;
            text-decoration: none;
        ">Accéder</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="nav-card">
        <h3 style="color: #C1272D;">ℹ️ À Propos</h3>
        <p style="color: #555;">Découvrez notre équipe et notre mission</p>
        <a href="/About_Us" target="_self" style="
            display: block;
            text-align: center;
            background: #C1272D;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            width: 100%;
            cursor: pointer;
            font-weight: bold;
            margin-top: 0.5rem;
            text-decoration: none;
        ">Accéder</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-card">
        <h3 style="color: #C1272D;">📩 Contact</h3>
        <p style="color: #555;">Envoyez-nous vos questions et commentaires</p>
        <a href="/Contact_Us" target="_self" style="
            display: block;
            text-align: center;
            background: #C1272D;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            width: 100%;
            cursor: pointer;
            font-weight: bold;
            margin-top: 0.5rem;
            text-decoration: none;
        ">Accéder</a>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div style="text-align: center; color: white; margin-top: 3rem;">
    <p style="color: white;">Projet Machine Learning - Licence d'Excellence en IA - Faculté des Sciences Ben M'Sik 2025</p>
</div>
""", unsafe_allow_html=True)
