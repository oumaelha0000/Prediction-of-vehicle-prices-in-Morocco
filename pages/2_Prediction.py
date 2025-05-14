import streamlit as st
import pandas as pd
import joblib, base64, pathlib
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime

st.set_page_config("\U0001F697 Prédiction de Prix Voiture", layout="wide")

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
            background: rgba(15,23,42,0.60);
            z-index: -1;
        }}
        label {{
            background: rgb(193, 39, 45);
            padding: 0.3rem 0.8rem;
            border-radius: 6px;
            color: #ffffff !important;
            font-size: 1.05rem;
            font-weight: 700 !important;
            text-shadow: 0 0 6px rgba(0,0,0,.4);
            margin-bottom: 6px;
            display: inline-block;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
        }}
        .title-box {{
            display: inline-block;
            padding: 0.2rem 1.6rem;
            border-radius: 10px;
            border: 1px solid rgba(255,255,255,.25);
            margin: 0.2rem auto 0.8rem auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }}
        .title-box h1 {{
            margin: 0;
            font-size: 4rem;
            font-weight: 600;
            letter-spacing: 3px;
            color: #fff;
        }}
        section.main > div {{
            max-width: 95% !important;
            padding-bottom: 0 !important;
        }}
        </style>
        <div class="overlay"></div>
    """, unsafe_allow_html=True)

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime

def generate_estimation_card(inputs: dict, price: float) -> BytesIO:
    try:
        bg = Image.open("carte_bg4.png").resize((800, 600))
    except:
        bg = Image.new("RGB", (800, 600), "#ffffff")

    image = bg.copy()
    draw = ImageDraw.Draw(image)
    width, height = image.size

    try:
        title_font = ImageFont.truetype("arialbd.ttf", 40)
        label_font = ImageFont.truetype("arial.ttf", 22)
        value_font = ImageFont.truetype("arial.ttf", 22)
        price_font = ImageFont.truetype("arialbd.ttf", 34)
        footer_font = ImageFont.truetype("arial.ttf", 16)
    except:
        title_font = label_font = value_font = price_font = footer_font = ImageFont.load_default()

    title_text = "Carte d'Estimation de Prix"
    bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_w = bbox[2] - bbox[0]
    draw.rounded_rectangle([50, 20, width - 50, 80], fill="#1e3a2a", radius=12)
    draw.text(((width - title_w) // 2, 30), title_text, font=title_font, fill="white")

    y = 110
    for label, value in inputs.items():
        draw.text((60, y), f"{label}:", fill="#374151", font=label_font)
        draw.text((400, y), str(value), fill="#111827", font=value_font)
        y += 32

    draw.rounded_rectangle([60, y + 20, width - 60, y + 90], fill="#dcfce7", radius=16)
    price_text = f"Prix estimé: {price:,.0f} MAD"
    bbox_price = draw.textbbox((0, 0), price_text, font=price_font)
    price_w = bbox_price[2] - bbox_price[0]
    draw.text(((width - price_w) // 2, y + 40), price_text, fill="#166534", font=price_font)

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    draw.text((60, height - 18), f"Estimation faite le: {timestamp}", fill="#111111", font=footer_font)
    draw.text((width - 390, height - 18), "Projet ML – Licence IA – FSB Ben M'Sik", fill="#111111", font=footer_font)

    img_bytes = BytesIO()
    image.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return img_bytes


set_background("cars2.png")

st.markdown("""
<div style="text-align:center">
    <div class="title-box">
        <h1>MOROCCAN CAR PRICE</h1>
    </div>
</div>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([2, 3])

with left_col:
    st.markdown("""
    <h2 style="
        font-size:2rem;
        font-weight:700;
        color:#ffffff;
        background-color:rgb(193, 39, 45);
        padding:0.5rem 1rem;
        border-radius:8px;
        margin-bottom:1.8rem;">
        💰 Prix estimé sera affiché ici :
    </h2>
    """, unsafe_allow_html=True)

model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

