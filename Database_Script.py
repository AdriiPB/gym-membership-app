
# Imports

import sqlite3

# Connect to our database (or create a new one if none exists)

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


# Populate the database with some data
insert_new_member("Chris", "Redfield", "21 Patrick St", "555-3840", "Basic", "3 Months", False, True, False, False, True, "Weekly")
insert_new_member("Jill", "Valentine", "16 Houston St", "555-3350", "Regular", "6 Months", True, False, False, True, True, "Weekly")
insert_new_member("Sherlock", "Holmes", "221B Baker St, London", "39857693", "Premium", "12 Months", True, False, False, False, True, "Monthly")
insert_new_member("Frank", "West", "19 Hitch Ln, Willamette", "555-3947", "Regular", "3 Months", True, False, False, True, False, "Weekly")
insert_new_member("Atticus", "Finch", "98 Windfall Rd, Tirau", "555-9827", "Basic", "6 Months", False, False, True, True, True, "Monthly")
insert_new_member("Dorothy", "Gale", "1 Yellow St, Warkworth", "555-1984", "Basic", "12 Months", True, True, True, True, False, "Monthly")
insert_new_member("Steven", "Rogers", "32 Frost Cr, Hamilton", "555-1920", "Premium", "12 Months", False, True, True, True, True, "Monthly")

# Example function to show current members
def show_all_members():
    for row in cursor.execute('''SELECT * FROM Memberships'''):
        print(row)

show_all_members()

# Close the database before exiting
conn.commit()
conn.close()