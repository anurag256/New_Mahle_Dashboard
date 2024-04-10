from duckdb import df
import streamlit as st
import base64
from methods.colours import color
import datetime
import pandas as pd
import streamlit.components.v1 as stcomp
from streamlit_extras.switch_page_button import switch_page


def header(name: str):
    st.set_page_config(layout="wide", page_title=f"{name}",
                       initial_sidebar_state="collapsed")
    st.markdown(
        "<style>.block-container { padding: 0.5rem; }</style>", unsafe_allow_html=True)

    hide_streamlit_style = ("<style>\n"
                            "    #MainMenu { visibility: hidden;}footer { visibility: hidden;}\n"
                            "    #MainMenu { visibility: hidden;}footer { visibility: hidden;}\n"
                            "    .st-emotion-cache-18ni7ap:nth-child(1), .st-emotion-cache-10zg0a4:nth-child(1){\n"
                            "            display: none;\n"
                            "            position: absolute;\n"
                            "        }"
                            "</style>")

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    # st.markdown(("\n"
    #                 "            <center>\n"
    #                 "                <div style=\"margin-bottom:0.6rem; background-color:darkblue; font-family:fantasy;\"><i><h1 style='color:white';>heading</h1></i></div>\n"
    #                 "            </center>").replace("heading", str(name)), unsafe_allow_html=True
    #                 )
    col1,col2 = st.columns((15,1))
    with col1:
        st.markdown(("\n"
                    "            <center>\n"
                    "                <div style=\"margin-bottom:0.6rem; background-color:darkblue; font-family:fantasy;\"><i><h1 style='color:white';>heading</h1></i></div>\n"
                    "            </center>").replace("heading", str(name)).replace("darkblue",str(color.blue)), unsafe_allow_html=True
                    )
    with col2:
        st.image("resources/Icons/Home.svg", width=62)
        st.markdown("""
            <style>
                .st-emotion-cache-1k67eer:nth-child(2){
                    position: relative;
                    bottom: 0rem;
                    right: 0rem;
                }
            </style>
        """, unsafe_allow_html=True)

    # st.markdown("""
    #         <style>
    #             .st-emotion-cache-1v0mbdj{
    #                 position: relative;
    #                 top: 0.5rem;
    #             }
    #         </style>
    #     """, unsafe_allow_html=True)
    
    # .st-emotion-cache-17nsjxc, .st-emotion-cache-ahgcz3, .st-emotion-cache-ab3tl4{
    #     position:relative;
    #     top: 0rem;
    # }
    # .st-emotion-cache-1gr9gcu
    st.write("\n"
             "            <style>\n"
             "            .st-emotion-cache-1now2ym:nth-child(1), .st-emotion-cache-hsah5s:nth-child(1){\n"
             "                display: none;\n"
             "                position: absolute;\n"
             "            }\n"
             "            .st-emotion-cache-1now2ym:nth-child(1), .st-emotion-cache-hsah5s:nth-child(1){\n"
             "            display: none;\n"
             "            position: absolute;\n"
             "            }\n"
             "            </style>\n"
             "        ", unsafe_allow_html=True)
    st.write("")
#.st-emotion-cache-ocqkz7:nth-child(0){ position:relative; bottom:1rem; }

def vertical_line(height: int):
    st.markdown(("\n"
                 "          <style>\n"
                 "           .vertical1 {\n"
                 "             border-left: 3px dashed grey;\n"
                 "             height: $$rem;\n"
                 "             top: 1px;\n"
                 "             position:absolute;\n"
                 "             left: 50%;\n"
                 "           }\n"
                 "         </style>\n"
                 "           <div class=\"vertical1\">\n"
                 "           </div>\n"
                 "           ").replace("$$", f"{height}"), unsafe_allow_html=True)


def horizontal_line(color_main=color.light_grey):
    st.markdown("\n"
                "           <style>\n"
                "           .horizontal1 {\n"
                f"               border-bottom: 3px dashed {color_main};\n"
                "               position: relative;\n"
                "               top: 0rem;\n"
                "               margin: 0.5rem 0rem;\n"
                "           }\n"
                "           </style>\n"
                "           <div class=\"horizontal1\">\n"
                "           </div>\n"
                "       ", unsafe_allow_html=True)


