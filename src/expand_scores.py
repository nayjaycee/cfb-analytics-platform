import pandas as pd
import ast

def expand_score_list_column(df, col_name, prefix=None, include_total=True):
    """
    Expands a column containing list-like score data (e.g., [7, 3, 14, 10, 6])
    into separate columns for each quarter and overtime period.
    Handles variable-length lists (OT games) safely.

    Parameters:
    ----------
    df : pd.DataFrame
        The dataframe containing the column.
    col_name : str
        The name of the column with list-like score data.
    prefix : str, optional
        Prefix to add to new columns (e.g., 'home' or 'away').
    include_total : bool, optional
        Whether to create a total points column (default=True).

    Returns:
    -------
    pd.DataFrame
        A new dataframe with the expanded columns added.
    """

    def safe_parse(x):
        """Safely parse list-like strings or lists into Python lists."""
        try:
            if isinstance(x, str):
                val = ast.literal_eval(x)
                if isinstance(val, list):
                    return val
            elif isinstance(x, list):
                return x
            return []
        except Exception:
            return []

    # Parse safely into lists
    df[col_name] = df[col_name].apply(safe_parse)

    # Find maximum list length (handles any # of OTs)
    max_len = df[col_name].apply(len).max()

    # Create dynamic labels for quarters and OTs
    labels = [f"Q{i + 1}" if i < 4 else f"OT{i - 3}" for i in range(max_len)]
    if prefix:
        labels = [f"{prefix}_{label}" for label in labels]

    # Expand into new columns, padding with 0s for missing entries
    expanded = pd.DataFrame(
        df[col_name].apply(lambda x: x + [0] * (max_len - len(x))).tolist(),
        index=df.index,
        columns=labels
    )

    # Merge expanded columns into main dataframe
    df = pd.concat([df.drop(columns=[col_name]), expanded], axis=1)

    # Optional: add total points column
    if include_total and prefix:
        total_col = f"{prefix}_points_total"
        df[total_col] = df[[c for c in df.columns if c.startswith(f"{prefix}_points_")]].sum(axis=1)

    return df
