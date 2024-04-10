import datetime
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from methods.SVG_generator import new_svg_gen, svg_gen
from methods.styles import header, vertical_line, image_loader, horizontal_line, sub_heading, new_svg_loader
from threading import Thread
import pandas as pd
import logging
from colorlog import ColoredFormatter
from methods.colours import color
from methods.data_filter import monthlyData

# CREATING LOGGER
log = logging.getLogger('example_logger')
log.setLevel(logging.DEBUG)
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-s:%(lineno)-s%(reset)s %(blue)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# Fetching Data Safety
xls = pd.ExcelFile("Excel/Safety/Safety.xlsx")
S_svg = pd.read_excel(xls, "S")
df_plant_running = pd.read_excel(xls, "Plant Running")
safety_monthly = monthlyData(S_svg)

# Fetching Data Quality
xls_quality = pd.ExcelFile("Excel/Quality/Customer Complaints.xlsx")
Q_svg = pd.read_excel(xls_quality, "Q")
df_complaint_since = pd.read_excel(xls_quality, "Complaint Since")
quality_monthly = monthlyData(Q_svg)
# print('check data')
# print(quality_monthly)

# Fetching Cost Data
xls_cost = pd.ExcelFile("Excel/Cost/Cost.xlsx")
C_svg = pd.read_excel(xls_cost, "C")
df_cost_since = pd.read_excel(xls_cost, "Days Since")
cost_monthly = monthlyData(C_svg)
# print(C_svg)

# Fetching Delivery Data
xls_delivery = pd.ExcelFile("Excel/Delivery/Delivery.xlsx")
D_svg = pd.read_excel(xls_delivery, "D")
df_delivery_since = pd.read_excel(xls_delivery, "Days Since")
# print(df_delivery_since)
delivery_monthly = monthlyData(D_svg)

# print(safety_monthly)
today = datetime.datetime.now() - datetime.timedelta(days=1)
today_pd = pd.to_datetime(today.date())
# print(today, today_pd)
# noinspection PyBroadException

# print(df_delivery_since[df_delivery_since["Date"] == today_pd])

try:
    plant_running_without_lost_time = int(df_plant_running[df_plant_running["Date"] == today_pd]["Plant Running Since"].tolist()[0])
except Exception as e:
    plant_running_without_lost_time = "Update"

# noinspection PyBroadException
try:
    customer_comp_since = int(df_complaint_since[df_complaint_since["Date"] == today_pd]["Complaint Since Days"].tolist()[0])
except Exception as e:
    customer_comp_since = "Update"

# noinspection PyBroadException
try:
    cost_since = int(df_cost_since[df_cost_since["Date"] == today_pd]["Days Since"].tolist()[0])
except:
    cost_since = "Update"

# noinspection PyBroadException
try:
    delivery_since = int(df_delivery_since[df_delivery_since["Date"] == today_pd]["Days since"].tolist()[0])
except Exception as e:
    print(e)
    delivery_since = "Update"

header(name="Shopfloor Management Dashboard")
# making main body columns
main_body_col1, main_body_col_spacer, main_body_col2 = st.columns((5, 0.1, 2))

