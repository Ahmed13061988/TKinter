import tkinter as tk

window = tk.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I'm a Label", font=("Arial", 24))
my_label.pack()

my_label.config(text="Press")

# Button




button2 = tk.Button(text="Rami")
button2.pack()

# Entry

input = tk.Entry(width=10)
users_value = input.get()
input.pack()


def button_clicked():
    my_label.config(text=input.get())


button = tk.Button(text="Click me!", command=button_clicked)
button.pack()

window.mainloop()
