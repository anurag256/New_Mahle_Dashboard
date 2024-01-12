import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.switch_page_button import switch_page
from methods.colours import color
from methods.styles import back_btn, header, horizontal_line, selected_date

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

header("Problem Solving")
col1, col2 = st.columns((5, 2))
with col1:
    back_btn()
with col2:
    date = selected_date()

year = date.year
month = date.month
current_month = "01"
if month < 10:
    current_month = f"0{month}"
if month > 10:
    current_month = f"{month}"

st.markdown(
    "\n"
    "            <style>\n"
    "            .custom {\n"
    "                margin: 0.4rem;\n"
    "                padding-top: 0.7rem;\n"
    "                border: 1px solid black;\n"
    "                height: 5rem;\n"
    "                border-radius: 0.7rem;\n"
    "                font-weight: bold;\n"
    "                font-size:0.7rem;\n"
    "                box-shadow: 5px 5px 10px;\n"
    "                text-align: center;\n"
    "            }\n"
    "            .custom h4{ color:white;font-weight:bold; padding-top:0.5rem; }\n"
    "            .heading{"
    "                  padding: 1rem;"
    "                   font-weight: bolder; "
    "              }"
    "            \n", unsafe_allow_html=True
)

xls_problem = pd.ExcelFile("Excel/PSP/Problem_solving_competency.xlsx")
df_problem_daily = pd.read_excel(xls_problem, "Problem Solving Competency")
df_problem_weekly = pd.read_excel(xls_problem, "Weekly Data")
df_problem_weekly_filtered = df_problem_weekly[df_problem_weekly['Month']
                                               == f'{year}-{current_month}']
df_problem_ytd = pd.read_excel(xls_problem, "Monthly Data")

df_problem_daily['Date'] = pd.to_datetime(df_problem_daily['Date'])

new_date = pd.to_datetime(date)

# Filter the DataFrame for the selected date
selected_date_data = df_problem_daily[df_problem_daily['Date'] == new_date]

starting_date = new_date - datetime.timedelta(days=6)

last_seven_days_data = df_problem_daily[(
    starting_date <= df_problem_daily['Date']) & (df_problem_daily["Date"] <= new_date)]

# df_last_data = df_problem_daily[df_problem_daily["Date"] >= (df_problem_daily["Date"].max() - datetime.timedelta(days=6))].fillna(
#     "NA"
# )

horizontal_line()

st.dataframe(last_seven_days_data, hide_index=True, use_container_width=True, column_config={
    "Date": st.column_config.DateColumn(
        format="YYYY-MM-DD",
    )
})

horizontal_line()

colA, colB = st.columns((1, 1))
with colA:
    # st.write("Daily Graph")
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
        df = df_problem_daily[df_problem_daily["Date"] == today_pd]
        count = 0
        # print(df)
        try:
            lst_y_opened.append(df["Target"].tolist()[0])
            lst_y_closed.append(df["PSP Competency (%)"].tolist()[0])
        except Exception as e:
            print(e)
            lst_y_opened.append(0)
            lst_y_closed.append(0)
        lst_x.append(today.__str__())

    data["Target"] = lst_y_opened
    data["PSP Competency (%)"] = lst_y_closed
    data["Date"] = lst_x

    fig = px.bar(
        data,
        x="Date",
        y=["Target", "PSP Competency (%)"],
        color_discrete_map={"Target": color.blue,
                            "PSP Competency (%)": color.skyblue},
        barmode="group",
        text_auto=True,
    )
    st.plotly_chart(fig, use_container_width=True)
with colB:
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
        df = df_problem_weekly_filtered[df_problem_weekly_filtered["Month"] == f"{year}-0{month}"].reset_index(
            drop=True)
    else:
        df = df_problem_weekly_filtered[df_problem_weekly_filtered["Month"] == f"{year}-{month}"].reset_index(
            drop=True)

    # print(df["Opened"])

    for i, opened in enumerate(df["Target"]):
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

    for i, closed in enumerate(df["PSP Competency (%)"]):
        if i == 0:
            lst_y_closed.append(closed)
        if i == 1:
            lst_y_closed.append(closed)
        if i == 2:
            lst_y_closed.append(closed)
        if i == 3:
            lst_y_closed.append(closed)

    data["Weeks"] = lst_x
    data["Target"] = lst_y_opened
    data["PSP Competency (%)"] = lst_y_closed
    # print(data)
    fig = px.bar(
        data,
        x="Weeks",
        y=["Target", "PSP Competency (%)"],
        barmode="group",
        text_auto=True,
        color_discrete_map={"Target": color.blue,
                            "PSP Competency (%)": color.skyblue},
    )
    st.plotly_chart(fig, use_container_width=True)

horizontal_line()
# st.write("Monthly Data")
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
        df = df_problem_ytd[df_problem_ytd["Month"]
                            == f"{year}-0{i}"][["Target"]].fillna(0)
        df_actual = df_problem_ytd[df_problem_ytd["Month"] ==
                                   f"{year}-0{i}"][["PSP Competency (%)"]].fillna(0)
    else:
        df = df_problem_ytd[df_problem_ytd["Month"]
                            == f"{year}-{i}"][["Target"]].fillna(0)
        df_actual = df_problem_ytd[df_problem_ytd["Month"]
                                   == f"{year}-{i}"][["PSP Competency (%)"]].fillna(0)

    for j, item in enumerate(df["Target"]):
        lst_x.append(f"{months[i - 1]}'{str(year)[2:]}")
        lst_y_Opened.append(item)

    for j, item in enumerate(df_actual["PSP Competency (%)"]):
        lst_y_Closed.append(item)

    data["Months"] = lst_x
    data["Target"] = lst_y_Opened
    data["PSP Competency (%)"] = lst_y_Closed

fig = px.bar(
    data,
    x="Months",
    y=["Target", "PSP Competency (%)"],
    color_discrete_map={"Target": color.blue,
                        "PSP Competency (%)": color.skyblue},
    barmode="group",
    text_auto=True,
)
st.plotly_chart(fig, use_container_width=True)
