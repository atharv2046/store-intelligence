import streamlit as st
import pandas as pd

total_visitors = 100

zone1 = 70
zone2 = 45
billing = 30

data = {
    "Section": [
        "Zone 1",
        "Zone 2",
        "Billing"
    ],

    "Visitors": [
        zone1,
        zone2,
        billing
    ]
}

df = pd.DataFrame(data)

df["Percentage"] = (
    df["Visitors"]
    / total_visitors
    * 100
).round(2)

st.title("Store Analytics")

st.metric(
    "Total Visitors",
    total_visitors
)

st.dataframe(df)

st.bar_chart(
    df.set_index("Section")["Visitors"]
)