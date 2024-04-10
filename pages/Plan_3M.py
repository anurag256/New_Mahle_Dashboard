import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import datetime
from methods.styles import header, horizontal_line

header("3M Plan")

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

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Line_1", "Line_2", "Line_3", "Line_4", "Line_5", "Line_6", "Line_7"])
with tab1:
    shift1,shift2,shift3 = st.tabs(["Shift_1", "Shift_2", "Shift_3"])
with tab2:
    shift1,shift2,shift3 = st.tabs(["Shift_1", "Shift_2", "Shift_3"])
with tab3:
    shift1,shift2,shift3 = st.tabs(["Shift_1", "Shift_2", "Shift_3"])
with tab4:
    shift1,shift2,shift3 = st.tabs(["Shift_1", "Shift_2", "Shift_3"])
with tab5:
    shift1,shift2,shift3 = st.tabs(["Shift_1", "Shift_2", "Shift_3"])
with tab6:
    shift1,shift2,shift3 = st.tabs(["Shift_1", "Shift_2", "Shift_3"])
with tab7:
    shift1,shift2,shift3 = st.tabs(["Shift_1", "Shift_2", "Shift_3"])