import streamlit as st

# Titel der Webanwendung
st.title('Meine Streamlit-Webanwendung')

# Einfacher Text
st.write('Willkommen auf meiner Website!')

# Fügen Sie eine Schaltfläche hinzu
if st.button('Klick mich'):
    st.write('Du hast die Schaltfläche geklickt!')

# Fügen Sie eine Texteingabe hinzu
user_input = st.text_input('Gib etwas ein:')
st.write('Du hast eingegeben:', user_input)