import datetime
from turtle import heading
import streamlit as st
from streamlit_modal import Modal
from st_click_detector import click_detector
import pandas as pd
import streamlit.components.v1 as stcomp
from xml.etree import ElementTree as ET
from methods.styles import new_svg_loader
from sqlalchemy import create_engine
import os


st.header("This page is for testing only!")

# df_xl = pd.ExcelFile("Excel/Cost/Cost.xlsx")
# s1 = pd.read_excel(df_xl,'C')
# cost_df = pd.DataFrame(s1)
# print(df_xl)



#********* Read Excel file and write all data in sqlite database file *********#
# # Read Excel data
# excel_file_path = 'Excel/Cost/Plant_Aggregate_OEE.xlsx'
# xls = pd.ExcelFile(excel_file_path)

# # Connect to SQLite database (create if not exists)
# db_url = 'sqlite:///sqlite/database.db'
# engine = create_engine(db_url)

# if not os.path.exists('database.db'):
#     # Create the database file if it doesn't exist
#     engine.connect()

# # Iterate through sheets and save each as a table
# for sheet_name in xls.sheet_names:
#     df = pd.read_excel(xls, sheet_name, header=0)
#     table_name = sheet_name.replace(' ', '_')  # Replace spaces with underscores
#     df.to_sql(table_name, engine, if_exists='replace', index=False)




# #********* Read all Excel files and write all data in sqlite database files *********#
# Function to process Excel files in a directory and its subdirectories
def process_excel_files(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.xlsx'):
                excel_file_path = os.path.join(root, file)
                process_single_excel(excel_file_path, root)

# Function to process a single Excel file
def process_single_excel(excel_file_path, root_folder):
    xls = pd.ExcelFile(excel_file_path)

    # Extract the Excel file name (excluding extension)
    file_name = os.path.splitext(os.path.basename(excel_file_path))[0]

    # Use the Excel file structure to create corresponding directories
    relative_path = os.path.relpath(os.path.dirname(excel_file_path), root_folder)
    db_directory = os.path.join('backup/database', relative_path)
    os.makedirs(db_directory, exist_ok=True)

    # Use the Excel file name as the database name
    db_url = f'sqlite:///{db_directory}/{file_name}.db'
    engine = create_engine(db_url)

    # If the database file doesn't exist, create it
    if not os.path.exists(f'{db_directory}/{file_name}.db'):
        engine.connect()

    # Iterate through sheets and save each as a table
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name, header=0)
        table_name = sheet_name.replace(' ', '_')  # Replace spaces with underscores
        df.to_sql(table_name, engine, if_exists='replace', index=False)

# Specify the root folder containing Excel files
root_folder = 'Excel' 

# Call the function to process Excel files in the specified root folder
# process_excel_files(root_folder)

if st.button("Click to get Backup in Database"):
    process_excel_files(root_folder)
    st.balloons()
    st.subheader("Data Backup is Done!")





# datas = {
#     'dates': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'] * 2,
#     'values': [3, 4, 5, 6, 8, 5, 6, 3, 4, 7],
#     'values1': [5, 6, 3, 4, 7, 6, 3, 4, 5, 9],
#     'values2': [6, 3, 4, 5, 9, 3, 4, 5, 6, 8]
# }
# new_data = pd.DataFrame(datas)
# def show_window(my_data):
#     def on_date_selected():
#         # selected_date = date_var.get()
#         select_date = caln.get_date()
#         changed_date_formet = datetime.datetime.strptime(select_date, "%m/%d/%y")
#         selected_date = changed_date_formet.strftime("%Y-%m-%d")

#         # print(f"Selected Date is: {selected_date}")
#         filtered_data = my_data[my_data['dates'] == selected_date]
#         root.after(0, update_treeview, filtered_data)

#     def update_treeview(data):
#         tree.delete(*tree.get_children())
#         for _, row in data.iterrows():
#             tree.insert("", tk.END, values=tuple(row))

#     root = tk.Tk()
#     root.title('Safety Data')

#     my_data['dates'] = pd.to_datetime(my_data['dates'])

#     caln = Calendar(root, selectmode='day', year=2022, month=1, day=1)
#     caln.pack(pady=10)

#     # date_var = tk.StringVar()
#     # date_picker = ttk.Combobox(root, textvariable=date_var, values=my_data['dates'].dt.strftime('%Y-%m-%d').unique())
#     # date_picker.set(my_data['dates'].min().strftime('%Y-%m-%d'))
#     # date_picker.pack(pady=10)

