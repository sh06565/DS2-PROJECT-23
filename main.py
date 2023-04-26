import tkinter as tk
import pandas as pd
from tkinter import ttk
import time


# create the main window
root = tk.Tk()
root.title("Enterprise Oracle")

# set the window size and background image
bg_image = tk.PhotoImage(file="images/ds2pic.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# add a label for the title
title_label = tk.Label(root, text="Enterprise Oracle", font=("Arial", 40), fg="#2C3E50", bg="white", 
                       highlightthickness=0, highlightbackground=root.cget("bg"))
title_label.pack(pady=50)

# add a button to go to another page
def go_to_another_page():
    # create a new window
    new_window = tk.Toplevel(root)
    new_window.title("Another Page")

    # set the window size and background image
    bg_image = tk.PhotoImage(file="images/ds2pic.png")
    bg_label = tk.Label(new_window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # add a button to add data to the csv file
    def add_data():
        
        # get the values entered in the entry boxes
        col1_val = col1_entry.get()
        col2_val = col2_entry.get()
        col3_val = col3_entry.get()
        col4_val = col4_entry.get()
        col5_val = col5_entry.get()

        # create a new row with the values entered
        new_row = pd.DataFrame({'Column 1': [col1_val],
                                'Column 2': [col2_val],
                                'Column 3': [col3_val],
                                'Column 4': [col4_val],
                                'Column 5': [col5_val]})

        # append the new row to the csv file
        with open('Data(with tags).csv', 'a') as f:
            new_row.to_csv(f, header=False, index=False)

        # update the treeview with the new data
        treeview.insert("", "end", values=[col1_val, col2_val, col3_val, col4_val, col5_val])

    add_button = tk.Button(new_window, text="Add Data", font=("Arial", 14), bg="#2C3E50", fg="white", 
                        activebackground="#34495E", activeforeground="white", 
                        bd=0, highlightthickness=0, padx=10, pady=5, 
                        command=add_data)
    add_button.place(relx=0.5, rely=0.3, anchor="center")

    # add entry boxes for each column of the csv file
    col1_entry = tk.Entry(new_window, width=20)
    col1_entry.place(relx=0.25, rely=0.4, anchor="center")
    col2_entry = tk.Entry(new_window, width=20)
    col2_entry.place(relx=0.4, rely=0.4, anchor="center")
    col3_entry = tk.Entry(new_window, width=20)
    col3_entry.place(relx=0.55, rely=0.4, anchor="center")
    col4_entry = tk.Entry(new_window, width=20)
    col4_entry.place(relx=0.7, rely=0.4, anchor="center")
    col5_entry = tk.Entry(new_window, width=20)
    col5_entry.place(relx=0.85, rely=0.4, anchor="center")

    
    # add a button to go back to the main page
    def go_back():
        new_window.destroy()
        root.deiconify()

    back_button = tk.Button(new_window, text="Go Back", font=("Arial", 20), bg="#2C3E50", fg="white", 
                            activebackground="#34495E", activeforeground="white", 
                            bd=0, highlightthickness=0, padx=20, pady=10, 
                            command=go_back)
    back_button.place(relx=0.1, rely=0.1, anchor="center")

    # add a search bar and search button
    # Add text that says "Search" above the search bar
    search_var = tk.StringVar()
    search_label = tk.Label(new_window, text="Search", font=("Arial", 14), bg=root.cget("bg"))
    search_label.place(relx=0.3, rely=0.2, anchor="center")
    search_entry = tk.Entry(new_window, textvariable=search_var, width=30)
    search_entry.place(relx=0.5, rely=0.2, anchor="center")

    search_button = tk.Button(new_window, text="Search", font=("Arial", 14), bg="#2C3E50", fg="white", 
                            activebackground="#34495E", activeforeground="white", 
                            bd=0, highlightthickness=0, padx=10, pady=5)
    search_button.place(relx=0.7, rely=0.2, anchor="center")
    # add a label for search time
    search_time_label = tk.Label(new_window, text="Search Time (s):", font=("Arial", 14), fg="#2C3E50", bg="white",
                                highlightthickness=0, highlightbackground=root.cget("bg"))
    search_time_label.place(relx=0.2, rely=0.3, anchor="e")

    # add a box for search time
    search_time = tk.StringVar()
    search_time_entry = tk.Entry(new_window, textvariable=search_time, width=10)
    search_time_entry.place(relx=0.25, rely=0.3, anchor="w")


    # add a treeview to display data from a csv file
    treeview = ttk.Treeview(new_window)
    treeview.place(relx=0.5, rely=0.75, anchor="center")

    # load data from a csv file
    data = pd.read_csv("Data(with tags).csv")
    
    # set up columns and headings for the treeview
    treeview["columns"] = list(data.columns)
    treeview["show"] = "headings"
    for column in treeview["columns"]:
        treeview.heading(column, text=column)

    # add data to the treeview
    for index, row in data.iterrows():
        treeview.insert("", "end", values=list(row))
    

    # set the background color of the new window to be the same as the main window
    new_window.config(bg=root.cget("bg"))

    

    # hide the main window
    root.withdraw()


go_button = tk.Button(root, text="Enter", font=("Arial", 20), bg="#2C3E50", fg="white", 
                      activebackground="#34495E", activeforeground="white", 
                      bd=0, highlightthickness=0, padx=20, pady=10, 
                      command=go_to_another_page)
go_button.place(relx=0.5, rely=0.5, anchor="center")

# run the main loop
root.mainloop()
