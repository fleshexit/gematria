from ciphers import Ciphers


def calculate_alphanumeric_qabbala_value(user_input):
    user_input = user_input.upper()  
    ciphers = Ciphers()
    ciphers.alphanumeric_qabbala() 

    value = 0
    for char in user_input:
        if char in ciphers.gematria:
            value += ciphers.gematria[char]

    return value
# 
# user_input = input("Enter a string: ")
# result = calculate_alphanumeric_qabbala_value(user_input)
# print(f"The alphanumeric qabbala value of '{user_input}' is: {result}")
# 
# 

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.master.configure(background="#000000")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter a string:")
        self.label.pack(side="top")

        self.entry = tk.Entry(self)
        self.entry.pack(side="top")

        self.button = tk.Button(self, text="Calculate", command=self.calculate)
        self.button.pack(side="top")

        self.result = tk.Label(self, text="")
        self.result.pack(side="top")

    def calculate(self):
        user_input = self.entry.get()
        result = calculate_alphanumeric_qabbala_value(user_input)
        self.result["text"] = f"'{user_input}' = AQ-{result}"


app = Application(master=tk.Tk())
app.master.title("Alphanumeric Qabbala Calculator")
app.master.geometry("300x150")
app.master.resizable(False, False)

app.mainloop()