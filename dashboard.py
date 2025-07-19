import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="GoAlgo Live Execution Dashboard", layout="wide")

st.title("📊 GoAlgo MVP Sprint - Live GPT Team Dashboard")

# Simulated Status Table
data = [
    ["🔐 AuthGPT", "Implement & test PIN lock", "T+1", "🚧 In Progress"],
    ["🎨 FrontendGPT", "Build chat shell + tabs", "T+2", "🚧 In Progress"],
    ["🔌 BackendGPT", "Create auth, portfolio, txn endpoints", "T+2", "🟢 Queued"],
    ["📊 DataGPT", "Connect to NIFTY & clean OHLCV", "T+2", "🟢 Queued"],
    ["📈 SimuGPT", "Wait for cleaned data", "T+3", "🔒 Blocked"],
    ["📉 QuantGPT", "Prepare metric formulas", "T+3", "🔒 Blocked"],
    ["📧 EmailGPT", "Scaffold export template", "T+5", "🟢 Queued"],
    ["🧪 TestGPT", "Define UI/flow test cases", "T+3", "🟡 Scoping"],
    ["👷 InfraGPT", "Manage daily sync & updates", "Daily", "✅ Active"]
]

columns = ["GPT Bot", "Today's Task", "ETA", "Status"]
df = pd.DataFrame(data, columns=columns)

# Conditional formatting for status
def status_color(val):
    if "✅" in val:
        return "background-color: #d3f9d8"
    elif "🚧" in val:
        return "background-color: #fff3bf"
    elif "🟢" in val:
        return "background-color: #d0ebff"
    elif "🔒" in val:
        return "background-color: #ffa8a8"
    elif "🟡" in val:
        return "background-color: #ffd8a8"
    return ""

styled_df = df.style.applymap(status_color, subset=["Status"])

st.dataframe(styled_df, use_container_width=True)

st.markdown("---")
st.subheader("📅 CEO Notes")
st.info("All modules briefed. InfraGPT now live-monitoring task flow. Blocked GPTs (Simu/Quant) scheduled to start after T+2 data readiness.")

st.caption("Updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
