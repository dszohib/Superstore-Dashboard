import pandas as pd

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)

    # Convert dates
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)
    df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True)

    # Convert numeric columns
    numeric_cols = ['sales', 'profit', 'discount', 'shipping_cost', 'quantity']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Create features
    df['shipping_time'] = (df['ship_date'] - df['order_date']).dt.days
    df['profit_margin'] = df['profit'] / df['sales']

    # Handle missing values
    df.fillna({
        'shipping_time': df['shipping_time'].median(),
        'profit_margin': df['profit_margin'].median()
    }, inplace=True)

    return df