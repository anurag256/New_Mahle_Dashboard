import datetime
from turtle import width
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from methods.styles import header, horizontal_line, svg_for_ftd, vertical_line
from methods.colours import color
import streamlit as st

xls = pd.ExcelFile("Excel/Safety/Safety.xlsx")
df_incidence_details = pd.read_excel(xls, "Safety Incidents Details").fillna(0)
df_incidence_tracking = pd.read_excel(xls, "Safety Incidents Tracking").fillna(0)

recordable_loss_time_injury: int = 0
recordable_accident: int = 0
firstaid: int = 0
near_miss: int = 0
fire: int = 0
testing: str = "Testing"

header("Safety FTD")
back = st.button("<- Back")
if back:
    switch_page("App")

# Setting up style sheet for cards
st.markdown(
    '\n'
    '            <style>\n'
    '            .custom {\n'
    '                margin: 0.4rem;\n'
    '                padding-top: 0.7rem;\n'
    '                border: 1px solid black;\n'
    '                height: 5rem;\n'
    '                border-radius: 0.7rem;\n'
    '                font-weight: bold;\n'
    '                font-size:0.7rem;\n'
    '                box-shadow: 5px 5px 10px;\n'
    '                text-align: center;\n'
    '            }\n'
    '            .custom h4{'
    f'                color:{color.white};'
    '                font-weight:bold;'
    '                padding-top:0.5rem;'
    '                }\n'
    '            \n'
    '            .heading{\n'
    '                padding:10px;\n'
    '                font-weight:bolder;\n'
    '                font-size: large;\n'
    '            }\n'
    '            .Recordable-loss-time{\n'
    '                padding : 2rem;\n'
    '                border: 1px solid black;\n'
    f'               background-color : {color.red};\n'
    '                border-radius : 30px;\n'
    f'               color: {color.black};\n'
    f'               font-size :12px;  '
    '            }\n'
    '             .name{'
    f'                color:{color.black};'
    f'                 font-weight : bolder  ;'
    '               }'
    '            }\n'
    '            .vertical1 {\n'
    '                  border-left: 3px dashed grey;\n'
    '                  height: 10rem;\n'
    '            }\n'
    '            .firstaid{\n'
    '                padding : 2rem;\n'
    '                border: 1px solid black;\n'
    f'                background-color : {color.orange};\n'
    '                border-radius : 30px;\n'
    f'               color: {color.black};\n'
    f'               font-size :12px;  '
    '            }\n'
    '            .nearMiss{\n'
    '                padding : 2rem;\n'
    '                border: 1px solid black;\n'
    f'               background-color : {color.yellow};\n'
    '                border-radius : 30px;\n'
    f'               color: {color.black};\n'
    f'               font-size :12px;  '
    '            }\n'
    '            .fire{\n'
    '                padding : 2rem;\n'
    '                border: 1px solid black;\n'
    f'               background-color : {color.maroon};\n'
    '                border-radius : 30px;\n'
    f'               color: {color.black};\n'
    f'               font-size :12px;  '
    '            }\n'
    '            .heading-1{\n'
    '                padding:35px;\n'
    '                font-weight:bolder;\n'
    '            }\n'
    '            .heading-2{\n'
    '                padding:35px;\n'
    '                font-weight:bolder;\n'
    '            }\n'
    '            </style>\n'
    '            ',
    unsafe_allow_html=True)

sub_col_1, sub_col_spacer, sub_col_2 = st.columns((4, 4, 5))
with sub_col_1:
    date = st.date_input(label="Select Date To View Status", value = datetime.datetime.now().date()-datetime.timedelta(days=1))
    # print(date)
with sub_col_2:
    st.write("")
    st.subheader(f"Satus As On : {date}")

horizontal_line()

# Getting daily Data
# for cards
today = pd.to_datetime(f"{date}")
df_daily_tracking = df_incidence_tracking[df_incidence_tracking["Date"] == today]
try:
    recordable_loss_time_injury = int(df_daily_tracking["Recordable Lost Time Injury FTD"].tolist()[0])
    recordable_accident = int(df_daily_tracking["Recordable Accident FTD"].tolist()[0])
    firstaid = int(df_daily_tracking["First Aid FTD"].tolist()[0])
    near_miss = int(df_daily_tracking["Near Miss FTD"].tolist()[0])
    fire = int(df_daily_tracking["Fire FTD"].tolist()[0])
except:
    recordable_loss_time_injury = 0
    recordable_accident = 0
    firstaid = 0
    near_miss = 0
    fire = 0

