import numpy as np
# import seaborn as sns
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
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