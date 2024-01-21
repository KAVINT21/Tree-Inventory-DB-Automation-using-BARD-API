# import streamlit as st
# from langchain_helper import get_few_shot_db_chain
#
# st.title("CSR Tree Adoption: Database Q&A ")
#
# question = st.text_input("Question: ")
#
# if question:
#     chain = get_few_shot_db_chain()
#     response = chain.run(question)
#
#     st.header("Answer")
#     st.write(response)

import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Set page title and favicon
st.set_page_config(
    page_title="Tree Inventory DB Automation",
    page_icon="🌳",  # You can use an emoji as a favicon
    layout="wide",
)

# Add a title and description
st.title("Tree Inventory DB: Database Q&A(DB Automation)")
st.markdown(
    "Ask questions about tree adoption, and get answers based on the Tree Inventory database."
)

# Add a sidebar with additional options
st.sidebar.header("Options")
selected_option = st.sidebar.radio("Select an option", ["Home", "About", "Contact"])

# Main content
if selected_option == "Home":
    question = st.text_input("Ask a Question:")
    if st.button("Get Answer"):
        if question:
            chain = get_few_shot_db_chain()
            response = chain.run(question)
            st.success("Answer:")
            st.write(response)
        else:
            st.warning("Please enter a question.")
elif selected_option == "About":
    st.header("Tree Availability")
    st.write("This is a platform for answering questions related to tree adoption.")
    # Add more information as needed
elif selected_option == "Contact":
    st.header("Contact Us")
    st.write("For inquiries, please email us at support@csrtreeadoption.com")
    # Add more contact information as needed
