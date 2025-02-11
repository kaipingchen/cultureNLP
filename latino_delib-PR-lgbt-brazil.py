import os
import streamlit as st
from utils.session import session_setup, get_session_state, set_session_state
from utils.pages import show_chat_page, show_feedback_page
from utils.configs.global_config import set_global_variables
from utils.configs.PR_config import set_PR_variables


# Configuration
def config():
    set_global_variables()
    set_PR_variables(1, 'Brasil', 'os direitos LGBTQ')


# Style
def load_css():
    css_file_path = os.path.join(os.path.dirname(__file__), 'styles', 'styles.css')

    with open(css_file_path, 'r') as f:
        css = f.read()

    background_color_user = get_session_state('background_color_user')
    background_color_bot = get_session_state('background_color_bot')

    st.markdown(f'''
        <style>
        :root {{
            --background-color-user: {background_color_user};
            --background-color-bot: {background_color_bot};
        }}
        {css}
        </style>
    ''', unsafe_allow_html=True)


st.set_page_config(
    layout='wide',
    page_title=os.getenv('chatbot'),
    page_icon='🤖'
)


# Start session
def main():
    config()
    session_setup()
    load_css()

    if st.session_state.get('next_page', False):
        set_session_state('current_page', 'feedback')

    current_page = st.session_state.get('current_page', 'chat')

    if current_page == 'feedback':
        show_feedback_page()
    else:
        show_chat_page()


if __name__ == '__main__':
    main()
