from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox
import ciphers  

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Alphanumeric Qabbala Calculator')
        self.setFixedSize(400, 300)  

        self.cipher_label = QLabel('Ciphers:')
        self.cipher_checkboxes = [
            QCheckBox('Alphanumeric Qabbala', self),
            QCheckBox('English Ordinal', self),
            QCheckBox('Synx', self),
        ]

        self.prompt_label = QLabel('Enter a string:')
        self.entry = QLineEdit()
        self.calc_button = QPushButton('Calculate', self)
        self.result_label = QLabel()

        vbox = QVBoxLayout()
        vbox.addWidget(self.cipher_label)
        for checkbox in self.cipher_checkboxes:
            vbox.addWidget(checkbox)

        vbox.addWidget(self.prompt_label)
        vbox.addWidget(self.entry)
        vbox.addWidget(self.calc_button)
        vbox.addWidget(self.result_label)

        vbox.setSpacing(10)
        vbox.setContentsMargins(10, 10, 10, 10)
        self.setLayout(vbox)

        self.calc_button.clicked.connect(self.calculate)

        self.show()

    def calculate(self):
        user_input = self.entry.text().strip()  # strip whitespace

        if not user_input:
            self.result_label.setText("Please enter a string.")
            return

        selected_ciphers = [checkbox.text() for checkbox in self.cipher_checkboxes if checkbox.isChecked()]

        if not selected_ciphers:
            self.result_label.setText("Please select at least one cipher.")
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

        self.result_label.setText("\n".join(result_texts))


if __name__ == '__main__':
    app = QApplication([])
    window = Application()
    app.exec_()
