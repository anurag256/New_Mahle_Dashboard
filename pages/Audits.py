import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

from methods.styles import header

xls_visit = pd.ExcelFile("Excel/Personal/Visit or audits.xlsx")
df = pd.read_excel(xls_visit, "Visits")

header("Visits and Audits")
col1, col2 = st.columns((5, 2))
with col1:
    st.write("")
    st.write("")
    back = st.button("<- Back")
    if back:
        switch_page("App")

st.dataframe(df, hide_index= True, use_container_width=True)