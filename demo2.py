import streamlit as st

# Import your function (assuming it's in a separate file)
from utils.openarena_chain import call_open_arena_chain

def main():
    st.title("Open Arena Chain Query App")

    # Input fields
    query = st.text_area("Enter your query:")
    esso_token = st.text_input("Enter ESSO token:")
    workflow_id = st.text_input("Enter workflow ID:")

    # Submit button
    if st.button("Submit"):
        if query and esso_token and workflow_id:
            try:
                # Call the function with user inputs
                response = call_open_arena_chain(query, esso_token, workflow_id)
                
                # Display the response
                st.subheader("Response:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please fill in all fields.")

if __name__ == "__main__":
    main()