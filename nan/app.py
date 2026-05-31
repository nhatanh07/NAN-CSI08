
import streamlit as st

st.set_page_config(page_title="MusicAI", page_icon="🎵", layout="wide")

st.markdown("""
<style>
#MainMenu,header,footer{visibility:hidden;}
.stApp{background:#121212;color:white;}
section[data-testid="stSidebar"]{background:#000;}
.hero{
background:linear-gradient(135deg,#1DB954,#0d7c3f);
padding:50px;border-radius:20px;margin-bottom:30px;color:white;
}
.card{
background:#181818;padding:12px;border-radius:16px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🎵 MusicAI")
st.sidebar.success("Spotify Style UI")

st.markdown('<div class="hero"><h1>AI Music Genre Classification</h1><p>Listen • Discover • Predict</p></div>', unsafe_allow_html=True)

st.subheader("🔥 Trending Songs")
cols = st.columns(4)
songs=["Pop Hit","Rock Star","Jazz Night","Classic Mood"]
for c,s in zip(cols,songs):
    with c:
        st.image("https://picsum.photos/300")
        st.markdown(f'<div class="card"><b>{s}</b></div>', unsafe_allow_html=True)
