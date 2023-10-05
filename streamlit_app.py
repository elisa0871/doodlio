import streamlit as st
import random

# Liste der Hintergrundbilder
background_images = ["1H2P1.png", "1H2P2.png", "1H3P1.png", "1H3P2.png", "3P1H.png", "1H1P1.png", "1H1P2.png"]

# Funktion zum Anzeigen eines zufälligen Hintergrundbilds
def set_random_background():
    background_image = random.choice(background_images)
    st.markdown(
        f'<style>body{{background-image: url("{background_image}"); background-size: cover;}}</style>',
        unsafe_allow_html=True,
    )

# Liste der Bilder
images = ["Boo!.png", "brokenheart.png", "GeschenkOffen.png", "Pilz.png", "SkelettBlob.png"]

# Streamlit-Anwendung
st.title("Bildwechsel-Webanwendung")

# Anzeigen der Hintergrundbilder
set_random_background()

# Buttons für den Bildwechsel
button_cols = st.beta_columns(5)
for i in range(len(images)):
    if button_cols[i].button(f"Button {i+1}"):
        st.image(images[i], use_column_width=True)

# Reset-Knopf
if st.button("Alle Bilder zurücksetzen"):
    set_random_background()