def image_loader(name: str, height: float = 12, left: float = 12, top: float = 1):
    html_ftd = None
    try:
        with open(f'resources/SVG-out/{name}.svg', 'r') as f:
            svg = f.read()
            b64 = base64.b64encode(svg.encode('utf-8')).decode('utf-8')
            match name:
                case "s":
                    html_ftd = r'<img src="data:image/svg+xml;base64,%s" class ="custom-image-s"/>' % b64
                    st.write(("\n"
                              "                <style>\n"
                              "                    .custom-image-s{\n"
                              "                        height : $$rem;\n"
                              "                         margin-top: -1.5rem;"
                              "                    }\n"
                              "                </style>\n"
                              "            ").replace("$$", f"{height}"), unsafe_allow_html=True)
                case "q":
                    html_ftd = r'<img src="data:image/svg+xml;base64,%s" class ="custom-image-q"/>' % b64
                    st.write(("\n"
                              "                <style>\n"
                              "                    .custom-image-q{\n"
                              "                        height : $$rem;\n"
                              "                         margin-top:-1.2rem;"
                              "                    }\n"
                              "                </style>\n"
                              "            ").replace("$$", f"{height}"), unsafe_allow_html=True)
                case "c":
                    html_ftd = r'<img src="data:image/svg+xml;base64,%s" class ="custom-image-c"/>' % b64
                    st.write(("\n"
                              "                <style>\n"
                              "                    .custom-image-c{\n"
                              "                        height : $$rem;\n"
                              "                        margin-top:-0.9rem;"
                              "                    }\n"
                              "                </style>\n"
                              "            ").replace("$$", f"{height}"), unsafe_allow_html=True)
                case "d":
                    html_ftd = r'<img src="data:image/svg+xml;base64,%s" class ="custom-image-d"/>' % b64
            st.write(("\n"
                      "                <style>\n"
                      "                    .custom-image-d{\n"
                      "                        height : $$rem;\n"
                      "                    }\n"
                      "                </style>\n"
                      "            ").replace("$$", f"{height}"), unsafe_allow_html=True)
        if name == "s":
            st.write(f"\n"
                     f"                             <style>\n"
                     f"                                .s{{ font-size:0.6rem; margin:5rem; position:absolute; font-weight:bold;}}\n"
                     f"                             </style>\n"
                     f"                             <div>{html_ftd}\n"
                     f"                                <p class=\"s\" style='left:{left}rem; top:{top}rem; color:{color.black};'>LEGEND:</p>\n"
                     f"                                <p class=\"s\" style='left:{left}rem; top:{top + 1.5}rem; color:{color.red};'>LOST TIME INCIDENT</p>\n"
                     f"                                <p class=\"s\" style='left:{left}rem; top:{top + 3}rem; color:{color.pink};'>RECORDABLE ACCIDENT</p>\n"
                     f"                                <p class=\"s\" style='left:{left}rem; top:{top + 4.5}rem; color:{color.maroon};'>FIRE</p>\n"
                     f"                                <p class=\"s\" style='left:{left}rem; top:{top + 6}rem; color:{color.orange};'>FIRST AID</p>\n"
                     f"                                <p class=\"s\" style='left:{left}rem; top:{top + 7.5}rem; color:{color.yellow};'>NEAR MISS</p>\n"
                     f"                                <p class=\"s\" style='left:{left}rem; top:{top + 9}rem; color:{color.green};'>NO INCIDENT</p>\n"
                     f"                                <p class=\"s\" style='left:{left}rem; top:{top + 10.5}rem; color:{color.plant_off};'>PLANT OFF</p>\n"
                     f"                                 <br>"
                     f"                                  <br>"
                     f"                             </div>", unsafe_allow_html=True)
        else:
            st.write(f"\n"
                     f"                    <style>\n"
                     f"                        .s{{ font-size:0.6rem; margin:0rem; position:absolute; font-weight:bold;}}\n"
                     f"                    </style>\n"
                     f"                    <div>{html_ftd}\n"
                     f"                        <p class=\"s\" style='left:{left}rem; top:{top}rem; color:{color.black};'>LEGEND:</p>\n"
                     f"                        <p class=\"s\" style='left:{left}rem; top:{top + 1.5}rem; color:{color.green};'>TARGET ACHIEVED</p>\n"
                     f"                        <p class=\"s\" style='left:{left}rem; top:{top + 3}rem; color:{color.red};'>TARGET MISSED</p>\n"
                     f"                        <p class=\"s\" style='left:{left}rem; top:{top + 4.5}rem; color:{color.plant_off};'>PLANT OFF</p>\n"
                     f"                         <br>"
                     f"                    </div>", unsafe_allow_html=True)

    except Exception as e:
        st.write(f"Can't load the image -- {e} ")

