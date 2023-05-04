import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

df = pd.read_csv("NBA_Rookies_by_Year.csv")

st.header(':blue[Draden Boyer Capstone]')
st.title(':red[Rookie of the Year]')

# Expander section
with st.expander("Project Details"):
  st.write("""The main goal of this project is to create a model that analyzes all of the data from previous rookie of the year award winners to be able to predict based on statistics who would be most likely to win that award each year. I think this subject is very interesting and I think a lot of others would agree. On average 1.6 million tune in to watch NBA regular season games across widely known tv streaming services. This does not include clips on social media or other platforms which many basketball fans use to keep up with the NBA""")

with st.expander("Hypothesis Model"):
  st.write("""The Player's statistics: The most important factor in predicting the NBA ROTY is the player's statistics. The model could take into account the player's points per game (PPG), rebounds per game (RPG), assists per game (APG), steals per game (SPG), blocks per game (BPG), efficiency (EFF), and so much more!""")

with st.expander("Dataset Descriptions"):
  st.write("""Historical Data: The NBA has a wealth of historical data on players, teams, and games, which can be used to identify patterns and trends in the performance of rookies over the years.
Predictive Modeling: A linear regression model can help predict which rookies are most likely to win the award based on their performance in various statistical categories, such as points per game, rebounds, assists, and field goal percentage.
Objective Evaluation: By using a data-driven approach, you can eliminate bias and subjectivity in the evaluation process, and focus solely on the statistical performance of the players.
Better Decision-Making: With a reliable model in place, you can make more informed decisions on which rookies to draft, trade, or sign in free agency, based on their potential to win the Rookie of the Year award and contribute to your team's success.
Competitive Advantage: By leveraging data and analytics to make smarter decisions, you can gain a competitive advantage over other teams that rely on more traditional scouting methods.
""")
# Image upload and text input section
st.subheader('The Award')
st.image('nba-rookie-year-award-pic.jpeg', width=500)


# Dataframe and Chart display section

st.subheader('Rookie Player Statistics 1980-2016')
st.dataframe(df) 


# Tabs section
st.subheader('Values/Models')
tab1, tab2 = st.tabs(["Coefficients", "Linear Regression"])

with tab1:
  st.image("coeff-values.jpg", width=600)
  st.image("coeff-titles.jpg", width=600)
  st.write("This might be a little confusing to understand and that’s okay. Explained very simply we have numeric values now each of those align with a column whether it be games played, minutes, or points scored. The values show how much impact they have on the selection of rookie of the year. The closer a value is to 1 the more impact it has on the selection. Based on the model EFF or efficiency of a player has a large impact on Rookie of the Year candidates.")

with tab2:
  st.image("rookie-stats-ss.jpg", caption="The numbers below the fitted section on the right indicate how likely a player was to win the roty award based on the model I have created. Now you might question people like Alonzo Mourning who had such a high rating but still did not win roty. That has a simple answer… his rookie season was the same as Shaquille ONeal. ", width=300)
  
  st.write('Do you like my model? ')
  agree = st.checkbox('Yes! I love it')
  disagree = st.checkbox("Nah! 😅")
  if agree:
    st.write('Lets Gooo! 🤤')
  if disagree:
    st.write('Ahhh cmon I worked hard 😒')

with st.sidebar:
  st.subheader('This is a secret')
  if st.button('Do not Click'):
    st.balloons()
  else:
    st.write(' ')

st.subheader('Players that averaged x amount of PTS')
st.bar_chart(df['PTS'].value_counts())
st.subheader('Players that averaged x amount of AST')
st.bar_chart(df['AST'].value_counts())
st.subheader('Players that averaged x amount of REB')
st.bar_chart(df['REB'].value_counts())