#     filter_button = tk.Button(root, text='Filter Data', command=on_date_selected)
#     filter_button.pack(pady=5)

#     tree = ttk.Treeview(root)
#     tree['columns'] = tuple(my_data.columns)
#     tree['show'] = 'headings'

#     for col in my_data.columns:
#         tree.heading(col, text=col)
#         tree.column(col, anchor=tk.CENTER)

#     update_treeview(my_data)

#     tree.pack(expand=True, fill=tk.BOTH)
#     root.mainloop()

# click = st.button('click')

# if click:
#     thread = threading.Thread(target=show_window, args=(new_data,))
#     thread.start()


# st.image("resources/Icons/new_info.jpg", width=50)


# data = {
#     'date': [1] * 10,
#     'value': [2]* 10
# }

# new_data = pd.DataFrame(data)
# st.dataframe(new_data, hide_index=True)



# with sqlite3.connect('sqlite/testing_db.db') as conn:
#     cur = conn.cursor()
#     qry = "SELECT * FROM new_table"
#     df = pd.read_sql_query(qry, conn)
#     new_df = pd.DataFrame(df)
#     selection = st.selectbox('Select',('','Check Data','Insert Data', 'Delete Data'), placeholder="What you want with Data!")
#     if selection == 'Insert Data':
#         with st.form("Testing Form", border=True, clear_on_submit=True):
#                 current_dt = datetime.datetime.now()

#                 my_date = st.date_input("Select Date")
#                 qr_data = st.text_input("Data", placeholder='write here')
#                 status = st.selectbox('status',('Open', 'Close'))
#                 submit = st.form_submit_button("Submit")
#                 if submit:
#                     cur.execute(f"INSERT INTO new_table (Timestamp, Date, QR_Code, Status) VALUES ('{current_dt}','{my_date}','{qr_data}','{status}')")
#                     st.write("Data submitted!")
#                 conn.commit()
#     if selection == 'Delete Data':
#         dlt_timestamp = st.text_input("Timestamp", placeholder='Copy and Past here timestamp which want to delete!')
#         dlt = st.button('Delete')
#         st.dataframe(new_df, hide_index=True, use_container_width=True)
#         if dlt:
#             try:
#                 cur.execute(f"DELETE FROM new_table WHERE Timestamp = '{dlt_timestamp}'")
#             except exception as e:
#                  print(f"Error in data deletation is: {e}")
#             st.write('Data Deleted!')
#         conn.commit()
#     if selection == 'Check Data':
#         st.subheader("Select Date to check data between dates!")
#         dt_col1,dt_col2 = st.columns((1,1))
#         with dt_col1:
#              start_date = st.date_input("Select Starting Date: ")
#         with dt_col2:
#              end_date = st.date_input("Select Ending Date: ")
#         # new_qry = 
#         new_df1 = pd.read_sql_query(f"SELECT * FROM new_table WHERE Date BETWEEN '{start_date}' AND '{end_date}'", conn)

#         print(new_df)
#         st.dataframe(new_df1, hide_index=True, use_container_width=True)



# st.title('Dynamic Time Display')

# # Display the current time
# current_time = datetime.datetime.now().strftime("%H:%M:%S")
# st.write(f"Current Time: {current_time}")

# # Add a hint about the rerun
# st.write("This app will rerun in 1 seconds...")

# # Sleep for 1 seconds before rerunning
# time.sleep(1)
# st.rerun()

# def filter_data(day):
#     datas = {
#         'dates': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10'],
#         'values': [3, 4, 5, 6, 8, 5, 6, 3, 4, 7],
#         'values1': [5, 6, 3, 4, 7, 6, 3, 4, 5, 9],
#         'values2': [6, 3, 4, 5, 9, 3, 4, 5, 6, 8]
#     }
#     df = pd.DataFrame(datas)
#     current_year = datetime.datetime.now().year
#     current_month = datetime.datetime.now().month
#     new_date = f"{current_year}-{current_month:02d}-{day:02d}"
#     filtered_data = df[df['dates'] == new_date]
#     return filtered_data

colors = ['yellow'] * 31

# tree = ET.parse("resources/S.svg")
# root = tree.getroot()
# for index, color in enumerate(colors):
#     index += 1
#     if index < 10:
#         target_element = root.find(f".//*[@id='untitled-u-day{index}']")
#     else:
#         target_element = root.find(f".//*[@id='untitled-u-day{index}_']")
#     target_element.set("fill", color)
# try:
#     tree.write("resources/SVG-out/s.svg")
# except Exception as e:
#     print(e)

