import streamlit as st
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

st.set_page_config(page_title="Universal Language Translator", layout="centered")

@st.cache_resource
def load_model():
    model_name = "facebook/m2m100_418M"
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

lang_map = {
    "English": "en", "French": "fr", "German": "de", "Spanish": "es", "Hindi": "hi",
    "Arabic": "ar", "Japanese": "ja", "Chinese": "zh", "Russian": "ru", "Italian": "it",
    "Tamil": "ta", "Telugu": "te", "Malayalam": "ml", "Bengali": "bn"
}

st.title("Lang chnager")
st.markdown("Translate text **from any language to any language** using AI 🤖")

src_text = st.text_area("✍️ Enter your text", height=150)
src_lang = st.selectbox("🌐 Select Source Language", list(lang_map.keys()))
tgt_lang = st.selectbox("🎯 Select Target Language", list(lang_map.keys()))

if st.button("Translate"):
    if src_text.strip() == "":
        st.warning("Please enter text to translate.")
    else:
        src_code = lang_map[src_lang]
        tgt_code = lang_map[tgt_lang]
        
        tokenizer.src_lang = src_code
        encoded = tokenizer(src_text, return_tensors="pt")
        generated_tokens = model.generate(
            **encoded, forced_bos_token_id=tokenizer.get_lang_id(tgt_code)
        )
        result = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
        st.success(f"✅ Translated Text:\n\n{result}")
