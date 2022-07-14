from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import pandas as pd

#Setting playable ranges
playable_ranges = [[['2As', '33o', '3As', '4As', '5As', '66o', '6As', '77o', '7Ao', '7As', '88o', '8Ao', '8As', '99o', '9Ao', '9As', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JQs', 'KKo', 'KQs', 'KTs', 'QQo', 'TTo']], [['2As', '33o', '3Ao', '3As', '44o', '4Ao', '4As', '55o', '5Ao', '5As', '66o', '6Ao', '6As', '77o', '7Ao', '7As', '88o', '8Ao', '8As', '99o', '9Ao', '9As', '9Ks', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'TTo'], ['2Ao', '2As', '33o', '3Ao', '3As', '44o', '4Ao', '4As', '55o', '5Ao', '66o', '6Ao', '6As', '6Ks', '7Ao', '7Ks', '8Ao', '8Ko', '8Ks', '8Qs', '99o', '9Js', '9Ko', '9Ks', '9Qs', 'AAo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'JJo', 'JQo', 'JQs', 'JTo', 'JTs', 'KKo', 'KTo', 'QQo', 'QTo', 'QTs', 'TTo']], [['22o', '2Ao', '2As', '33o', '3Ao', '3As', '3Ks', '44o', '4Ao', '4As', '4Ko', '4Ks', '55o', '5Ao', '5As', '5Ko', '5Ks', '66o', '6Ao', '6As', '6Js', '6Ko', '6Ks', '6Qs', '6Ts', '77o', '78s', '7Ao', '7As', '7Js', '7Ko', '7Ks', '7Qs', '88o', '89s', '8Ao', '8As', '8Ko', '8Ks', '8Qo', '99o', '9Ao', '9As', '9Js', '9Ko', '9Ks', '9Qo', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTo', 'JTs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTo', 'QTs', 'TTo'], ['22o', '2Ao', '2As', '2Ks', '33o', '3Ao', '3As', '3Ks', '44o', '4Ao', '4As', '4Ko', '4Ks', '55o', '5Ao', '5As', '5Ko', '5Ks', '5Qs', '66o', '6Ao', '6As', '6Ko', '6Ks', '6Qs', '77o', '7Ao', '7As', '7Js', '7Ko', '7Ks', '7Qs', '88o', '8Ao', '8As', '8Js', '8Ko', '8Ks', '8Qo', '8Qs', '8Ts', '99o', '9Ao', '9As', '9Jo', '9Js', '9Ko', '9Ks', '9Qo', '9Qs', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTo', 'JTs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTo', 'QTs', 'TTo'], ['55o', '5As', '66o', '77o', '7As', '88o', '99o', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATs', 'JJo', 'KKo', 'KQs', 'QQo', 'TTo']], [['22o', '2Ao', '2As', '2Ko', '2Ks', '2Qs', '33o', '3Ao', '3As', '3Ko', '3Ks', '3Qs', '44o', '4Ao', '4As', '4Ko', '4Ks', '4Qs', '55o', '5Ao', '5As', '5Js', '5Ko', '5Ks', '5Qo', '5Qs', '66o', '6Ao', '6As', '6Js', '6Ko', '6Ks', '6Qo', '6Qs', '77o', '7Ao', '7As', '7Jo', '7Js', '7Ko', '7Ks', '7Qo', '7Qs', '7Ts', '88o', '89s', '8Ao', '8As', '8Jo', '8Js', '8Ko', '8Ks', '8Qo', '8Qs', '8To', '8Ts', '99o', '9Ao', '9As', '9Jo', '9Js', '9Ko', '9Ks', '9Qo', '9Qs', '9To', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTo', 'JTs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTo', 'QTs', 'TTo'], ['44o', '55o', '5As', '66o', '6As', '77o', '7As', '88o', '8Ao', '8As', '99o', '9Ao', '9As', '9Js', '9Ks', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTs', 'KKo', 'KQo', 'KQs', 'KTs', 'QQo', 'QTs', 'TTo'], ['AAo', 'AKo', 'AKs', 'AQs', 'JJo', 'KKo', 'QQo']]]
player1,player2,player3,player4 = playable_ranges

def get_results(current_hand):
  results = pd.DataFrame()
  results["position"] = [1,2,2,3,3,3,4,4,4]
  results["all_ins"] = [0,0,1,0,1,2,1,2,3]
  decisions = [current_hand in player1[0],
               current_hand in player2[0],
               current_hand in player2[1],
               current_hand in player3[0],
               current_hand in player3[1],
               current_hand in player3[2],
               current_hand in player4[0],
               current_hand in player4[1],
               current_hand in player4[2]]
  results["decisions"] = decisions
  results = results.groupby(["position","all_ins"])["decisions"].first().unstack()
  return results
  
  

def get_current_hand(card1,card2,is_suited):
  if card1 == card2:
    result = str(card1)+str(card2)+"o"
    return result
  else:
    result = sorted(str(card1) + str(card2) + str(is_suited))
    return "".join(result)


cards = [str(k) for k in range(2,10)] + ["A","K","Q","J","T"]
suits = ["o","s"]

st.sidebar.title("All In Or Fold")

card_1 = st.sidebar.radio("Pick First Card",cards)
card_2 = st.sidebar.radio("Pick Second Card",cards)

suited = st.sidebar.radio("Suited",suits)

current_hand = get_current_hand(card_1,card_2,suited)

st.title(current_hand)

results = get_results(current_hand)

st.dataframe(results)




