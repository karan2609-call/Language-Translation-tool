import streamlit as st
import urllib.request
import urllib.parse
import json

# Page Configuration
st.set_page_config(page_title="Language Translation Tool", page_icon="🌐", layout="centered")

st.title("🌐 AI Language Translation Tool")
st.write("Translate text seamlessly across multiple languages.")

# Supported languages dictionary
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

# UI Layout for Language Selection
col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", list(languages.keys()), index=0)
with col2:
    target_lang = st.selectbox("Target Language", list(languages.keys())[1:], index=1)

# Text Input
input_text = st.text_area("Enter text to translate:", height=150, placeholder="Type or paste your text here...")

def translate_text(text, src, dest):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src}&tl={dest}&dt=t&q={urllib.parse.quote(text)}"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        # Extract translated segments
        translated_sentence = "".join([sentence[0] for sentence in result[0]])
        return translated_sentence

# Translate Action
if st.button("Translate", type="primary"):
    if input_text.strip():
        try:
            translated_text = translate_text(
                input_text, 
                languages[source_lang], 
                languages[target_lang]
            )
            
            st.subheader("Translated Output:")
            st.code(translated_text, language=None)
        except Exception as e:
            st.error(f"Translation error: {e}")
    else:
        st.warning("Please enter some text first.")