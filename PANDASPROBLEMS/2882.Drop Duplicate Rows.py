import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
 return customers.drop_duplicates(["email"])
  #we use the .drop_duplicates() to drop duplicate rows
  #adding ["email"]specifies duplicates in the email column
  #we can also use
  import pandas as pd

def removeDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset="email", keep="first")
