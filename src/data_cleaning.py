import pandas as pd

def clean_games(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleanup for CFBD game data."""
    df = df.copy()
    df["startDate"] = pd.to_datetime(df["startDate"])
    df = df[df["completed"] == True]  # keep only finished games
    df = df.drop_duplicates(subset=["id"])
    return df
#%%
