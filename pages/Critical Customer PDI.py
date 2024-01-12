import datetime
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
from methods.colours import color
from methods.styles import back_btn, header, horizontal_line, selected_date, vertical_line

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

header("Critical Customer PDI")

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

# Getting Ford Data
xls_ford = pd.ExcelFile("Excel/Delivery/CCPDI/Ford.xlsx")
df_ford_daily = pd.read_excel(xls_ford, "Daily Data")
df_ford_weekly = pd.read_excel(xls_ford, "Weekly Data")
df_ford_ytd = pd.read_excel(xls_ford, "Monthly Data")
# Getting Filtered Data
df_ford_weekly_filtered = df_ford_weekly[df_ford_weekly["Month"] == f"{year}-{current_month}"]

# Getting Data GM Spares
xls_gm_spares = pd.ExcelFile("Excel/Delivery/CCPDI/GM Data.xlsx")
df_gm_daily = pd.read_excel(xls_gm_spares, "Daily Data")
df_gm_weekly = pd.read_excel(xls_gm_spares, "Weekly Data")
df_gm_ytd = pd.read_excel(xls_gm_spares, "Monthly Data")
# Getting Filtered Data
df_gm_weekly_filtered = df_gm_weekly[df_gm_weekly["Month"] == f"{year}-{current_month}"]

# Getting Data HD Data Spares
xls_hd = pd.ExcelFile("Excel/Delivery/CCPDI/HD Data.xlsx")
df_hd_daily = pd.read_excel(xls_hd, "Daily Data")
df_hd_weekly = pd.read_excel(xls_hd, "Weekly Data")
df_hd_ytd = pd.read_excel(xls_hd, "Monthly Data")
# Getting Filtered Data
df_hd_weekly_filtered = df_hd_weekly[df_hd_weekly["Month"] == f"{year}-{current_month}"]

# Getting Data Honda Spares
xls_honda = pd.ExcelFile("Excel/Delivery/CCPDI/Honda.xlsx")
df_honda_daily = pd.read_excel(xls_honda, "Daily Data")
df_honda_weekly = pd.read_excel(xls_honda, "Weekly Data")
df_honda_ytd = pd.read_excel(xls_honda, "Monthly Data")
df_honda_weekly_filtered = df_honda_weekly[df_honda_weekly["Month"] == f"{year}-{current_month}"]

# Getting Data MSIL Spares
xls_MSIL = pd.ExcelFile("Excel/Delivery/CCPDI/MSIL.xlsx")
df_MSIL_daily = pd.read_excel(xls_MSIL, "Daily Data")
df_MSIL_weekly = pd.read_excel(xls_MSIL, "Weekly Data")
df_MSIL_ytd = pd.read_excel(xls_MSIL, "Monthly Data")
df_MSIL_weekly_filtered = df_MSIL_weekly[df_MSIL_weekly["Month"] == f"{year}-{current_month}"]

# Getting Data RNAIPL Spares
xls_RNAIPL = pd.ExcelFile("Excel/Delivery/CCPDI/RNAIPL.xlsx")
df_RNAIPL_daily = pd.read_excel(xls_RNAIPL, "Daily Data")
df_RNAIPL_weekly = pd.read_excel(xls_RNAIPL, "Weekly Data")
df_RNAIPL_ytd = pd.read_excel(xls_RNAIPL, "Monthly Data")
df_RNAIPL_weekly_filtered = df_RNAIPL_weekly[df_RNAIPL_weekly["Month"] == f"{year}-{current_month}"]

tab1, tab2, tab3, tab4 = st.tabs(["MSIL", "HD", "Honda", "GM"])

