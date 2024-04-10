import tkinter as tk



import streamlit as st

# Your SVG content
svg_content = """
<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="20" fill="white">1</text>
</svg>
"""

# Display the SVG with interactivity
selected_day = st.image(svg_content)

# Define text for each day
text_1 = "This is text for Day 1."
text_2 = "This is text for Day 2."

# Display text based on the selected day
if selected_day:
    if selected_day.button("1"):
        st.markdown(text_1)
    elif selected_day.button("2"):
        st.markdown(text_2)


root = tk.Tk()

# root.title('Title')
# lbl = tk.Label(root, text='hello world', width=60, height=10).pack()

frame = tk.Frame(root)
frame.pack()
btn = tk.Button(frame, text='click')
btn.pack()
 
# # frame inside root window
# frame = tk.Frame(root)                  
 
# # geometry method
# frame.pack()                          
 
# # button inside frame which is 
# # inside root
# button = tk.Button(frame, text ='Geek')  
# button.pack()         

root.mainloop()
