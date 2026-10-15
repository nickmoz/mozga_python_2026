import tkinter


def button_action():
    name = textfield.get()
    message = f"Hello {name}"
    label.configure(text=message)


window = tkinter.Tk()
window.title("Simple Window")
window.geometry("400x300")

textfield = tkinter.Entry(window)
textfield.grid(row=0, column=0)

button = tkinter.Button(window, text="Go", command=button_action)
button.grid(row=1, column=0)

label = tkinter.Label(window, text="---")
label.grid(row=2, column=0)


window.mainloop()
