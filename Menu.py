# Imports

import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox as msgbox
# I proceed to import the gym_app that was created for assignemnt 2.
from membership_form import gym_app
# I have imported the search fucntion I have created here.
from search_function import search_function
# I have importect here the statistics function that I have created in a different file.
from statistics import info_function 


#------------------------------
# Tkinter setup
#------------------------------

#---------------
# Tkinter setup
#---------------
root = tk.Tk()
root.geometry("300x180")                    # Set window dimensions
root.title("Gym App")               # Set title of window
root.config(background = "Light Blue")     # Set a background colour

#---------------
# Functions for our menu commands
#---------------
# Functions need to be created before calling them.

# I create a function to open the membership form.

def open_membership_form():
    gym_app()

def search():
    search_function()

def statistics():
    info_function()

def help():
    msgbox.showinfo("Help", "This is the help section.\n\n"
                            "Click Open Membership Form to open the form and register new members.\n"
                            "Click Search to search for existing members.\n"
                            "Click Statistics to display membership statistics.\n"
                            "Click Help to show this help information.")

                                      
#---------------
# Tkinter menu setup
#---------------

menubar = tk.Menu(root)                     # Create a new menubar
root.config(menu=menubar)                   # Attach to the window

#---------------
# Menu options

# Declare the menu options and attach them to the menubar
# tearoff = False will disable the Tkinter feature to detach menus
main_menu = tk.Menu(menubar, tearoff=False)
membership_form = tk.Menu(menubar, tearoff=False)
search_form = tk.Menu(menubar, tearoff=False)
statistics_form = tk.Menu(menubar, tearoff=False)
help_menu = tk.Menu(menubar, tearoff=False)

#---------------
# Add menus to the menu bar

menubar.add_cascade(label="Main Menu", menu=main_menu)

#---------------
# Menu commands
# I added all the comands to the main menu.

#main_menu.add_command(label="Open", command=menu_file_open)

main_menu.add_command(label="Open Membership Form", command=open_membership_form)

### /search
main_menu.add_command(label="Search", command=search)

#### Statistics
main_menu.add_command(label="Statistics", command=statistics)

#### Help
main_menu.add_command(label="Help", command=help)

# I have added the version number.
version_label = ttk.Label(root, text="Gym App by Adrian Version: 1.0", anchor='center')
version_label.pack(side='bottom', pady=10, expand=True)

#---------------
# Tkinter main loop
#---------------

root.mainloop()