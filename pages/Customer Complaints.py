import datetime
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from methods.styles import back_btn, header, selected_date, vertical_line, horizontal_line
import plotly.express as px

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

header("Customer Complaints")
col1, col2 = st.columns((5, 2))
with col1:
    back_btn()
with col2:
    date = selected_date()

year = date.year
month = date.month
if month < 10:
    current_month = f"0{month}"
else:
    current_month = f"{month}"

# Getting Excel File
xls_customer_complaints = pd.ExcelFile("Excel/Quality/Customer Complaints.xlsx")

# Getting Daily customer complain data
df_customer_complaints_daily = pd.read_excel(xls_customer_complaints, "Daily Data").fillna("NA")

# Getting Weekly Data
df_customer_complaints_weekly = pd.read_excel(xls_customer_complaints, "Weekly Data").fillna("NA")
df_customer_complaints_filtered_weekly = df_customer_complaints_weekly[
    df_customer_complaints_weekly["Month"] == f"{year}-{current_month}"]

# Getting Monthly Data
df_customer_complaints_monthly = pd.read_excel(xls_customer_complaints, "Monthly Data").fillna("NA")

# Getting Customer Complaint Details
df_customer_complaints = pd.read_excel(xls_customer_complaints, "Complaint Details").fillna("NA")

horizontal_line()

st.markdown(
    "\n"
    "            <style>\n"
    "            .heading{"
    "                  padding: 1rem;"
    "                   font-weight: bolder; "
    "              }"
    "            \n", unsafe_allow_html=True
)

body_main_col1, body_main_col2 = st.columns((1, 1))
with body_main_col1:
    st.write("""
           <div class = "heading">
               Daily Trends
           </div>
       """, unsafe_allow_html=True)
    data = {}
    lst_x_daily = []
    lst_y_daily = []
    for i in range(7, 0, -1):
        today = date - datetime.timedelta(days=i)
        today_pd = pd.to_datetime(today)
        df = df_customer_complaints_daily[df_customer_complaints_daily["Date"] == today_pd]
        lst_x_daily.append(f"{today.__str__()}")
        try:
            lst_y_daily.append(df["Reported Complaint"].tolist()[0])
        except:
            lst_y_daily.append(0)

    data["Days"] = lst_x_daily
    data["Number Of Complaints"] = lst_y_daily

    fig = px.bar(
        data,
        x="Days",
        y="Number Of Complaints",
        text_auto=True,
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
    )
with body_main_col2:
    lst_x = list()
    lst_y = list()
    st.write("""
               <div class = "heading">
                   Weekly Trends
               </div>
           """, unsafe_allow_html=True)
    data = {}
    df = df_customer_complaints_filtered_weekly[["Total"]]
    for i, item in enumerate(df["Total"]):
        if i == 0:
            lst_x.append(f"W{i + 1}(01-07)")
            lst_y.append(item)
        if i == 1:
            lst_x.append(f"W{i + 1}(08-15)")
            lst_y.append(item)
        if i == 2:
            lst_x.append(f"W{i + 1}(16-23)")
            lst_y.append(item)
        if i == 3:
            lst_x.append(f"W{i + 1}(24-31)")
            lst_y.append(item)

    # print(lst_x.__len__())
    data["Weeks"] = lst_x
    data["No. Of Complaints"] = lst_y
    fig = px.bar(
        data,
        x="Weeks",
        y="No. Of Complaints",
        text_auto=True,
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )

horizontal_line()

st.write("""
       <div class = "heading">
           Monthly Trends
       </div>
   """, unsafe_allow_html=True)
# print(df_safety_filtered_monthly)
data_monthly = {}
lst_x = []
lst_y = []
for i in range(1, 13):
    if i < 10:
        df = df_customer_complaints_monthly[df_customer_complaints_monthly["Month"] == f"{year}-0{i}"][["Total"]]
    else:
        df = df_customer_complaints_monthly[df_customer_complaints_monthly["Month"] == f"{year}-{i}"][["Total"]]

    for j, item in enumerate(df["Total"]):
        lst_x.append(f"{months[i - 1]}'{str(year)[2:]}")
        lst_y.append(item)

    data_monthly["Months"] = lst_x
    data_monthly["No. Of Complaints"] = lst_y

fig = px.bar(pd.DataFrame(data_monthly), x="Months", y="No. Of Complaints", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

horizontal_line()
tab1, tab2 = st.tabs(["Open", "Closed"])
with tab1:
    st.write("Open Complaints")
    st.dataframe(df_customer_complaints[df_customer_complaints["Status"] == "Open"],
                 use_container_width=True,
                 hide_index=True)
with tab2:
    st.write("Closed Complaints")
    st.dataframe(df_customer_complaints[df_customer_complaints["Status"] == "Closed"],
                 use_container_width=True,
                 hide_index=True)
