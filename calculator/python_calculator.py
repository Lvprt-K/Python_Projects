#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

def clear_entry():
    input_text.set("")

def insert_value(value):
    current_text = input_text.get()
    input_text.set(current_text + value)

def calculate_result():
    try:
        expression = input_text.get()
        if expression:
            result = eval(expression)
            input_text.set(expression + " = " + str(result))
    except Exception as e:
        input_text.set("Error")

root = tk.Tk()
root.geometry("240x300")
root.title("Calculator")
root.maxsize(240, 300)
root.minsize(240, 300)

input_text = tk.StringVar()

# Entry Widget
inp = tk.Entry(root, width=20, borderwidth=3, relief=tk.RIDGE, textvariable=input_text)
inp.grid(pady=10, row=0, column=0, columnspan=4)

# Define Buttons and their actions
buttons = [
    ('C', 'red', 'white', clear_entry),
    ('7', 'black', 'white', lambda: insert_value('7')),
    ('8', 'black', 'white', lambda: insert_value('8')),
    ('9', 'black', 'white', lambda: insert_value('9')),
    ('/', 'black', 'white', lambda: insert_value('/')),
    ('4', 'black', 'white', lambda: insert_value('4')),
    ('5', 'black', 'white', lambda: insert_value('5')),
    ('6', 'black', 'white', lambda: insert_value('6')),
    ('*', 'black', 'white', lambda: insert_value('*')),
    ('1', 'black', 'white', lambda: insert_value('1')),
    ('2', 'black', 'white', lambda: insert_value('2')),
    ('3', 'black', 'white', lambda: insert_value('3')),
    ('-', 'black', 'white', lambda: insert_value('-')),
    ('0', 'black', 'white', lambda: insert_value('0')),
    ('00', 'black', 'white', lambda: insert_value('00')),
    ('.', 'black', 'white', lambda: insert_value('.')),
    ('+', 'black', 'white', lambda: insert_value('+')),
    ('%', 'black', 'white', lambda: insert_value('%')),
    ('=', 'red', 'white', calculate_result)
]

row_val = 1
col_val = 0

# Creating buttons dynamically
for button in buttons:
    btn_text, btn_bg, btn_fg, btn_command = button
    tk.Button(root, text=btn_text, width=4, height=2, bg=btn_bg, fg=btn_fg, relief=tk.RIDGE, command=btn_command).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()


# In[ ]:




