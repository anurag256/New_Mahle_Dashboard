import datetime
from xml.etree.ElementInclude import include
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from methods.colours import color
from methods.styles import header, horizontal_line, svg_for_ftd, vertical_line

header("Quality FTD")
back = st.button("<- Back")
if back:
    switch_page("App")

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

colA, spacer, colB = st.columns((2, 2, 2))
with colA:
    date = st.date_input("Please Select The Date", value=datetime.datetime.now() - datetime.timedelta(days=1))
with (colB):
    st.write("")
    st.subheader(f"Status As on {date}")
horizontal_line()

# Setting up today's date
today_pd = pd.to_datetime(date)

# Getting Excel File
xls_complaints = pd.ExcelFile("Excel/Quality/Customer Complaints.xlsx")
xls_plant_ppm = pd.ExcelFile("Excel/Quality/Plant_PPM.xlsx")
xls_supplier_ppm = pd.ExcelFile("Excel/Quality/Supplier_PPM.xlsx")
xls_ftp = pd.ExcelFile("Excel/Quality/First_time_pass.xlsx")
xls_reported_rej = pd.ExcelFile("Excel/Quality/Reported_rejection (Per).xlsx")
xls_reported_rej_inr = pd.ExcelFile("Excel/Quality/Reported_rejection (INR).xlsx")

# Getting Complaints Data
df_customer_complaints_daily = pd.read_excel(xls_complaints, "Complaint Details").fillna("NA")
customer_complain_filtered_daily = df_customer_complaints_daily[df_customer_complaints_daily["Date"] == today_pd]

# Getting Plant PPM Data
df_plant_PPM = pd.read_excel(xls_plant_ppm, "Plant PPM")
df_plant_PPM_daily = df_plant_PPM[df_plant_PPM["Date"] == today_pd]

# Getting Issues for Plant PPM
df_plant_PPM_issues = pd.read_excel(xls_plant_ppm, "PPM Issue").fillna("NA")
df_plant_PPM_issues_daily = df_plant_PPM_issues[df_plant_PPM_issues["Date"] == today_pd]

# Function to remove commas from strings
def format_value(val):
    if isinstance(val, (int, float)):
        return f'{val:.0f}'  # Format numerical values without commas
    return val

df_plant_PPM_issues_daily = df_plant_PPM_issues_daily.map(format_value)

# Getting Supplier PPM
df_supplier_ppm = pd.read_excel(xls_supplier_ppm, "Supplier PPM").fillna("NA")
df_supplier_ppm_daily = df_supplier_ppm[df_supplier_ppm["Date"] == today_pd]

# Getting Suppliers issues
df_supplier_issues = pd.read_excel(xls_supplier_ppm, "Supplier Issue").fillna("NA")
df_supplier_issues_daily = df_supplier_issues[df_supplier_issues["Date"] == today_pd]

# Getting First Time Pass
df_ftp = pd.read_excel(xls_ftp, "First Time Pass").fillna("NA")
df_ftp_daily = df_ftp[df_ftp["Date"] == today_pd]

# ftp issues
df_ftp_issues = pd.read_excel(xls_ftp, "Issues").fillna("NA")
df_ftp_issues_daily = df_ftp_issues[df_ftp_issues["Date"] == today_pd]

# Reported rej
df_reported_rej = pd.read_excel(xls_reported_rej, "Reported Rejection Percentage").fillna("NA")
df_reported_rej_daily = df_reported_rej[df_reported_rej["Date"] == today_pd]

# Reported rejection issues
df_rej_issues = pd.read_excel(xls_reported_rej, "Issues").fillna("NA")
df_rej_issues_daily = df_rej_issues[df_rej_issues["Date"] == today_pd]

# reported Rejection INR
df_rej_inr = pd.read_excel(xls_reported_rej_inr, "Reported Rejection (INR)").fillna("NA")
df_rej_inr_daily = df_rej_inr[df_rej_inr["Date"] == today_pd]

col_main_body1, col_main_body2, col_main_body3 = st.columns((2, 0.5, 5))

with col_main_body1:
    # image_loader("q", height=30, left=1, top=25)
    svg_for_ftd("q", new_height=450, new_width=450, left=1, top=0)

with col_main_body2:
    pass

with col_main_body3:
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Complains", "Plant PPM", "Supplier PPM", "FTP", "Reported Rejection", "Reported Rejection INR"])

    with tab1:
        no_of_comp = 0
        for item in customer_complain_filtered_daily[customer_complain_filtered_daily["Complaints"] != "No Complaint"]["Complaints"]:
            no_of_comp += 1
        st.write(f"Today's Total Complaints : {no_of_comp}")
        st.dataframe(customer_complain_filtered_daily[
                         ["Complaint Description", "Raise Date", "Target Date", "Responsibility", "Status"]],
                     hide_index=True,
                     use_container_width=True)

    with tab2:
        st.write("Today's Plant PPM: ")
        colA, colB = st.columns((1, 1))
        with colA:
            try:
                ppm_target = df_plant_PPM_daily["Target"].tolist()[0]
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)
        with colB:
            try:
                ppm_target = round(df_plant_PPM_daily["Actual"].tolist()[0])
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)
        st.write("")
        st.write("Issues : ")
        st.dataframe(df_plant_PPM_issues_daily[["Issue", "Part", "Rejected Qty", "Corrective Action", "Status"]],
                     use_container_width=True,
                     hide_index=True,
                     )

    with tab3:
        st.write("Today's Supplier PPM: ")
        colA, colB = st.columns((1, 1))
        with colA:
            try:
                ppm_target = df_supplier_ppm_daily["Target"].tolist()[0]
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)
        with colB:
            try:
                ppm_target = df_supplier_ppm_daily["Actual"].tolist()[0]
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)
        st.write("")
        st.write("Issues : ")
        st.dataframe(df_supplier_issues_daily, hide_index=True, use_container_width=True)

    with tab4:
        st.write("Today's First Time Pass:")
        colA, colB = st.columns((1, 1))
        with colA:
            try:
                ppm_target = df_ftp_daily["Target"].tolist()[0]
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)
        with colB:
            try:
                ppm_target = round(df_ftp_daily["Actual"].tolist()[0])
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)

        st.write("")
        st.write("Issues : ")
        st.dataframe(df_ftp_issues_daily[["Issue", "Part", "Corrective Action", "Target Date", "Status"]], hide_index=True, use_container_width=True)

    with tab5:
        st.write("Today's Reported Rjection (%):")
        colA, colB = st.columns((1, 1))
        with colA:
            try:
                ppm_target = df_reported_rej_daily["Target"].tolist()[0]
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)
        with colB:
            try:
                ppm_target = df_reported_rej_daily["Actual"].tolist()[0]
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)

        st.write("")
        st.write("Issues : ")
        st.dataframe(df_rej_issues_daily[["Issue", "Part", "Corrective Action", "Target Date", "Status"]],
                     hide_index=True, use_container_width=True)

    with tab6:
        st.write("Today's Reported Rejection INR:")
        colA, colB = st.columns((1, 1))
        with colA:
            try:
                ppm_target = df_rej_inr_daily["Target"].tolist()[0]
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)
        with colB:
            try:
                ppm_target = df_rej_inr_daily["Actual"].tolist()[0]
            except Exception as e:
                print(e)
                ppm_target = "Update"
            st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                        f'                            <h4>{ppm_target}</h4></div>',
                        unsafe_allow_html=True)