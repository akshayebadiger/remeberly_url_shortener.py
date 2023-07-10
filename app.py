import streamlit as st
from url_shortener import URLShortener

st.title('Rememberly')

url_shortener = URLShortener()

url_input = st.text_input('Enter your URL here:')
theme = st.selectbox('Choose a theme:', ['marvel', 'hollywood', 'elements', 'animals', 'fruits'])
if url_input:
    short_url = url_shortener.shorten_url(url_input, theme)
    st.write(f'Your shortened URL is: {short_url}')
