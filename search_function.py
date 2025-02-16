import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def search_function():
    #Toplevel() will create a new window. it will reference our root window and will close if our main window it's closed.
    search_window = tk.Toplevel()
    search_window.geometry("1400x700")
    search_window.title("Search database")

    DATABASE_NAME = "gym_database.db"
    TABLE_NAME = "Memberships"

    ####################
    # Database functions
    def execute_query(query):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()

    def select_query(query):
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    ########################

    ########################
    # Build search query
    def submit():
        query = ""

        # Read the GUI widgets and build the query
        # I have made sure the query is not case sensitive.
        query = f"""SELECT * FROM {TABLE_NAME} WHERE
                    First_Name = '{EDIT_FNAME.get()}' COLLATE NOCASE OR
                    Last_Name = '{EDIT_LNAME.get()}' COLLATE NOCASE OR
                    Address = '{EDIT_ADDRESS.get()}' COLLATE NOCASE OR
                    Mobile = '{EDIT_MOBILE.get()}' COLLATE NOCASE OR
                    Membership_Type = '{EDIT_MEMBERSHIP_TYPE.get()}' COLLATE NOCASE OR
                    Membership_Duration = '{EDIT_MEMBERSHIP_DURATION.get()}' COLLATE NOCASE OR
                    Direct_Debit = '{EDIT_DIRECT_DEBIT.get()}' OR
                    Extra_1 = '{EDIT_EXTRA_1.get()}' OR
                    Extra_2 = '{EDIT_EXTRA_2.get()}' OR
                    Extra_3 = '{EDIT_EXTRA_3.get()}' OR
                    Extra_4 = '{EDIT_EXTRA_4.get()}' OR
                    Payment_Frequency = '{EDIT_PAYMENT_FREQUENCY.get()}' COLLATE NOCASE"""


        # If a query has been built, run the query and update the Treeview
        if query:
            rows = select_query(query)
            if not rows:
                # messagebox if not members
                messagebox.showinfo("Search Result", "No members found.")
                return
        update_treeview(rows)
    ########################
    def return_to_menu():
        search_window.destroy()
    ########################
    # Search widgets
    EDIT_FNAME = tk.StringVar()
    EDIT_LNAME = tk.StringVar()
    EDIT_ADDRESS = tk.StringVar()
    EDIT_MOBILE = tk.StringVar()
    EDIT_MEMBERSHIP_TYPE = tk.StringVar()
    EDIT_MEMBERSHIP_DURATION = tk.StringVar()
    EDIT_DIRECT_DEBIT = tk.StringVar()
    EDIT_EXTRA_1 = tk.StringVar()
    EDIT_EXTRA_2 = tk.StringVar()
    EDIT_EXTRA_3 = tk.StringVar()
    EDIT_EXTRA_4 = tk.StringVar()
    EDIT_PAYMENT_FREQUENCY = tk.StringVar()

    search_frame = tk.LabelFrame(search_window, text="Search Options")
    search_frame.grid(column=0, row=0, padx=20, pady=20, sticky="ew")

    lbl_fname = ttk.Label(search_frame, text="First Name:").grid(row=0, column=0)
    lbl_lname = ttk.Label(search_frame, text="Last Name:").grid(row=1, column=0)
    lbl_address = ttk.Label(search_frame, text="Address:").grid(row=2, column=0)
    lbl_mobile = ttk.Label(search_frame, text="Mobile:").grid(row=3, column=0)
    lbl_membership_type = ttk.Label(search_frame, text="Membership Type:").grid(row=4, column=0)
    lbl_membership_duration = ttk.Label(search_frame, text="Membership Duration:").grid(row=5, column=0)
    lbl_direct_debit = ttk.Label(search_frame, text="Direct Debit:").grid(row=6, column=0)
    lbl_extra_1 = ttk.Label(search_frame, text="Extra 1:").grid(row=7, column=0)
    lbl_extra_2 = ttk.Label(search_frame, text="Extra 2:").grid(row=8, column=0)
    lbl_extra_3 = ttk.Label(search_frame, text="Extra 3:").grid(row=9, column=0)
    lbl_extra_4 = ttk.Label(search_frame, text="Extra 4:").grid(row=10, column=0)
    lbl_payment_frequency = ttk.Label(search_frame, text="Payment Frequency:").grid(row=11, column=0)

    en_fname = ttk.Entry(search_frame, textvariable=EDIT_FNAME).grid(row=0, column=1)
    en_lname = ttk.Entry(search_frame, textvariable=EDIT_LNAME).grid(row=1, column=1)
    en_address = ttk.Entry(search_frame, textvariable=EDIT_ADDRESS).grid(row=2, column=1)
    en_mobile = ttk.Entry(search_frame, textvariable=EDIT_MOBILE).grid(row=3, column=1)
    en_membership_type = ttk.Entry(search_frame, textvariable=EDIT_MEMBERSHIP_TYPE).grid(row=4, column=1)
    en_membership_duration = ttk.Entry(search_frame, textvariable=EDIT_MEMBERSHIP_DURATION).grid(row=5, column=1)
    en_direct_debit = ttk.Entry(search_frame, textvariable=EDIT_DIRECT_DEBIT).grid(row=6, column=1)
    en_extra_1 = ttk.Entry(search_frame, textvariable=EDIT_EXTRA_1).grid(row=7, column=1)
    en_extra_2 = ttk.Entry(search_frame, textvariable=EDIT_EXTRA_2).grid(row=8, column=1)
    en_extra_3 = ttk.Entry(search_frame, textvariable=EDIT_EXTRA_3).grid(row=9, column=1)
    en_extra_4 = ttk.Entry(search_frame, textvariable=EDIT_EXTRA_4).grid(row=10, column=1)
    en_payment_frequency = ttk.Entry(search_frame, textvariable=EDIT_PAYMENT_FREQUENCY).grid(row=11, column=1)

    search_button = ttk.Button(search_frame, text="Search", command=submit).grid(row=12, column=1, rowspan=2)
    #I have added a return button to return to the main menu
    return_to_menu_button = ttk.Button(search_frame, text="Return", command=return_to_menu).grid(row=14, column=1, rowspan=2)
    ########################
    
    ########################
    # Treeview code
    def update_treeview(rows):
        for item in TREE.get_children():
            TREE.delete(item)

        temp_list = []
        for member in rows:
            # Adjust indices as needed based on the number of columns in the query results
            temp_list.append((member[1], member[2], member[3], member[4], member[5], member[6], member[7], member[8], member[9], member[10], member[11], member[12]))

        for row in temp_list:
            TREE.insert("", tk.END, values=row)

    tree_frame = tk.LabelFrame(search_window, text="Search Results")
    tree_frame.grid(column=0, row=1, padx=20, pady=20, sticky="we")

    TREE = ttk.Treeview(tree_frame, columns=["First Name", "Last Name", "Address", "Mobile", "Membership Type", "Membership Duration", "Direct Debit", "Extra 1", "Extra 2", "Extra 3", "Extra 4", "Payment Frequency"], show='headings')

    TREE.heading("First Name", text="First Name")
    TREE.column("First Name", minwidth=0, width=100)
    TREE.heading("Last Name", text="Last Name")
    TREE.column("Last Name", minwidth=0, width=100)
    TREE.heading("Address", text="Address")
    TREE.column("Address", minwidth=0, width=100)
    TREE.heading("Mobile", text="Mobile")
    TREE.column("Mobile", minwidth=0, width=100)
    TREE.heading("Membership Type", text="Membership Type")
    TREE.column("Membership Type", minwidth=0, width=100)
    TREE.heading("Membership Duration", text="Membership Duration")
    TREE.column("Membership Duration", minwidth=0, width=100)
    TREE.heading("Direct Debit", text="Direct Debit")
    TREE.column("Direct Debit", minwidth=0, width=100)
    TREE.heading("Extra 1", text="Extra 1")
    TREE.column("Extra 1", minwidth=0, width=100)
    TREE.heading("Extra 2", text="Extra 2")
    TREE.column("Extra 2", minwidth=0, width=100)
    TREE.heading("Extra 3", text="Extra 3")
    TREE.column("Extra 3", minwidth=0, width=100)
    TREE.heading("Extra 4", text="Extra 4")
    TREE.column("Extra 4", minwidth=0, width=100)
    TREE.heading("Payment Frequency", text="Payment Frequency")
    TREE.column("Payment Frequency", minwidth=0, width=100)

    TREE.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=TREE.yview)
    TREE.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')
    ########################
   


