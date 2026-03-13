import nflreadpy as nfl
import polars as pl


print("Fetching NFL team data...")
teams = nfl.load_teams()
schedules = nfl.load_schedules(
    [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])

# Calculates the mean score for a given team when they are the home team and the specified score column is not null


def calc_home_mean(team: str, score_col: str) -> float:
    mean_score = schedules.filter(pl.col(score_col).is_not_null() & (
        pl.col("home_team") == team)).select(pl.col(score_col).mean().round(1))
    return mean_score.item()

# Calculates the mean score for a given team when they are the away team and the specified score column is not null


def calc_away_mean(team: str, score_col: str) -> float:
    mean_score = schedules.filter(pl.col(score_col).is_not_null() & (
        pl.col("away_team") == team)).select(pl.col(score_col).mean().round(1))
    return mean_score.item()


# Gets user input for home and away team abbreviations, calculates mean scores
home_team_input = input(
    "Enter a team abbreviation for home score mean calculation: ")
away_team_input = input(
    "Enter a team abbreviation for away score mean calculation: ")
home_team_mean = calc_home_mean(home_team_input, "home_score")
away_team_mean = calc_away_mean(away_team_input, "away_score")

print(f"Home mean score: {home_team_mean}")
print(f"Away mean score: {away_team_mean}")

# Compares the teams to determine a favorite
if home_team_mean > away_team_mean:
    print(f"{home_team_input} is the favorite by {home_team_mean - away_team_mean} points.")
elif away_team_mean > home_team_mean:
    print(f"{away_team_input} is the favorite by {away_team_mean - home_team_mean} points.")
else:
    print("The teams are evenly matched.")
