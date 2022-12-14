# SETUP
import streamlit as st

import pandas as pd
import altair as alt


#-------------------#
# IMPORT LOCAL DATA

# Data import (you may need to change the path)
df = pd.read_csv("../data/external/data.csv")


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
# SIDEBAR

# Header
st.sidebar.header("This is my sidebar")

# Make a slider
satisfaction = st.sidebar.slider('What is your life satisfaction?', 0, 10, 1)

# Show output of slider selection
st.sidebar.write("My life satisfaction is around ", satisfaction, 'points')

#-------------------#
# BODY

col1, col2 = st.columns(2)


st.write("The data was sourced from fivethrityeight.com on Nov. 30 2022.")
# Show static DataFrame
st.dataframe(df)

st.write("Take a look at my chart")
# Make a chart with altair
c = alt.Chart(df).mark_circle(size=60).encode(
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


# Show plot
with col1:
    st.altair_chart(c, use_container_width=True)

with col2:
    st.altair_chart(c2, use_container_width=True)

###-------------------###
# END OF APP