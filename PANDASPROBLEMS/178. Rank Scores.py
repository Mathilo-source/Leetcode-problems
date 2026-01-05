import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Create a rank column using dense ranking
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    
    # Sort by score descending
    scores = scores.sort_values(by='score', ascending=False)
    
    # Return only required columns
    return scores[['score', 'rank']]
