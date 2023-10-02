import tkinter as tk


def button_clicked():
    my_label.config(text=input.get())


window = tk.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I'm a Label", font=("Arial", 24))

my_label.config(text="Press")

# Button
new_botton = tk.Button()

# Entry

input = tk.Entry(width=10)

button = tk.Button(text="Click me!", command=button_clicked)
my_label.grid(column=0, row=0)
button.grid(column=2, row=2)
new_botton.grid(column=3, row=0)
input.grid(column=4, row=4)

window.mainloop()
