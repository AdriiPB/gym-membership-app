# Import modules
import sqlite3

import tkinter as tk

from tkinter import ttk

def info_function():
    statistic_window = tk.Tk()
    statistic_window.geometry('300x180')
    statistic_window.title("Statistic")

    # Define variables

    conn = sqlite3.connect("gym_database.db")

    cursor = conn.cursor()
  

    #Our search query

    query = "SELECT * FROM Memberships;"

    cursor.execute(query)

    rows = cursor.fetchall()

    #I create a variable for the number of members
    members = len(rows)

    #Basic Members query

    query = "SELECT * FROM Memberships WHERE Membership_type == 'Basic ($10 pw)';"

    cursor.execute(query)

    basic_members = cursor.fetchall()
    #I create a variable for the number of Basic members
    basic_count = len(basic_members)

    #Regular Members query

    query = "SELECT * FROM Memberships WHERE Membership_type == 'Regular ($15 pw)';"

    cursor.execute(query)

    regular_members = cursor.fetchall()
    #I create a variable for the number of Regular members
    regular_count = len(regular_members)

    #Premium Members query

    query = "SELECT * FROM Memberships WHERE Membership_type == 'Premium ($20pw)';"

    cursor.execute(query)

    premium_members = cursor.fetchall()
    #I create a variable for the number of Regular members
    premium_count = len(premium_members)


    #Now I need to calculate the extras, I have calculated the total number for extra 1, 2, 3 and 4 and add them together.

    query = "SELECT * FROM Memberships WHERE Extra_1 == 1;"

    cursor.execute(query)

    extras_1 = cursor.fetchall()
    
    extra1_count = len(extras_1)


    query = "SELECT * FROM Memberships WHERE Extra_2 == 1;"

    cursor.execute(query)

    extras_2 = cursor.fetchall()
    
    extra2_count = len(extras_2)


    query = "SELECT * FROM Memberships WHERE Extra_3 == 1;"

    cursor.execute(query)

    extras_3 = cursor.fetchall()
    
    extra3_count = len(extras_3)


    query = "SELECT * FROM Memberships WHERE Extra_4 == 1;"

    cursor.execute(query)

    extras_4 = cursor.fetchall()
   
    extra4_count = len(extras_4)

    extras_count = extra1_count + extra2_count + extra3_count + extra4_count


    query = "SELECT * FROM Memberships WHERE Direct_Debit == 1;"

    cursor.execute(query)

    d_debit = cursor.fetchall()
   
    direct_debit_count = len(d_debit)

    def return_to_menu():
        statistic_window.destroy()
    # Here I create the labels with the statistics
    lbl_members_count = ttk.Label(statistic_window, text=f"Total members: {members}")
    lbl_basic_count = ttk.Label(statistic_window, text=f"Basic members: {basic_count}")
    lbl_regular_count = ttk.Label(statistic_window, text=f"Regular members: {regular_count}")
    lbl_premium_count = ttk.Label(statistic_window, text=f"Premium members: {premium_count}")
    lbl_extras_count = ttk.Label(statistic_window, text=f"Total Extras: {extras_count}")
    lbl_ddbit_count = ttk.Label(statistic_window, text=f"Direct Debit count: {direct_debit_count}")
    #i have added a return button
    return_to_menu_button = ttk.Button(statistic_window, text="Return", command=return_to_menu)

    # I will place the labels below.
    lbl_members_count.grid(row = 0, column = 0)
    lbl_basic_count.grid(row = 1, column = 0)
    lbl_regular_count.grid(row = 2, column = 0)
    lbl_premium_count.grid(row = 3, column = 0)
    lbl_extras_count.grid(row = 4, column = 0)
    lbl_ddbit_count.grid(row = 5, column = 0)
    return_to_menu_button.grid(row=6, column=0)
    
    conn.close()

