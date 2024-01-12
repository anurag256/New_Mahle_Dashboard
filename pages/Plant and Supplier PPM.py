import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from streamlit_extras.switch_page_button import switch_page
from methods.colours import color
from methods.styles import back_btn, header, horizontal_line, selected_date

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

header("Plant and Supplier PPM")
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

# Getting Excel File Plant PPM
xls_plant_ppm = pd.ExcelFile("Excel/Quality/Plant_PPM.xlsx")

# Getting data for daily
df_plant_ppm_daily = pd.read_excel(xls_plant_ppm, "Plant PPM").fillna(0)
# print(df_plant_ppm_daily)

# getting data for weekly
df_plant_ppm_weekly = pd.read_excel(xls_plant_ppm, "Weekly Data").fillna(0)
df_plant_ppm_weekly_filtered = df_plant_ppm_weekly[df_plant_ppm_weekly["Month"] == f"{year}-{current_month}"]

# Getting Monthly Data
df_plant_ppm_monthly = pd.read_excel(xls_plant_ppm, "Monthly Data")

# getting issues
df_plant_ppm_issues = pd.read_excel(xls_plant_ppm, "PPM Issue").fillna("NA")

# Getting Excel File Supplier PPM
xls_supplier_ppm = pd.ExcelFile("Excel/Quality/Supplier_PPM.xlsx")

# Getting data for daily
df_supplier_ppm_daily = pd.read_excel(xls_supplier_ppm, "Supplier PPM").fillna(0)
# print(df_plant_ppm_daily)

# getting data for weekly
df_supplier_ppm_weekly = pd.read_excel(xls_supplier_ppm, "Weekly Data").fillna(0)
df_supplier_ppm_weekly_filtered = df_supplier_ppm_weekly[df_supplier_ppm_weekly["Month"] == f"{year}-{current_month}"]
# print(df_supplier_ppm_weekly_filtered)

# Getting Monthly Data
df_supplier_ppm_monthly = pd.read_excel(xls_supplier_ppm, "Monthly Data")

# getting issues
df_supplier_ppm_issues = pd.read_excel(xls_supplier_ppm, "Supplier Issue").fillna("Update")

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


