import tkinter as tk
from tkinter import messagebox

import mysql.connector

# Create the main application window
window = tk.Tk()
window.title("Finite Automaton (FA) Manager")
window.geometry("300x210")

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
    btn_deterministic.config(state=tk.DISABLED)  # Disable the button

    popup = tk.Toplevel(window)
    popup.title("Finite Automaton Designer")
    popup.geometry("300x100")

    def close_popup():
        btn_deterministic.config(state=tk.NORMAL)  # Enable the button
        popup.destroy()

    popup.protocol("WM_DELETE_WINDOW", close_popup)  # Handle window close event

    # Test if a FA is deterministic or non-deterministic
    def check_deterministic(selected_fa):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='12345678',
                database='automata'
            )

            cursor = connection.cursor()
            query = "SELECT id, transitions FROM finite_automata WHERE id=%s"
            cursor.execute(query, (selected_fa,))
            result = cursor.fetchone()

            if not result:
                messagebox.showinfo("ID Not Found", f"ID '{selected_fa}' not found in the database.")
            else:
                name, is_deterministic = result
                messagebox.showinfo("ID Information", f"ID: {id}\nDeterministic: {'Yes' if is_deterministic else 'No'}")

        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"An error occurred while connecting to the database: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        close_popup()  # Close the popup window

    def on_button_click():
        selected_fa = entry.get()
        check_deterministic(selected_fa)

    # GUI Setup
    label = tk.Label(popup, text="Enter FA ID:")
    label.pack()

    entry = tk.Entry(popup)
    entry.pack()

    button = tk.Button(popup, text="Check Deterministic", command=on_button_click)
    button.pack()



def test_acceptance():
    # Test if a string is accepted by an FA
    input_string = messagebox.askstring("Input", "Enter an input string:")
    if input_string is not None:
        if fa.accepts_string(input_string):
            messagebox.showinfo("Information", "Accepted")
        else:
            messagebox.showinfo("Information", "Rejected")

def construct_dfa():
    # Construct an equivalent DFA from an NFA
    dfa = fa.construct_equivalent_dfa()
    messagebox.showinfo("Information", "Equivalent DFA constructed")

def minimize_dfa():
    # Minimize the DFA
    fa.minimize()
    messagebox.showinfo("Information", "DFA minimized!")

# Create buttons for each functionality
btn_design = tk.Button(window, text="Design FA", command=design_fa)
btn_design.pack(pady=10)

btn_deterministic = tk.Button(window, text="Test Deterministic", command=test_deterministic)
btn_deterministic.pack(pady=5)

btn_acceptance = tk.Button(window, text="Test Acceptance", command=test_acceptance)
btn_acceptance.pack(pady=5)

btn_dfa = tk.Button(window, text="Construct DFA", command=construct_dfa)
btn_dfa.pack(pady=5)

btn_minimize = tk.Button(window, text="Minimize DFA", command=minimize_dfa)
btn_minimize.pack(pady=5)

# Start the GUI event loop
window.mainloop()