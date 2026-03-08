# analytics.py
import pandas as pd

# --- 1. Sales and profit by market and region ---
def sales_profit_by_region(df):
    result = df.groupby(['market', 'region'])[['sales', 'profit']].sum().sort_values('sales', ascending=False)
    return result

# --- 2. Top product categories/sub-categories ---
def top_categories(df, n=10):
    result = df.groupby(['category', 'sub_category'])[['sales', 'profit']].sum().sort_values('sales', ascending=False).head(n)
    return result

# --- 3. Impact of discount on profit ---
def discount_vs_profit(df):
    grouped = df.groupby('discount')[['profit', 'sales']].mean().reset_index()
    return grouped

# --- 4. Shipping modes and priorities ---
def shipping_analysis(df):
    mode_counts = df['ship_mode'].value_counts()
    priority_counts = df['order_priority'].value_counts()
    return mode_counts, priority_counts

# --- 5. Customer segment revenue ---
def customer_segment_analysis(df):
    segment_sales = df.groupby('segment')[['sales', 'profit']].sum().sort_values('sales', ascending=False)
    return segment_sales