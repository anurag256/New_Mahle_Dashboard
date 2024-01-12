import pandas as pd
from methods.styles import back_btn, header
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

header("Layer Audit and Action Points")

col1, col2 = st.columns((5, 2))
with col1:
    back_btn()

df_xl = pd.ExcelFile("Excel/PSP/Layer and Audit Action Points.xlsx")
action_points_xl = pd.read_excel(df_xl, 'Sheet1') 
st.dataframe(action_points_xl, use_container_width=True, hide_index=True)