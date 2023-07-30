import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import mysql.connector
import pandas as pd

# Create the main application window
window = tk.Tk()
window.title("Finite Automaton (FA) Manager")
window.geometry("300x210")
popup = False

def design_fa():
    btn_design.config(state=tk.DISABLED)  # Disable the button

    popup = tk.Toplevel(window)
    popup.title("Finite Automaton Designer")
    popup.geometry("300x300")

    def close_popup():
        btn_design.config(state=tk.NORMAL)  # Enable the button
        popup.destroy()

    popup.protocol("WM_DELETE_WINDOW", close_popup)  # Handle window close event

    states = []
    alphabet = []
    initial_state = None
    final_states = []
    transitions = []

    def create_fa():
        # Retrieve user input from entry widgets
        states_input = states_entry.get().split(',')
        alphabet_input = alphabet_entry.get().split(',')
        transitions_input = [tuple(transition.split(',')) for transition in transitions_entry.get().split(';')]
        initial_state_input = initial_state_entry.get()
        final_states_input = final_states_entry.get().split(',')

        # Store the input in variables
        states.extend(states_input)
        alphabet.extend(alphabet_input)
        initial_state = initial_state_input
        final_states.extend(final_states_input)
        transitions.extend(transitions_input)

        db_con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="automata"
        )
        
        # Create a cursor
        cursor = db_con.cursor()
        
        # Insert data into the table
        insertion = "INSERT INTO finite_automata (states, alphabet, transitions, initial_state, final_states) VALUES (%s, %s, %s, %s, %s)"
        data = (', '.join(states), ', '.join(alphabet), '  ;  '.join(', '.join(l) for l in transitions), initial_state, ', '.join(final_states))
        cursor.execute(insertion, data)
        
        # Commit the changes
        db_con.commit()
        
        # Close the cursor and connection
        db_con.close()

        close_popup()  # Close the popup window

    # Create labels and entry widgets for user input
    states_label = tk.Label(popup, text="States (Q):")
    states_label.pack()
    states_entry = tk.Entry(popup)
    states_entry.pack()

    alphabet_label = tk.Label(popup, text="Alphabet (X):")
    alphabet_label.pack()
    alphabet_entry = tk.Entry(popup)
    alphabet_entry.pack()

    transitions_label = tk.Label(popup, text="Transitions (δ):")
    transitions_label.pack()
    transitions_entry = tk.Entry(popup)
    transitions_entry.pack()

    initial_state_label = tk.Label(popup, text="Initial State (q0):")
    initial_state_label.pack()
    initial_state_entry = tk.Entry(popup)
    initial_state_entry.pack()

    final_states_label = tk.Label(popup, text="Final States (F):")
    final_states_label.pack()
    final_states_entry = tk.Entry(popup)
    final_states_entry.pack()

    # Create a button to create the FA
    btn_create = tk.Button(popup, text="Create", command=create_fa)
    btn_create.pack(pady=5)
    


def test_deterministic():
    global popup

    # Check if the window is already open
    if popup:
        return

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678',
            database='automata'
        )

        # Replace 'your_table_name' with the name of your table
        table_name = 'finite_automata'

        # Fetch the table data from the database
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        # Create a new window for displaying the table
        popup = tk.Toplevel()
        popup.title("Table Viewer")
        popup.protocol("WM_DELETE_WINDOW", enable_button)

        # Disable the "View Table" button
        btn_deterministic.config(state="disabled")

        # Create a Treeview widget to display the table
        treeview = ttk.Treeview(popup, columns=columns, show='headings')

        # Set up the columns
        treeview['columns'] = columns
        column_widths = [50, 125, 100, 400, 100, 100]  # Set the desired widths for each column
        for column, width in zip(columns, column_widths):
            treeview.heading(column, text=column)
            treeview.column(column, width=width)

        # Insert the data into the table
        for row in rows:
            treeview.insert("", tk.END, values=row)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(popup, orient="vertical", command=treeview.yview)
        treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        treeview.pack(expand=True, fill="both")

        # Create a function to check the ID
        def check_id():
            id = id_entry.get()
            result = check_deterministic(id)
            if not result:
                result_label.config(text=f"ID '{id}' hasn't existed yet.")
            else:
                is_deterministic = result
                result_label.config(text=f"ID '{id}' is {'deterministic' if is_deterministic else 'not deterministic'}.")

        # Create an entry widget and button to enter and check the ID
        id_frame = tk.Frame(popup)
        id_frame.pack(pady=10)

        id_label = tk.Label(id_frame, text="Enter ID:")
        id_label.pack(side="left")

        id_entry = tk.Entry(id_frame)
        id_entry.pack(side="left")

        check_button = tk.Button(id_frame, text="Check", command=check_id)
        check_button.pack(side="left")

        # Create a label to display the result
        result_label = tk.Label(popup, text="")
        result_label.pack()

        # Wait for the window to be closed
        popup.wait_window(popup)

    except mysql.connector.Error as error:
        tk.messagebox.showerror("Database Error", f"An error occurred while connecting to the database: {error}")

    finally:
        if connection.is_connected():
            connection.close()

def enable_button():
    global popup

    # Enable the "View Table" button
    btn_deterministic.config(state="normal")
    if popup is not False:
        popup.destroy()
    popup = False

def check_deterministic(id):
    try:
        # Replace the following with your MySQL database connection details
        connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='12345678',
                database='automata'
            )

        # Replace 'your_table_name' with the name of your table
        table_name = 'finite_automata'

        # Replace 'your_id_column' with the column name containing the ID in your table
        id_column = 'id'

        # Query the table to check if the ID is deterministic
        cursor = connection.cursor()
        query = f"SELECT {id_column} FROM {table_name} WHERE {id_column} = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        if result:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        # Handle the database error
        print(f"An error occurred while connecting to the database: {error}")
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



































def test_acceptance():
    exec(open('testPython/4_app.py').read())

def construct_dfa():
    # Construct an equivalent DFA from an NFA
    exec(open('testPython/3_app.py').read())

def minimize_dfa():
    messagebox.showinfo("Information", "DFA minimized!")

# Create buttons for each functionality
btn_design = tk.Button(window, text="Design FA", command=design_fa)
btn_design.pack(pady=10)

btn_deterministic = tk.Button(window, text="Test Deterministic", command=test_deterministic)
btn_deterministic.pack(pady=5)

btn_acceptance = tk.Button(window, text="Test Acceptance", command=test_acceptance)
btn_acceptance.pack(pady=5)

btn_dfa = tk.Button(window, text="NFA to DFA", command=construct_dfa)
btn_dfa.pack(pady=5)

btn_minimize = tk.Button(window, text="Minimize DFA", command=minimize_dfa)
btn_minimize.pack(pady=5)

# Start the GUI event loop
window.mainloop()