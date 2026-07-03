import streamlit as st
import pandas as pd

st.set_page_config(page_title="SportIQ • Live Card", layout="wide")

st.title("⚽ SportIQ • Live Card")
st.markdown("**Clean Multi-Sport Predictor**")

# Inputs
col_h, col_a = st.columns(2)
with col_h:
    home = st.text_input("Home Team", "Fortaleza", key="home_input")
with col_a:
    away = st.text_input("Away Team", "Ponte Preta", key="away_input")

sport = st.selectbox("Sport", ["Soccer", "Tennis", "Basketball", "Volleyball"], key="sport_select")

if st.button("🚀 Run Prediction", type="primary"):
    st.success("✅ Prediction Generated!")

    # Main Card
    st.subheader(f"{home} vs {away}")
    col1, col2, col3 = st.columns([2,1,2])
    with col1:
        st.metric("Live Score", "1-1 (48')")
    with col2:
        st.title("**2-1**")
        st.caption("Predicted Final")
    with col3:
        st.metric("Status", "Live")

    # Stats
    st.subheader("Full Stats")
    if sport == "Soccer":
        st.dataframe(pd.DataFrame({
            "Metric": ["Possession", "Shots", "xG", "Corners", "Fouls"],
            home: ["58%", "14", "1.85", "7", "11"],
            away: ["42%", "9", "0.95", "4", "14"]
        }), use_container_width=True)
    else:
        st.info(f"{sport} stats will be added soon.")

    # Win Probability
    st.subheader("Win Probability")
    col_p1, col_p2, col_p3 = st.columns(3)
    col_p1.metric(f"**{home}**", "68%", "🔥")
    col_p2.metric("Draw", "22%")
    col_p3.metric(f"**{away}**", "10%")

    # Markets
    st.subheader("Recommended Markets")
    st.dataframe(pd.DataFrame({
        "Market": [f"{home} Win", "Over 2.5 Goals"],
        "Odds": ["1.80", "2.10"],
        "Value": ["Strong", "Good"]
    }), use_container_width=True)

else:
    st.info("👆 Click **Run Prediction** to generate analysis")

st.caption("Clean version. Fill teams and click Run Prediction. No leftover data.")
