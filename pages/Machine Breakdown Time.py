import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.switch_page_button import switch_page
from methods.colours import color
from methods.styles import back_btn, header, horizontal_line, selected_date

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

header("Machine Breakdown Time")
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

# Getting Data fo Breakdown
xls_breakdown = pd.ExcelFile("Excel/Cost/Breakdown Time.xlsx")
df_breakdown_daily = pd.read_excel(xls_breakdown, "Daily Data")
df_breakdown_weekly = pd.read_excel(xls_breakdown, "Weekly Data")
df_breakdown_ytd = pd.read_excel(xls_breakdown, "Monthly Data")
df_breakdown_issues = pd.read_excel(xls_breakdown, "Breakdown Details")

# print(df_breakdown_weekly)

# Getting Filtered Data
df_breakdown_weekly_filtered = df_breakdown_weekly[df_breakdown_weekly["Month"] == f"{year}-{current_month}"]

colA, colB = st.columns((1, 1))
with colA:
    st.write("\n"
             "<div class = \"heading\">\n"
             "   Daily Trends\n"
             "</div>\n", unsafe_allow_html=True)
    data = {}
    lst_x = []
    lst_y_opened = []
    lst_y_closed = []

    for i in range(6, -1, -1):
        today = date - datetime.timedelta(days=i)
        today_pd = pd.to_datetime(today)
        df = df_breakdown_daily[df_breakdown_daily["Date"] == today_pd]
        count = 0
        # print(df)
        try:
            lst_y_opened.append(df["Limit"].tolist()[0])
            lst_y_closed.append(df["Breakdown Time"].tolist()[0])
        except Exception as e:
            print(e)
            lst_y_opened.append(0)
            lst_y_closed.append(0)
        lst_x.append(today.__str__())

    data["Limit"] = lst_y_opened
    data["Breakdown Time"] = lst_y_closed
    data["Date"] = lst_x

    # print(data["Limit"].__len__())

    fig = px.bar(
        data,
        x="Date",
        y=["Limit", "Breakdown Time"],
        color_discrete_map={"Limit": color.blue, "Breakdown Time": color.skyblue},
        barmode="group",
        text_auto=True,
    )
    st.plotly_chart(fig, use_container_width=True)
with colB:
    lst_x = list()
    lst_y_opened = list()
    lst_y_closed = list()

    st.write("\n"
             "<div class = \"heading\">\n"
             "   Weekly Trends\n"
             "</div>\n", unsafe_allow_html=True)

    data = {}
    for i, opened in enumerate(df_breakdown_weekly_filtered["Limit"]):
        if i == 0:
            lst_x.append(f"W{i + 1}(01-07)")
            lst_y_opened.append(opened)
        if i == 1:
            lst_x.append(f"W{i + 1}(08-15)")
            lst_y_opened.append(opened)
        if i == 2:
            lst_x.append(f"W{i + 1}(16-23)")
            lst_y_opened.append(opened)
        if i == 3:
            lst_x.append(f"W{i + 1}(24-31)")
            lst_y_opened.append(opened)

    for i, closed in enumerate(df_breakdown_weekly_filtered["Breakdown Time"]):
        if i == 0:
            lst_y_closed.append(closed)
        if i == 1:
            lst_y_closed.append(closed)
        if i == 2:
            lst_y_closed.append(closed)
        if i == 3:
            lst_y_closed.append(closed)

    data["Weeks"] = lst_x
    data["Limit"] = lst_y_opened
    data["Breakdown Time"] = lst_y_closed

    fig = px.bar(
        data,
        x="Weeks",
        y=["Limit", "Breakdown Time"],
        barmode="group",
        text_auto=True,
        color_discrete_map={"Limit": color.blue, "Breakdown Time": color.skyblue},
    )
    st.plotly_chart(fig, use_container_width=True)

horizontal_line()
data = {}
lst_x = list()
lst_y_Opened = list()
lst_y_Closed = list()

st.write("""
             <div class = "heading">
                 Monthly Trends
             </div>
         """, unsafe_allow_html=True)


for i in range(1, 13):
    if i < 10:
        df = df_breakdown_ytd[df_breakdown_ytd["Month"] == f"{year}-0{i}"][["Limit"]].fillna(0)
        df_actual = df_breakdown_ytd[df_breakdown_ytd["Month"] == f"{year}-0{i}"][["Breakdown Time"]].fillna(0)
    else:
        df = df_breakdown_ytd[df_breakdown_ytd["Month"] == f"{year}-{i}"][["Limit"]].fillna(0)
        df_actual = df_breakdown_ytd[df_breakdown_ytd["Month"] == f"{year}-{i}"][["Breakdown Time"]].fillna(0)

    for j, item in enumerate(df["Limit"]):
        lst_x.append(f"{months[i - 1]}'{str(year)[2:]}")
        lst_y_Opened.append(item)

    for j, item in enumerate(df_actual["Breakdown Time"]):
        lst_y_Closed.append(item)

    data["Months"] = lst_x
    data["Limit"] = lst_y_Opened
    data["Breakdown Time"] = lst_y_Closed

fig = px.bar(
    data,
    x="Months",
    y=["Limit", "Breakdown Time"],
    color_discrete_map={"Limit": color.blue, "Breakdown Time": color.skyblue},
    barmode="group",
    text_auto=True,
)
st.plotly_chart(fig, use_container_width=True)

tab_open, tab_closed = st.tabs(["Open", "Closed"])
with tab_open:
    st.dataframe(df_breakdown_issues[df_breakdown_issues["Status"] == "Open"], hide_index=True, use_container_width=True)
with tab_closed:
    st.dataframe(df_breakdown_issues[df_breakdown_issues["Status"] == "Closed"], hide_index=True, use_container_width=True)