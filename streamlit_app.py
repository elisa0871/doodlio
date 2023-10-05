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
images = ["GeschenkZu.png", "Boo!.png", "brokenheart.png", "GeschenkOffen.png", "Pilz.png", "SkelettBlob.png"]

# Zufällige Reihenfolge der Bilder
random.shuffle(images)

# Streamlit-Anwendung
st.title("Bildwechsel-Webanwendung")

# Anzeigen der Hintergrundbilder
set_random_background()

# Buttons für den Bildwechsel
button_cols = st.columns(5)  # Verwenden Sie st.columns statt st.beta_columns

for i in range(len(images)):
    if i < len(button_cols) and button_cols[i].button(f"Button {i+1}"):
        st.image(images[i], use_column_width=True)


# Reset-Knopf
if st.button("Alle Bilder zurücksetzen"):
    set_random_background()

