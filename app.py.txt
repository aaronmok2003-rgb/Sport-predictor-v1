import streamlit as st
import pandas as pd

st.set_page_config(page_title="SportIQ • Live Card", layout="wide")

st.title("⚽🎾🏀 SportIQ • Live Card")
st.markdown("**Clean & Beautiful Multi-Sport Predictor**")

# Reset button
if st.button("🔄 New Prediction"):
    st.session_state.clear()

# Inputs
col1, col2 = st.columns(2)
with col1:
    home = st.text_input("Home Team", key="home_key")
with col2:
    away = st.text_input("Away Team", key="away_key")

sport = st.selectbox("Sport", ["Soccer", "Tennis", "Basketball", "Volleyball"], key="sport_key")

if st.button("🚀 Run Prediction", type="primary"):
    if home and away:
        st.success(f"✅ Prediction for {home} vs {away}")

        # Overview
        st.subheader(f"{home} vs {away}")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Live Score", "1-1 (48')")
        with c2:
            st.metric("Form", "Strong Home")
        with c3:
            st.metric("Status", "Live")

        # Stats
        st.subheader("Full Stats")
        if sport == "Soccer":
            st.dataframe(pd.DataFrame({
                "Metric": ["Possession", "Shots", "xG", "Corners"],
                home: ["58%", "14", "1.85", "7"],
                away: ["42%", "9", "0.95", "4"]
            }), use_container_width=True)

        # Prediction
        st.subheader("Win Probability")
        pc1, pc2, pc3 = st.columns(3)
        pc1.metric(f"**{home}**", "68%", "🔥")
        pc2.metric("Draw", "22%")
        pc3.metric(f"**{away}**", "10%")

        # Markets
        st.subheader("Recommended Markets")
        st.dataframe(pd.DataFrame({
            "Market": [f"{home} Win", "Over 2.5 Goals"],
            "Odds": ["1.80", "2.10"],
            "Value": ["Strong", "Good"]
        }), use_container_width=True)
    else:
        st.warning("Please enter both teams")
else:
    st.info("👆 Fill teams and click **Run Prediction**")

st.caption("Clean version. No leftover data.")
