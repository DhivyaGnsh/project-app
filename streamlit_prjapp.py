import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data(file_path=None):
    if file_path:
        return pd.read_csv(https://github.com/DhivyaGnsh/project-app/blob/main/retail_orders.csv)
    else:
        st.error("No file provided. Please upload a CSV file or check the default path.")
        return pd.DataFrame()  

data = load_data()
data['revenue'] = data['sale_price'] * data['quantity']
data['order_year'] = pd.to_datetime(data['order_date']).dt.year

# Sidebar for query selection
st.sidebar.title("Guvi Queries")
query_options = [
    "Top 10 Highest Revenue-Generating Products",
    "Top 5 Cities with the Highest Profit Margins",
    "Total Discount Given per Category",
    "Average Sale Price per Product Category",
    "Region with the Highest Average Sale Price",
    "Total Profit per Category",
    "Top 3 Segments with the Highest Quantity of Orders",
    "Average Discount Percentage Given per Region",
    "Product Category with the Highest Total Profit",
    "Total Revenue Generated per Year"
]
selected_query = st.sidebar.selectbox("Select a Query to Run:", query_options)

# Execute the selected query
st.title("Retail Orders Analysis")

if selected_query == "Top 10 Highest Revenue-Generating Products":
    top_revenue_products = data.groupby('product_id')['revenue'].sum().nlargest(10).reset_index()
    st.write("### Top 10 Highest Revenue-Generating Products")
    st.dataframe(top_revenue_products)

elif selected_query == "Top 5 Cities with the Highest Profit Margins":
    city_profit_margin = data.groupby('city')['profit'].sum().nlargest(5).reset_index()
    st.write("### Top 5 Cities with the Highest Profit Margins")
    st.dataframe(city_profit_margin)

elif selected_query == "Total Discount Given per Category":
    total_discount_per_category = data.groupby('category')['discount'].sum().reset_index()
    st.write("### Total Discount Given per Category")
    st.dataframe(total_discount_per_category)

elif selected_query == "Average Sale Price per Product Category":
    average_sale_price_per_category = data.groupby('category')['sale_price'].mean().reset_index()
    st.write("### Average Sale Price per Product Category")
    st.dataframe(average_sale_price_per_category)

elif selected_query == "Region with the Highest Average Sale Price":
    average_sale_price_per_region = data.groupby('region')['sale_price'].mean().reset_index()
    highest_avg_sale_price_region = average_sale_price_per_region.loc[average_sale_price_per_region['sale_price'].idxmax()]
    st.write("### Region with the Highest Average Sale Price")
    st.write(highest_avg_sale_price_region)

elif selected_query == "Total Profit per Category":
    total_profit_per_category = data.groupby('category')['profit'].sum().reset_index()
    st.write("### Total Profit per Category")
    st.dataframe(total_profit_per_category)

elif selected_query == "Top 3 Segments with the Highest Quantity of Orders":
    top_segments_by_quantity = data.groupby('segment')['quantity'].sum().nlargest(3).reset_index()
    st.write("### Top 3 Segments with the Highest Quantity of Orders")
    st.dataframe(top_segments_by_quantity)

elif selected_query == "Average Discount Percentage Given per Region":
    average_discount_per_region = data.groupby('region')['discount_percent'].mean().reset_index()
    st.write("### Average Discount Percentage Given per Region")
    st.dataframe(average_discount_per_region)

elif selected_query == "Product Category with the Highest Total Profit":
    total_profit_per_category = data.groupby('category')['profit'].sum().reset_index()
    highest_profit_category = total_profit_per_category.loc[total_profit_per_category['profit'].idxmax()]
    st.write("### Product Category with the Highest Total Profit")
    st.write(highest_profit_category)

elif selected_query == "Total Revenue Generated per Year":
    total_revenue_per_year = data.groupby('order_year')['revenue'].sum().reset_index()
    st.write("### Total Revenue Generated per Year")
    st.dataframe(total_revenue_per_year)

st.sidebar.title("My Queries")
query_options = [
    "Total Number of Orders per Region",
    "Top 5 Products with Highest Discount Percentage",
    "Average Discount Percentage per Product Category",
    "Total Revenue Generated per City",
    "Top 3 Most Expensive Products by List Price",
    "Total Profit per Region",
    "Product Category with Highest Average Sale Price",
    "Top 3 Cities with Highest Number of Orders",
    "Average Order Value per Segment",
    "Total Revenue and Number of Orders per Product"
]
selected_query = st.sidebar.selectbox("Select a Query to Run:", query_options)

# Execute the selected query
st.title("Retail Orders Analysis")

if selected_query == "Total Number of Orders per Region":
    orders_per_region = data['region'].value_counts().reset_index()
    orders_per_region.columns = ['Region', 'Total Orders']
    st.write("### Total Number of Orders per Region")
    st.dataframe(orders_per_region)

elif selected_query == "Top 5 Products with Highest Discount Percentage":
    top_discount_products = data[['product_id', 'discount_percent']].nlargest(5, 'discount_percent')
    st.write("### Top 5 Products with Highest Discount Percentage")
    st.dataframe(top_discount_products)

elif selected_query == "Average Discount Percentage per Product Category":
    avg_discount_per_category = data.groupby('category')['discount_percent'].mean().reset_index()
    st.write("### Average Discount Percentage per Product Category")
    st.dataframe(avg_discount_per_category)

elif selected_query == "Total Revenue Generated per City":
    revenue_per_city = data.groupby('city')['revenue'].sum().reset_index()
    st.write("### Total Revenue Generated per City")
    st.dataframe(revenue_per_city)

elif selected_query == "Top 3 Most Expensive Products by List Price":
    top_expensive_products = data[['product_id', 'list_price']].nlargest(3, 'list_price')
    st.write("### Top 3 Most Expensive Products by List Price")
    st.dataframe(top_expensive_products)

elif selected_query == "Total Profit per Region":
    profit_per_region = data.groupby('region')['profit'].sum().reset_index()
    st.write("### Total Profit per Region")
    st.dataframe(profit_per_region)

elif selected_query == "Product Category with Highest Average Sale Price":
    avg_sale_price_per_category = data.groupby('category')['sale_price'].mean().reset_index()
    highest_avg_sale_price_category = avg_sale_price_per_category.loc[avg_sale_price_per_category['sale_price'].idxmax()]
    st.write("### Product Category with Highest Average Sale Price")
    st.write(highest_avg_sale_price_category)

elif selected_query == "Top 3 Cities with Highest Number of Orders":
    top_cities_by_orders = data['city'].value_counts().nlargest(3).reset_index()
    top_cities_by_orders.columns = ['City', 'Total Orders']
    st.write("### Top 3 Cities with Highest Number of Orders")
    st.dataframe(top_cities_by_orders)

elif selected_query == "Average Order Value per Segment":
    avg_order_value_per_segment = data.groupby('segment')['revenue'].mean().reset_index()
    st.write("### Average Order Value per Segment")
    st.dataframe(avg_order_value_per_segment)

elif selected_query == "Total Revenue and Number of Orders per Product":
    revenue_and_orders_per_product = data.groupby('product_id').agg({
        'revenue': 'sum',
        'order_id': 'count'
    }).reset_index()
    revenue_and_orders_per_product.columns = ['Product ID', 'Total Revenue', 'Number of Orders']
    st.write("### Total Revenue and Number of Orders per Product")
    st.dataframe(revenue_and_orders_per_product)