localisations = sorted([c.replace("localisation_", "") for c in columns if c.startswith("localisation_")])
boites = sorted([c.replace("boite_vitesses_", "") for c in columns if c.startswith("boite_vitesses_")])
carburants = sorted([c.replace("type_carburant_", "") for c in columns if c.startswith("type_carburant_")])
origines = sorted([c.replace("origine_", "") for c in columns if c.startswith("origine_")])
etats = sorted([c.replace("etat_", "") for c in columns if c.startswith("etat_")])
modeles = sorted([c.replace("modele_", "") for c in columns if c.startswith("modele_")])
marques = sorted([c.replace("marque_", "") for c in columns if c.startswith("marque_")])

with right_col:
    col1, col2 = st.columns(2)

    with col1:
        localisation = st.selectbox("Localisation", localisations)
        annee_modele = st.number_input("Année du modèle", 1980, 2025, step=1)
        marque = st.selectbox("Marque", marques)
        modele = st.selectbox("Modèle", modeles)
        nombre_de_portes = st.selectbox("Nombre de portes", [2, 3, 4, 5])
        premiere_main = st.selectbox("Première main", ["Oui", "Non"])

    with col2:
        boite_vitesses = st.selectbox("Boîte de vitesses", boites)
        type_carburant = st.selectbox("Type de carburant", carburants)
        kilometrage = st.number_input("Kilométrage (km)", 0, 800_000, step=1_000)
        puissance_fiscale = st.number_input("Puissance fiscale", 1, 20)
        origine = st.selectbox("Origine", origines)
        etat = st.selectbox("État", etats)

    input_dict = {
        "annee_modele": annee_modele,
        "kilometrage": kilometrage,
        "nombre_de_portes": nombre_de_portes,
        "puissance_fiscale": puissance_fiscale,
        "premiere_main": 1 if premiere_main == "Oui" else 0,
        f"localisation_{localisation}": 1,
        f"boite_vitesses_{boite_vitesses}": 1,
        f"type_carburant_{type_carburant}": 1,
        f"origine_{origine}": 1,
        f"etat_{etat}": 1,
        f"marque_{marque}": 1,
        f"modele_{modele}": 1,
    }

    X_input = pd.DataFrame([0] * len(columns), index=columns).T
    for k, v in input_dict.items():
        if k in X_input.columns:
            X_input[k] = v

    X_input[scaler.feature_names_in_] = scaler.transform(X_input[scaler.feature_names_in_])

    if st.button("\U0001F4B0 Prédire le prix", use_container_width=True):
        price = model.predict(X_input)[0]

        with left_col: 
            st.markdown(f"""
                <div style='
                    background:rgba(34,197,94,.15);
                    border:1px solid #22c55e;
                    border-radius:12px;
                    padding:1.2rem;
                    font-size:1.8rem;
                    font-weight:bold;
                    text-align:center;
                    color:#bbf7d0;
                    margin-top:1rem;'>
                     {price:,.0f} MAD
                </div>
            """, unsafe_allow_html=True)

        user_info = {
            "Marque": marque,
            "Modèle": modele,
            "Année": annee_modele,
            "Kilométrage": f"{kilometrage:,} km",
            "Boîte de Vitesses": boite_vitesses,
            "Type de Carburant": type_carburant,
            "Puissance Fiscale": puissance_fiscale,
            "Nombre de Portes": nombre_de_portes,
            "État": etat,
            "Première Main": premiere_main,
            "Origine": origine,
            "Localisation": localisation,
        }

        card_img = generate_estimation_card(user_info, price)
        st.download_button(
            label="📅 Télécharger la carte d'estimation",
            data=card_img,
            file_name="carte_estimation.png",
            mime="image/png"
        )

st.markdown("""
<div style="text-align: center; color: white; margin-top: 3rem;">
    <p style="color: white;">Projet Machine Learning - Licence d'Excellence en IA - Faculté des Sciences Ben M'Sik 2025</p>
</div>
""", unsafe_allow_html=True)
