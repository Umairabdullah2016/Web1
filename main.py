import streamlit as st

st.title("All In One Diary of a Wimpy Kid book")

pdf_url = "https://jumpshare.com/share/OzBRI4N7wDSZX1kXQn9s"

# Try embedding with iframe
st.markdown(f'''
<iframe src="{pdf_url}" width="100%" height="800px"></iframe>
''', unsafe_allow_html=True)

st.write("Credit: Jeff Kinney")

