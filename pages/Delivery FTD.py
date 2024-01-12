import datetime
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from methods.colours import color
from methods.styles import header, horizontal_line, svg_for_ftd
import pandas as pd

header("Delivery FTD")
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
today_pd = pd.to_datetime(date)

# Getting Data
xls_sale_actual = pd.ExcelFile("Excel/Delivery/Sale_vs_actual_plan.xlsx")
df_sale_daily = pd.read_excel(xls_sale_actual, "Sale vs Actual Plan")
df_sale_issues = pd.read_excel(xls_sale_actual, "Issues")

# ************ OTIF Data Fetch ************ #
xls_OE = pd.ExcelFile("Excel/Delivery/OTIF/OE.xlsx")
xls_OE_daily = pd.read_excel(xls_OE, "Daily Data")
xls_OE_weekly = pd.read_excel(xls_OE, "Weekly Data")
xls_OE_monthly = pd.read_excel(xls_OE, "Monthly Data")

xls_OE_Spare = pd.ExcelFile("Excel/Delivery/OTIF/OE Spare.xlsx")
xls_OE_Spare_daily = pd.read_excel(xls_OE_Spare, "Daily Data")
xls_OE_Spare_weekly = pd.read_excel(xls_OE_Spare, "Weekly Data")
xls_OE_Spare_monthly = pd.read_excel(xls_OE_Spare, "Monthly Data")

xls_Aftermarket = pd.ExcelFile("Excel/Delivery/OTIF/AfterMarket.xlsx")
xls_Aftermarket_daily = pd.read_excel(xls_Aftermarket, "Daily Data")
xls_Aftermarket_weekly = pd.read_excel(xls_Aftermarket, "Weekly Data")
xls_Aftermarket_monthly = pd.read_excel(xls_Aftermarket, "Monthly Data")

xls_Export = pd.ExcelFile("Excel/Delivery/OTIF/Export.xlsx")
xls_Export_daily = pd.read_excel(xls_Export, "Daily Data")
xls_Export_weekly = pd.read_excel(xls_Export, "Weekly Data")
xls_Export_monthly = pd.read_excel(xls_Export, "Monthly Data")

# ************ Critical Customer PDI Data Fetch ************ #
xls_Ford = pd.ExcelFile("Excel/Delivery/CCPDI/Ford.xlsx")
xls_Ford_daily = pd.read_excel(xls_Ford, "Daily Data")
xls_Ford_weekly = pd.read_excel(xls_Ford, "Weekly Data")
xls_Ford_monthly = pd.read_excel(xls_Ford, "Monthly Data")

xls_GM = pd.ExcelFile("Excel/Delivery/CCPDI/GM Data.xlsx")
xls_GM_daily = pd.read_excel(xls_GM, "Daily Data")
xls_GM_weekly = pd.read_excel(xls_GM, "Weekly Data")
xls_GM_monthly = pd.read_excel(xls_GM, "Monthly Data")

xls_HD = pd.ExcelFile("Excel/Delivery/CCPDI/HD Data.xlsx")
xls_HD_daily = pd.read_excel(xls_HD, "Daily Data")
xls_HD_weekly = pd.read_excel(xls_HD, "Weekly Data")
xls_HD_monthly = pd.read_excel(xls_HD, "Monthly Data")

xls_Honda = pd.ExcelFile("Excel/Delivery/CCPDI/Honda.xlsx")
xls_Honda_daily = pd.read_excel(xls_Honda, "Daily Data")
xls_Honda_weekly = pd.read_excel(xls_Honda, "Weekly Data")
xls_Honda_monthly = pd.read_excel(xls_Honda, "Monthly Data")

xls_MSIL = pd.ExcelFile("Excel/Delivery/CCPDI/MSIL.xlsx")
xls_MSIL_daily = pd.read_excel(xls_MSIL, "Daily Data")
xls_MSIL_weekly = pd.read_excel(xls_MSIL, "Weekly Data")
xls_MSIL_monthly = pd.read_excel(xls_MSIL, "Monthly Data")

xls_RNAIPL = pd.ExcelFile("Excel/Delivery/CCPDI/RNAIPL.xlsx")
xls_RNAIPL_daily = pd.read_excel(xls_RNAIPL, "Daily Data")
xls_RNAIPL_weekly = pd.read_excel(xls_RNAIPL, "Weekly Data")
xls_RNAIPL_monthly = pd.read_excel(xls_RNAIPL, "Monthly Data")

xls_OE_daily = xls_OE_daily[xls_OE_daily['Date'] == today_pd]
xls_OE_Spare_daily = xls_OE_Spare_daily[xls_OE_Spare_daily['Date'] == today_pd]
xls_Aftermarket_daily = xls_Aftermarket_daily[xls_Aftermarket_daily['Date'] == today_pd]
xls_Export_daily = xls_Export_daily[xls_Export_daily['Date'] == today_pd]

xls_Ford_daily = xls_Ford_daily[xls_Ford_daily['Date'] == today_pd]
xls_GM_daily = xls_GM_daily[xls_GM_daily['Date'] == today_pd]
xls_HD_daily = xls_HD_daily[xls_HD_daily['Date'] == today_pd]
xls_Honda_daily = xls_Honda_daily[xls_Honda_daily['Date'] == today_pd]
xls_MSIL_daily = xls_MSIL_daily[xls_MSIL_daily['Date'] == today_pd]
xls_RNAIPL_daily = xls_RNAIPL_daily[xls_RNAIPL_daily['Date'] == today_pd]

