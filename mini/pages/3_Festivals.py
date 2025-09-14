import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="Festival Recommendations", layout="wide")
st.title("🎪 Festival Event Recommendations")

# Load CSV
try:
    df = pd.read_csv("festivals.csv")
except FileNotFoundError:
    st.error("❌ 'festivals.csv' not found.")
    st.stop()

# Filters
cities = sorted(df["city"].dropna().unique().tolist())
levels = sorted(df["level"].dropna().unique().tolist())
types = sorted(df["subtype"].dropna().unique().tolist())

city = st.selectbox("Select City", options=[""] + cities)
level = st.selectbox("Select Level", options=[""] + levels)
subtype = st.selectbox("Select Festival Type", options=[""] + types)

# Apply Filters
filtered = df.copy()
if city:
    filtered = filtered[filtered["city"] == city]
if level:
    filtered = filtered[filtered["level"] == level]
if subtype:
    filtered = filtered[filtered["subtype"] == subtype]

filtered = filtered.sort_values(by="popularity", ascending=False)

# Display Results
if not city and not level and not subtype:
    display_df = df.sort_values(by="popularity", ascending=False).head(10)
    st.subheader("🔥 Top 10 Trending Festivals")
else:
    display_df = filtered
    st.subheader("🎯 Recommended Festivals")

if display_df.empty:
    st.warning("No festivals found matching the selected filters.")
else:
    # Grid Layout for Events
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
        color: #8e44ad;
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
