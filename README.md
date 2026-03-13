# :football: NFL Predictor

(Live at https://nflmatchuppredictor.streamlit.app)
A data-driven, effective-yet-simple NFL matchup predictor built with Python and Polars. This project leverages
10 seasons of historical NFL data (2015–2024) to calculate performance-based spreads and predict game outcomes

# :rocket: Tech Stack

- Python 3.13
- Polars
- UV
- nflreadpy (Data source)

# :hammer_and_wrench: Setup

Clone repo:

`git clone https://github.com/noah-roland/Nfl_Matchup_Predictor.git`

Install dependencies and sync the environment:

`uv sync`

Run the predictor:

`uv run nfl_test.py`

# 📊 Current Logic

- The engine currently utilizes a Baseline Mean Comparison model:
- Fetches historical schedules and scores from the last 10 seasons.
- Isolates team performance based on Home vs. Away splits.
- Calculates a predicted point spread based on historical scoring averages.

# :calendar: Project Roadmap

- [x] Phase 1: Core Data Integration (nflreadpy + Polars).
- [x] Phase 2: Basic Aggregation Logic (Home/Away Mean scores).
- [ ] Phase 3: Environmental Variables (Integrating weather, wind, and surface data).
- [ ] Phase 4: Advanced Weighting (Rolling means and strength of schedule).
- [ ] Phase 5: Interactive UI (Streamlit web dashboard).