with tab1:
    card1, card2, card3, card4 = st.columns((1, 1, 1, 1))
    with card2:
        try:
            target = df_MSIL_ytd[df_MSIL_ytd["Month"] == f"{year}-{current_month}"]["Target"].tolist()[0]
        except Exception as e:
            print(e)
            target = "Update"
        st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Monthly Target :\n"
                    f"                            <h4>{target}</h4></div>", unsafe_allow_html=True)
    with card3:
        try:
            actual = target = df_MSIL_ytd[df_MSIL_ytd["Month"] == f"{year}-{current_month}"]["Actual"].tolist()[0]
        except Exception as e:
            print(e)
            actual = "Update"
        with card3:
            st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Monthly Actual :\n"
                        f"                            <h4>{actual}</h4></div>", unsafe_allow_html=True)
    colA, colB = st.columns((1, 1))
    with colA:
        st.write("\n"
                 "                                      <div class = \"heading\">\n"
                 "                                          Daily Trends\n"
                 "                                      </div>\n"
                 "                                  ", unsafe_allow_html=True)
        data = {}
        lst_x = []
        lst_y_opened = []
        lst_y_closed = []

        for i in range(6, -1, -1):
            today = date - datetime.timedelta(days=i)
            today_pd = pd.to_datetime(today)
            df = df_MSIL_daily[df_MSIL_daily["Date"] == today_pd]
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
        # print(df["Opened"])

        for i, opened in enumerate(df_MSIL_weekly_filtered["Target"]):
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

        for i, closed in enumerate(df_MSIL_weekly_filtered["Actual"]):
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
            df = df_MSIL_ytd[df_MSIL_ytd["Month"] == f"{year}-0{i}"][["Target"]].fillna(0)
            df_actual = df_MSIL_ytd[df_MSIL_ytd["Month"] == f"{year}-0{i}"][["Actual"]].fillna(0)
        else:
            df = df_MSIL_ytd[df_MSIL_ytd["Month"] == f"{year}-{i}"][["Target"]].fillna(0)
            df_actual = df_MSIL_ytd[df_MSIL_ytd["Month"] == f"{year}-{i}"][["Actual"]].fillna(0)

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

with tab2:
    card1, card2, card3, card4 = st.columns((1, 1, 1, 1))
    with card2:
        try:
            target = df_hd_ytd[df_hd_ytd["Month"] == f"{year}-{current_month}"]["Target"].tolist()[0]
        except Exception as e:
            print(e)
            target = "Update"
        st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Monthly Target :\n"
                    f"                            <h4>{target}</h4></div>", unsafe_allow_html=True)
    with card3:
        try:
            actual = df_hd_ytd[df_hd_ytd["Month"] == f"{year}-{current_month}"]["Actual"].tolist()[0]
        except Exception as e:
            print(e)
            actual = "Update"
        with card3:
            st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Monthly Actual :\n"
                        f"                            <h4>{actual}</h4></div>", unsafe_allow_html=True)
    colA, colB = st.columns((1, 1))
    with colA:
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
            df = df_hd_daily[df_hd_daily["Date"] == today_pd]
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

        st.write("\n"
                 "                                  <div class = \"heading\">\n"
                 "                                      Weekly Trends\n"
                 "                                  </div>\n"
                 "                              ", unsafe_allow_html=True)
        data = {}
        # print(df["Opened"])

        for i, opened in enumerate(df_hd_weekly_filtered["Target"]):
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

        for i, closed in enumerate(df_hd_weekly_filtered["Actual"]):
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
    data = {}
    lst_x = list()
    lst_y_Opened = list()
    lst_y_Closed = list()

    st.write("\n"
             "                    <div class = \"heading\">\n"
             "                        Monthly Trends\n"
             "                    </div>\n"
             "                ", unsafe_allow_html=True)
    # print(df_safety_filtered_monthly)
    for i in range(1, 13):
        if i < 10:
            df = df_hd_ytd[df_hd_ytd["Month"] == f"{year}-0{i}"][["Target"]].fillna(0)
            df_actual = df_hd_ytd[df_hd_ytd["Month"] == f"{year}-0{i}"][["Actual"]].fillna(0)
        else:
            df = df_hd_ytd[df_hd_ytd["Month"] == f"{year}-{i}"][["Target"]].fillna(0)
            df_actual = df_hd_ytd[df_hd_ytd["Month"] == f"{year}-{i}"][["Actual"]].fillna(0)

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

