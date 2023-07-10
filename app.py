import streamlit as st
from url_shortener import URLShortener

st.title('URL Shortener')

url_shortener = URLShortener()

url_input = st.text_input('Enter your URL here:')
if url_input:
    short_url = url_shortener.shorten_url(url_input)
    st.write(f'Your shortened URL is: {short_url}')
