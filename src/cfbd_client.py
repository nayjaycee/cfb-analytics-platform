"""
CFBD Client Module
Handles authentication and requests to the CollegeFootballData API.
"""

import cfbd
import pandas as pd


# --------------------------------------------------
# Configuration
# --------------------------------------------------

API_KEY = "tGeN4t2UF9PRuUuJUnsIu/fCf09ZDbVKv7Zh2z22Q5Rg407tcpcOKHax/xkfcbkK"

configuration = cfbd.Configuration()
configuration.access_token = API_KEY


# --------------------------------------------------
# Core Functions
# --------------------------------------------------

def get_games_by_year(year: int) -> pd.DataFrame:
    """Fetch game-level data for a given season."""
    with cfbd.ApiClient(configuration) as api_client:
        api_instance = cfbd.GamesApi(api_client)
        games = api_instance.get_games(year=year)
        return pd.DataFrame([g.to_dict() for g in games])

