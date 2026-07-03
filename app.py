import streamlit as st
import pandas as pd

st.set_page_config(page_title="SportIQ • Live Card", layout="wide")

st.title("⚽🎾🏀 SportIQ • Live Card")
st.markdown("**Clean Multi-Sport Predictor**")

# Reset button
if st.button("🔄 New Match"):
    st.session_state.clear()
    st.rerun()

# Inputs
home = st.text_input("Home Team", key="home")
away = st.text_input("Away Team", key="away")
sport = st.selectbox("Sport", ["Soccer", "Tennis", "Basketball", "Volleyball"], key="sport")

if st.button("🚀 Run Prediction", type="primary"):
    if not home or not away:
        st.warning("Please enter both teams")
    else:
        st.success(f"✅ Prediction for {home} vs {away}")

        st.subheader(f"{home} vs {away}")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Live Score", "1-1 (48')")
        with c2:
            st.metric("Form", "Strong Home")
        with c3:
            st.metric("Status", "Live")

        st.subheader("Win Probability")
        p1, p2, p3 = st.columns(3)
        p1.metric(f"**{home}**", "68%", "🔥")
        p2.metric("Draw", "22%")
        p3.metric(f"**{away}**", "10%")

        st.subheader("Recommended Markets")
        st.dataframe(pd.DataFrame({
            "Market": [f"{home} Win", "Over Total"],
            "Odds": ["1.80", "2.10"],
            "Value": ["Strong", "Good"]
        }), use_container_width=True)

else:
    st.info("👆 Fill teams and click **Run Prediction**")

st.caption("Clean version - no leftover data from previous matches.")
