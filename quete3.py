import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth

# Récupération des données depuis un dataframe
df = pd.DataFrame([["utilisateur", "utilisateurMDP", "utilisateur@gmail.com", 0, False, "utilisateur"],
                   ["root", "rootMDP", "admin@gmail.com", 0, False, "administrateur"]], columns=["name", "password", "email", "failed_login_attemps", "logged_in", "role"])

# Mise en forme des données pour la fonction stauth.Authenticate()
dictionnairesDesDonnees = {}
for ligne in range(df.shape[0]):
   dictionnairesDesDonnees[df.loc[ligne, "name"]] = df.loc[ligne, :].to_dict()

dictionnaireFormate = {"usernames" : dictionnairesDesDonnees}

authenticator = stauth.Authenticate(
    dictionnaireFormate, #config['credentials'],
    "cookie name",#config['cookie']['name'],
    "cookie key", #config['cookie']['key'],
    30, #config['cookie']['expiry_days'],
    )

def accueil():
    st.title('Bienvenue sur ma page')
    st.image("https://media.giphy.com/media/l44QgmICy0c9u1cJO/giphy.gif")

def photos():
    st.title("Bienvenue dans l'album de mon chat🐱")
    col1, col2, col3 = st.columns(3)
    col1.image("téléchargement1.JPG")
    col2.image("téléchargement2.JPG")
    col3.image("téléchargement3.JPG")

authenticator.login()

if st.session_state["authentication_status"]:
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.write(f'Bienvenue *{st.session_state["name"]}*')
        selection = option_menu(
            menu_title=None,
            options = ["🤩 Accueil", "🐱 Les photos de mon chat"]
        )

    if selection == "🤩 Accueil":
        accueil()
    elif selection == "🐱 Les photos de mon chat":
        photos()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')