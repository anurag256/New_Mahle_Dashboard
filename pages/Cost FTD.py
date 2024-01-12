import datetime
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from methods.colours import color
from methods.styles import header, horizontal_line, svg_for_ftd

header("Cost FTD")
back = st.button("<- Back")
if back:
    switch_page("App")

colA, spacer, colB = st.columns((2, 2, 2))

with colA:
    date = st.date_input("Please Select The Date", value=datetime.datetime.now() - datetime.timedelta(days=1))
with (colB):
    st.write("")
    st.subheader(f"Status As on {date}")

horizontal_line()
today_pd = pd.to_datetime(date)

# Getting Human Productivity Data
xls_human_prod = pd.ExcelFile("Excel/Cost/Human_Productivity.xlsx")
df_human_prod_daily = pd.read_excel(xls_human_prod, "Human Productivity")
df_human_prod_issues = pd.read_excel(xls_human_prod, "Issues")

# Getting OEE Data
xls_oee = pd.ExcelFile("Excel/Cost/Plant_Aggregate_OEE.xlsx")
df_oee_daily = pd.read_excel(xls_oee, "Plant Aggregate OEE")
df_oee_issues_daily = pd.read_excel(xls_oee, "Issues")

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
    "                font-size:1rem;\n"
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

col_main_body1, col_main_body2, col_main_body3 = st.columns((2, 0.5, 5))

with col_main_body1:
    # image_loader("c", height=30, top=30, left=4)
    svg_for_ftd("c", new_height=450, new_width=450, top=0, left=4)
    st.write("")
with col_main_body2:
    pass
with col_main_body3:
    tab1, tab2 = st.tabs(["Human Productivity", "Plant Aggregate OEE"])

    with tab1:
        colA, colB = st.columns((1, 1))
        with colA:
            try:
                target = df_human_prod_daily[df_human_prod_daily["Date"] == today_pd]["Target"].tolist()[0]
            except:
                target = "Update"

            st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Human Productivity Target:\n"
                        f"                           <h4>{target}</h4></div>", unsafe_allow_html=True)
        with colB:
            try:
                actual = df_human_prod_daily[df_human_prod_daily["Date"] == today_pd]["Actual"].tolist()[0]
            except:
                actual = "Update"
            st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Human Productivity Actual:\n"
                        f"                           <h4>{actual}</h4></div>", unsafe_allow_html=True)

        st.write("")
        st.write("Issues : ")
        st.dataframe(df_human_prod_issues[df_human_prod_issues["Date"] == today_pd], use_container_width=True,
                     hide_index=True)

    with tab2:
        colA, colB = st.columns((1, 1))
        with colA:
            try:
                target = df_oee_daily[df_oee_daily["Date"] == today_pd]["Target"].tolist()[0]
            except:
                target = "Update"

            st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Plant Aggregate OEE Target:\n"
                        f"                           <h4>{target}</h4></div>", unsafe_allow_html=True)
        with colB:
            try:
                actual = df_oee_daily[df_oee_daily["Date"] == today_pd]["Actual"].tolist()[0]
            except:
                actual = "Update"
            st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Plant Aggregate OEE Actual:\n"
                        f"                           <h4>{actual}</h4></div>", unsafe_allow_html=True)

        st.write("")
        st.write("Issues : ")
        st.dataframe(df_oee_issues_daily[df_oee_issues_daily["Date"] == today_pd], use_container_width=True,
                     hide_index=True)
