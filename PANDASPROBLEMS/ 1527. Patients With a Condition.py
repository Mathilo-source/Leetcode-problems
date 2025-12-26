import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
     mask = (
        patients['conditions'].str.startswith('DIAB1', na=False) |
        patients['conditions'].str.contains(' DIAB1', na=False)
    )
    
     return patients[mask]
