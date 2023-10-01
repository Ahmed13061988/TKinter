import tkinter as tk

window = tk.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I'm a Label", font=("Arial", 24))
my_label.pack(side="left")


# def my_function(a=1, b=4, c=10):
#     return a + b * c
#
#
# result = 0
# result = my_function()
# print(result)

def add(*arg):
    for i in arg:
        print(i)
add(1,2,3,4,5,6,7,"a")

window.mainloop()
