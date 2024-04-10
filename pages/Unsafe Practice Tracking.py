import datetime
import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from methods.styles import back_btn, header, horizontal_line, selected_date
from methods.colours import color
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

header("Unsafe Practice Tracking")

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

col1, col2 = st.columns((5, 2))
with col1:
    back_btn()
with col2:
    date = selected_date()

year = date.year
month = date.month

unsafe_practices_per_daily: int = 0
unsafe_practices_per_weekly: int = 0
unsafe_practices_per_mtd: int = 0
unsafe_practices_per_ytd: int = 0

# Getting Data

xls = pd.ExcelFile("Excel/Safety/UNSAFE_PRACTICES_TRACKING.xlsx")
df_closure_per = pd.read_excel(xls, "YTD")
df_unsafe_practices_daily = pd.read_excel(xls, "Unsafe Practices Tracking")
df_unsafe_practices_weekly = pd.read_excel(xls, "Weekly Data")
df_unsafe_practices_ytd = pd.read_excel(xls, "Monthly Data")
df_unsafe_practices_daily_data = pd.read_excel(xls, "Daily Data")

# Generating Cards value
today_pd = pd.to_datetime(date - datetime.timedelta(days=1))
# df_filter_closure_per = df_closure_per[df_closure_per["Date"] == today_pd]

df_filter_daily_closure_per = df_unsafe_practices_daily_data[df_unsafe_practices_daily_data["Date"] == today_pd]

if month < 10:
    df_unsafe_practices_filter_weekly = df_unsafe_practices_weekly[
        df_unsafe_practices_weekly["Month"] == f"{year}-0{month}"].reset_index(
        drop=True)
else:
    df_unsafe_practices_filter_weekly = df_unsafe_practices_weekly[df_unsafe_practices_weekly["Month"] == f"{year}-{month}"].reset_index(
        drop=True)

# for i in range(1, 13):
#     if i < 10:
#         df_unsafe_practices_filter_monthly = df_unsafe_practices_ytd[df_unsafe_practices_ytd["Month"] == f"{year}-0{i}"][["Closure %"]].fillna(0)
#         df_actual = df_unsafe_practices_ytd[df_unsafe_practices_ytd["Month"] == f"{year}-0{i}"][["Actual"]].fillna(0)
#     else:
#         df_unsafe_practices_filter_monthly = df_unsafe_practices_ytd[df_unsafe_practices_ytd["Month"] == f"{year}-{i}"][["Closure %"]].fillna(0)
#         df_actual = df_unsafe_practices_ytd[df_unsafe_practices_ytd["Month"] == f"{year}-{i}"][["Actual"]].fillna(0)
# print(round(df_filter_daily_closure_per['Closure %'].iloc[-1]))

try:
    unsafe_practices_per_daily = round(df_filter_daily_closure_per['Closure %'].iloc[-1])
    unsafe_practices_per_weekly = round(df_unsafe_practices_filter_weekly["Closure %"].iloc[-1])
    unsafe_practices_per_mtd = round(df_unsafe_practices_ytd["Closure %"].iloc[-1])
    unsafe_practices_per_ytd = round(df_closure_per["YTD Closure %"].iloc[-1])
except Exception as e:
    print(f"Error Occurred --{e}")
    # noinspection PyTypeChecker
    unsafe_practices_per_daily = 0
    # noinspection PyTypeChecker
    unsafe_practices_per_weekly = 0
    # noinspection PyTypeChecker
    unsafe_practices_per_mtd = 0
    # noinspection PyTypeChecker
    unsafe_practices_per_ytd = 0
print(unsafe_practices_per_daily)
# try:
#     unsafe_practices_per_daily = int(df_filter_closure_per[["Daily Closure %"]]["Daily Closure %"].tolist()[0])
#     unsafe_practices_per_weekly = int(df_filter_closure_per[["Weekly Closure %"]]["Weekly Closure %"].tolist()[0])
#     unsafe_practices_per_mtd = int(df_filter_closure_per[["Monthly Closure %"]]["Monthly Closure %"].tolist()[0])
#     unsafe_practices_per_ytd = int(df_filter_closure_per[["YTD %"]]["YTD %"].tolist()[0])
# except Exception as e:
#     print(f"Error Occurred --{e}")
#     # noinspection PyTypeChecker
#     unsafe_practices_per_daily = "Update"
#     # noinspection PyTypeChecker
#     unsafe_practices_per_weekly = "Update"
#     # noinspection PyTypeChecker
#     unsafe_practices_per_mtd = "Update"
#     # noinspection PyTypeChecker
#     unsafe_practices_per_ytd = "Update"

st.markdown(
    "\n"
    "            <style>\n"
    "            .custom {\n"
    "                margin: 0.2rem;\n"
    "                padding-top: 0.7rem;\n"
    "                border: 1px solid black;\n"
    "                height: 5rem;\n"
    "                border-radius: 0.7rem;\n"
    "                font-weight: bold;\n"
    "                font-size:1rem;\n"
    "                box-shadow: 5px 5px 10px;\n"
    "                text-align: center;\n"
    "            }\n"
    "            .heading{"
    "                  padding: 1rem;"
    "                   font-weight: bolder; "
    "              }"
    "            \n", unsafe_allow_html=True)

