import streamlit as st
import nflreadpy as nfl
import polars as pl

st.set_page_config(page_title="NFL Matchup Precictor",)


@st.cache_data
def get_nfl_data():
    teams_df = nfl.load_teams()
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    schedules_df = nfl.load_schedules(years)
    return teams_df, schedules_df


# Create a text element and let the reader know the NFL data is loading.
data_load_state = st.text('Fetching NFL data...')
# Load the dataframe.
teams, schedules = get_nfl_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Loaded NFL Data! (using st.cache_data)")
st.title("🏈 NFL Matchup Predictor")

# 3. Team Selection UI
st.subheader("Select Teams")
col1, col2 = st.columns(2)

# Get sorted list of abbreviations for the dropdowns
team_list = sorted(teams['team_abbr'].to_list())

with col1:
    home_team = st.selectbox("Home Team", team_list, index=team_list.index(
        'DAL') if 'DAL' in team_list else 0)

with col2:
    away_team = st.selectbox("Away Team", team_list, index=team_list.index(
        'PHI') if 'PHI' in team_list else 1)

# 4. Display Selected Data (Proof of Concept)
st.divider()
st.write(f"Predicting matchup: **{away_team}** @ **{home_team}**")

# Show raw data for the selected home team as requested
st.subheader(f"{home_team} Reference Data")
st.write(teams.filter(pl.col('team_abbr') == home_team))