#  for labels
df_incidence_daily = df_incidence_details[df_incidence_details["Date"] == today]
# print(df_incidence_daily[["Incident"]])

incident_lost = " "
location_lost = " "
medical_lost = " "
time_lost = " "
action_lost = " "

incident_first = " "
location_fist = " "
medical_first = " "
time_fist = " "
action_first = " "

incident_near = " "
location_near = " "
medical_near = " "
time_near = " "
action_near = " "

incident_fire = " "
location_fire = " "
medical_fire = " "
time_fire = " "
action_fire = " "

if (df_incidence_daily['Category'] == 'Lost time Injury & Recordable Accident').any():
    incident_lost =  df_incidence_daily[["Incident"]]["Incident"].to_list()[0]
    location_lost = df_incidence_daily[["Plant Area"]]["Plant Area"].to_list()[0]
    medical_lost = df_incidence_daily[["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
    time_lost = df_incidence_daily[["Time"]]["Time"].to_list()[0]
    action_lost = df_incidence_daily[["Preventinve measures implemented and lessons learnt"]]["Preventinve measures implemented and lessons learnt"].to_list()[0]
else:
    incident_lost = "None"
    location_lost = "None"
    medical_lost = "None"
    time_lost = "None"
    action_lost = "None"
    
if (df_incidence_daily['Category'] == 'First Aid').any():
    incident_first = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Incident"]]["Incident"].to_list()[0]
    location_fist = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Plant Area"]]["Plant Area"].to_list()[0]
    medical_first = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
    time_fist = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Time"]]["Time"].to_list()[0]
    action_first = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Preventinve measures implemented and lessons learnt"]]["Preventinve measures implemented and lessons learnt"].to_list()[0]
else:
    incident_first = "None"
    location_fist = "None"
    medical_first = "None"
    time_fist = "None"
    action_first = "None"

if (df_incidence_daily['Category'] == 'Near Miss').any():
    incident_near = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Incident"]]["Incident"].to_list()[0]
    location_near = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Plant Area"]]["Plant Area"].to_list()[0]
    medical_near = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
    time_near = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Time"]]["Time"].to_list()[0]
    action_near = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Preventinve measures implemented and lessons learnt"]]["Preventinve measures implemented and lessons learnt"].to_list()[0]
else:
    incident_near = "None"
    location_near = "None"
    medical_near = "None"
    time_near = "None"
    action_near = "None"

if (df_incidence_daily['Category'] == 'Fire').any():
    incident_fire = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Incident"]]["Incident"].to_list()[0]
    location_fire = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Plant Area"]]["Plant Area"].to_list()[0]
    medical_fire = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
    time_fire = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Time"]]["Time"].to_list()[0]
    action_fire = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Preventinve measures implemented and lessons learnt"]]["Preventinve measures implemented and lessons learnt"].to_list()[0]
else:
    incident_fire = "None"
    location_fire = "None"
    medical_fire = "None"
    time_fire = "None"
    action_fire = "None"

# print(incident_near)

# try:
#     incident_lost = df_incidence_daily["Incident"].tolist()[0]
#     location_lost = df_incidence_daily["Plant Area"].tolist()[0]
#     medical_lost = df_incidence_daily["Medical Aid Given"].tolist()[0]
#     time_lost = df_incidence_daily["Time"].tolist()[0]
#     action_lost = df_incidence_daily["Preventinve measures implemented and lessons learnt"].tolist()[0]

#     incident_first = df_incidence_daily["Incident"].tolist()[1]
#     location_fist = df_incidence_daily["Plant Area"].tolist()[1]
#     medical_first = df_incidence_daily["Medical Aid Given"].tolist()[1]
#     time_fist = df_incidence_daily["Time"].tolist()[1]
#     action_first = df_incidence_daily["Preventinve measures implemented and lessons learnt"].tolist()[1]

#     incident_near = df_incidence_daily["Incident"].tolist()[2]
#     location_near = df_incidence_daily["Plant Area"].tolist()[2]
#     medical_near = df_incidence_daily["Medical Aid Given"].tolist()[2]
#     time_near = df_incidence_daily["Time"].tolist()[2]
#     action_near = df_incidence_daily["Preventinve measures implemented and lessons learnt"].tolist()[2]

#     incident_fire = df_incidence_daily["Incident"].tolist()[3]
#     location_fire = df_incidence_daily["Plant Area"].tolist()[3]
#     medical_fire = df_incidence_daily["Medical Aid Given"].tolist()[3]
#     time_fire = df_incidence_daily["Time"].tolist()[3]
#     action_fire = df_incidence_daily["Preventinve measures implemented and lessons learnt"].tolist()[3]
# except:
#     incident_lost = "None"
#     location_lost = "None"
#     medical_lost = "None"
#     time_lost = "None"
#     action_lost = "None"

#     incident_first = "None"
#     location_fist = "None"
#     medical_first = "None"
#     time_fist = "None"
#     action_first = "None"

#     incident_near = "None"
#     location_near = "None"
#     medical_near = "None"
#     time_near = "None"
#     action_near = "None"

card1, card2, card3, card4, card5 = st.columns((1, 1, 1, 1, 1))

with card1:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.red};'>Lost Time Injury :\n"
                f"                            <h4>{recordable_loss_time_injury}</h4></div>", unsafe_allow_html=True)
