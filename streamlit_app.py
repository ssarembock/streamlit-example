from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import pandas as pd

#Setting playable ranges
#iteration 11 new version
playable_sets =[{0: ['22o', '2As', '33o', '3As', '44o', '4Ao', '4As', '55o', '5Ao', '5As', '66o', '6Ao', '6As', '77o', '7Ao', '7As', '7Ks', '88o', '8Ao', '8As', '8Ks', '8Qs', '99o', '9Ao', '9As', '9Js', '9Ks', '9Qs', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTo', 'QTs', 'TTo']}, {0: ['22o', '2Ao', '2As', '33o', '3Ao', '3As', '44o', '4Ao', '4As', '55o', '5Ao', '5As', '5Ks', '66o', '6Ao', '6As', '6Ks', '77o', '7Ao', '7As', '7Ks', '88o', '89s', '8Ao', '8As', '8Js', '8Ks', '8Qs', '99o', '9Ao', '9As', '9Js', '9Ko', '9Ks', '9Qs', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTo', 'JTs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTo', 'QTs', 'TTo'], 1: ['55o', '66o', '77o', '88o', '99o', '9As', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'KKo', 'KQs', 'QQo', 'TTo']}, {(0, 1): ['2As', '33o', '44o', '4As', '55o', '5As', '66o', '6As', '77o', '7As', '88o', '8Ao', '8As', '99o', '9Ao', '9As', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKs', 'JQs', 'KKo', 'KQo', 'KQs', 'KTs', 'QQo', 'TTo'], (1, 0): ['55o', '66o', '77o', '7As', '88o', '8As', '99o', '9Ao', '9As', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKs', 'KKo', 'KQo', 'KQs', 'QQo', 'TTo'], (0, 0): ['22o', '2Ao', '2As', '2Js', '2Ko', '2Ks', '2Qs', '2Ts', '33o', '34s', '35s', '3Ao', '3As', '3Js', '3Ko', '3Ks', '3Qs', '44o', '45s', '46s', '47s', '48s', '4Ao', '4As', '4Js', '4Ko', '4Ks', '4Qo', '4Qs', '4Ts', '55o', '56s', '57s', '58s', '59s', '5Ao', '5As', '5Js', '5Ko', '5Ks', '5Qo', '5Qs', '66o', '67o', '67s', '68s', '69s', '6Ao', '6As', '6Js', '6Ko', '6Ks', '6Qo', '6Qs', '6Ts', '77o', '78o', '78s', '79o', '79s', '7Ao', '7As', '7Jo', '7Js', '7Ko', '7Ks', '7Qo', '7Qs', '7To', '7Ts', '88o', '89o', '89s', '8Ao', '8As', '8Jo', '8Js', '8Ko', '8Ks', '8Qo', '8Qs', '8To', '8Ts', '99o', '9Ao', '9As', '9Jo', '9Js', '9Ko', '9Ks', '9Qo', '9Qs', '9To', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTo', 'JTs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTo', 'QTs', 'TTo'], (1, 1): ['66o', '77o', '88o', '99o', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATs', 'JJo', 'JKs', 'KKo', 'KQs', 'KTs', 'QQo', 'TTo']}, {(0, 1, 1): ['33o', '55o', '66o', '77o', '88o', '8As', '8Qs', '99o', '9As', '9Ks', '9Qs', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKs', 'JQs', 'JTs', 'KKo', 'KQo', 'KQs', 'KTs', 'QQo', 'QTs', 'TTo'], (1, 1, 0): ['44o', '55o', '66o', '77o', '88o', '99o', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATs', 'JJo', 'JKs', 'JTs', 'KKo', 'KQo', 'KQs', 'KTs', 'QQo', 'TTo'], (1, 0, 0): ['22o', '33o', '3As', '44o', '4As', '55o', '5As', '66o', '6As', '77o', '7Ao', '7As', '88o', '8Ao', '8As', '99o', '9Ao', '9As', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'KKo', 'KQo', 'KQs', 'KTs', 'QQo', 'TTo'], (0, 0, 1): ['22o', '2Ao', '2As', '2Ks', '33o', '3Ao', '3As', '3Ks', '44o', '4Ao', '4As', '4Ks', '55o', '5Ao', '5As', '5Ko', '5Ks', '66o', '6Ao', '6As', '6Ko', '6Ks', '77o', '7Ao', '7As', '7Ko', '7Ks', '7Qs', '88o', '8Ao', '8As', '8Ko', '8Ks', '8Qs', '99o', '9Ao', '9As', '9Js', '9Ko', '9Ks', '9Qo', '9Qs', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTo', 'JTs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTo', 'QTs', 'TTo'], (1, 0, 1): ['55o', '66o', '77o', '88o', '8As', '99o', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKs', 'JQs', 'JTs', 'KKo', 'KQo', 'KQs', 'KTs', 'QQo', 'QTs', 'TTo'], (0, 0, 0): ['22o', '23o', '23s', '24o', '24s', '25o', '25s', '26o', '26s', '27o', '27s', '28o', '28s', '29o', '29s', '2Ao', '2As', '2Jo', '2Js', '2Ko', '2Ks', '2Qo', '2Qs', '2To', '2Ts', '33o', '34o', '34s', '35o', '35s', '36o', '36s', '37o', '37s', '38o', '38s', '39o', '39s', '3Ao', '3As', '3Jo', '3Js', '3Ko', '3Ks', '3Qo', '3Qs', '3To', '3Ts', '44o', '45o', '45s', '46o', '46s', '47o', '47s', '48o', '48s', '49o', '49s', '4Ao', '4As', '4Jo', '4Js', '4Ko', '4Ks', '4Qo', '4Qs', '4To', '4Ts', '55o', '56o', '56s', '57o', '57s', '58o', '58s', '59o', '59s', '5Ao', '5As', '5Jo', '5Js', '5Ko', '5Ks', '5Qo', '5Qs', '5To', '5Ts', '66o', '67o', '67s', '68o', '68s', '69o', '69s', '6Ao', '6As', '6Jo', '6Js', '6Ko', '6Ks', '6Qo', '6Qs', '6To', '6Ts', '77o', '78o', '78s', '79o', '79s', '7Ao', '7As', '7Jo', '7Js', '7Ko', '7Ks', '7Qo', '7Qs', '7To', '7Ts', '88o', '89o', '89s', '8Ao', '8As', '8Jo', '8Js', '8Ko', '8Ks', '8Qo', '8Qs', '8To', '8Ts', '99o', '9Ao', '9As', '9Jo', '9Js', '9Ko', '9Ks', '9Qo', '9Qs', '9To', '9Ts', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQo', 'JQs', 'JTo', 'JTs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTo', 'QTs', 'TTo'], (0, 1, 0): ['22o', '2As', '33o', '3As', '44o', '4Ao', '4As', '55o', '5Ao', '5As', '66o', '6Ao', '6As', '77o', '7Ao', '7As', '88o', '8Ao', '8As', '99o', '9Ao', '9As', '9Ks', 'AAo', 'AJo', 'AJs', 'AKo', 'AKs', 'AQo', 'AQs', 'ATo', 'ATs', 'JJo', 'JKo', 'JKs', 'JQs', 'KKo', 'KQo', 'KQs', 'KTo', 'KTs', 'QQo', 'QTs', 'TTo'], (1, 1, 1): ['35s', '5Ks', '5Qs', '68s', '6Ks', '6Ts', '77o', '7As', '7Ks', '88o', '8As', '8Js', '8Ts', '99o', '9Ks', 'AAo', 'AKo', 'AKs', 'AQo', 'AQs', 'JJo', 'JQs', 'JTs', 'KKo', 'KQs', 'QQo', 'TTo']}]

#player1,player2,player3,player4 = playable_ranges

def get_results(current_hand):
  yes_no = {}
  player_num = 0
  for players in playable_sets:
    yes_no[player_num] = {}
    for key in players.keys():
        yes_no[player_num][key] = current_hand in players[key]
    player_num+=1
  result = pd.DataFrame(yes_no)
  result.columns = ["First","Dealer","Small","Big"]
  

  return result[["First","Dealer"]][:2],result["Small"][2:6].sort_index(),result["Big"][6:].sort_index()

  
  

def get_current_hand(card1,card2,is_suited):
  if card1 == card2:
    result = str(card1)+str(card2)+"o"
    return result
  else:
    result = sorted(str(card1) + str(card2) + str(is_suited))
    return "".join(result)


cards = [str(k) for k in range(2,10)] + ["T","J","Q","K","A"]
suits = ["o","s"]

st.sidebar.title("All In Or Fold")

card_1 = st.sidebar.radio("Pick First Card",cards)
card_2 = st.sidebar.radio("Pick Second Card",cards)

suited = st.sidebar.radio("Suited",suits)

current_hand = get_current_hand(card_1,card_2,suited)

st.title(current_hand)

results = get_results(current_hand)

st.write("First Or Dealer")
st.dataframe(results[0])

st.write("Small")
st.dataframe(results[1])

st.write("Big")
st.dataframe(results[2])




