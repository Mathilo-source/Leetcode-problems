import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'
    return users[users['mail'].str.match(valid_pattern)]