with main_body_col1:
    color_dict = {"s": [], "q": [], "d": [], "c": []}
    for item in safety_monthly["Category"]:
        # print(f"Incident: {item}")
        if item == "No Accident":
            color_dict["s"].append(color.green)
        if item == "Plant off":
            color_dict["s"].append(color.plant_off)
        if item == "Lost Time Injury":
            color_dict["s"].append(color.red)
        if item == "Recordable accident":
            color_dict["s"].append(color.pink)
        if item == "First Aid":
            color_dict["s"].append(color.orange)
        if item == "Near Miss":
            color_dict["s"].append(color.yellow)
        if item == "Fire":
            color_dict["s"].append(color.maroon)

    for item in quality_monthly["Complaints"]:
        if item == "No Complaint":
            color_dict["q"].append(color.green)
        if item == "Plant off":
            color_dict["q"].append(color.plant_off)
        if item == "Complaint":
            color_dict["q"].append(color.red)

    for item in cost_monthly["Cost_Target"]:
        if item == "Achieved":
            color_dict["c"].append(color.green)
        if item == "Plant off":
            color_dict["c"].append(color.plant_off)
        if item == "Not Achieved":
            color_dict["c"].append(color.red)

    for item in delivery_monthly["Delivery Target"]:
        if item == "Achieved":
            color_dict["d"].append(color.green)
        if item == "Plant off":
            color_dict["d"].append(color.plant_off)
        if item == "Not Achieved":
            color_dict["d"].append(color.red)

    # print(color_dict["q"]) 
    # print(quality_monthly["Date"])
    image_list = ['s', 'q', 'd', 'c']
    for image in image_list:
        # print(color_dict[f"{image}"], f"{image}")
        th = Thread(target=lambda: new_svg_gen(color_dict[f"{image}"], f"{image}"))
        th.start()
        th.join()

    image_col1, image_col_spacer, image_col2 = st.columns((2, 0.1, 2))
    with image_col1:
        sub_heading("Safety")
        # image_loader(name="s", left=15, top=-1.5)
        new_svg_loader(name="s", left=15, top=-13, height=210, width=215)
        st.write("\n"
                 "                <center>\n"
                 "                <span style = \"font-size:56px;\"> </span>\n"
                f"                    <div class = \"custom-font\"><b>{plant_running_without_lost_time}</b> days without lost time injury.<div>\n"
                 "                </center>\n"
                 "                <style>\n"
                 "                    .custom-font{\n"
                 "                    font-size : 14px;\n"
                 "                    position : relative;\n"
                 "                    bottom : 1.7rem;\n"
                 "                    }\n"
                 "                .st-emotion-cache-1yr3x52{\n"
                 "                    position : absolute;\n"
                 "                }\n"
                 "                .st-emotion-cache-adlo16:nth-child(22){margin-bottom: -2rem;}\n"
                 "                </style>\n"
                 "            ", unsafe_allow_html=True)
        horizontal_line()
        sub_heading("Delivery")
        # image_loader(name="d", height=20, top=1, left=15)
        new_svg_loader(name="d", top=-13, left=15, height=210, width=215)
        st.write("\n"
                 "            <center>\n"
                 f"                <div class = \"custom-font\"><b>{delivery_since}</b> days since OE delivery Failure</div>\n"
                 "            </center>\n"
                 "        ", unsafe_allow_html=True)

    with image_col_spacer:
        vertical_line(height=37)

    with image_col2:
        sub_heading(
            "Quality"
        )
        # image_loader(name="q", height=13, top=0, left=15)
        new_svg_loader(name="q", top=-13, left=15, height=205, width=215)
        st.write("\n"
                 "                    <center>\n"
                 f"                        <div class = \"custom-font-1\"><b>{customer_comp_since}</b> days since Customer Complaints</div>\n"
                 "                    </center>\n"
                 "                    <style>\n"
                 "                        .custom-font-1{\n"
                 "                            font-size : 14px;\n"
                 "                            position : relative;\n"
                 "                            bottom : 1.7rem;\n"
                 "                        }\n"
                 "                    </style>\n"
                 "                ", unsafe_allow_html=True)
        horizontal_line()
        sub_heading("Cost")
        # image_loader(name="c", height=12, left=15, top=0)
        new_svg_loader(name="c", left=15, top=-13, height=210, width=215)
        st.write("\n"
                 "                    <center>\n"
                 f"                        <div class = \"custom-font\"><b>{cost_since}</b> days since Productivity Target Missed</div>\n"
                 "                    </center>\n"
                 "                ", unsafe_allow_html=True)

with main_body_col_spacer:
    vertical_line(height=37)