def selected_date():
    return st.date_input("Please Select Month and Year (Any Date)",
            value=datetime.datetime.now())# - datetime.timedelta(days=1))

def back_btn():
    back = st.button("<- Back")
    if back:
        switch_page("App")

def sub_heading(name: str):
    st.markdown(
        f"<center><div style='background-color:{color.light_grey}; width:95%; font-weight:bold;'>{name}</div></center>",
        unsafe_allow_html=True)



# Get Data from excel files
df_xl = pd.ExcelFile("Excel/Safety/Safety.xlsx")
s1 = pd.read_excel(df_xl, 'Safety Incidences')
safety_df = pd.DataFrame(s1)

df_xl = pd.ExcelFile("Excel/Quality/Customer Complaints.xlsx")
s1 = pd.read_excel(df_xl, 'Complaint Details')
complaint_df = pd.DataFrame(s1)

df_xl = pd.ExcelFile("Excel/Delivery/Delivery.xlsx")
s1 = pd.read_excel(df_xl, 'D')
delivery_df = pd.DataFrame(s1)

df_xl = pd.ExcelFile("Excel/Cost/Cost.xlsx")
s1 = pd.read_excel(df_xl, 'C')
cost_df = pd.DataFrame(s1)

#*********** Load Data and combine with SVG ***********#
def my_alert(day, letter: str):
    # Get Date on click
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    new_date = f"{current_year}-{current_month:02d}-{day:02d}"

    match letter:
        case 's':
            # Filter Data according to the date which was click
            df_incidence_daily = safety_df[safety_df['Date'] == new_date]

            incident = " "
            # location = " "
            # medical = " "
            # time = " "
            action = " "

            if (df_incidence_daily['Category'] == 'Lost time Injury & Recordable Accident').any():
                incident =  df_incidence_daily[["Incident"]]["Incident"].to_list()[0]
                # location = df_incidence_daily[["Plant Area"]]["Plant Area"].to_list()[0]
                # medical = df_incidence_daily[["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
                # time = df_incidence_daily[["Time"]]["Time"].to_list()[0]
                action = df_incidence_daily[["Action"]]["Action"].to_list()[0]
            
            elif (df_incidence_daily['Category'] == 'First Aid').any():
                incident = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Incident"]]["Incident"].to_list()[0]
                # location = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Plant Area"]]["Plant Area"].to_list()[0]
                # medical = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
                # time = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Time"]]["Time"].to_list()[0]
                action = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Action"]]["Action"].to_list()[0]

            elif (df_incidence_daily['Category'] == 'Near Miss').any():
                incident = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Incident"]]["Incident"].to_list()[0]
                # location = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Plant Area"]]["Plant Area"].to_list()[0]
                # medical = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
                # time = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Time"]]["Time"].to_list()[0]
                action = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Action"]]["Action"].to_list()[0]

            elif (df_incidence_daily['Category'] == 'Fire').any():
                incident = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Incident"]]["Incident"].to_list()[0]
                # location = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Plant Area"]]["Plant Area"].to_list()[0]
                # medical = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
                # time = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Time"]]["Time"].to_list()[0]
                action = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Action"]]["Action"].to_list()[0]
            
            else:
                incident = " "
                # location = " "
                # medical = " "
                # time = " "
                action = " "
            
            return f"""
                function(){{
                    swal.fire({{html: `<h5>Date: {new_date}</h5><b style='color:{color.red};'>Incident: </b> <p>{incident}</p> <b style='color:{color.green};'>Action: </b> <p>{action}</p>`}});
                }}
            """

        case 'q':
            # Filter Data according to the date which was click
            df_complaint_daily = complaint_df[complaint_df['Date'] == new_date]

            complaint = " "
            # raise_date = " "
            # target_date = " "
            # responsibility = " "
            action = " "

            if (df_complaint_daily['Complaints'] == 'Complaint').any():
                complaint = df_complaint_daily[['Complaint Description']]['Complaint Description'].to_list()[0]
                # raise_date = df_complaint_daily[['Raise Date']]['Raise Date'].to_list()[0]
                # target_date = df_complaint_daily[['Target Date']]['Target Date'].to_list()[0]
                # responsibility = df_complaint_daily[['Responsibility']]['Responsibility'].to_list()[0]
                action = df_complaint_daily[['Action']]['Action'].to_list()[0]
            else:
                complaint = ' '
                # raise_date = ' '
                # target_date = ' '
                # responsibility = ' '
                action = ' '

            return f"""
                function(){{
                    swal.fire({{html: `<h5>Date: {new_date}</h5><b style='color:{color.red};'>Complaint: </b> <p>{complaint}</p> <b style='color:{color.green};'>Action: </b> <p>{action}</p>`}});
                }}
            """
        case 'd':
            d_reason = ' '
            d_action = ' '
            
            # Filter Data according to the date which was click
            df_delivery_daily = delivery_df[delivery_df['Date'] == new_date]
            if (df_delivery_daily['Delivery Target'] == 'Not Achieved').any():
                d_reason = df_delivery_daily[['Description']]['Description'].to_list()[0]
                d_action = df_delivery_daily[['Action']]['Action'].to_list()[0]
            else:
                d_reason = ' '
                d_action = ' '

            return f"""
                function(){{
                    swal.fire({{html: `<h5>Date: {new_date}</h5><b style='color:{color.red};'>Description: </b> <p>{d_reason}</p> <b style='color:{color.green};'>Action: </b> <p>{d_action}</p>`}});
                }}
            """

        case 'c':
            c_reason = ' '
            c_action = ' '

            # Filter Data according to the date which was click
            df_cost_daily = cost_df[cost_df['Date'] == new_date]

            if (df_cost_daily['Cost_Target'] == 'Not Achieved').any():
                c_reason = df_cost_daily[['Description']]['Description'].to_list()[0]
                c_action = df_cost_daily[['Action']]['Action'].to_list()[0]
            else:
                c_reason = ' '
                c_action = ' '

            return f"""
                function(){{
                    swal.fire({{html: `<h5>Date: {new_date}</h5><b style='color:{color.red};'>Description: </b> <p>{c_reason}</p> <b style='color:{color.green};'>Action: </b> <p>{c_action}</p>`}});
                }}
            """


