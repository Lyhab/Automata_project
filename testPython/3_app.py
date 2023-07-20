import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox

def convert_nfa_to_dfa():
    nfa = {}
    n = int(states_entry.get())
    t = int(transitions_entry.get())

    for i in range(n):
        state = states[i].get()
        nfa[state] = {}
        for j in range(t):
            path = transitions[j].get()
            print("Enter end state from state {} travelling through path {} : ".format(state, path))
            reaching_state = [x for x in end_states[i][j].get().split()]
            nfa[state][path] = reaching_state

    new_states_list = []
    dfa = {}
    keys_list = list(list(nfa.keys())[0])
    path_list = list(nfa[keys_list[0]].keys())

    dfa[keys_list[0]] = {}
    for y in range(t):
        var = "".join(nfa[keys_list[0]][path_list[y]])
        dfa[keys_list[0]][path_list[y]] = var
        if var not in keys_list:
            new_states_list.append(var)
            keys_list.append(var)

    while len(new_states_list) != 0:
        dfa[new_states_list[0]] = {}
        for _ in range(len(new_states_list[0])):
            for i in range(len(path_list)):
                temp = []
                for j in range(len(new_states_list[0])):
                    temp += nfa[new_states_list[0][j]][path_list[i]]
                s = "".join(temp)
                if s not in keys_list:
                    new_states_list.append(s)
                    keys_list.append(s)
                dfa[new_states_list[0]][path_list[i]] = s

        new_states_list.remove(new_states_list[0])

    result_label.config(text="DFA: " + str(dfa))
    dfa_table = pd.DataFrame(dfa)
    print(dfa_table.transpose())

    dfa_states_list = list(dfa.keys())
    dfa_final_states = []
    for x in dfa_states_list:
        for i in x:
            if i in nfa_final_state.get().split():
                dfa_final_states.append(x)
                break

    messagebox.showinfo("Final States", "Final states of the DFA are: " + str(dfa_final_states))

# Create the main application window
root = tk.Tk()
root.title("NFA to DFA Converter")

# Add labels and entry fields for NFA input
states_label = tk.Label(root, text="No. of states:")
states_label.grid(row=0, column=0)
states_entry = tk.Entry(root)
states_entry.grid(row=0, column=1)

transitions_label = tk.Label(root, text="No. of transitions:")
transitions_label.grid(row=1, column=0)
transitions_entry = tk.Entry(root)
transitions_entry.grid(row=1, column=1)

states = []
transitions = []
end_states = []

def create_nfa_inputs():
    num_states = int(states_entry.get())
    num_transitions = int(transitions_entry.get())

    for i in range(num_states):
        state_label = tk.Label(root, text=f"State {i + 1}:")
        state_label.grid(row=i + 2, column=0)
        state_entry = tk.Entry(root)
        state_entry.grid(row=i + 2, column=1)
        states.append(state_entry)

        end_states_row = []
        for j in range(num_transitions):
            transition_label = tk.Label(root, text=f"Path {j + 1}:")
            transition_label.grid(row=i + 2, column=j + 2)
            transition_entry = tk.Entry(root)
            transition_entry.grid(row=i + 2, column=j + 3)
            end_states_row.append(transition_entry)
        end_states.append(end_states_row)

create_inputs_button = tk.Button(root, text="Create NFA Inputs", command=create_nfa_inputs)
create_inputs_button.grid(row=0, column=2, columnspan=1)

convert_button = tk.Button(root, text="Convert NFA to DFA", command=convert_nfa_to_dfa)
convert_button.grid(row=1, column=2, columnspan=1)

nfa_final_label = tk.Label(root, text="Enter final state(s) of NFA (separate multiple states with space):")
nfa_final_label.grid(row=0, column=3, columnspan=4)
nfa_final_state = tk.Entry(root)
nfa_final_state.grid(row=1, column=3)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=1)

root.mainloop()
