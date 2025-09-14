import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="Concert Recommendations", layout="wide")

st.title("🎵 Concert Recommendations")

# Load the CSV
try:
    df = pd.read_csv("concerts.csv")
except FileNotFoundError:
    st.error("❌ 'concerts.csv' not found.")
    st.stop()

# Dropdown filters
cities = sorted(df["city"].dropna().unique().tolist())
levels = sorted(df["level"].dropna().unique().tolist())
subtypes = sorted(df["subtype"].dropna().unique().tolist())

city = st.selectbox("Select City", options=[""] + cities)
level = st.selectbox("Select Level", options=[""] + levels)
subtype = st.selectbox("Select Subtype", options=[""] + subtypes)

# Filter logic
filtered = df.copy()
if city:
    filtered = filtered[filtered["city"] == city]
if level:
    filtered = filtered[filtered["level"] == level]
if subtype:
    filtered = filtered[filtered["subtype"] == subtype]

# Sort by popularity
filtered = filtered.sort_values(by="popularity", ascending=False)

# Determine whether to show top 10 or filtered results
if not city and not level and not subtype:
    display_df = df.sort_values(by="popularity", ascending=False).head(10)
    st.subheader("🔥 Top 10 Trending Concerts")
else:
    display_df = filtered
    st.subheader("🎯 Recommended Concerts")

if display_df.empty:
    st.warning("No concerts found matching the selected filters.")
else:
    # Grid layout with 3 per row
    cards_html = """
    <style>
    .grid-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: flex-start;
        padding-top: 10px;
    }
    .event-card {
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        padding: 20px;
        width: calc(33% - 20px);
        box-sizing: border-box;
        transition: transform 0.2s ease, box-shadow 0.3s ease;
    }
    .event-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }
    .event-title {
        font-size: 18px;
        font-weight: bold;
        color: #ffffff;
        color: #3f51b5;
        padding: 8px 12px;
        border-radius: px;
        display: inline-block;
    }
    .event-info {
        font-size: 14px;
        color: #333;
        margin-top: 6px;
    }
    </style>
    <div class="grid-container">
    """

    for _, row in display_df.iterrows():
        cards_html += f"""
        <div class="event-card">
            <div class="event-title">{row['name']}</div>
            <div class="event-info">📅 {row['date']}</div>
            <div class="event-info">📍 {row['city']}</div>
            <div class="event-info">🏷️ {row['subtype']}</div>
            <div class="event-info">🌍 {row['level']}</div>
            <div class="event-info">🔥 Popularity: {row['popularity']}</div>
        </div>
        """

    cards_html += "</div>"
    components.html(cards_html, height=800, scrolling=True)
