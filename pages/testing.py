import streamlit as st
import pandas as pd
import plotly.express as px

# Load your Excel data into a DataFrame
# Assuming your Excel file is named 'data.xlsx' and the data is in a sheet named 'Sheet1'
data = pd.read_excel("Excel/Safety/Safety.xlsx", sheet_name="Safety Incidences").fillna(0)

# Convert date columns to datetime if they are not already
data['Date'] = pd.to_datetime(data['Date'])

# Streamlit app
st.title('Data Visualization with Streamlit and Plotly')

# Date range selection
start_date = st.date_input("Start date", data['Date'].min())
end_date = st.date_input("End date", data['Date'].max())

# Convert date inputs to Pandas Timestamp objects
start_date = pd.Timestamp(start_date)
end_date = pd.Timestamp(end_date)

# Filter data based on selected date range
filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Display filtered data
st.write('Filtered Data:')
st.write(filtered_data)

# Create bar graph using Plotly
fig = px.bar(filtered_data, x='Date', y='Category', title='Data between selected dates')

# Plot the figure
st.plotly_chart(fig)

# Option to download the graph as an image or HTML file
download_format = st.selectbox("Download format:", ["PNG", "JPEG", "WebP", "SVG", "PDF", "HTML"])
if st.button("Download Graph"):
    if download_format == "HTML":
        fig.write_html("graph.html")
    else:
        fig.write_image(f"graph.{download_format.lower()}")