import tkinter as tk
from tkinter import messagebox
import mysql.connector

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

def on_button_click():
    selected_fa = entry.get()
    check_deterministic(selected_fa)

# GUI Setup
root = tk.Tk()
root.title("Deterministic FA Checker")

label = tk.Label(root, text="Enter FA ID:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Check Deterministic", command=on_button_click)
button.pack()

root.mainloop()
