import sys
sys.path.append('C:\\Users\\6063454\\AppData\\Roaming\\Python\\Python312\\site-packages')

import streamlit as st
from utils.openarena_chain import call_open_arena_chain

# Use an absolute path to the image
st.image("C:\\Users\\6063454\\MyStreamlitApp\\TR.png")
st.title("Open Arena Chains Demo")

query = st.text_area("Enter your Query Here")

workflow_id = st.text_input("Enter your Workflow Id Here")

chain_token = st.text_input("Enter your token", type="password")

submit_button = st.button("Submit")

if submit_button:
    if query and workflow_id and chain_token:
        response = call_open_arena_chain(query=query, esso_token=chain_token, workflow_id=workflow_id)
        st.subheader("Response")
        st.write(response)
    else:
        st.warning("Please fill all the required fields")