horizontal_line()
# st.write("Closure Percentages")
st.write("""
               <div class = "heading">
                   Closure Percentages
               </div>
           """, unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns((1, 1, 1, 1, 1, 1))

with col2:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.green};'>Daily:\n"
                f"                            <h4>{unsafe_practices_per_daily} %</h4></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.green};'>Weekly:\n"
                f"                            <h4>{unsafe_practices_per_weekly} %</h4></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.green};'>Monthly:\n"
                f"                            <h4>{unsafe_practices_per_mtd} %</h4></div>", unsafe_allow_html=True)
with col5:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.green};'>YTD:\n"
                f"                            <h4>{unsafe_practices_per_ytd} %</h4></div>", unsafe_allow_html=True)

horizontal_line()

main_body_1, main_body_2 = st.columns((1, 1))

with main_body_1:
    st.write("""
               <div class = "heading">
                   Daily Trends
               </div>
           """, unsafe_allow_html=True)
    data = {}
    lst_x = []
    lst_y_opened = []
    lst_y_closed = []

    for i in range(7, 0, -1):
        today = date - datetime.timedelta(days=i)
        today_pd = pd.to_datetime(today)
        df = df_unsafe_practices_daily_data[df_unsafe_practices_daily_data["Date"] == today_pd]
        count = 0
        try:
            lst_y_opened.append(df["Opened"].tolist()[0])
            lst_y_closed.append(df["Closed"].tolist()[0])
        except Exception as e:
            print(e)
            lst_y_opened.append(0)
            lst_y_closed.append(0)
        lst_x.append(today.__str__())

    data["Incidences Opened"] = lst_y_opened
    data["Incidences Closed"] = lst_y_closed
    data["Date"] = lst_x

    fig = px.bar(
        data,
        x="Date",
        y=["Incidences Opened", "Incidences Closed"],
        color_discrete_map={"Incidences Closed": color.green, "Incidences Opened": color.red},
        barmode="group",
        text_auto=True,
    )
    st.plotly_chart(fig, use_container_width=True)
with (main_body_2):
    # print(df_safety_filtered_weekly)
    lst_x = list()
    lst_y_opened = list()
    lst_y_closed = list()

    st.write("""
               <div class = "heading">
                   Weekly Trends
               </div>
           """, unsafe_allow_html=True)
    data = {}
    if month < 10:
        df = df_unsafe_practices_weekly[df_unsafe_practices_weekly["Month"] == f"{year}-0{month}"].reset_index(
            drop=True)
    else:
        df = df_unsafe_practices_weekly[df_unsafe_practices_weekly["Month"] == f"{year}-{month}"].reset_index(drop=True)

    # print(df["Opened"])

    for i, opened in enumerate(df["Opened"]):
        if i == 0:
            lst_x.append(f"W{i + 1}(00-07)")
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

    for i, closed in enumerate(df["Closed"]):
        if i == 0:
            lst_y_closed.append(closed)
        if i == 1:
            lst_y_closed.append(closed)
        if i == 2:
            lst_y_closed.append(closed)
        if i == 3:
            lst_y_closed.append(closed)

    data["Weeks"] = lst_x
    data["Incidences Closed"] = lst_y_closed
    data["Incidences Opened"] = lst_y_opened
    # print(data)
    fig = px.bar(
        data,
        x="Weeks",
        y=["Incidences Opened", "Incidences Closed"],
        barmode="group",
        text_auto=True,
        color_discrete_map={"Incidences Closed" : color.green, "Incidences Opened": color.red},
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
# print(df_safety_filtered_monthly)
for i in range(1, 13):
    if i < 10:
        df = df_unsafe_practices_ytd[df_unsafe_practices_ytd["Month"] == f"{year}-0{i}"][["Opened"]].fillna(0)
        df_closed = df_unsafe_practices_ytd[df_unsafe_practices_ytd["Month"] == f"{year}-0{i}"][["Closed"]].fillna(0)
    else:
        df = df_unsafe_practices_ytd[df_unsafe_practices_ytd["Month"] == f"{year}-{i}"][["Opened"]].fillna(0)
        df_closed = df_unsafe_practices_ytd[df_unsafe_practices_ytd["Month"] == f"{year}-{i}"][["Closed"]].fillna(0)

    for j, item in enumerate(df["Opened"]):
        lst_x.append(f"{months[i - 1]}'{str(year)[2:]}")
        lst_y_Opened.append(item)

    for j, item in enumerate(df_closed["Closed"]):
        lst_y_Closed.append(item)

    data["Months"] = lst_x
    data["Incidences Opened"] = lst_y_Opened
    data["Incidences Closed"] = lst_y_Closed

fig = px.bar(
    data,
    x="Months",
    y=["Incidences Opened", "Incidences Closed"],
    color_discrete_map={"Incidences Closed": color.green, "Incidences Opened": color.red},
    barmode="group",
    text_auto=True,
)
st.plotly_chart(fig, use_container_width=True)

tab1, tab2 = st.tabs(["Open", "Closed"])
with tab1:
    st.dataframe(df_unsafe_practices_daily[df_unsafe_practices_daily["Status"] == "Open"], hide_index=True, use_container_width=True)
with tab2:
    df = df_unsafe_practices_daily[df_unsafe_practices_daily["Status"] == "Closed"]
    st.dataframe(df, hide_index=True, use_container_width=True)
# with tab3:
#     st.dataframe(df_unsafe_practices_daily[df_unsafe_practices_daily["Status"] == "In Process"],hide_index=True)
