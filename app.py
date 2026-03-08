# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from src.preprocess import load_and_preprocess
from src.analytics import sales_profit_by_region, top_categories, discount_vs_profit, shipping_analysis, customer_segment_analysis

# Load data
df = load_and_preprocess('data/superstore_sales.csv')

st.title("📊 Superstore Sales Analytics Dashboard")
st.markdown("Explore sales, profit, discounts, shipping, and customer segments.")

# --- Filters ---
years = st.multiselect("Select Year(s)", options=df['year'].unique(), default=df['year'].unique())
categories = st.multiselect("Select Categories", options=df['category'].unique(), default=df['category'].unique())
regions = st.multiselect("Select Regions", options=df['region'].unique(), default=df['region'].unique())
segments = st.multiselect("Select Customer Segments", options=df['segment'].unique(), default=df['segment'].unique())

# Apply filters
filtered_df = df[(df['year'].isin(years)) & 
                 (df['category'].isin(categories)) & 
                 (df['region'].isin(regions)) & 
                 (df['segment'].isin(segments))]

# --- KPI Metrics ---
total_sales = filtered_df['sales'].sum()
total_profit = filtered_df['profit'].sum()
avg_discount = filtered_df['discount'].mean()
avg_shipping_time = filtered_df['shipping_time'].mean()

st.subheader("Key Metrics")
st.write(f"**Total Sales:** ${total_sales:,.2f}")
st.write(f"**Total Profit:** ${total_profit:,.2f}")
st.write(f"**Average Discount:** {avg_discount:.2f}")
st.write(f"**Average Shipping Time (days):** {avg_shipping_time:.1f}")

# --- Visualizations ---
st.subheader("1️⃣ Sales & Profit by Market and Region")
region_sales = sales_profit_by_region(filtered_df).reset_index()
fig1 = px.bar(region_sales, x='region', y='sales', color='profit', barmode='group', title="Sales and Profit by Region")
st.plotly_chart(fig1)

st.subheader("2️⃣ Top Categories & Sub-Categories")
top_cat = top_categories(filtered_df)
fig2 = px.bar(top_cat.reset_index(), x='sub_category', y='sales', color='profit', title="Top Sub-Categories by Sales & Profit")
st.plotly_chart(fig2)

st.subheader("3️⃣ Discount vs Profit")
discount_profit = discount_vs_profit(filtered_df)
fig3 = px.scatter(discount_profit, x='discount', y='profit', size='sales', color='profit', title="Discount vs Average Profit")
st.plotly_chart(fig3)

st.subheader("4️⃣ Shipping Modes and Priorities")
mode_counts, priority_counts = shipping_analysis(filtered_df)
fig4 = px.pie(names=mode_counts.index, values=mode_counts.values, title="Shipping Mode Distribution")
fig5 = px.pie(names=priority_counts.index, values=priority_counts.values, title="Order Priority Distribution")
st.plotly_chart(fig4)
st.plotly_chart(fig5)

st.subheader("5️⃣ Customer Segment Revenue")
segment_sales = customer_segment_analysis(filtered_df).reset_index()
fig6 = px.bar(segment_sales, x='segment', y='sales', color='profit', title="Customer Segment Sales & Profit")
st.plotly_chart(fig6)