col_main_body_1, col_main_body_2, col_main_body_3 = st.columns((2,0.5,5))

with col_main_body_1:
    # image_loader('d', height=29, top=29, left=2)
    svg_for_ftd('d', new_height=450, new_width=450, top=0, left=2)

with col_main_body_2:
    pass

with col_main_body_3:

    tab1, tab2, tab3 = st.tabs(["Plan vs Actual Sale", "OTIF", "Critical Customer PDI"])

    with tab1:
        colA, colB = st.columns((1, 1))
        with colA:
            try:
                target = df_sale_daily[df_sale_daily["Date"] == today_pd]["Budgeted Sale (B)"].tolist()[0]
            except:
                target = "Update"

            st.markdown(f"<div class=\"custom\" style='background-color:{color.blue}; color:{color.white}'>Budgeted Sale (B) :\n"
                        f"                           <h4>{target}</h4></div>", unsafe_allow_html=True)
        with colB:
            try:
                actual = df_sale_daily[df_sale_daily["Date"] == today_pd]["Actual Sale (S)"].tolist()[0]
            except Exception as e:
                actual = "Update"
            st.markdown(f"<div class=\"custom\" style='background-color:{color.skyblue};'>Actual Sale (S) :\n"
                        f"                           <h4>{actual}</h4></div>", unsafe_allow_html=True)

        st.write("")
        st.write("Issues :")
        st.dataframe(df_sale_issues[df_sale_issues["Date"] == today_pd][["Part Number", "Raise Date", "Action", "Target Date", "Status"]], hide_index=True, use_container_width=True)

    with tab2:
        sub_tab1, sub_tab2, sub_tab3, sub_tab4 = st.tabs(["OE", "OE SPARE", "AFTERMARKET", "EXPORT"])
        with sub_tab1:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    OE_target = xls_OE_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    OE_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{OE_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    OE_actual = round(xls_OE_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    OE_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{OE_actual}</h4></div>',
                            unsafe_allow_html=True)
        with sub_tab2:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    OE_Spare_target = xls_OE_Spare_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    OE_Spare_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{OE_Spare_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    OE_Spare_actual = round(xls_OE_Spare_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    OE_Spare_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{OE_Spare_actual}</h4></div>',
                            unsafe_allow_html=True)
        with sub_tab3:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    Aftermarket_target = xls_Aftermarket_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    Aftermarket_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{Aftermarket_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    Aftermarket_actual = round(xls_Aftermarket_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    Aftermarket_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{Aftermarket_actual}</h4></div>',
                            unsafe_allow_html=True)
        with sub_tab4:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    Export_target = xls_Export_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    Export_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{Export_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    Export_actual = round(xls_Export_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    Export_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{Export_actual}</h4></div>',
                            unsafe_allow_html=True)
                            
    with tab3:
        sub_tab1, sub_tab2, sub_tab3, sub_tab4, sub_tab5, sub_tab6 = st.tabs(["Ford", "GM", "HD", "Honda", "MSIL", "RNAIPL"])
        with sub_tab1:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    Ford_target = xls_Ford_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    Ford_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{Ford_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    Ford_actual = round(xls_Ford_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    Ford_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{Ford_actual}</h4></div>',
                            unsafe_allow_html=True)
        with sub_tab2:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    GM_target = xls_GM_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    GM_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{GM_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    GM_actual = round(xls_GM_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    GM_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{GM_actual}</h4></div>',
                            unsafe_allow_html=True)
        with sub_tab3:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    HD_target = xls_HD_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    HD_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{HD_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    HD_actual = round(xls_HD_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    HD_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{HD_actual}</h4></div>',
                            unsafe_allow_html=True)
        with sub_tab4:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    Honda_target = xls_Honda_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    Honda_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{Honda_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    Honda_actual = round(xls_Honda_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    Honda_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{Honda_actual}</h4></div>',
                            unsafe_allow_html=True)
        with sub_tab5:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    MSIL_target = xls_MSIL_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    MSIL_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{MSIL_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    MSIL_actual = round(xls_MSIL_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    MSIL_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{MSIL_actual}</h4></div>',
                            unsafe_allow_html=True)
        with sub_tab6:
            colA, colB = st.columns((1, 1))
            with colA:
                try:
                    RNAIPL_target = xls_RNAIPL_daily["Target"].tolist()[0]
                except Exception as e:
                    print(e)
                    RNAIPL_target = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.blue}; color:{color.white}\'>Target:\n'
                            f'                            <h4>{RNAIPL_target}</h4></div>',
                            unsafe_allow_html=True)
            with colB:
                try:
                    RNAIPL_actual = round(xls_RNAIPL_daily["Actual"].tolist()[0])
                except Exception as e:
                    print(e)
                    RNAIPL_actual = "Update"
                st.markdown(f'<div class="custom" style=\'background-color:{color.skyblue};\'>Actual :\n'
                            f'                            <h4>{RNAIPL_actual}</h4></div>',
                            unsafe_allow_html=True)

