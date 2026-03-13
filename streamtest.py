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

# Get sorted list of abbreviations for the dropdowns!
team_list = sorted(teams['team_abbr'].to_list())

with col1:
    home_team = st.selectbox("Home Team", team_list, index=team_list.index(
        'MIA') if 'MIA' in team_list else 0)

with col2:
    away_team = st.selectbox("Away Team", team_list, index=team_list.index(
        'NE') if 'NE' in team_list else 1)

st.divider()

# Calculates the mean score for a given team when the specified score column is not null


def calc_home_mean(team: str, score_col: str) -> float:
    mean_score = schedules.filter(pl.col(score_col).is_not_null() & (
        pl.col("home_team") == team)).select(pl.col(score_col).mean().round(1))
    return mean_score.item()


def calc_away_mean(team: str, score_col: str) -> float:
    mean_score = schedules.filter(pl.col(score_col).is_not_null() & (
        pl.col("away_team") == team)).select(pl.col(score_col).mean().round(1))
    return mean_score.item()


if st.button("Calculate Winner", width="stretch"):
    st.divider()

    # Perform the calculations
    home_val = calc_home_mean(home_team, "home_score")
    away_val = calc_away_mean(away_team, "away_score")

    # Display the scores
    col_a, col_b = st.columns(2)
    col_a.metric(f"{home_team} Avg", home_val)
    col_b.metric(f"{away_team} Avg", away_val)

    # The Result
    if home_val > away_val:
        st.success(
            f"**{home_team}** is projected to win by {round(home_val - away_val, 1)} points!")
    elif away_val > home_val:
        st.success(
            f"**{away_team}** is projected to win by {round(away_val - home_val, 1)} points!")
    else:
        st.info("It's a projected toss-up!")

    st.divider()

# Show raw data for the selected home team as requested
st.subheader(f"{home_team} Reference Data")
st.write(teams.filter(pl.col('team_abbr') == home_team))
