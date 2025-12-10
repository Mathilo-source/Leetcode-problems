import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
     self_views = views[views["author_id"] == views["viewer_id"]]

    # get unique ids and sort
     result = (
        self_views[["author_id"]]
        .drop_duplicates()
        .rename(columns={"author_id": "id"})
        .sort_values("id")
        .reset_index(drop=True)
    )

     return result
  Filters rows where author_id == viewer_id

#Drops duplicates
#Renames column to id
#Sorts ascending
#Resets index as expected
