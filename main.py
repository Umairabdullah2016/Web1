import streamlit as st

st.set_page_config(
    page_title="Diary Of A Wimpy Kid | The Third Wheel",
    page_icon="📖",  # You can use an emoji or a path to an image file
    layout="wide",   # optional: 'centered' or 'wide'
)

st.title("Diary of a Wimpy Kid | The Third Wheel")

pdf_url = "https://jumpshare.com/share/OzBRI4N7wDSZX1kXQn9s"

# Try embedding with iframe
st.markdown(f'''
<iframe src="{pdf_url}" width="100%" height="800px"></iframe>
''', unsafe_allow_html=True)

st.write("Credit: Jeff Kinney")