# new_svg_loader('s',left=15, top = 0)

#***** New SVG Gen *****#

# Load the SVG file
# tree = ET.parse("resources/S.svg")
# root = tree.getroot()
# # Define the namespace mapping
# namespace_mapping = {"": "http://www.w3.org/2000/svg"}

# for index, color in enumerate(colors):
#     index += 1
#     if index < 10:
#         target_element = root.find(f".//*[@id='untitled-u-day{index}']")
#     else:
#         target_element = root.find(f".//*[@id='untitled-u-day{index}_']")
#     target_element.set("fill", color)
# # Remove the namespace prefix from all elements
# for elem in root.iter():
#     if '}' in elem.tag:
#         elem.tag = elem.tag.split('}', 1)[1]  # Remove the namespace prefix
# # Update the namespace in the XML declaration
# if "xmlns" in root.attrib:
#     root.attrib["xmlns"] = namespace_mapping[""]
# # Iterate through the elements and update the namespace
# for elem in root.iter():
#     if "}" in elem.tag:
#         elem.tag = elem.tag.split("}", 1)[1]
#         elem.attrib = {k.split("}", 1)[1]: v for k, v in elem.attrib.items()}
# # Save the modified SVG file
# try:
#     tree.write("resources/s_out.svg", encoding="utf-8", xml_declaration=True)
# except Exception as e:
#     print(e)

# def open_svg(letter:str, new_height: int = 450, new_width: int = 450):
#     with open(f'resources/SVG-out/{letter}.svg') as f:
#         svg_file = f.read()
#         stcomp.html(f"""
#             <div>{svg_file}</div>
#         """,height=new_height,width=new_width)

# open_svg('s',new_height=250,new_width=250)
# def my_alert(day, letter: str):
#     # Get Date on click
#     current_year = datetime.datetime.now().year
#     current_month = datetime.datetime.now().month
#     new_date = f"{current_year}-{current_month:02d}-{day:02d}"

#     match letter:
#         case 's':
#             # Get Data from excel file
#             df_xl = pd.ExcelFile("Excel/Safety/Safety.xlsx")
#             s1 = pd.read_excel(df_xl, 'Safety Incidences')
#             safety_df = pd.DataFrame(s1)

#             # Filter Data according to the date which was click
#             df_incidence_daily = safety_df[safety_df['Date'] == new_date]

#             incident = " "
#             location = " "
#             medical = " "
#             time = " "
#             action = " "

#             if (df_incidence_daily['Category'] == 'Lost time Injury & Recordable Accident').any():
#                 incident =  df_incidence_daily[["Incident"]]["Incident"].to_list()[0]
#                 location = df_incidence_daily[["Plant Area"]]["Plant Area"].to_list()[0]
#                 medical = df_incidence_daily[["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
#                 time = df_incidence_daily[["Time"]]["Time"].to_list()[0]
#                 action = df_incidence_daily[["Preventinve measures implemented and lessons learnt"]]["Preventinve measures implemented and lessons learnt"].to_list()[0]
            
#             elif (df_incidence_daily['Category'] == 'First Aid').any():
#                 incident = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Incident"]]["Incident"].to_list()[0]
#                 location = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Plant Area"]]["Plant Area"].to_list()[0]
#                 medical = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
#                 time = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Time"]]["Time"].to_list()[0]
#                 action = df_incidence_daily[df_incidence_daily['Category'] == 'First Aid'][["Preventinve measures implemented and lessons learnt"]]["Preventinve measures implemented and lessons learnt"].to_list()[0]

#             elif (df_incidence_daily['Category'] == 'Near Miss').any():
#                 incident = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Incident"]]["Incident"].to_list()[0]
#                 location = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Plant Area"]]["Plant Area"].to_list()[0]
#                 medical = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
#                 time = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Time"]]["Time"].to_list()[0]
#                 action = df_incidence_daily[df_incidence_daily['Category'] == 'Near Miss'][["Preventinve measures implemented and lessons learnt"]]["Preventinve measures implemented and lessons learnt"].to_list()[0]

