from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import pandas as pd

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
cards = [str(k) for k in range(2,9)] + ["A","K","Q","J","T"]
suits = ["o","s"]

card_1 = st.radio("Pick First Card",cards)
card_2 = st.radio("Pick Second Card",cards)

suited = st.radio("Suited",suits)

