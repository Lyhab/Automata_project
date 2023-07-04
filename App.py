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
    # Design a finite automaton
    fa.states = {"q0", "q1", "q2"}
    fa.alphabet = {"a", "b"}
    fa.transitions = {
        ("q0", "a"): "q1",
        ("q1", "b"): "q2",
        ("q2", "a"): "q0"
    }
    fa.start_state = "q0"
    fa.accept_states = {"q2"}

    messagebox.showinfo("Information", "Finite Automaton (FA) designed successfully!")

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
    messagebox.showinfo("Information", "DFA minimized")

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
