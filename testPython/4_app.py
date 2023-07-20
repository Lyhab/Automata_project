import tkinter as tk
from tkinter import simpledialog, messagebox

def convert(p, q):
    li.append(k[s.index(p)][t.index(q)])
    return k[s.index(p)][t.index(q)]

def check_string():
    li.clear()
    start = s[0]
    q = simpledialog.askstring("Input", "Enter the string to check:")
    if q is not None:
        for i in q:
            start = convert(start, i)
        if li[-1] == last:
            messagebox.showinfo("Result", "The string is accepted!")
        else:
            messagebox.showinfo("Result", "The string is not accepted.")

# Create the main application window
root = tk.Tk()
root.title("State Transition App")

# Add labels and entry fields for NFA input
num_states = tk.simpledialog.askinteger("Input", "Enter the number of states:")
s = []
for i in range(num_states):
    state = simpledialog.askstring("Input", f"Enter state {i + 1}:")
    s.append(state)

num_keys = tk.simpledialog.askinteger("Input", "Enter the number of keys:")
t = []
for i in range(num_keys):
    key = simpledialog.askstring("Input", f"Enter key {i + 1}:")
    t.append(key)

last = simpledialog.askstring("Input", "Enter the final state:")

k = [[0 for _ in range(len(t))] for _ in range(len(s))]
for i in range(len(s)):
    for j in range(len(t)):
        k[i][j] = simpledialog.askstring("Input", f"From {s[i]} if {t[j]} go to:")

li = []  # Define 'li' here

# Create a button to check strings
check_button = tk.Button(root, text="Check String", command=check_string)
check_button.pack()

root.mainloop()
