# Gym Management Application

This is a simple gym management application built using Python and Tkinter for the graphical user interface (GUI), and SQLite for the database management. The app allows gym administrators to manage members, view statistics, and access member information with ease.

This project was developed as part of the **BIT 502 Programming 1** course at **Open Polytechnic**.

## Features

- **Membership Registration**: Users can register new gym members, selecting membership type, duration, and extras.
- **Search Functionality**: Search for existing members based on criteria such as name or membership type.
- **Statistics**: View various statistics about the gym, such as total number of members, number of members per membership type, and extras selected.
- **Help Section**: A basic help section to guide users on how to use the application.

## Installation

To get started with this project, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/gym-management-app.git
cd gym-management-app
```

### 2. Install dependencies:
Make sure you have Python installed. If you need additional libraries, use pip:
```bash
pip install -r requirements.txt
```

### 3. Run the Application:
Once everything is set up, you can start the application:
```bash
python main.py
```

## Project Structure

```bash
gym-management-app/
│
├── main.py               # Main application file (entry point)
├── membership_form.py    # Membership form creation logic
├── search_function.py    # Logic for searching members
├── statistics.py         # Logic for displaying statistics
├── gym_database.db       # SQLite database file for storing member data
├── requirements.txt      # List of dependencies (if any)
└── README.md             # This file
```

## Database Structure

The SQLite database contains a single table, `Memberships`, with the following columns:

- `MemberID`: Primary key, auto-incremented.
- `First_Name`: The member's first name.
- `Last_Name`: The member's last name.
- `Address`: The member's address.
- `Mobile`: The member's mobile phone number.
- `Membership_Type`: Type of membership (e.g., Basic, Regular, Premium).
- `Membership_Duration`: Duration of the membership (e.g., 3 Months, 6 Months, 12 Months).
- `Direct_Debit`: Boolean indicating whether direct debit is selected.
- `Extra_1`, `Extra_2`, `Extra_3`, `Extra_4`: Booleans indicating whether the member has selected various extras.
- `Payment_Frequency`: Payment frequency (e.g., Weekly, Monthly).

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. For major changes, please open an issue first to discuss what you'd like to change.

## License

This project is open-source and available under the MIT License.

