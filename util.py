#READ THE CSV FILE
#clean and convert values
import pandas as pd 


def get_data(PATH):
    df = pd.read_csv(PATH)
    df.rename(columns = {"item_price":"order_price"}, inplace=True)
    df['order_price'] = df['order_price'].str.replace('$', '').astype(float)
    revenue = df.groupby('item_name')['order_price'].sum()
    top10 = revenue.sort_values(ascending = False).head(10).to_frame()
    top10.reset_index(inplace = True)
    return top10