#*********** Load SVG and make it Interactive ***********#
def svg_loader(letter: str, new_height, new_width):
    with open(f'resources/SVG-out/{letter}.svg', 'r') as f:
        svg_img = f.read()
        stcomp.html(f"""
            <div>{svg_img}</div>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11">
            <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
            <script type="text/javascript">
                function attachClickEvent(elementId, clickFunction) {{
                    var element = document.getElementById(elementId);
                    if (element) {{
                        element.addEventListener('click', clickFunction);
                    }}
                }}
                {"".join([
                    f"attachClickEvent('untitled-u-day{i}', {my_alert(i, letter)}) || "
                    f"attachClickEvent('untitled-u-text{i}', {my_alert(i, letter)});" 
                    for i in range(1, 10)])}
                {"".join([
                    f"attachClickEvent('untitled-u-day{i}_', {my_alert(i, letter)}) || "
                    f"attachClickEvent('untitled-u-text{i}', {my_alert(i, letter)});" 
                    for i in range(10, 32)])}
            </script>
        """, height=new_height, width=new_width)


#*********** Get SVG and add legends Home Page ***********#
def new_svg_loader(name: str, height: float = 210, width: float = 210, left: float = 12, top: float = 1):
    match name:
        case "s":
            svg_loader('s', height, width)
        case "q":
            svg_loader('q', height, width)
        case "c":
            svg_loader('c', height, width)
        case "d":
            svg_loader('d', height, width)
    if name == "s":
        st.write(f"\n"
                    f"                             <style>\n"
                    f"                                .s{{ font-size:0.7rem; margin:5rem; position:absolute; font-weight:bold;}}\n"
                    f"                             </style>\n"
                    f"                             <div style='margin:-2rem;'>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top}rem; color:{color.black};'>LEGEND:</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 1.5}rem; color:{color.red};'>LOST TIME INCIDENT</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 3}rem; color:{color.pink};'>RECORDABLE ACCIDENT</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 4.5}rem; color:{color.maroon};'>FIRE</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 6}rem; color:{color.orange};'>FIRST AID</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 7.5}rem; color:{color.yellow};'>NEAR MISS</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 9}rem; color:{color.green};'>NO INCIDENT</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 10.5}rem; color:{color.plant_off};'>PLANT OFF</p>\n"
                    f"                                 <br>"
                    f"                                  <br>"
                    f"                             </div>", unsafe_allow_html=True)
    else:
        st.write(f"\n"
                    f"                    <style>\n"
                    f"                        .s{{ font-size:0.7rem; margin:0rem; position:absolute; font-weight:bold;}}\n"
                    f"                    </style>\n"
                    f"                    <div style='margin:-0.2rem;height:1.5rem;'>\n"
                    f"                        <p class=\"s\" style='left:{left}rem; top:{top}rem; color:{color.black};'>LEGEND:</p>\n"
                    f"                        <p class=\"s\" style='left:{left}rem; top:{top + 1.5}rem; color:{color.green};'>TARGET ACHIEVED</p>\n"
                    f"                        <p class=\"s\" style='left:{left}rem; top:{top + 3}rem; color:{color.red};'>TARGET MISSED</p>\n"
                    f"                        <p class=\"s\" style='left:{left}rem; top:{top + 4.5}rem; color:{color.plant_off};'>PLANT OFF</p>\n"
                    f"                         <br>"
                    f"                    </div>", unsafe_allow_html=True)


