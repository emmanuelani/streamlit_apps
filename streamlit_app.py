import numpy as np
# import seaborn as sns
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from datetime import datetime, time
plt.style.use("ggplot")

# defining the header
st.header("Day 5 of 30 Days of Streamlit - st.write() function")

# using st.write

st.write("Learning streamlit has been fun so far!")

st.write("This particular text is written to the streamit app with st.write")

# creating a pandas dataframe
df = pd.DataFrame(
    {
        "country" : ["Nigeria", "Ghana", "Russia", "Mexico", "Japan"],
        "continent": ["Africa", "Africa", "Europe", "North America", "Asia"],
        "population": [225_000_000, 34_000_000, 143_000_000, 128_000_000, 122_000_000]
    }
)

# using the st.write function to write the dataframe to the streamlit app
st.write("Below is a dataframe:", df, "Above is a dataframe")

# # plotting with seaborn
# plt.figure(figsize=(6, 4))
# sns.barplot(x=df["country"], y=df["population"])
# # plt.savefig("ply")

# st.pyplot(plt)

# adding a slider object/widget
st.header("st.slider")

# creating a sub-header
st.subheader("Slider")

st.write("Slider supports the following datatypes: int, float, data, time, and datetime")

salary = st.slider("How much do you make in your current job in USD?", 0, 500, 55)

st.write(f"I make {salary}K USD")

st.subheader("Range slider")

time = st.slider(
    "How much time do you spend coding in a day?",
    value=(time(1, 40), time(5, 30)) # default value
)

st.write(f"I spend {time[1].hour-time[0].hour} hours coding in a day")

# print(type(time))

st.subheader("Datatime slider")

start = st.slider(
    "When did you start data science?",
    value=datetime(2021, 2, 1, 9, 20),
    format="MM/DD/YYY"
)

st.write(f"I started data science back in {start}")