#             elif (df_incidence_daily['Category'] == 'Fire').any():
#                 incident = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Incident"]]["Incident"].to_list()[0]
#                 location = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Plant Area"]]["Plant Area"].to_list()[0]
#                 medical = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Medical Aid Given"]]["Medical Aid Given"].to_list()[0]
#                 time = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Time"]]["Time"].to_list()[0]
#                 action = df_incidence_daily[df_incidence_daily['Category'] == 'Fire'][["Preventinve measures implemented and lessons learnt"]]["Preventinve measures implemented and lessons learnt"].to_list()[0]
            
#             else:
#                 incident = "None"
#                 location = "None"
#                 medical = "None"
#                 time = "None"
#                 action = "None"

#             return f"""
#                 function(){{
#                     alert(`Data is showing on: {new_date} \n\nIncident: {incident} \n\nPlant Area: {location} \n\nAction: {action}`);
#                 }}
#             """

#         case 'q':
#             # Get Data from excel file
#             df_xl = pd.ExcelFile("Excel/Quality/Customer Complaints.xlsx")
#             s1 = pd.read_excel(df_xl, 'Complaint Details')
#             complaint_df = pd.DataFrame(s1)

#             # Filter Data according to the date which was click
#             df_complaint_daily = complaint_df[complaint_df['Date'] == new_date]

#             complaint = " "
#             raise_date = " "
#             target_date = " "
#             responsibility = " "

#             if (df_complaint_daily['Complaints'] == 'Complaint').any():
#                 complaint = df_complaint_daily[['Complaint Description']]['Complaint Description'].to_list()[0]
#                 raise_date = df_complaint_daily[['Raise Date']]['Raise Date'].to_list()[0]
#                 target_date = df_complaint_daily[['Target Date']]['Target Date'].to_list()[0]
#                 responsibility = df_complaint_daily[['Responsibility']]['Responsibility'].to_list()[0]
#             else:
#                 complaint = 'No Complaint'
#                 raise_date = 'No Complaint'
#                 target_date = 'No Complaint'
#                 responsibility = 'No Complaint'

#             return f"""
#                 function(){{
#                     swal(`Data is showing on: {new_date} \n\nComplaint: {complaint} \n\nRaise Date: {raise_date} \n\nTarget Date: {target_date} \n\nResponsibility: {responsibility}`);
#                 }}
#             """
#         case 'd':
#             pass
#         case 'c':
#             pass


# # Open and read SVG file
# with open(f'resources/SVG-out/s.svg', 'r') as f:
#     svg = f.read()
#     col1,col2,col3 = st.columns((1,1,1))
#     with col2:
#         stcomp.html(f"""
#             <div>{svg}</div>
#             <button onClick='myclick()'>click</button>
#             <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11.10.2/dist/sweetalert2.min.css">
#             <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
#             <script type="text/javascript">
#                 function myclick(){{ swal("Hello, SweetAlert!", "This is a custom alert message.", "success"); }}
#                 function attachClickEvent(elementId, clickFunction) {{
#                     var element = document.getElementById(elementId);
#                     if (element) {{
#                         element.addEventListener('click', clickFunction);
#                     }}
#                 }}
#                 {"".join([f"attachClickEvent('untitled-u-day{i}', {my_alert(i, 's')});" for i in range(1, 10)])}
#                 {"".join([f"attachClickEvent('untitled-u-day{i}_', {my_alert(i, 's')});" for i in range(10, 32)])}
#             </script>
#         """, height=350, width=250)


# def svg_loader(letter):
#     with open(f'resources/SVG-out/{letter}.svg', 'r') as f:
#         svg_img = f.read()
#         stcomp.html(f"""
#             <div>{svg_img}</div>
#             <script type="text/javascript">
#                 function attachClickEvent(elementId, clickFunction) {{
#                     var element = document.getElementById(elementId);
#                     if (element) {{
#                         element.addEventListener('click', clickFunction);
#                     }}
#                 }}
#                 {"".join([f"attachClickEvent('untitled-u-day{i}', {my_alert(i, letter)});" for i in range(1, 10)])}
#                 {"".join([f"attachClickEvent('untitled-u-day{i}_', {my_alert(i, letter)});" for i in range(10, 32)])}
#             </script>
#         """, height=250, width=250)

# col1,col2,col3,col4 = st.columns((0.5,1,1,0.5))
# with col2:
#     new_svg_loader('s')
# with col3:
#     new_svg_loader('q')
#             # <button onClick="alert(`Hello again! This is how we \nadd line breaks to an alert box!`)">Click1</button>
#             # <center><button onClick="alert('test')">Click1</button></center>