#*********** Load SVG for all FTD pages ***********#
def svg_for_ftd(letter:str, new_height: int = 450, new_width: int = 450, left: float=1, top: float=10):
    with open(f'resources/SVG-out/{letter}.svg') as f:
        svg_file = f.read()
        stcomp.html(f"""
            <div>{svg_file}</div>
        """,height=new_height,width=new_width)
    
    if letter == "s":
        st.write(f"\n"
                    f"                             <style>\n"
                    f"                                .s{{ font-size:1rem; margin:5rem; position:absolute; font-weight:bold;}}\n"
                    f"                             </style>\n"
                    f"                             <div style='margin:-2rem;'>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top}rem; color:{color.black};'>LEGEND:</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 1.5}rem; color:{color.red};'>LOST TIME INCIDENT</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 3}rem; color:{color.pink};'>RECORDABLE ACCIDENT</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 4.5}rem; color:{color.maroon};'>FIRE</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 6}rem; color:{color.orange};'>FIRST AID</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 7.5}rem; color:{color.yellow};'>NEAR MISS</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 9}rem; color:{color.green};'>NO INCIDENT</p>\n"
                    f"                                <p class=\"s\" style='left:{left}rem; top:{top + 10.5}rem; color:{color.plant_off};'>PLANT OFF</p>\n"
                    f"                                 <br>"
                    f"                                  <br>"
                    f"                             </div>", unsafe_allow_html=True)
    else:
        st.write(f"\n"
                    f"                    <style style='margin:-2rem;'>\n"
                    f"                        .s{{ font-size:1rem; margin:0rem; position:absolute; font-weight:bold;}}\n"
                    f"                    </style>\n"
                    f"                    <div style='margin:-0.2rem;height:1.5rem;'>\n"
                    f"                        <p class=\"s\" style='left:{left}rem; top:{top}rem; color:{color.black};'>LEGEND:</p>\n"
                    f"                        <p class=\"s\" style='left:{left}rem; top:{top + 1.5}rem; color:{color.green};'>TARGET ACHIEVED</p>\n"
                    f"                        <p class=\"s\" style='left:{left}rem; top:{top + 3}rem; color:{color.red};'>TARGET MISSED</p>\n"
                    f"                        <p class=\"s\" style='left:{left}rem; top:{top + 4.5}rem; color:{color.plant_off};'>PLANT OFF</p>\n"
                    f"                         <br>"
                    f"                    </div>", unsafe_allow_html=True)