tab1, tab2 = st.tabs(["Plant PPM", "Supplier PPM"])
with tab1:
    try:
        target = df_plant_ppm_monthly[df_plant_ppm_monthly['Month'] == f'{year}-{current_month}']['Target'].tolist()[0]
    except Exception as e:
        print(e)
        target = "Update"

    try:
        actual = df_plant_ppm_monthly[df_plant_ppm_monthly['Month'] == f'{year}-{current_month}']['Actual'].tolist()[0]
    except Exception as e:
        print(e)
        actual = "Update"

    card1, card2, card3, card4 = st.columns((1, 1, 1, 1))
    with card2:
        st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Monthly Target :\n"
                    f"                            <h4>{target}</h4></div>", unsafe_allow_html=True)
    with card3:
        st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Monthly Actual :\n"
                    f"                            <h4>{actual}</h4></div>", unsafe_allow_html=True)

    st.write("")
    colA, colB = st.columns((1, 1))
    with colA:
        # st.write("Daily Graph")
        st.write("\n"
                 "                                      <div class = \"heading\">\n"
                 "                                          Daily Trends\n"
                 "                                      </div>\n"
                 "                                  ", unsafe_allow_html=True)
        data = {}
        lst_x = []
        lst_y_opened = []
        lst_y_closed = []

        for i in range(7, 0, -1):
            today = date - datetime.timedelta(days=i)
            today_pd = pd.to_datetime(today)
            df = df_plant_ppm_daily[df_plant_ppm_daily["Date"] == today_pd]
            count = 0
            # print(df)
            try:
                lst_y_opened.append(df["Target"].tolist()[0])
                lst_y_closed.append(df["Actual"].tolist()[0])
            except Exception as e:
                print(e)
                lst_y_opened.append(0)
                lst_y_closed.append(0)
            lst_x.append(today.__str__())

        data["Target"] = lst_y_opened
        data["Actual"] = lst_y_closed
        data["Date"] = lst_x

        # print(data["Target"].__len__())

        fig = px.bar(
            data,
            x="Date",
            y=["Target", "Actual"],
            color_discrete_map={"Target": color.blue, "Actual": color.skyblue},
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
            df = df_plant_ppm_weekly_filtered[df_plant_ppm_weekly_filtered["Month"] == f"{year}-0{month}"].reset_index(
                drop=True)
        else:
            df = df_plant_ppm_weekly_filtered[df_plant_ppm_weekly_filtered["Month"] == f"{year}-{month}"].reset_index(
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

        for i, closed in enumerate(df["Actual"]):
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
        data["Actual"] = lst_y_closed
        # print(data)
        fig = px.bar(
            data,
            x="Weeks",
            y=["Target", "Actual"],
            barmode="group",
            text_auto=True,
            color_discrete_map={"Target": color.blue, "Actual": color.skyblue},
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
            df = df_plant_ppm_monthly[df_plant_ppm_monthly["Month"] == f"{year}-0{i}"][["Target"]].fillna(0)
            df_actual = df_plant_ppm_monthly[df_plant_ppm_monthly["Month"] == f"{year}-0{i}"][["Actual"]].fillna(0)
        else:
            df = df_plant_ppm_monthly[df_plant_ppm_monthly["Month"] == f"{year}-{i}"][["Target"]].fillna(0)
            df_actual = df_plant_ppm_monthly[df_plant_ppm_monthly["Month"] == f"{year}-{i}"][["Actual"]].fillna(0)

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
    tabA, tabB = st.tabs(["Open", "Closed"])
    with tabA:
        st.dataframe(df_plant_ppm_issues[df_plant_ppm_issues["Status"] == "Open"], hide_index=True,
                     use_container_width=True)
    with tabB:
        st.dataframe(df_plant_ppm_issues[df_plant_ppm_issues["Status"] == "Closed"], hide_index=True,
                     use_container_width=True)
with tab2:
    try:
        target = df_supplier_ppm_monthly[df_supplier_ppm_monthly['Month'] == f'{year}-{current_month}']['Target'].tolist()[0]
    except Exception as e:
        print(e)
        target = "Update"

    try:
        actual = df_supplier_ppm_monthly[df_supplier_ppm_monthly['Month'] == f'{year}-{current_month}']['Actual'].tolist()[0]
    except Exception as e:
        print(e)
        actual = "Update"

    card1, card2, card3, card4 = st.columns((1, 1, 1, 1))
    with card2:
        st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Monthly Target :\n"
                    f"                            <h4>{target}</h4></div>", unsafe_allow_html=True)
    with card3:
        st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Monthly Actual :\n"
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
            df = df_supplier_ppm_daily[df_supplier_ppm_daily["Date"] == today_pd]
            count = 0
            # print(df)
            try:
                lst_y_opened.append(df["Target"].tolist()[0])
                lst_y_closed.append(df["Actual"].tolist()[0])
            except Exception as e:
                print(e)
                lst_y_opened.append(0)
                lst_y_closed.append(0)
            lst_x.append(today.__str__())

        data["Target"] = lst_y_opened
        data["Actual"] = lst_y_closed
        data["Date"] = lst_x

        # print(data["Target"].__len__())

        fig = px.bar(
            data,
            x="Date",
            y=["Target", "Actual"],
            color_discrete_map={"Target": color.blue, "Actual": color.skyblue},
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
            df = df_supplier_ppm_weekly_filtered[df_supplier_ppm_weekly_filtered["Month"] == f"{year}-0{month}"].reset_index(
                drop=True)
        else:
            df = df_supplier_ppm_weekly_filtered[df_supplier_ppm_weekly_filtered["Month"] == f"{year}-{month}"].reset_index(
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

        for i, closed in enumerate(df["Actual"]):
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
        data["Actual"] = lst_y_closed
        # print(data)
        fig = px.bar(
            data,
            x="Weeks",
            y=["Target", "Actual"],
            barmode="group",
            text_auto=True,
            color_discrete_map={"Actual": color.skyblue, "Target": color.blue},
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
            df = df_supplier_ppm_monthly[df_supplier_ppm_monthly["Month"] == f"{year}-0{i}"][["Target"]].fillna(0)
            df_actual = df_supplier_ppm_monthly[df_supplier_ppm_monthly["Month"] == f"{year}-0{i}"][["Actual"]].fillna(0)
        else:
            df = df_supplier_ppm_monthly[df_supplier_ppm_monthly["Month"] == f"{year}-{i}"][["Target"]].fillna(0)
            df_actual = df_supplier_ppm_monthly[df_supplier_ppm_monthly["Month"] == f"{year}-{i}"][["Actual"]].fillna(0)

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
    tabA, tabB = st.tabs(["Open", "Closed"])
    with tabA:
        st.dataframe(df_supplier_ppm_issues[df_supplier_ppm_issues["Status"] == "Open"], hide_index=True,
                     use_container_width=True)
    with tabB:
        st.dataframe(df_supplier_ppm_issues[df_supplier_ppm_issues["Status"] == "Closed"], hide_index=True,
                     use_container_width=True)