with main_body_col2:
    st.markdown(
        f"""<center><div style='background-color:{color.light_grey}; width:100%; font-weight:bold;'>KPI Information</div></center>""",
        unsafe_allow_html=True)
    st.markdown("<style>\n"
                "                            .st-emotion-cache-115gedg:nth-child(1){ bottom:0rem; }\n"
                "                            .st-emotion-cache-115gedg:nth-child(2){ position:relative; bottom:1.7rem; }\n"
                "                            .st-emotion-cache-1r6slb0:nth-child(1){ bottom:0.5rem; }\n"
                "                            .st-emotion-cache-ocqkz7{ height:3rem }\n"
                "                            .element-container:nth-child(25){position: absolute;}"
                "                        </style>", unsafe_allow_html=True)

    col_icon, col_selector = st.columns((1, 2))
    with col_icon:
        st.image("resources/Icons/info_1.svg", width=46)
    with col_selector:
        generalInfo = st.selectbox("General Information", [
            "General Information", "Ground rule of meeting"], index=None, placeholder="General Information",
                                   label_visibility="hidden")
    col_icon, col_selector = st.columns((1, 2))
    with col_icon:
        st.image("resources/Icons/safety.svg", width=50)
    with col_selector:
        safetySelection = st.selectbox("Safety",
                                       ["Safety FTD", "Safety Incidents Tracking", "Unsafe Practice Tracking"],
                                       key="safety", index=None, placeholder="Safety", label_visibility="hidden")
    col_icon, col_selector = st.columns((1, 2))
    with col_icon:
        # st.markdown("<br>", unsafe_allow_html=True)
        st.image("resources/Icons/quality.svg", width=50)
    with col_selector:
        qualitySelection = st.selectbox("Quality", ["Quality FTD", "Customer Complaints", "Plant PPM & Supplier PPM",
                                                    "FTP and Reported Rejection"],
                                        key="quality", index=None, placeholder="Quality", label_visibility="hidden")
    col_icon, col_selector = st.columns((1, 2))
    with col_icon:
        st.image("resources/Icons/delivery.svg", width=50)
    with col_selector:
        # "Critical Customer PDI",
        deliverySelection = st.selectbox("Delivery",
                                         ["Delivery FTD", "Sale Plan vs Actual", "OTIF"],   # , "Critical Customer PDI"
                                         key='personal', index=None, placeholder="Delivery", label_visibility="hidden")

    col_icon, col_selector = st.columns((1, 2))
    with col_icon:
        st.image("resources/Icons/cost.svg", width=50)
    with col_selector:
        #
        costSelection = st.selectbox("Cost", ["Cost FTD", "Productivity and OEE", "Machine Breakdown Time"],
                                     key='delivery', index=None, placeholder="Cost",
                                     label_visibility="hidden")

    col_icon, col_selector = st.columns((1, 2))
    with col_icon:
        st.image("resources/Icons/psp.svg", width=50)

    with col_selector:
        PSP = st.selectbox("PSP", [
            "Problem Solving", "Layer Audit Action Points"], index=None, placeholder="PSP", label_visibility="hidden")

    col_icon, col_selector = st.columns((1, 2))
    with col_icon:
        # st.markdown("<br>", unsafe_allow_html=True)
        st.image("resources/Icons/personal.svg", width=50)
    with col_selector:
        personalSelection = st.selectbox("Personnel", [
            "Headcount", "Visits/Audits"], key='cost', index=None, placeholder="Personnel",
                                         label_visibility="hidden")

    # col_icon, col_selector = st.columns((1, 2))
    # with col_selector:
    #     pass
    
    col1, col2 = st.columns((1,1.5))
    with col1:
        pass
    with col2:
        st.write('')
        st.write('')
        st.write('')
        st.image("resources/Icons/mahle.svg", width=180)

match generalInfo:
    case "General Information":
        switch_page("General_info")
    case "Ground rule of meeting":
        switch_page("Ground Rule Of Meeting")

match safetySelection:
    case "Safety FTD":
        switch_page("Safety FTD")
    case "Safety Incidents Tracking":
        switch_page("Safety Incident Tracking")
    case "Unsafe Practice Tracking":
        switch_page("Unsafe Practice Tracking")

match qualitySelection:
    case "Quality FTD":
        switch_page("Quality FTD")
    case "Customer Complaints":
        switch_page("Customer Complaints")
    case "Plant PPM & Supplier PPM":
        switch_page("Plant and Supplier PPM")
    case "FTP and Reported Rejection":
        switch_page("FTP and Reported Rejection")

match costSelection:
    case "Cost FTD":
        switch_page("Cost FTD")
    case "Productivity and OEE":
        switch_page("Productivity and OEE")
    case "Machine Breakdown Time":
        switch_page("Machine Breakdown Time")

match deliverySelection:
    case "Delivery FTD":
        switch_page("Delivery FTD")
    case "Sale Plan vs Actual":
        switch_page("Sale Plan Vs Actual")
    case "OTIF":
        switch_page("OTIF")
    # case "Critical Customer PDI":
    #     switch_page("Critical Customer PDI")

match personalSelection:
    case "Headcount":
        switch_page("Personal Gap")
    case "Visits/Audits":
        switch_page("Audits")

match PSP:
    case "Problem Solving":
        switch_page("Problem Solving")
    case "Layer Audit Action Points":
        switch_page("Layer Audit Points")