import streamlit as st
import webbrowser

st.set_page_config(
    page_title="Sentimental Analysis",
    page_icon="🤖",
    initial_sidebar_state="collapsed"
)
def redirect(_url):
    link = ""
    st.markdown(link, unsafe_allow_html=True)
st.title("Login")
username=st.text_input('username', '')
password=st.text_input('password', '',type='password')
if st.button('SUBMIT'):
    if username=='admin' and password =='admin':
        webbrowser.open("http://localhost:8501/main")
    else:
        st.write("Invalid user/password")
