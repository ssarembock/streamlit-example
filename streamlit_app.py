from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import pandas as pd

"""
# Decision


"""
cards = [str(k) for k in range(2,9)] + ["A","K","Q","J","T"]
suits = ["o","s"]

st.sidebar.title("All In Or Fold")

card_1 = st.sidebar.radio("Pick First Card",cards)
card_2 = st.sidebar.radio("Pick Second Card",cards)

suited = st.sidebar.radio("Suited",suits)

