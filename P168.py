import tkinter as tk

def callback():
    """
    callback function for button click
    """
    listbox.insert(tk.END, "Hello World!")

if __name__ == "__main__":
    master = tk.Tk()

    button = tk.Button(master, text="OK", command=callback)
    button.pack()

    listbox = tk.Listbox(master)
    listbox.pack()
    tk.mainloop()