import tkinter as tk

window = tk.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I'm a Label", font=("Arial", 24))
my_label.pack()

my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked!")


button = tk.Button(text="Click me!", command=button_clicked)
button.pack()

window.mainloop()
