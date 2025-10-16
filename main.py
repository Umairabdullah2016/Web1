import streamlit as st

st.title("All In One Diary of a wimpy kid book")

pdf_url = "https://jumpshare.com/share/OzBRI4N7wDSZX1kXQn9s"

# Try embedding with iframe
st.markdown(f'''
<iframe src="{pdf_url}" width="100%" height="800px")

st.write("Credit: Jeff Kinney")
