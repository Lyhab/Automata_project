import tkinter as tk
from tkinter import messagebox

class FiniteAutomaton:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()

    def is_deterministic(self):
        # Check if the FA is deterministic or non-deterministic
        for state in self.states:
            for symbol in self.alphabet:
                if (state, symbol) in self.transitions and len(self.transitions[(state, symbol)]) > 1:
                    return False
        return True

    def accepts_string(self, input_string):
        # Test if a string is accepted by the FA
        current_state = self.start_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.accept_states

    def construct_equivalent_dfa(self):
        # Construct an equivalent DFA from an NFA
        dfa = FiniteAutomaton()
        # ...
        return dfa

    def minimize(self):
        # Minimize the DFA
        # ...
        return self

# Create the main application window
window = tk.Tk()
window.title("Finite Automaton (FA) Manager")
window.geometry("300x200")

# Create a FiniteAutomaton instance
fa = FiniteAutomaton()

def design_fa():
    btn_design.config(state=tk.DISABLED)  # Disable the button

    popup = tk.Toplevel(window)
    popup.title("Finite Automaton Designer")

    def close_popup():
        btn_design.config(state=tk.NORMAL)  # Enable the button
        popup.destroy()

    popup.protocol("WM_DELETE_WINDOW", close_popup)  # Handle window close event

    # Create labels and entry widgets for user input
    states_label = tk.Label(popup, text="States (comma-separated):")
    states_label.pack()
    states_entry = tk.Entry(popup)
    states_entry.pack()

    alphabet_label = tk.Label(popup, text="Alphabet (comma-separated):")
    alphabet_label.pack()
    alphabet_entry = tk.Entry(popup)
    alphabet_entry.pack()

    transitions_label = tk.Label(popup, text="Transitions (source, input, destination; semicolon-separated):")
    transitions_label.pack()
    transitions_entry = tk.Entry(popup)
    transitions_entry.pack()

    initial_state_label = tk.Label(popup, text="Initial State:")
    initial_state_label.pack()
    initial_state_entry = tk.Entry(popup)
    initial_state_entry.pack()

    final_states_label = tk.Label(popup, text="Final States (comma-separated):")
    final_states_label.pack()
    final_states_entry = tk.Entry(popup)
    final_states_entry.pack()

    def create_fa():
        # Retrieve user input from entry widgets
        states = states_entry.get().split(',')
        alphabet = alphabet_entry.get().split(',')
        transitions = [tuple(transition.split(',')) for transition in transitions_entry.get().split(';')]
        initial_state = initial_state_entry.get()
        final_states = final_states_entry.get().split(',')

        # Call your function to create the FA with the provided input
        # Example: create_fa(states, alphabet, transitions, initial_state, final_states)
        # Replace this line with your own function call

        close_popup()  # Close the popup window

    # Create a button to create the FA
    btn_create = tk.Button(popup, text="Create FA", command=create_fa)
    btn_create.pack(pady=5)
    
def test_deterministic():
    # Test if a FA is deterministic or non-deterministic
    if fa.is_deterministic():
        messagebox.showinfo("Information", "The FA is deterministic")
    else:
        messagebox.showinfo("Information", "The FA is non-deterministic")

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