# with open('resources/SVG-out/s.svg', 'r') as f:
#     new_svg = f.read()
#     # st.image(new_svg)
#     st.markdown(f"""
#         <div>{new_svg}</div>
#     """,unsafe_allow_html=True)
#     # stcomp.html(f"<div>{new_svg}</div>")


    # import streamlit.components.v1 as scv
    # def handle_click():
    #     st.session_state.click_count += 1
    #     st.write(f"Button clicked {st.session_state.click_count} times")

    # # Initialize session state if it doesn't exist
    # if "click_count" not in st.session_state:
    #     st.session_state.click_count = 0

    # # Wrap the `img` tag with a `button` tag
    # # button_tag = f'<button>{html_ftd}</button>'
    # button_tag = f'<button onclick="handleButtonClick()" id="myButton">{html_ftd}</button>'

    # # Display the button in Streamlit using the `streamlit.components.v1.html` function
    # # click = scv.html(button_tag, height=250)
    # # Add the JavaScript code for handling button clicks

    # scv.html(
    #     f"""
    #     <script>
    #         function handleButtonClick() {{
    #             let myButton = document.getElementById("myButton");
    #             let buttonClicks = {st.session_state.click_count};
    #             myButton.innerText = `Clicked $buttonClicks times`;
    #         }}
    #     </script>
    #     {button_tag}
    #     """,
    #     height=250
    # )


# content = """<p><a href='#' id='Link 1'>First link</a></p>
#     <p><a href='#' id='Link 2'>Second link</a></p>
#     <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
#     <a href='#' id='Image 2'><img width='20%' src='https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=200'></a>
#     """
# clicked = click_detector(content)

# st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")

# testing = """
#         <a href='#' id='click testing'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
#     """
# click_test = click_detector(testing)
# st.write(click_test)





# options = st.selectbox("Category", ["Delivery", "Sale vs Actual Plan", "Breakdown Time", "Cost", "Human Productivity",
#                                     "Plant Aggregate OEE", "Customer Complaints", "First Time Pass", "Plant PPM", 
#                                     "Reported Rejection (INR)", "Reported Rejection (%)", "Supplier PPM", "Safety Incidents",
#                                      "Unsafe Practices", "Problem Solving Competency", "Personal Gap", "visit or Audits" ],
#                                         key="category", index=None, placeholder="Category", label_visibility="hidden")

# if options == "Delivery":
#     df_xl = pd.ExcelFile("Excel/Delivery/Delivery.xlsx")
#     s1 = pd.read_excel(df_xl, 'D')
#     # Get unique years from the DataFrame
#     unique_years = sorted(s1['Date'].dt.year.unique(), reverse=True)

#     # Selectbox for year
#     selected_year = st.selectbox("Select a year:", unique_years)

#     #  Selectbox for month
#     selected_month = st.selectbox("Select a month:", range(1, 13), format_func=lambda x: datetime.date(1900, x, 1).strftime('%B'))

#     # Filter DataFrame based on selected month and year
#     filtered_df = s1[(s1['Date'].dt.year == selected_year) & (s1['Date'].dt.month == selected_month)]
#     if st.button("Get Data"):     
#         st.dataframe(filtered_df, use_container_width=True, hide_index=True)
#         # modal = Modal(key="Demo Key",title="Popup", max_width=1000)
#         # if st.button("click"):
#         #     with modal.container():
#         #         st.markdown("""
#         #                 <style>
#         #                     .st-emotion-cache-p1slk:nth-child(1){
#         #                         position: relative;
#         #                         bottom: 32rem;
#         #                         left: 60rem
#         #                     }
#         #                     .st-emotion-cache-0{
#         #                         position: relative;
#         #                         bottom: 1rem;
#         #                     }
                            
#         #                 </style>
#         #         """, unsafe_allow_html=True)
#         #         st.dataframe(filtered_df, use_container_width=True, hide_index=True)
# elif options == "Sale vs Actual Plan":
#     df_xl = pd.ExcelFile("Excel/Delivery/Sale_vs_actual_plan.xlsx")
#     s1 = pd.read_excel(df_xl, 'Sale vs Actual Plan')
#     # Get unique years from the DataFrame
#     unique_years = sorted(s1['Date'].dt.year.unique(), reverse=True)

#     # Selectbox for year
#     selected_year = st.selectbox("Select a year:", unique_years)