with card2:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.pink};'>Recordable Accident :\n"
                f"                            <h4>{recordable_accident}</h4></div>", unsafe_allow_html=True)
with card3:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.maroon};'>Fire :\n"
                f"                           <h4>{fire}</h4></div>", unsafe_allow_html=True)
with card4:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.orange};'>First Aid:\n"
                f"                           <h4>{firstaid}</h4></div>", unsafe_allow_html=True)
with card5:
    st.markdown(f"<div class=\"custom\" style='background-color:{color.yellow};'>Near Miss :\n"
                f"                           <h4>{near_miss}</h4></div>", unsafe_allow_html=True)

col_main_body1, col_main_body_2, col_main_body_3 = st.columns((2,0.5,5))
with col_main_body1:
    svg_for_ftd(letter="s", new_height=450, new_width=450, left=-2, top=0)

with col_main_body_2:
    pass

with col_main_body_3:
    st.write("")
    st.write("<div class= \"heading\">\n"
             "    Recordable Loss Time Injury\n"
             "</div>", unsafe_allow_html=True)
    st.markdown("\n"
                "           <div class= \"Recordable-loss-time\">\n"
                f"                <span class='name'>Incident :</span> {incident_lost} <br>\n"
                f"                 <span class='name'>Time :</span> {time_lost} <br>\n"
                f"                 <span class='name'>Location :</span> {location_lost}<br> \n"
                f"                 <span class='name'>Medical :</span> {medical_lost}<br>\n"
                f"                 <span class='name'>Preventive Measure :</span> {action_lost}<br> \n"
                "            </div>\n"
                "\n", unsafe_allow_html=True)
    st.write("<div class= \"heading\">\n"
             "    First Aid\n"
             "</div>", unsafe_allow_html=True)
    st.markdown("\n"
                "           <div class= \"firstaid\">\n"
                f"                <span class='name'>Incident :</span>{incident_first} <br>\n"
                f"                 <span class='name'>Time :</span> {time_fist} <br>\n"
                f"                 <span class='name'>Location :</span> {location_fist}<br> \n"
                f"                 <span class='name'>Medical :</span> {medical_first}<br>\n"
                f"                 <span class='name'>Preventive Measure :</span> {action_first}<br> \n"
                "            </div>\n"
                "\n", unsafe_allow_html=True)
    st.write("<div class= \"heading\">\n"
             "    Near Miss\n"
             "</div>", unsafe_allow_html=True)
    st.markdown("\n"
                "           <div class= \"nearMiss\">\n"
                f"                <span class='name'>Incident :</span> {incident_near} <br>\n"
                f"                 <span class='name'>Time :</span> {time_near} <br>\n"
                f"                 <span class='name'>Location :</span> {location_near}<br> \n"
                f"                 <span class='name'>Medical :</span> {medical_near}<br>\n"
                f"                 <span class='name'>Preventive Measure :</span> {action_near}<br> \n"
                "            </div>\n"
                "\n", unsafe_allow_html=True)
    st.write("<div class= \"heading\">\n"
             "    Fire\n"
             "</div>", unsafe_allow_html=True)
    st.markdown("\n"
                "           <div class= \"fire\">\n"
                f"                <span class='name'>Incident :</span> {incident_fire} <br>\n"
                f"                 <span class='name'>Time :</span> {time_fire} <br>\n"
                f"                 <span class='name'>Location :</span> {location_fire}<br> \n"
                f"                 <span class='name'>Medical :</span> {medical_fire}<br>\n"
                f"                 <span class='name'>Preventive Measure :</span> {action_fire}<br> \n"
                "            </div>\n"
                "\n", unsafe_allow_html=True)
    st.write("")
