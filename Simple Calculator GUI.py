import tkinter as tk
from tkinter import messagebox
import json
import os

HISTORY_FILE = 'history.json'


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return[]


def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)
        
        
def add_to_history(expression, result):
    history = load_history()
    history.append({'expression': expression, 'result': result})
    save_history(history)
    
    
def show_history():
    history = load_history()
    if not history:
        messagebox.showinfo('History', 'No calculations yet.')
        return
    history_text = '\n'.join([f'{item["expression"]} = {item["result"]}' for item in history])
    messagebox.showinfo('Calculation History', history_text)
    
    
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)
    
    
def clear():
    entry.delete(0, tk.END)
    
    
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])


def percentage():
    try:
        current = float(entry.get())
        result = current / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        messagebox.showerror('Error', 'Invalid percentage calculation.')
        
        
def calculate():
    try:
        expression = entry.get().replace('×', '*').replace('÷', '/')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        add_to_history(expression, result)
    except:
        messagebox.showerror('Error', 'Invalid calculation.')
        
        
root = tk.Tk()
root.title('Simple Calculator')
root.geometry('370x500')
root.config(bg='#1e1e1e')
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), bd=0, bg='#2e2e2e', fg='white', insertbackground='white', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=15, padx=10, ipady=15)

btn_bg = '#3b3b3b'
btn_fg = 'white'
op_bg = '#ff9f43'
special_bg = '#ff4b4b'


def create_button(text, row, col,command, bg_color=btn_bg):
    btn = tk.Button(root, text=text, font=('Arial', 18), bg=bg_color, fg=btn_fg, activebackground='#5a5a5a',
                    activeforeground='white', relief='flat', width=5,
                    height=2, command=command)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')


buttons = [
    ('c', 1, 0, clear, special_bg),
    ('⌫', 1, 1, backspace, special_bg),
    ('%', 1, 2, percentage, op_bg),
    ('÷', 1, 3, lambda: click_button('÷'), op_bg),
    
    ('7', 2, 0, lambda: click_button('7')),
    ('8', 2, 1, lambda: click_button('8')),
    ('9', 2, 2, lambda: click_button('9')),
    ('×', 2, 3, lambda: click_button('×'), op_bg),
    
    ('4', 3, 0, lambda: click_button('4')),
    ('5', 3, 1, lambda: click_button('5')),
    ('6', 3, 2, lambda: click_button('6')),
    ('-', 3, 3, lambda: click_button('-'), op_bg),
    
    ('1', 4, 0, lambda: click_button('1')),
    ('2', 4, 1, lambda: click_button('2')),
    ('3', 4, 2, lambda: click_button('3')),
    ('+', 4, 3, lambda: click_button('+'), op_bg),
    
    ('0', 5, 0, lambda: click_button('0')),
    ('.', 5, 1, lambda: click_button('.')),
    ('History', 5, 2, show_history, '#3498db'),
    ('=', 5, 3, calculate, '#2ecc71'),
    ]


for (text, row, col, cmd, *color) in buttons:
    create_button(text, row, col, cmd, color[0] if color else btn_bg)


root.mainloop()
        
        