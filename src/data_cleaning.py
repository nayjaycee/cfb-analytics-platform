import pandas as pd
import ast

def flatten_nested_column(df, col_name, prefix=None):
    """Recursively flatten a column containing nested dict-like data."""
    def safe_parse(x):
        try:
            return ast.literal_eval(x) if isinstance(x, str) and x.startswith("{") else {}
        except Exception:
            return {}

    df[col_name] = df[col_name].apply(safe_parse)

    def flatten_dict(d, parent_key="", sep="_"):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    expanded = df[col_name].apply(flatten_dict).apply(pd.Series)
    if prefix:
        expanded = expanded.add_prefix(f"{prefix}_")
    return pd.concat([df.drop(columns=[col_name]), expanded], axis=1)