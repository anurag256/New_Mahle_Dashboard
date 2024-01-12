import datetime
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from methods.styles import back_btn, header, horizontal_line, color, selected_date
import plotly.express as px

header("Sale Plan Vs Actual")

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

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

horizontal_line()

# Getting Excel File Plant PPM
xls_sale_vs_actual = pd.ExcelFile("Excel/Delivery/Sale_vs_actual_plan.xlsx")

# Getting data for daily
df_sale_vs_actual_daily = pd.read_excel(xls_sale_vs_actual, "Sale vs Actual Plan").fillna(0)
# print(df_sale_vs_actual_daily)

# getting data for weekly
df_sale_vs_actual_weekly = pd.read_excel(xls_sale_vs_actual, "Weekly Data").fillna(0)
df_sale_vs_actual_weekly_filtered = df_sale_vs_actual_weekly[df_sale_vs_actual_weekly["Month"] == f"{year}-{current_month}"]

# Getting Monthly Data
df_sale_vs_actual_monthly = pd.read_excel(xls_sale_vs_actual, "Monthly Data")

# getting issues
df_sale_vs_actual_issues = pd.read_excel(xls_sale_vs_actual, "Issues").fillna("NA")

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
    "                font-size:0.8rem;\n"
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

try:
    target = df_sale_vs_actual_monthly[df_sale_vs_actual_monthly['Month'] == f'{year}-{current_month}']['Budgeted Sale'].tolist()[0]
except Exception as e:
    print(e)
    target = "Update"

try:
    actual = df_sale_vs_actual_monthly[df_sale_vs_actual_monthly['Month'] == f'{year}-{current_month}']['Actual Sale'].tolist()[0]
except Exception as e:
    print(e)
    actual = "Update"

card1, card2, card3, card4 = st.columns((1, 1, 1, 1))
with card2:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Monthly Budgeted Sale:\n"
                f"                            <h4>{target}</h4></div>", unsafe_allow_html=True)
with card3:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Monthly Actual Sale:\n"
                f"                            <h4>{actual}</h4></div>", unsafe_allow_html=True)
    
st.write("")
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
        df = df_sale_vs_actual_daily[df_sale_vs_actual_daily["Date"] == today_pd]
        count = 0
        # print(df)
        try:
            lst_y_opened.append(df["Actual Sale"].tolist()[0])
            lst_y_closed.append(df["Budgeted Sale"].tolist()[0])
        except Exception as e:
            print(e)
            lst_y_opened.append(0)
            lst_y_closed.append(0)
        lst_x.append(today.__str__())

    data["Actual Sale"] = lst_y_opened
    data["Budgeted Sale"] = lst_y_closed
    data["Date"] = lst_x

    # print(data["Target"].__len__())

    fig = px.bar(
        data,
        x="Date",
        y=["Budgeted Sale", "Actual Sale"],
        color_discrete_map={"Budgeted Sale": color.blue, "Actual Sale": color.skyblue},
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
        df = df_sale_vs_actual_weekly_filtered[df_sale_vs_actual_weekly_filtered["Month"] == f"{year}-0{month}"].reset_index(
            drop=True)
    else:
        df = df_sale_vs_actual_weekly_filtered[df_sale_vs_actual_weekly_filtered["Month"] == f"{year}-{month}"].reset_index(
            drop=True)

    # print(df["Opened"])

    for i, opened in enumerate(df["Actual Sale"]):
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

    for i, closed in enumerate(df["Budgeted Sale"]):
        if i == 0:
            lst_y_closed.append(closed)
        if i == 1:
            lst_y_closed.append(closed)
        if i == 2:
            lst_y_closed.append(closed)
        if i == 3:
            lst_y_closed.append(closed)

    data["Weeks"] = lst_x
    data["Budgeted Sale"] = lst_y_closed
    data["Actual Sale"] = lst_y_opened
    # print(data)
    fig = px.bar(
        data,
        x="Weeks",
        y=["Budgeted Sale", "Actual Sale"],
        barmode="group",
        text_auto=True,
        color_discrete_map={"Budgeted Sale": color.blue, "Actual Sale": color.skyblue},
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
        df = df_sale_vs_actual_monthly[df_sale_vs_actual_monthly["Month"] == f"{year}-0{i}"][["Budgeted Sale"]].fillna(0)
        df_actual = df_sale_vs_actual_monthly[df_sale_vs_actual_monthly["Month"] == f"{year}-0{i}"][["Actual Sale"]].fillna(0)
    else:
        df = df_sale_vs_actual_monthly[df_sale_vs_actual_monthly["Month"] == f"{year}-{i}"][["Budgeted Sale"]].fillna(0)
        df_actual = df_sale_vs_actual_monthly[df_sale_vs_actual_monthly["Month"] == f"{year}-{i}"][["Actual Sale"]].fillna(0)

    for j, item in enumerate(df["Budgeted Sale"]):
        lst_x.append(f"{months[i - 1]}'{str(year)[2:]}")
        lst_y_Opened.append(item)

    for j, item in enumerate(df_actual["Actual Sale"]):
        lst_y_Closed.append(item)

    data["Months"] = lst_x
    data["Budgeted Sale"] = lst_y_Opened
    data["Actual Sale"] = lst_y_Closed

fig = px.bar(
    data,
    x="Months",
    y=["Budgeted Sale", "Actual Sale"],
    color_discrete_map={"Budgeted Sale": color.blue, "Actual Sale": color.skyblue},
    barmode="group",
    text_auto=True,
)
st.plotly_chart(fig, use_container_width=True)
tabA, tabB = st.tabs(["Open", "Closed"])
with tabA:
    st.dataframe(df_sale_vs_actual_issues[df_sale_vs_actual_issues["Status"] == "Open"], hide_index=True,
                    use_container_width=True)
with tabB:
    st.dataframe(df_sale_vs_actual_issues[df_sale_vs_actual_issues["Status"] == "Closed"], hide_index=True,
                    use_container_width=True)