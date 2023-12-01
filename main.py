import tkinter as tk
from tkinter import ttk
import ciphers

# planning a move to customtkinter.py

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Alphanumeric Qabbala Calculator')
        self.geometry('400x300')

        self.cipher_label = tk.Label(self, text='Ciphers:')
        self.cipher_checkboxes = [
            ttk.Checkbutton(self, text='Alphanumeric Qabbala'),
            ttk.Checkbutton(self, text='English Ordinal'),
            ttk.Checkbutton(self, text='Synx'),
        ]

        self.prompt_label = tk.Label(self, text='Enter a string:')
        self.entry = tk.Entry(self)
        self.calc_button = tk.Button(self, text='Calculate', command=self.calculate)
        self.result_label = tk.Label(self, text='')

        self.cipher_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))
        for i, checkbox in enumerate(self.cipher_checkboxes, start=1):
            checkbox.grid(row=i, column=0, columnspan=2, sticky='w')

        self.prompt_label.grid(row=len(self.cipher_checkboxes) + 1, column=0, columnspan=2, pady=(10, 0))
        self.entry.grid(row=len(self.cipher_checkboxes) + 2, column=0, columnspan=2, pady=(0, 10))
        self.calc_button.grid(row=len(self.cipher_checkboxes) + 3, column=0, columnspan=2, pady=(0, 10))
        self.result_label.grid(row=len(self.cipher_checkboxes) + 4, column=0, columnspan=2, pady=(10, 0))

    def calculate(self):
        user_input = self.entry.get().strip()

        if not user_input:
            self.result_label.config(text="Please enter a string.")
            return

        selected_ciphers = [checkbox.cget("text") for checkbox in self.cipher_checkboxes if checkbox.instate(['selected'])]

        if not selected_ciphers:
            self.result_label.config(text="Please select at least one cipher.")
            return

        result_texts = []
        for cipher_name in selected_ciphers:
            if cipher_name == "Alphanumeric Qabbala":
                aq = ciphers.AlphanumericQabbala()
                result_texts.append(f"'{user_input}' = AQ - {aq.calculate(user_input)}")

            elif cipher_name == "English Ordinal":
                eo = ciphers.EnglishOrdinal()
                result_texts.append(f"'{user_input}' = EO - {eo.calculate(user_input)}")

            else:
                result_texts.append(f"Support for '{cipher_name}' will be coming soon.")

        self.result_label.config(text="\n".join(result_texts))


if __name__ == '__main__':
    app = Application()
    app.mainloop()
