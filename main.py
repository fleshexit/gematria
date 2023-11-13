import ciphers
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Alphanumeric Qabbala Calculator')
        self.setGeometry(200, 200, 400, 150)  

        self.cipher_label = QLabel('Ciphers:')
        self.cipher_combo = QComboBox(self)
        self.cipher_combo.addItems(['Alphanumeric Qabbala', 'English Ordinal', 'Synx'])

        self.prompt_label = QLabel('Enter a string:')
        self.entry = QLineEdit()
        self.calc_button = QPushButton('Calculate', self)
        self.result_label = QLabel()

        vbox = QVBoxLayout()
        vbox.addWidget(self.cipher_label)
        vbox.addWidget(self.cipher_combo)
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
        
        if self.cipher_combo.currentText() == "Alphanumeric Qabbala":
            aq = ciphers.AlphanumericQabbala()
            result = aq.calculate(user_input)
            self.result_label.setText(f"'{user_input}' = AQ - {result}")
        
        elif self.cipher_combo.currentText() == "English Ordinal":
            eo = ciphers.EnglishOrdinal()
            result = eo.calculate(user_input)
            self.result_label.setText(f"'{user_input}' = EO - {result}")

        else:
            self.result_label.setText("Support for this cipher will be coming soon.")


if __name__ == '__main__':
    app = QApplication([])
    window = Application()
    app.exec_()
