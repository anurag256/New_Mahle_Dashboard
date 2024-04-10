import datetime
import plotly.express as px
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from methods.styles import back_btn, header, horizontal_line, selected_date
from methods.colours import color
import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

recordable_loss_time_injury: int = 0
recordable_accident: int = 0
firstaid: int = 0
near_miss: int = 0
fire: int = 0
testing: str = "Testing"

header("Safety Incident Tracking")

col1, col2 = st.columns((5, 2))
with col1:
    back_btn()
with col2:
    date = selected_date()

# Getting The data
xls = pd.ExcelFile("Excel/Safety/Safety.xlsx")
month = date.month
year = date.year
if month < 10:
    current_month = f"0{month}"
else:
    current_month = f"{month}"

df_safety_weekly = pd.read_excel(xls, sheet_name="Weekly_data").fillna(0)
df_safety_monthly = pd.read_excel(xls, sheet_name="Monthly_data").fillna(0)
df_safety_daily = pd.read_excel(xls, sheet_name="Safety Incidents Tracking").fillna(0)
df_safety_incidences = pd.read_excel(xls, sheet_name="Safety Incidences").fillna(0)

df_safety_filtered_weekly = df_safety_weekly[df_safety_weekly["Month"] == f"{year}-{current_month}"]
df_safety_filtered_monthly = df_safety_monthly[df_safety_monthly["Month"] == f"{year}-{current_month}"]
# noinspection PyBroadException
try:
    recordable_loss_time_injury = int(df_safety_filtered_monthly["Recordable Lost Time Injury"].tolist()[0])
    recordable_accident = int(df_safety_filtered_monthly["Recordable Accident"].tolist()[0])
    firstaid = int(df_safety_filtered_monthly["First Aid"].tolist()[0])
    near_miss = int(df_safety_filtered_monthly["Near Miss"].tolist()[0])
    fire = int(df_safety_filtered_monthly["Fire"].tolist()[0])

except Exception as e:
    # noinspection PyTypeChecker
    recordable_loss_time_injury = "Update"
    # noinspection PyTypeChecker
    recordable_accident = "Update"
    # noinspection PyTypeChecker
    firstaid = "Update"
    # noinspection PyTypeChecker
    near_miss = "Update"
    # noinspection PyTypeChecker
    fire = "Update"

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

card1, card2, card3, card4, card5 = st.columns((1, 1, 1, 1, 1))

with card1:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.red};'>Monthly Lost Time Injury:\n"
                f"                            <h4>{recordable_loss_time_injury}</h4></div>", unsafe_allow_html=True)
with card2:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.pink};'>Monthly Recordable Accident:\n"
                f"                            <h4>{recordable_accident}</h4></div>", unsafe_allow_html=True)
with card3:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.orange};'>Monthly Fire Incidence:\n"
                f"                           <h4>{fire}</h4></div>", unsafe_allow_html=True)
with card4:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.yellow};'>Monthly First Aid:\n"
                f"                           <h4>{firstaid}</h4></div>", unsafe_allow_html=True)
with card5:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Monthly Near Miss:\n"
                f"                           <h4>{near_miss}</h4></div>", unsafe_allow_html=True)

horizontal_line()

daily, weekly = st.columns((1, 1))
with daily:
    st.write("""
        <div class = "heading">
            Daily Trends
        </div>
    """, unsafe_allow_html=True)
    data = {}
    lst_x_daily = []
    lst_y_daily = []
    for i in range(30, 0, -1):
        today = date - datetime.timedelta(days=i)
        today_pd = pd.to_datetime(today)
        df = df_safety_daily[df_safety_daily["Date"] == today_pd]
        lst_x_daily.append(f"{today.__str__()}")
        try:
            lst_y_daily.append(df["Total"].tolist()[0])
        except:
            lst_y_daily.append(0)

    data["Days"] = lst_x_daily
    data["Incidences"] = lst_y_daily

    fig = px.bar(
        data,
        x="Days",
        y="Incidences",
        text_auto=True,
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
    )
with weekly:
    # print(df_safety_filtered_weekly)
    lst_x = list()
    lst_y = list()
    st.write("""
           <div class = "heading">
               Weekly Trends
           </div>
       """, unsafe_allow_html=True)
    data = {}
    df = df_safety_filtered_weekly[["Total"]]
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
    data["Incidences"] = lst_y
    fig = px.bar(
        data,
        x="Weeks",
        y="Incidences",
        text_auto=True,
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )

data = {}
lst_x = list()
lst_y = list()
st.write("""
       <div class = "heading">
           Monthly Trends
       </div>
   """, unsafe_allow_html=True)
# print(df_safety_filtered_monthly)
for i in range(1, 13):
    if i < 10:
        df = df_safety_monthly[df_safety_monthly["Month"] == f"{year}-0{i}"][["Total"]]
    else:
        df = df_safety_monthly[df_safety_monthly["Month"] == f"{year}-{i}"][["Total"]]

    for j, item in enumerate(df["Total"]):
        lst_x.append(f"{months[i - 1]}'{str(year)[2:]}")
        lst_y.append(item)

    data["Months"] = lst_x
    data["Incidences"] = lst_y

fig = px.bar(pd.DataFrame(data), x="Months", y="Incidences", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

# noinspection SpellCheckingInspection
opened, closed = st.tabs(["Open", "Closed"])
with opened:
    st.dataframe(df_safety_incidences[df_safety_incidences["Status"] == "Open"], hide_index=True,
                 use_container_width=True)
with closed:
    st.dataframe(df_safety_incidences[df_safety_incidences["Status"] == "Closed"], hide_index=True,
                 use_container_width=True)
# with inprocess:
#     st.dataframe(df_safety_incidences[df_safety_incidences["Status"] == "In Process"], hide_index=True,
#                  use_container_width=True)
