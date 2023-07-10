import streamlit as st
from url_shortener import URLShortener

st.set_page_config(page_title='Remember.ly', page_icon=":link:")

url_shortener = URLShortener()

st.title('Remember.ly')
st.markdown('## Your personal and memorable URL shortener')

url_input = st.text_input('Enter your URL here:')
if url_input:
    short_url = url_shortener.shorten_url(url_input)
    st.success(f'Your shortened URL is: {short_url}')
