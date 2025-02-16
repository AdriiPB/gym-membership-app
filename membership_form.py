# This application calculates the fees and extras for a gym, also creates a data base with the clients.
# I have done some esthetic changes without affecting the funcionality and then created two functions for calculating the fees and submit the application.
# It needs to be open on VS Code.
#
#
# BIT502, Adrian Prada Barba, student number: 5068590, assessment 2.

# ------------------------------
# Imports
# ------------------------------
def gym_app():
    import tkinter
    # I need to import messagebox to can use messagebox
    from tkinter import messagebox
    # Import the os module to give us access to file functions
    import os
    # This will be the location where the Python file is being run from
    cwd = os.getcwd()
    # I import sqlite3
    import sqlite3

    # ------------------------------
    # Tkinter setup
    # ------------------------------

    window = tkinter.Tk()
    window.title("City Gym Membership Form")
    # I change the background color to improve the design.
    window.config(background = "light blue")


    # ------------------------------
    # Variables
    # ------------------------------

    # Store text in the variables so we can change it later if we need to
    # I added the fees for extra information 

    basic = "Basic ($10 pw)"
    regular = "Regular ($15 pw)"
    premium = "Premium ($20pw)"
    three_months = "3 months"
    six_months = "6 months"
    twelve_months = "12 months"
    weekly = "Weekly"
    monthly = "Monthly"
    optional_1 = "24/7 Access ($1 pw)"
    optional_2 = "Personal training ($20 pw)"
    optional_3 = "Diet consultation ($20 pw)"
    optional_4 = "Online video access ($2 pw)"

    # I create the variables  to store the string in the entry or text
    name_variable = ""
    last_name_variable = ""
    address_variable = ""
    mobile_variable = ""



    # Variables that store the results of the elements
    # I have changed the member type, duration, and payment frequently I can handle the errors if none selected.

    member_type = tkinter.StringVar(window, " ")                # Selected membership type
    member_duration = tkinter.StringVar(window, " ")            # Duration of membership
    direct_debit = tkinter.BooleanVar(window, False)            # Direct debit
    extra1 = tkinter.BooleanVar(window, False)                  # Optional extra 1
    extra2 = tkinter.BooleanVar(window, False)                  # Optional extra 2
    extra3 = tkinter.BooleanVar(window, False)                  # Optional extra 3
    extra4 = tkinter.BooleanVar(window, False)                  # Optional extra 4
    payment_frequency = tkinter.StringVar(window, " ")          # Payment frequency weekly/monthly




    # ------------------------------
    # Functions
    # ------------------------------

    def calculate():
        # TODO: Build the calculation system, error checking and other tasks
        # First I will calculate the membership cost
        # in this case I didn't need to handle errors becasue automatically was an option selected,
        # so I changed them to none selected and then show a messagebox if the user forget to select them,
        # for membership cost I will include plan, duration and direct debit discount in one variable.

        # As i need to use the following variables in the submit function, i will declare them global:

        global membership_cost
        global duration_discount
        global payment_discount
        global discount
        global extras_cost
        global total_amount
        global regular_payment

        
        # I create a variable to storage the base cost.
        membership_cost = 0
        if(member_type.get() == basic): 
            membership_cost += 10
        elif(member_type.get() == regular): 
            membership_cost += 15
        elif(member_type.get() == premium): 
            membership_cost += 20
        else:
            messagebox.showinfo("Error ", "Please select a membership type")
            return
        # I will add the discount depending on the duration.
        duration_discount = 0
        if(member_duration.get() == three_months):
            duration_discount = 0
        elif(member_duration.get() == six_months):
            duration_discount = 2
        elif(member_duration.get() == twelve_months):
            duration_discount = 5
        else:
            messagebox.showinfo("Error", "please select the membership duration")
            return
        # For the base fee I calculate the disocunt if paying by direct debit, I haven't calculate any extra yet so is only over the base fee.
        payment_discount = 0
        if(direct_debit.get()):
            payment_discount = membership_cost*0.01
        # If not discount, the discount will be 0.

        discount = duration_discount + payment_discount

        label_total_cost_base.config(text = f"${membership_cost:.2f}")
        label_total_cost_discount.config(text = f"${discount:.2f}")

        # Now i will create a variable for the extras.

        extras_cost = 0

        if(extra1.get()):
            extras_cost += 1
        if(extra2.get()):
            extras_cost += 20
        if(extra3.get()):
            extras_cost += 20
        if(extra4.get()):
            extras_cost += 2

        label_total_cost_extras.config(text = f"${extras_cost:.2f}")

        # Now I will calculate the total.

        total_amount = membership_cost + extras_cost - discount
        label_total_cost_total.config(text = f"${total_amount:.2f}")

        # Finally, i need to calculate if is weekly of monthly.
        # I create a variable named regular_payment.

        regular_payment = 0
        if(payment_frequency.get() ==weekly):
            regular_payment = total_amount
        elif(payment_frequency.get() ==monthly):
            regular_payment = total_amount*4
        else:
            messagebox.showinfo("Error ", "Please select payment frequency")
            return
        
        label_total_cost_payment.config(text = f"${regular_payment:.2f}")

    # I have rounded everything to two decimals as requested.

    def submit():
    # First I will do error checking and if there is an error with the return function will prevent the programme to write the information into the text file.

        if entry_first_name.get().strip() == "" or not entry_first_name.get().strip().isalpha():
            messagebox.showinfo("Error", "Please enter the first name properly.")
            return

        elif entry_last_name.get().strip() == "" or not entry_last_name.get().strip().isalpha():
            messagebox.showinfo("Error", "Please enter the last name properly.")
            return

        elif entry_address.get().strip() == "":
            messagebox.showinfo("Error", "Please enter a valid address.")
            return

        elif not entry_mobile.get().strip().isdigit():
            messagebox.showinfo("Error", "Please enter a valid mobile number.")
            return

        elif member_type.get().strip() == "":
            messagebox.showinfo("Error", "Please select a membership type.")
            return

        elif member_duration.get().strip() == "":
            messagebox.showinfo("Error", "Please select a membership duration.")
            return

        elif payment_frequency.get().strip() == "":
            messagebox.showinfo("Error", "Please select a payment frequency.")
            return
        else:
            # If not errors, we can proceed to write the file.
            # I need to call the calculate function so I can get the costs.
            calculate()

            # Here I make the change so the information will be saved in the SQL database and not in a text file.
            # I am using the code from appendix 3 and I have modified to adjust to my assessment 2.
            conn = sqlite3.connect("gym_database.db")
            cursor = conn.cursor()

            # Create the database
            cursor.execute('''CREATE TABLE IF NOT EXISTS Memberships (
                                MemberID INTEGER PRIMARY KEY NOT NULL,
                                First_Name TEXT NOT NULL,
                                Last_Name TEXT NOT NULL,
                                Address TEXT NOT NULL,
                                Mobile TEXT NOT NULL,
                                Membership_Type TEXT NOT NULL,
                                Membership_Duration TEXT NOT NULL,
                                Direct_Debit BOOLEAN NOT NULL,
                                Extra_1 BOOLEAN NOT NULL,
                                Extra_2 BOOLEAN NOT NULL,
                                Extra_3 BOOLEAN NOT NULL,
                                Extra_4 BOOLEAN NOT NULL,
                                Payment_Frequency TEXT NOT NULL
                                )''')

            # Basic insert new member function
            def insert_new_member(First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency):
                cursor.execute('''INSERT INTO Memberships (First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                (First_Name, Last_Name, Address, Mobile, Membership_Type, Membership_Duration, Direct_Debit, Extra_1, Extra_2, Extra_3, Extra_4, Payment_Frequency))

            # Call insert_new_member with the correct parameters
            insert_new_member(
                First_Name=entry_first_name.get(),
                Last_Name=entry_last_name.get(),
                Address=entry_address.get(),
                Mobile=entry_mobile.get(),
                Membership_Type=member_type.get(),
                Membership_Duration=member_duration.get(),
                Direct_Debit=direct_debit.get(),
                Extra_1=extra1.get(),
                Extra_2=extra2.get(),
                Extra_3=extra3.get(),
                Extra_4=extra4.get(),
                Payment_Frequency=payment_frequency.get()
            )

            # Commit changes and close connection
            conn.commit()
            conn.close()

            # Messagebox to indicate the user the information has been saved. 
            messagebox.showinfo("Thank you!", "The data has been saved successfully")

            # I need to clear the form, I think the fastest way is closing and opening the form again.
            window.destroy()
            gym_app()

    # I have created a new function to return to the previous menu.        
    def return_to_menu():
        window.destroy()


    # ------------------------------
    # Widget definitions
    # ------------------------------
    # The widget definitions are found in this section, no positioning has been done here, just declaration
    # I wil change the color for all the widgets to match the background. 

    #### Labels ####

    label_first_name = tkinter.Label(window, text = "First Name:", background= "light blue")
    label_last_name = tkinter.Label(window, text = "Last Name:", background= "light blue")
    label_address = tkinter.Label(window, text = "Address:", background= "light blue")
    label_mobile = tkinter.Label(window, text = "Mobile:",background= "light blue")

    label_membership_type = tkinter.Label(window, text = "Membership Plan", background= "light blue")
    label_membership_duration = tkinter.Label(window, text = "Membership Duration", background= "light blue")
    label_direct_debit = tkinter.Label(window, text = "Direct Debit", background= "light blue")
    label_payment_frequency = tkinter.Label(window, text = "Payment Frequency", background= "light blue")

    label_optional_extras = tkinter.Label(window, text = "Optional Extras:", background= "light blue")

    label_total_header = tkinter.Label(window, text = "Totals", background= "light blue")
    label_total_base = tkinter.Label(window, text = "Membership:", background= "light blue")
    label_total_extras = tkinter.Label(window, text = "Extras:", background= "light blue")
    label_total_discount = tkinter.Label(window, text = "Discount:", background= "light blue")
    label_total_total = tkinter.Label(window, text = "Total:", background= "light blue")
    label_total_payment = tkinter.Label(window, text = "Regular payment:",background= "light blue")


    label_total_cost_base = tkinter.Label(window, text = "--", background= "light blue")
    label_total_cost_extras = tkinter.Label(window, text = "--",background= "light blue")
    label_total_cost_discount = tkinter.Label(window, text = "--", background= "light blue")
    label_total_cost_total = tkinter.Label(window, text = "--", background= "light blue")
    label_total_cost_payment = tkinter.Label(window, text = "--", background= "light blue")


    #### Entry text boxes ####

    entry_first_name = tkinter.Entry(window, textvariable = name_variable)
    entry_last_name = tkinter.Entry(window, textvariable = last_name_variable)
    entry_address = tkinter.Entry(window, textvariable = address_variable)
    entry_mobile = tkinter.Entry(window, textvariable = mobile_variable)

    #### Radio buttons ####

    radio_member_1 = tkinter.Radiobutton(window, text = basic, variable = member_type, value = basic, background= "light blue")
    radio_member_2 = tkinter.Radiobutton(window, text = regular, variable = member_type, value = regular, background= "light blue")
    radio_member_3 = tkinter.Radiobutton(window, text = premium, variable = member_type, value = premium, background= "light blue")

    radio_duration_1 = tkinter.Radiobutton(window, text = three_months, variable = member_duration, value = three_months, background= "light blue")
    radio_duration_2 = tkinter.Radiobutton(window, text = six_months, variable = member_duration, value = six_months, background= "light blue")
    radio_duration_3 = tkinter.Radiobutton(window, text = twelve_months, variable = member_duration, value = twelve_months, background= "light blue")

    radio_payment_1 = tkinter.Radiobutton(window, text = weekly, variable = payment_frequency, value = weekly, background= "light blue")
    radio_payment_2 = tkinter.Radiobutton(window, text = monthly, variable = payment_frequency, value = monthly, background= "light blue")

    #### Checkbuttons ####

    checkbutton_direct_debit = tkinter.Checkbutton(window, text = "", variable = direct_debit, onvalue = True, offvalue = False, background= "light blue")

    checkbutton_extra1 = tkinter.Checkbutton(window, text = optional_1, variable = extra1, onvalue = True, offvalue = False, background= "light blue")
    checkbutton_extra2 = tkinter.Checkbutton(window, text = optional_2, variable = extra2, onvalue = True, offvalue = False, background= "light blue")
    checkbutton_extra3 = tkinter.Checkbutton(window, text = optional_3, variable = extra3, onvalue = True, offvalue = False, background= "light blue")
    checkbutton_extra4 = tkinter.Checkbutton(window, text = optional_4, variable = extra4, onvalue = True, offvalue = False, background= "light blue")


    #### Buttons ####
    #I have changed the background colour to improve user experience.

    button_calculate = tkinter.Button(window, text = "Calculate", command = calculate, background= "orange")
    button_submit = tkinter.Button(window, text = "Submit", command = submit, background= "orange")
    button_return = tkinter.Button(window, text = "Return", command = return_to_menu, background= "orange")


    # ------------------------------
    # Widget positioning
    # ------------------------------
    # All of the widget positioning is found here
    # Another method of positioning widgets can be used if you comment this code out and use your own design

    label_first_name.grid(row = 0, column = 0, sticky = "w")
    label_last_name.grid(row = 1, column = 0, sticky = "w")
    label_address.grid(row = 2, column = 0, sticky = "w")
    label_mobile.grid(row = 3, column = 0, sticky = "w")

    label_membership_type.grid(row = 4, column = 0, sticky = "w")
    label_membership_duration.grid(row = 7, column = 0, sticky = "w")
    label_direct_debit.grid(row = 10, column = 0, sticky = "w")
    label_payment_frequency.grid(row = 16, column = 0, sticky = "w")

    entry_first_name.grid(row = 0, column = 1, sticky = "w")
    entry_last_name.grid(row = 1, column = 1, sticky = "w")
    entry_address.grid(row = 2, column = 1, sticky = "w")
    entry_mobile.grid(row = 3, column = 1, sticky = "w")

    radio_member_1.grid(row = 4, column = 1, sticky = "w")
    radio_member_2.grid(row = 5, column = 1, sticky = "w")
    radio_member_3.grid(row = 6, column = 1, sticky = "w")

    radio_duration_1.grid(row = 7, column = 1, sticky = "w")
    radio_duration_2.grid(row = 8, column = 1, sticky = "w")
    radio_duration_3.grid(row = 9, column = 1, sticky = "w")

    checkbutton_direct_debit.grid(row = 10, column = 1, sticky = "w")

    label_optional_extras.grid(row = 11, column = 0, sticky = "w")
    checkbutton_extra1.grid(row = 11, column = 1, sticky = "w")
    checkbutton_extra2.grid(row = 12, column = 1, sticky = "w")
    checkbutton_extra3.grid(row = 13, column = 1, sticky = "w")
    checkbutton_extra4.grid(row = 14, column = 1, sticky = "w")

    radio_payment_1.grid(row = 16, column = 1, sticky = "w")
    radio_payment_2.grid(row = 17, column = 1, sticky = "w")

    label_total_header.grid(row = 18, column = 0, sticky = "w")
    label_total_base.grid(row = 19, column = 0, sticky = "w")
    label_total_extras.grid(row = 20, column = 0, sticky = "w")
    label_total_discount.grid(row = 21, column = 0, sticky = "w")
    label_total_total.grid(row = 22, column = 0, sticky = "w")
    label_total_payment.grid(row = 23, column = 0, sticky = "w")

    label_total_cost_base.grid(row = 19, column = 1, sticky = "w")
    label_total_cost_extras.grid(row = 20, column = 1, sticky = "w")
    label_total_cost_discount.grid(row = 21, column = 1, sticky = "w")
    label_total_cost_total.grid(row = 22, column = 1, sticky = "w")
    label_total_cost_payment.grid(row = 23, column = 1, sticky = "w")

    button_calculate.grid(row = 24, column = 0)
    button_submit.grid(row = 24, column = 1)
    button_return.grid(row = 24, column = 2)




