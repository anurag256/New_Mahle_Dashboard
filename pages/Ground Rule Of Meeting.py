from streamlit_extras.switch_page_button import switch_page
from methods.styles import header
import streamlit as st


header("Ground Rule Of Meetings")
back = st.button("<- Back")
if back:
    switch_page("App")

st.markdown("""
        <div style='padding:1rem;'>
            <ol>
                <li>Start or end meeting on time.</li>
                <li>Stay on task no side conversation.</li>
                <li>Listen to others and don't interrupt.</li>
                <li>Remain focused and don't attend calls.</li>
                <li>Make decision based on clear information</li>
                <li>Bring closure to decision</li>
                <li>Identify actions that results from decisions.</li>
                <li>Accept the fact that there will be difference in opinion.</li>
                <li>Show mutual respect.</li>
                <li>Honor brainstorming without being attached to viewpoint.</li>
                <li>Keep notes of the meeting as an individual.</li>
                <li>Attack the problems not the person - “no blame game”.</li>
                <li>Speak your mind without fear or reprisal.</li>
            </ol>
        </div>
""", unsafe_allow_html=True)