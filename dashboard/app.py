# SETUP
import streamlit as st

import pandas as pd
import altair as alt


#-------------------#
# IMPORT LOCAL DATA

# Data import (you may need to change the path)
df = pd.read_csv("../data/external/data.csv")


#-------------------#
# CREATE CHARTS

### Home Team Rating-to-Win Probability
c1 = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X('home_team_pregame_rating',
            axis=alt.Axis(title="Pregame Rating",
                          labelAngle=0,
                          titleAnchor="start"),
            scale=alt.Scale(zero=False)),
    y=alt.Y('home_team_winprob',
                    axis=alt.Axis(title = "Win Probability",
                                titleAnchor="end",
                                format='%')),
    tooltip=['home_team_pregame_rating','home_team_winprob','home_team'],
    ).properties(
        title='Home Team Rating-to-Win Probability'
        
    ).interactive()

### Away Team Rating-to-Win Probability
c2 = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X('away_team_pregame_rating',
            axis=alt.Axis(title="Pregame Rating",
                          labelAngle=0,
                          titleAnchor="start"),
            scale=alt.Scale(zero=False)),
    y=alt.Y('away_team_winprob',
                    axis=alt.Axis(title = "Win Probability",
                                titleAnchor="end",
                                format='%')),
    tooltip=['away_team_pregame_rating','away_team_winprob','away_team'],
    color=alt.value('green')
    ).properties(
        title='Away Team Rating-to-Win Probability'
        
    ).interactive()

### Away & Home Team Rating-to-Win Probability
c1_2 = (c1 + c2).properties(title="Comparison Win Probability Home Team & Away Team")

### Game Evaluation
source = pd.DataFrame({'Quality': df.game_quality_rating,
                     'Importance': df.game_importance_rating,
                     'Overall': df.game_overall_rating})

c3 = alt.Chart(source).mark_rect().encode(
            x=alt.X('Quality:O',
                        axis=alt.Axis(
                            title="Game Quality",
                            titleAnchor='start'
                        ),
                        scale=alt.Scale(
                            domain=(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100)
                        )),
            y=alt.Y('Importance:O',
                        axis=alt.Axis(
                            title="Game Importance"
                        ),
                        scale=alt.Scale(
                            domain=(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100)
                        )),
            color=alt.Color('Overall:Q'),
            tooltip=['Quality','Importance','Overall']
).properties(
    title="Game Evaluation",
    width = 600,
    height = 550
)

### Home Team to Game Rating
c4 = alt.Chart(df).mark_boxplot(extent='min-max').encode(
    x=alt.X('home_team:O',
            axis = alt.Axis(title="Home Team",
                            titleAnchor="start")),
    y=alt.Y('home_team_postgame_rating:Q',
            scale=alt.Scale(zero=False),
            axis = alt.Axis(title="Home Team Postgame Rating", titleAnchor="end")),
).properties(
        title='Estimation of postgame ratings on Home Team side',
        height = 600
    )

c5 = alt.Chart(df).mark_boxplot(extent='min-max').encode(
    x=alt.X('home_team:O',
            axis = alt.Axis(title="Home Team",
                            titleAnchor="start")),
    y=alt.Y('away_team_pregame_rating:Q',
            scale=alt.Scale(zero=False),
            axis = alt.Axis(title="Away Team Pregame Rating", titleAnchor="end")),
).properties(
        title='Pregame ratings of Away Teams when playing against Home Teams',
        height=700        
    )

###-------------------###
# START OF OUR APP

#-------------------#
# HEADER

# Title of our app
st.title("2022-23 NHL Predictions")

# Add image


# Add header
st.header("Exploring Data - NHL Predicitons 2023")



#-------------------#
# BODY




st.write("The data was sourced from fivethrityeight.com on Nov. 30 2022.")
# Show static DataFrame
st.dataframe(df)

st.subheader("Comparison of Win Probabilities of the teams")


tab1, tab2 = st.tabs(["Individual Charts", "Joint Data"])
# Show plot
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.altair_chart(c1, use_container_width=True)

    with col2:
        st.altair_chart(c2, use_container_width=True)
    
    st.write("Here could be the explanantion and analysis of the data visualized in the charts above. However there ist not. This is just a spaceholder text snippet that is supposed to illustrate said paragraph - because the analysis is not part of the given task.")

with tab2:
    st.altair_chart(c1_2, use_container_width=True)


st.subheader("Game Evaluation - Pregame")
st.altair_chart(c3)




st.subheader("Pregame Rating of the Home Teams")
st.write("In the following chart we can see the Pregame Points of the Home Teams. The red line indicates the mean of the Home Team Ratings, thus showing which teams are rated above or below average.")
with st.echo():
        bar = alt.Chart(df).mark_bar().encode(
        x=alt.X('home_team:O', sort='-y',
                axis=alt.Axis(title="Home Team", titleAnchor="start")),
        y=alt.Y('home_team_pregame_rating:Q', 
                scale=alt.Scale(zero=False), 
                axis=alt.Axis(title = "Home Team Pregame Rating", titleAnchor="end"))
        )

        rule = alt.Chart(df).mark_rule(color='red').encode(
            y=alt.Y('mean(home_team_pregame_rating):Q')

        )

        (bar + rule).properties(width=600,title='Home Teams Pregame Rating')

st.write("The chart sadly will not load correctly...")

st.subheader("Game Ratings - Home Team Postgame Estimation")
st.altair_chart(c4)

st.subheader("Game Rating - Away Team Pregame per Home Team oponent")
st.altair_chart(c5)

###-------------------###
# END OF APP