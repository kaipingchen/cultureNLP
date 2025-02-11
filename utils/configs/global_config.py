import os
import streamlit as st

def set_global_variables():
    os.environ['intro_max_tokens'] = '512'
    os.environ['gen_max_tokens'] = '512'

    os.environ['minimum_responses'] = '10'
    os.environ['warning_responses'] = '10'
    os.environ['maximum_responses'] = '15'

    os.environ['intro_temp'] = '0.7'
    os.environ['intro_top_p'] = '0.9'
    os.environ['intro_rep_penalty'] = '1'

    os.environ['temp'] = '0.8'
    os.environ['top_p'] = '0.9'
    os.environ['rep_penalty'] = '1.2'