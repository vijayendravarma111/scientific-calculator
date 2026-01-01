import tkinter as tk
import math

def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))


def click(x):
    entry.insert(tk.END, x)

def clear():
    entry.delete(0, tk.END)

def backspace():
    if entry.get():
        entry.delete(len(entry.get()) - 1, tk.END)

def calci():
    try:
        expr = entry.get()
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Zero Division Error")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Math Error")


root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#1c1c1c")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="#d9d9d9",
    fg="black",
    bd=2,
    relief="solid",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=8)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '+',
    '0', '.', ')', '-',
    'sin(', 'cos(', 'tan(', '='
]

r, c = 1, 0

for b in buttons:
    cmd = calci if b == "=" else lambda x=b: click(x)

    if b in "+-*/":
        bg, fg = "#f4c430", "black"
    elif b in ["sin(", "cos(", "tan(", ")", "="]:
        bg, fg = "#555555", "white"
    else:
        bg, fg = "#2b2b2b", "white"

    tk.Button(
        root,
        text=b,
        command=cmd,
        bg=bg,
        fg=fg,
        font=("Segoe UI", 12),
        bd=0,
        width=6,
        height=2
    ).grid(row=r, column=c, padx=5, pady=5)

    c += 1
    if c == 4:
        c = 0
        r += 1


tk.Button(
    root,
    text="⌫",
    command=backspace,
    bg="#888888",
    fg="black",
    font=("Segoe UI", 12),
    bd=0,
    width=12,
    height=2
).grid(row=r, column=0, columnspan=2, pady=6)

tk.Button(
    root,
    text="Clear",
    command=clear,
    bg="#e53935",
    fg="white",
    font=("Segoe UI", 12),
    bd=0,
    width=12,
    height=2
).grid(row=r, column=2, columnspan=2, pady=6)

root.mainloop()
