import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars="product",           # column to keep
    var_name="quarter",          # new column name for quarter
    value_name="sales"           # new column name for sales
)
