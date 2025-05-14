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
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            max-width: 800px;
            margin: 0 auto;
        }}
        .main-title {{
            font-size: 3rem;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}
        # .stTextInput>div>div>input, .stTextArea>div>textarea {{
        #     border: 1px solid #E74C3C;
        #     border-radius: 8px;
        #     background: rgba(255,255,255,0.8);
        # }}
        .stButton>button {{
            background-color: rgb(193, 39, 45);
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            width: 100%;
        }}
        .contact-info {{
            background: rgb(231 76 60 / 49%);
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 2rem;
        }}
        </style>
        <div class="overlay"></div>
    """, unsafe_allow_html=True)

set_background("cars11.png")

st.markdown('<div class="main-title">📩 Contactez-Nous</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Nom Complet*")
        email = st.text_input("Email*")
        subject = st.text_input("Sujet")
        message = st.text_area("Message*", height=150)
        
        st.markdown("<small>* Champs obligatoires</small>", unsafe_allow_html=True)
        
        submitted = st.form_submit_button("Envoyer le Message")
        if submitted:
            if name and email and message:
                st.success("Merci pour votre message! Nous vous contacterons bientôt.")
            else:
                st.error("Veuillez remplir tous les champs obligatoires")
    
    st.markdown("""
    <div class="contact-info">
    <h3>📌 Notre Équipe</h3>
    <p><strong>Service client :</strong> Disponible du lundi au vendredi, 9h-17h</p>
    <p><strong>Email :</strong> contact@moroccancarprice.com</p>
    <p><strong>Téléphone :</strong> +212 6 00 00 00 11</p>
</div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
if st.button("← Retour à l'accueil"):
    st.switch_page("pages/1_Accueil.py")

st.markdown("""
<div style="text-align: center; color: white; margin-top: 3rem;">
    <p style="color: white;">Projet Machine Learning - Licence d'Excellence en IA - Faculté des Sciences Ben M'Sik 2025</p>
</div>
""", unsafe_allow_html=True)