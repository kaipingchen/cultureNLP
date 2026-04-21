from pymongo import MongoClient
import streamlit as st
import certifi
import os
from utils.session import get_session_state


# MongoDB Setup
def get_mongo_client():
    mongo_uri = st.secrets['mongo_uri']
    client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
    return client


# Insert user data into database
def insert_data_to_db(data):
    client = get_mongo_client()
    db = client['latinx-nlp']
    collection = db['user-data']
    collection.insert_one(data)
    client.close()


# Register new user data
def handle_new_submission():
    data = {
        'country': os.getenv('country'),
        'topic': os.getenv('topic'),
        'id': get_session_state('respondent_id'),
        'system_instruction': get_session_state('system_instruction'),
        'shorter_system_instruction': get_session_state('shorter_system_instruction'),
        'introduction': get_session_state('introduction'),
        'intro_reaction': get_session_state('intro_reaction'),
        'chat_history': get_session_state('chat_history'),
        'reaction_history': get_session_state('reaction_history'),
        'comments': get_session_state('comments')
    }
    insert_data_to_db(data)
