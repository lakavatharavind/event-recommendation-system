import streamlit as st

st.set_page_config(page_title="Event Recommender", layout="centered")

st.markdown("""
    <style>
    .btn-container {
        display: flex;
        justify-content: space-around;
        margin-top: 60px;
    }
    .btn {
        display: inline-block;
        padding: 20px 40px;
        background: linear-gradient(135deg, #4c6ef5, #15aabf);
        color: white;
        border-radius: 20px;
        font-size: 20px;
        font-weight: bold;
        text-decoration: none;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .btn:hover {
        background: linear-gradient(135deg, #15aabf, #4c6ef5);
        transform: translateY(-5px);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎉 Welcome to the Event Recommendation System")

st.markdown("""
    <div class="btn-container">
        <a href="/Concerts" class="btn">🎵 Concerts</a>
        <a href="/Sports" class="btn">🏟️ Sports</a>
        <a href="/Festivals" class="btn">🎪 Festivals</a>
    </div>
""", unsafe_allow_html=True)