#     #  Selectbox for month
#     selected_month = st.selectbox("Select a month:", range(1, 13), format_func=lambda x: datetime.date(1900, x, 1).strftime('%B'))

#     # Filter DataFrame based on selected month and year
#     filtered_df = s1[(s1['Date'].dt.year == selected_year) & (s1['Date'].dt.month == selected_month)]
#     if st.button("Get Data"):     
#         st.dataframe(filtered_df, use_container_width=True, hide_index=True)





# current_date = datetime.date.today().month  # 12
# current_month = pd.Timestamp('now').to_period('M')  # 2023-12
# st.write(current_month)

# # Streamlit app
# st.title("Image Hover Event")

# st.image("resources/extra/new.jpg")

# # HTML and JavaScript code for image with hover effect
# html_code = f"""
#     <style>
#         .st-emotion-cache-1v0mbdj img {{
#             width: 100%;
#             height: 100%;
#             transition: opacity 0.6s ease-in-out;
#         }}

#         .st-emotion-cache-1v0mbdj:hover img {{
#             opacity: 0;

#         }}
#     </script>
# """

# # Display the HTML code
# st.markdown(html_code, unsafe_allow_html=True)



# # Streamlit app
# st.title("Show DataFrame on Image Hover")

# # Sample DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 22],
#         'City': ['New York', 'San Francisco', 'Los Angeles']}
# df = pd.DataFrame(data)

# # Image URL
# image_url = "resources/extra/new.jpg"

# # CSS code for styling
# css_code = """
# <style>
#     .image-container {
#         position: relative;
#         width: 200px;
#         height: 200px;
#     }

#     .image-container img {
#         width: 100%;
#         height: 100%;
#     }

#     .data-frame {
#         position: absolute;
#         top: 0;
#         left: 0;
#         background-color: white;
#         padding: 10px;
#         border: 1px solid #ddd;
#         display: none;
#         opacity: 0;
#         transition: opacity 0.3s ease-in-out;
#     }

#     .image-container:hover .data-frame {
#         display: block;
#         opacity: 1;
#     }

#     .dataframe {
#         width: 100%;
#         border-collapse: collapse;
#         margin-top: 10px;
#     }

#     .dataframe th, .dataframe td {
#         border: 1px solid #ddd;
#         padding: 8px;
#         text-align: left;
#     }
# </style>
# """

# # Display the CSS code
# st.markdown(css_code, unsafe_allow_html=True)

# # Display the image and DataFrame
# st.markdown(f"""
#     <div class="image-container">
#         <img src="{image_url}" alt="Your Image">
#         <div class="data-frame">
#             {st.date_input("select date")}
#             {df.to_html(classes='dataframe', index=False)}
#         </div>
#     </div>
# """, unsafe_allow_html=True)



# import streamlit as st
# import tkinter as tk
# from tkinter import messagebox
# from multiprocessing import Process

# def run_tk_popup():
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window
#     messagebox.showinfo("Popup", "Hello, this is a popup!")
#     root.destroy()

# def main():
#     st.title("Streamlit with Tkinter Popup Example")
#     if st.button("Show Popup"):
#         # Run the Tkinter popup in a separate process
#         popup_process = Process(target=run_tk_popup)
#         popup_process.start()
#         popup_process.join()



#********* About Us Page *********#
def about_us():
    st.title("About Us")
    col1,col2 = st.columns((1,5))
    with col1:
        st.image("resources/extra/abc.jpeg", use_column_width=True)

    st.write(
        """
        Welcome to our Streamlit App! 🚀 We are a team of passionate individuals dedicated to creating
        innovative solutions and providing valuable information through this platform.

        ## 🌟 Our Mission
        Our mission is to [insert mission statement here].

        ## 🚀 Meet the Team
        ### John Doe - CEO
        John is a visionary leader with a background in [insert background here]. He is passionate
        about [insert specific interests or focus areas].

        ### Jane Smith - CTO
        Jane is a tech enthusiast with expertise in [insert technologies or fields]. She leads our
        technical team and ensures the seamless functioning of our applications.

        ### Alex Johnson - Head of Design
        Alex has a keen eye for design and aesthetics. With a background in [insert design-related
        fields], Alex ensures that our applications are not only functional but also visually appealing.

        ## 📧 Contact Us
        Feel free to reach out to us at [insert contact information]. We value your feedback and
        are always open to collaboration opportunities.

        Thank you for choosing our Streamlit App! 👋
        """
    )

# about_us()

# if __name__ == "__main__":
#     about_us()


