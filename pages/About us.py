from enum import auto
from re import T
from methods.styles import header
import streamlit as st

header("About us")

def about_us():
    # Container div with your "About Us" content
    with st.container() as container:
        logo, title = st.columns((1,5))
        with logo:
            # Company Logo
            st.image("resources/extra/logo.png", width=200)
        with title:
            st.markdown("""
                <center><h1>Welcome to VR Technologies</h1></center><br>
                <marquee><h2>Innovators in Industrial Automation and IoT Solutions.</h3></marquee>
            """,unsafe_allow_html=True)
        st.markdown("""

        ## Our Mission

        At VR Technologies, we are on a mission to revolutionize industrial automation by delivering cutting-edge PLC machines, IoT devices, and powerful dashboards. Our solutions are designed to enhance efficiency, productivity, and connectivity in every industry we serve.

        ## What Sets Us Apart

        - **Expertise:** With years of experience, our team comprises experts in industrial automation, IoT, and data visualization.
        - **Innovation:** We pride ourselves on staying ahead of the curve, incorporating the latest technologies into our products.
        - **Reliability:** Our PLC machines and IoT devices are built to the highest standards, ensuring robust and dependable performance.
        - **Custom Solutions:** We understand that every industry is unique. That's why we offer customizable solutions to meet specific business needs.

        """)

        col1,col2,col3 = st.columns((1,1,1))
        with col1:
            st.markdown("""                
                <h2>PLC & SPM Machines</h2>
                <div style="height:8rem;">
                    Our Programmable Logic Controllers (PLC) machines are at the heart of industrial automation. They provide seamless control and monitoring, enabling businesses to optimize processes and maximize efficiency.
                </div>
            """, unsafe_allow_html=True)
            st.image("resources/extra/plc.jpg", width=440)
        with col2:
            st.markdown("""                
                <h2>IoT Devices</h2>
                <div style="height:8rem;">
                    Our Internet of Things (IoT) devices connect the physical and digital worlds, unlocking new possibilities for data collection, analysis, and real-time decision-making.
                </div>
            """,unsafe_allow_html=True)
            st.image("resources/extra/iot.jpg", width=440)
        with col3:
            st.markdown("""                
                <h2>Dashboards</h2>
                <div style="height:8rem;">
                    Transform raw data into actionable insights with our powerful dashboards. Visualize performance metrics, monitor trends, and make informed decisions to drive success.
                </div>
            """,unsafe_allow_html=True)
            st.image("resources/extra/dash.png", width=440)
        
        st.markdown("""
            <h2>Contact Us</h2>
            <div>Ready to elevate your industrial processes? Contact us today to explore how our solutions can benefit your business.</div>
        """,unsafe_allow_html=True)
        add, email, phone = st.columns((1,1,1))
        with add:
            st.markdown("""
                <center><h5>Address</h5>
                <div>Plot no .199,Sector 7, IMT Manesar, <br>Gurgaon, Haryana <br>122051 </div></center>
            """,unsafe_allow_html=True)
        with email:
            st.markdown("""
                <center><h5>Email</h5>
                <div>info@vrtechnologiesindia.in <br>sales@vrtechnologiesindia.in </div></center>
            """,unsafe_allow_html=True)
        with phone:
            st.markdown("""
                <center><h5>Phone Numbers</h5>
                <div>+91-8447220420 <br>+91-9910325134 </div></center>
            """,unsafe_allow_html=True)
        st.markdown("""

            ## Join Us on the Journey

            Follow us on [our website](https://vrtechnologiesindia.in/) for the latest updates, news, and industry insights.

            Thank you for choosing VR Technologies as your partner in industrial innovation!
        """)

def main():
    about_us()

if __name__ == "__main__":
    main()