with tab3:
    card1, card2, card3, card4 = st.columns((1, 1, 1, 1))
    with card2:
        try:
            target = df_honda_ytd[df_honda_ytd["Month"] == f"{year}-{current_month}"]["Target"].tolist()[0]
        except Exception as e:
            print(e)
            target = "Update"
        st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Monthly Target :\n"
                    f"                            <h4>{target}</h4></div>", unsafe_allow_html=True)
    with card3:
        try:
            actual = df_honda_ytd[df_honda_ytd["Month"] == f"{year}-{current_month}"]["Actual"].tolist()[0]
        except Exception as e:
            print(e)
            actual = "Update"
        with card3:
            st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Monthly Actual :\n"
                        f"                            <h4>{actual}</h4></div>", unsafe_allow_html=True)
    colA, colB = st.columns((1, 1))
    with colA:
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
            df = df_honda_daily[df_honda_daily["Date"] == today_pd]
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

        st.write("\n"
                 "                                  <div class = \"heading\">\n"
                 "                                      Weekly Trends\n"
                 "                                  </div>\n"
                 "                              ", unsafe_allow_html=True)
        data = {}
        # print(df["Opened"])

        for i, opened in enumerate(df_honda_weekly_filtered["Target"]):
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

        for i, closed in enumerate(df_honda_weekly_filtered["Actual"]):
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
    data = {}
    lst_x = list()
    lst_y_Opened = list()
    lst_y_Closed = list()

    st.write("\n"
             "                    <div class = \"heading\">\n"
             "                        Monthly Trends\n"
             "                    </div>\n"
             "                ", unsafe_allow_html=True)
    # print(df_safety_filtered_monthly)
    for i in range(1, 13):
        if i < 10:
            df = df_honda_ytd[df_honda_ytd["Month"] == f"{year}-0{i}"][["Target"]].fillna(0)
            df_actual = df_honda_ytd[df_honda_ytd["Month"] == f"{year}-0{i}"][["Actual"]].fillna(0)
        else:
            df = df_honda_ytd[df_honda_ytd["Month"] == f"{year}-{i}"][["Target"]].fillna(0)
            df_actual = df_honda_ytd[df_honda_ytd["Month"] == f"{year}-{i}"][["Actual"]].fillna(0)

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

with tab4:
    card1, card2, card3, card4 = st.columns((1, 1, 1, 1))
    with card2:
        try:
            target = df_gm_ytd[df_gm_ytd["Month"] == f"{year}-{current_month}"]["Target"].tolist()[
                0]
        except Exception as e:
            print(e)
            target = "Update"
        st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Monthly Target :\n"
                    f"                            <h4>{target}</h4></div>", unsafe_allow_html=True)
    with card3:
        try:
            actual = df_gm_ytd[df_gm_ytd["Month"] == f"{year}-{current_month}"]["Actual"].tolist()[
                0]
        except Exception as e:
            print(e)
            actual = "Update"
        with card3:
            st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Monthly Actual :\n"
                        f"                            <h4>{actual}</h4></div>", unsafe_allow_html=True)
    colA, colB = st.columns((1, 1))
    with colA:
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
            df = df_gm_daily[df_gm_daily["Date"] == today_pd]
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

        st.write("\n"
                 "                                  <div class = \"heading\">\n"
                 "                                      Weekly Trends\n"
                 "                                  </div>\n"
                 "                              ", unsafe_allow_html=True)
        data = {}
        # print(df["Opened"])

        for i, opened in enumerate(df_gm_weekly_filtered["Target"]):
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

        for i, closed in enumerate(df_gm_weekly_filtered["Actual"]):
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
    data = {}
    lst_x = list()
    lst_y_Opened = list()
    lst_y_Closed = list()

    st.write("\n"
             "                    <div class = \"heading\">\n"
             "                        Monthly Trends\n"
             "                    </div>\n"
             "                ", unsafe_allow_html=True)
    # print(df_safety_filtered_monthly)
    for i in range(1, 13):
        if i < 10:
            df = df_gm_ytd[df_gm_ytd["Month"] == f"{year}-0{i}"][["Target"]].fillna(0)
            df_actual = df_gm_ytd[df_gm_ytd["Month"] == f"{year}-0{i}"][["Actual"]].fillna(0)
        else:
            df = df_gm_ytd[df_gm_ytd["Month"] == f"{year}-{i}"][["Target"]].fillna(0)
            df_actual = df_gm_ytd[df_gm_ytd["Month"] == f"{year}-{i}"][["Actual"]].fillna(0)

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