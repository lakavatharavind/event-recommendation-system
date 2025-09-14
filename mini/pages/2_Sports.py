import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="Sports Recommendations", layout="wide")
st.title("🏅 Sports Event Recommendations")

# Load CSV
try:
    df = pd.read_csv("sports.csv")
except FileNotFoundError:
    st.error("❌ 'sports_events.csv' not found.")
    st.stop()

# Filters
cities = sorted(df["city"].dropna().unique().tolist())
levels = sorted(df["level"].dropna().unique().tolist())
main_types = ["Indoor", "Outdoor"]

city = st.selectbox("Select City", options=[""] + cities)
level = st.selectbox("Select Level", options=[""] + levels)
main_type = st.radio("Select Event Type", options=main_types, horizontal=True)

# Filter subtypes based on Indoor/Outdoor
if main_type == "Indoor":
    subtypes = sorted(df[df["subtype"].str.lower().str.contains("indoor")]["subtype"].unique())
else:
    subtypes = sorted(df[df["subtype"].str.lower().str.contains("outdoor")]["subtype"].unique())

# Remove the "Indoor" or "Outdoor" part from subtype for display
subtypes = [subtype.replace("Indoor ", "").replace("Outdoor ", "") for subtype in subtypes]

subtype = st.selectbox("Select Sport", options=[""] + subtypes)

# Apply Filters
filtered = df.copy()
if city:
    filtered = filtered[filtered["city"] == city]
if level:
    filtered = filtered[filtered["level"] == level]
if subtype:
    filtered = filtered[filtered["subtype"].str.contains(subtype, case=False)]

filtered = filtered.sort_values(by="popularity", ascending=False)

# Display Results
if not city and not level and not subtype:
    display_df = df.sort_values(by="popularity", ascending=False).head(10)
    st.subheader("🔥 Top 10 Trending Sports Events")
else:
    display_df = filtered
    st.subheader("🎯 Recommended Sports Events")

if display_df.empty:
    st.warning("No events found matching the selected filters.")
else:
    # Grid Layout
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
        color: #2e7d32;
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
        # Display only the sport name without "Indoor" or "Outdoor"
        event_subtype = row['subtype'].replace("Indoor ", "").replace("Outdoor ", "")
        cards_html += f"""
        <div class="event-card">
            <div class="event-title">{row['name']}</div>
            <div class="event-info">📅 {row['date']}</div>
            <div class="event-info">📍 {row['city']}</div>
            <div class="event-info">🏷️ {event_subtype}</div>
            <div class="event-info">🌍 {row['level']}</div>
            <div class="event-info">🔥 Popularity: {row['popularity']}</div>
        </div>
        """

    cards_html += "</div>"
    components.html(cards_html, height=800, scrolling=True)
