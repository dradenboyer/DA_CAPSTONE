import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import random

df = pd.read_csv("NBA_Rookies_by_Year.csv")

st.header(':blue[Draden Boyer DA_Capstone]')
st.title(':red[Rookie of the Year]')

st.set_option('deprecation.showPyplotGlobalUse', False)


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

st.subheader('The Award')
st.image('nba-rookie-year-award-pic.jpeg', width=500)

st.subheader('Rookie Player Statistics 1980-2016')
st.dataframe(df) 

with st.expander('Variable Descriptions'):
  st.write('GP: Games Played that season.')
  st.write('MIN: Average amount of minutes played')
  st.write('PTS: Average amount of points scored')
  st.write('FGM: Field goals made')
  st.write('FGA: Field goals attempted')
  st.write('FG%: Field goal percentage')
  st.write('3P Made: Amount of 3 pointers made')
  st.write('3PA: Amount of 3 Pointers Attempted')
  st.write('FTM: Amount of free throws made')
  st.write('FTA: Amount of free throws attempted')
  st.write('FT%: Free throw percentage of makes and attempts')
  st.write('OREB: Amount of offensive rebounds')
  st.write('DREB: Amount of defensive rebounds')
  st.write('REB: Total amount of rebounds')
  st.write('AST: Amount of assist completed')
  st.write('STL: Amount of steals completed')
  st.write('BLK: Amount of blocks completed')
  st.write('TOV: Amount of turnovers had')
  st.write('EFF: Overall efficiency of the player')


st.subheader('Values/Models')
tab1, tab2, tab3 = st.tabs(["Coefficients", "Linear Regression", "OLS Summary"])

with tab1:
  st.image("coeff-values.jpg", width=600)
  st.image("coeff-titles.jpg", width=600)
  st.write("This might be a little confusing to understand and that’s okay. Explained very simply we have numeric values now each of those align with a column whether it be games played, minutes, or points scored. The values show how much impact they have on the selection of rookie of the year. The closer a value is to 1 the more impact it has on the selection. Based on the model EFF or efficiency of a player has a large impact on Rookie of the Year candidates.")
with tab2:
  st.image("rookie-stats-ss.jpg", width=300)
  st.write("The numbers below the fitted section on the right indicate how likely a player was to win the roty award based on the model I have created. Now you might question people like Alonzo Mourning who had such a high rating but still did not win roty. That has a simple answer… his rookie season was the same as Shaquille ONeal.")
  st.write('Do you like my model? ')
  agree = st.checkbox('Yes! I love it')
  disagree = st.checkbox("Nah! 😅")
  if agree:
    st.write('Lets Gooo! 🤤')
  if disagree:
    st.write('Ahhh cmon I worked hard 😒')

with tab3:
  st.image('ols-final-sum.jpg', width=600)
  st.write('In the summary output provided, the p-values are listed under the "P>|t|" column in the table. These p-values indicate the significance of the corresponding independent variables in predicting the dependent variable in this case, fitted. The null hypothesis in this case is that the corresponding independent variable has no significant effect on the dependent variable. So, if the p-value is less than the significance level usually 0.05, we can reject the null hypothesis and conclude that the corresponding independent variable has a significant effect on the dependent variable.Looking at the output provided, we see that all of the independent variables  have p-values less than 0.05. This suggests that they are statistically significant in predicting the dependent variable. Also meaning we can reject the Null-Hypothesis. The R-squared value of 1.000 indicates that about 100% of the variance in the dependent variable can be explained by the independent variables included in the model.')

st.write("Based on my linear regression model here are some of the most likely players to have won the Roty award:")
st.image("top-rookies.jpg", width=600)


with st.sidebar:
  st.subheader('This Projects Github Link')
  st.write('https://github.com/dradenboyer/DA_CAPSTONE')
  st.subheader('Video Walkthrough')
  st.write('put video link here')
  st.subheader('My Portfolio')
  st.write('https://dradenboyer.github.io/')
  if st.button('Thanks for tuning in!'):
    st.balloons()
  else:
    st.write(' ')

st.subheader('Rookie Averages')

with st.expander("Players that averaged x amount of PTS"):
  st.subheader('Players that averaged x amount of PTS')
  st.bar_chart(df['PTS'].value_counts())

with st.expander("Players that averaged x amount of AST"):
  st.subheader('Players that averaged x amount of AST')
  st.bar_chart(df['AST'].value_counts())

with st.expander("Players that averaged x amount of REB"):
  st.subheader('Players that averaged x amount of REB')
  st.bar_chart(df['REB'].value_counts())

with st.expander("Players that averaged x amount of STL"):
  st.subheader('Players that averaged x amount of STL')
  st.bar_chart(df['STL'].value_counts())

with st.expander("Players that averaged x amount of BLK"):
  st.subheader('Players that averaged x amount of BLK')
  st.bar_chart(df['BLK'].value_counts())

with st.expander("Players that averaged x amount of EFF"):
  st.subheader('Players that averaged x amount of EFF')
  st.bar_chart(df['EFF'].value_counts())

# Create a function to generate the plot
def plot_top_players(df, columns, n=5):
    # Sort the DataFrame by multiple columns and select the top n rows
    top_n = df.sort_values(columns, ascending=False).head(n)

    # Create the line chart with multiple lines
    for col in columns:
        plt.plot(top_n['Name'], top_n[col], label=col)

    # Customize the plot
    plt.title(f'Best {n} Rookie Statlines')
    plt.xlabel('')
    plt.ylabel('')
    plt.legend()

    # Show the plot
    st.pyplot()

# Define the columns to plot
columns_to_plot = ['PTS', 'AST', 'REB', 'STL', 'BLK', 'EFF']


# Show the plot for the selected columns
plot_top_players(df, columns_to_plot)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.write('From looking at these top 5 players and above at the rest of the other Rookie Statlinesx we can deduct that Statlines are very important when conducting a voting process for ROTY, So few players had such high EFF as well as PTS scored so with those 2 categories specifically being crucially important we see why these 5 rookies were some of the best to ever do it.')

