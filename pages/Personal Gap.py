import datetime
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
from methods.colours import color
from methods.styles import back_btn, header, horizontal_line

header("Personnel")

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

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

col1, col2 = st.columns((5, 2))
with col1:
    back_btn()
with col2:
    date = st.date_input("Please Select Month and Year (Any Date)",
                         value=datetime.datetime.now() - datetime.timedelta(days=1))
year = date.year
month = date.month
current_month = "01"
if month < 10:
    current_month = f"0{month}"
else:
    current_month = f"{month}"

horizontal_line()

# Getting Data
xls_per = pd.ExcelFile("Excel/Personal/Personal Gap.xlsx")
df_per_daily = pd.read_excel(xls_per, "Personal Gap Details")
df_per_weekly = pd.read_excel(xls_per, "Weekly Data")
df_per_ytd = pd.read_excel(xls_per, "Monthly Data")
df_issues = pd.read_excel(xls_per, "Issues")


df_per_weekly_filtered = df_per_weekly[df_per_weekly["Month"] == f"{year}-{current_month}"]


card1, card2, card3, card4, card5 = st.columns((1, 1, 1, 1, 1))
with card2:
    try:
        req = int(df_per_daily[df_per_daily["Date"] == pd.to_datetime(date)]["Planned Manpower Required (K)"].tolist()[0])
        per = df_per_daily[df_per_daily["Date"] == pd.to_datetime(date)]["Actual Manpower Available (L)"].tolist()[0]
        gap = df_per_daily[df_per_daily["Date"] == pd.to_datetime(date)]["Personal Gap (PG)"].tolist()[0]
    except Exception as e:
        print(e)
        req = "Update"
        per = "Update"
        gap = "Update"

    st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Required Headcount :\n"
                f"                            <h4>{req}</h4></div>", unsafe_allow_html=True)
with card3:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Total Headcount :\n"
                f"                            <h4>{int(per)}</h4></div>", unsafe_allow_html=True)
with card4:
    st.markdown(f"<div class=\"custom\" style='background-color:#c4bab9;'>Absenteeism:\n"
                f"                            <h4>{gap}%</h4></div>", unsafe_allow_html=True)

main_col1, main_col2 = st.columns((1, 1))
with main_col1:
    st.write("\n"
             "                                      <div class = \"heading\">\n"
             "                                          Daily Headcount Trend\n"
             "                                      </div>\n"
             "                                  ", unsafe_allow_html=True)
    data = {}
    lst_x = []
    lst_y_opened = []
    lst_y_closed = []

    for i in range(6, -1, -1):
        today = date - datetime.timedelta(days=i)
        today_pd = pd.to_datetime(today)
        df = df_per_daily[df_per_daily["Date"] == today_pd]
        count = 0
        # print(df)
        try:
            lst_y_opened.append(df["Planned Manpower Required (K)"].tolist()[0])
            lst_y_closed.append(df["Actual Manpower Available (L)"].tolist()[0])
        except Exception as e:
            print(e)
            lst_y_opened.append(0)
            lst_y_closed.append(0)
        lst_x.append(today.__str__())

    data["Required HC"] = lst_y_opened
    data["Total HC"] = lst_y_closed
    data["Date"] = lst_x

    # print(data["Target"].__len__())

    fig = px.bar(
        data,
        x="Date",
        y=["Required HC", "Total HC"],
        color_discrete_map={"Required HC": color.blue, "Total HC": color.skyblue},
        barmode="group",
        text_auto=True,
        labels= {
            "Required": "Manpower",
            "Date": "Date"
        }
    )
    st.plotly_chart(fig, use_container_width=True)

with main_col2:
    lst_x = list()
    lst_y_opened = list()
    lst_y_closed = list()

    st.write("\n"
             "                                  <div class = \"heading\">\n"
             "                                      Weekly Headcount Trend\n"
             "                                  </div>\n"
             "                              ", unsafe_allow_html=True)
    data = {}
    # print(df["Opened"])

    for i, opened in enumerate(df_per_weekly_filtered["Target"]):
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

    for i, closed in enumerate(df_per_weekly_filtered["Actual"]):
        if i == 0:
            lst_y_closed.append(closed)
        if i == 1:
            lst_y_closed.append(closed)
        if i == 2:
            lst_y_closed.append(closed)
        if i == 3:
            lst_y_closed.append(closed)

    data["Weeks"] = lst_x
    data["Required HC"] = lst_y_opened
    data["Total HC"] = lst_y_closed

    fig = px.bar(
        data,
        x="Weeks",
        y=["Required HC", "Total HC"],
        barmode="group",
        text_auto=True,
        color_discrete_map={"Required HC": color.blue, "Total HC": color.skyblue},
    )
    st.plotly_chart(fig, use_container_width=True)

horizontal_line()

data = {}
lst_x = list()
lst_y_Opened = list()
lst_y_Closed = list()

st.write("""
             <div class = "heading">
                 Monthly Sales/Headcount Trend
             </div>
         """, unsafe_allow_html=True)
# print(df_safety_filtered_monthly)
for i in range(1, 13):
    if i < 10:
        df = df_per_ytd[df_per_ytd["Month"] == f"{year}-0{i}"][["Target"]].fillna(0)
        df_actual = df_per_ytd[df_per_ytd["Month"] == f"{year}-0{i}"][["Actual"]].fillna(0)
    else:
        df = df_per_ytd[df_per_ytd["Month"] == f"{year}-{i}"][["Target"]].fillna(0)
        df_actual = df_per_ytd[df_per_ytd["Month"] == f"{year}-{i}"][["Actual"]].fillna(0)

    for j, item in enumerate(df["Target"]):
        lst_x.append(f"{months[i - 1]}'{str(year)[2:]}")
        lst_y_Opened.append(item)

    for j, item in enumerate(df_actual["Actual"]):
        lst_y_Closed.append(item)

    data["Months"] = lst_x
    data["Target"] = lst_y_Opened
    data["Actual"] = lst_y_Closed

fig = px.bar(
    data,
    x="Months",
    y=["Target", "Actual"],
    color_discrete_map={"Target": color.blue, "Actual": color.skyblue},
    barmode="group",
    text_auto=True,
)
st.plotly_chart(fig, use_container_width=True)

tab_open, tab_closed = st.tabs(["Open", "Closed"])

with tab_open:
    st.dataframe(df_issues[df_issues["Status"] == "Open"], hide_index=True, use_container_width=True)
with tab_closed:
    st.dataframe(df_issues[df_issues["Status"] == "Closed"], hide_index=True, use_container_width=True)