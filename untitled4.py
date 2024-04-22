#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:15:57 2024

@author: benkelly
"""
import streamlit as st
import altair as alt 
import pandas as pd

st.title("Plotly NFL Fantasy Football RB Matchup Ratings")
st.header("Week 16")
st.subheader("Player Matchup Data")

stats = {
    'Week 16 Starting RB (Team)': ['Christian McCaffrey (SF)', 'Kyren Williams (LAR)', 'Alvin Kamara (NO)', 'Raheem Mostert (MIA)', 'Jahmyr Gibbs (DET)', 'Travis Etienne Jr. (JAC)', 'Rachaad White (TB)', 'Saquon Barkley (NY)', 'Joe Mixon (CIN)', 'James Cook (BUF)', 'Isiah Pacheco (KC)', 'Austin Ekeler (LAC)', 'Derrick Henry (TEN)','Tony Pollard (DAL)', 'Kenneth Walker III (SEA)', 'Breece Hall (NYJ)', 'Bijan Robinson (ATL)', 'DAndre Swift (PHI)', 'James Conner (ARI)', 'Jerome Ford (CLE)', 'Gus Edwards (BAL)', 'Jaylen Warren (PIT)', 'Aaron Jones (GB)', 'Javonte Williams (DEN)', 'Chuba Hubbard (CAR)', 'DOnta Foreman (CHI)', 'Devin Singletary (HOU)', 'Ezekiel Elliot (NE)', 'Antonio Gibson (WAS)', 'Ty Chandler (MIN)', 'Zamir White (LV)', 'Trey Sermon (IND)'],
    'Opposing Team': ['BAL', 'NO', 'LAR', 'DAL', 'MIN', 'TB', 'JAC', 'PHI', 'PIT', 'LAC', 'LV', 'BUF', 'SEA', 'MIA', 'TEN', 'WAS', 'IND', 'NYG', 'CHI', 'HOU', 'SF', 'CIN', 'CAR', 'NE', 'GB', 'ARI', 'CLE', 'DEN', 'NYJ', 'DET', 'KC', 'ATL'],
    'RB Points per Reception PPG': ['25.2', '20.9', '19.8', '18.3', '17', '16.9', '16.2', '15.6', '15.3', '15.3', '14.5', '14.4', '14.3', '13.9', '13.9', '13.6', '13.5', '12.6', '12.3', '12.2', '11.4', '11.3', '10.9', '10.7', '10.6', '10.1', '9.5', '9.2', '8.1', '5.6', '2.8', '1.0'],
    'Opponent RB PPG Ranking': ['8', '11', '1', '18', '9', '3', '15', '6', '21', '23', '24', '14', '31', '13', '7', '30', '28', '26', '19', '16', '5', '20', '27', '17', '22', '32', '12', '29', '25', '2', '10', '4']
}
tabledata = pd.DataFrame(stats) #creating table so the user can see the data going into the graph

tabledata.index += 1 #changing starting number on far left from 0 to 1

table = st.table(tabledata)

#allowing the user to sort the graph by the streamlit button feature, sort by each column
sorted_tabledata = tabledata.copy()
sorted_data = {}

for column in tabledata.columns:
    sorted_data[column] = st.button(f'Sort by {column}')
    if sorted_data[column]:
        if column in ['RB Points per Reception PPG']:
            sorted_tabledata[column] = sorted_tabledata[column].astype(float)
        elif column in ['Opponent RB PPG Ranking']:
            sorted_tabledata[column] = sorted_tabledata[column].astype(int)
        sorted_tabledata = sorted_tabledata.sort_values(by=column) 


table.table(sorted_tabledata)

#Entering x-axis and y-axis points, and adding the player initials for each point as label
source = pd.DataFrame({
    'Opponent RB Defense Rank': [8, 11, 1, 18, 9, 3, 15, 6, 21, 23, 24, 14, 31, 13, 7, 30, 28, 26, 19, 16, 5, 20, 27, 17, 22, 32, 12, 29, 25, 2, 10, 4],
    'RB PPG': [25.2, 20.9, 19.8, 18.3, 17.0, 16.9, 16.2, 15.6, 15.3, 15.3, 14.5, 14.4, 14.3, 13.9, 13.9, 13.6, 13.5, 12.6, 12.3, 12.2, 11.4, 11.3, 10.9, 10.7, 10.6, 10.1, 9.5, 9.2, 8.1, 5.6, 2.8, 1.0],
    'RB Names': ['CMC', 'KW', 'AK', 'RM', 'JG', 'TE', 'RW', 'SB', 'JM', 'JC', 'IP', 'AE', 'DH', 'TP', 'KW', 'BH', 'BR', 'DSW', 'JC', 'JF', 'GE', 'JWA', 'AJ', 'JWI', 'CH', 'DF', 'DSI', 'EE', 'AG', 'TC', 'ZW', 'TS']
})
#altair scatter plot syntax to help make graph and change x and y axis titles
points = alt.Chart(source).mark_point().encode(
    x='Opponent RB Defense Rank:Q',
    y='RB PPG:Q'
)

text = points.mark_text(
   align='left',
   baseline='middle',
    dx=7
).encode(
   text='RB Names'
)

points + text

final_stats = {
    'Week 16 Starting RB (Team)': ['Christian McCaffrey (SF)', 'Kyren Williams (LAR)', 'Alvin Kamara (NO)', 'Raheem Mostert (MIA)', 'Jahmyr Gibbs (DET)', 'Travis Etienne Jr. (JAC)', 'Rachaad White (TB)', 'Saquon Barkley (NY)', 'Joe Mixon (CIN)', 'James Cook (BUF)', 'Isiah Pacheco (KC)', 'Austin Ekeler (LAC)', 'Derrick Henry (TEN)','Tony Pollard (DAL)', 'Kenneth Walker III (SEA)', 'Breece Hall (NYJ)', 'Bijan Robinson (ATL)', 'DAndre Swift (PHI)', 'James Conner (ARI)', 'Jerome Ford (CLE)', 'Gus Edwards (BAL)', 'Jaylen Warren (PIT)', 'Aaron Jones (GB)', 'Javonte Williams (DEN)', 'Chuba Hubbard (CAR)', 'DOnta Foreman (CHI)', 'Devin Singletary (HOU)', 'Ezekiel Elliot (NE)', 'Antonio Gibson (WAS)', 'Ty Chandler (MIN)', 'Zamir White (LV)', 'Trey Sermon (IND)'],
    'RB Week 16 PPR Points': ['25.1', '16.4', '8.5', '12', '24', '6.1', '19.7', '19.4', '9.0', '5.0', '10.6', '11.6', '21.4', '5.3', '6.6', '43.1', '19.2', '15.2', '22.2', '9.3', '14.0', '10.4', '14.5', '10.9', '12.1', '0.0', '9.3', '21.0', '10.2', '7.7', '14.5', '0.3' ],
    'Opposing Team': ['BAL', 'NO', 'LAR', 'DAL', 'MIN', 'TB', 'JAC', 'PHI', 'PIT', 'LAC', 'LV', 'BUF', 'SEA', 'MIA', 'TEN', 'WAS', 'IND', 'NYG', 'CHI', 'HOU', 'SF', 'CIN', 'CAR', 'NE', 'GB', 'ARI', 'CLE', 'DEN', 'NYJ', 'DET', 'KC', 'ATL'],
    'RB Points per Reception PPG': ['25.2', '20.9', '19.8', '18.3', '17', '16.9', '16.2', '15.6', '15.3', '15.3', '14.5', '14.4', '14.3', '13.9', '13.9', '13.6', '13.5', '12.6', '12.3', '12.2', '11.4', '11.3', '10.9', '10.7', '10.6', '10.1', '9.5', '9.2', '8.1', '5.6', '2.8', '1.0'],
    'Opponent RB PPG Ranking': ['8', '11', '1', '18', '9', '3', '15', '6', '21', '23', '24', '14', '31', '13', '7', '30', '28', '26', '19', '16', '5', '20', '27', '17', '22', '32', '12', '29', '25', '2', '10', '4']
}

week16_table = pd.DataFrame(final_stats) #creating table so that the user can use the drop down select

chosen_player = st.selectbox("Choose a player", week16_table['Week 16 Starting RB (Team)']) #allows user to choose a player, and see how they performed in week 16 and compare to the original data

if chosen_player:
    st.subheader(f"Week 16 Stats of {chosen_player}")
    fantasy_points = week16_table[week16_table['Week 16 Starting RB (Team)'] == chosen_player]
    st.write(fantasy_points)
