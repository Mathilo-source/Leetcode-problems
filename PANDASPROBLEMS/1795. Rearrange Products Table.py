import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
     # Unpivot the store columns into rows
    result = products.melt(
        id_vars=['product_id'],           # Keep product_id fixed
        value_vars=['store1', 'store2', 'store3'],  # Columns to unpivot
        var_name='store',                 # Name for the new column with store names
        value_name='price'                # Name for the new column with prices
    )
    # Drop rows where price is NaN (product not available in that store)
    result = result.dropna(subset=['price']).reset_index(drop=True)
    return result
