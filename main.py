from ciphers import Ciphers
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('Enter a string:')
        self.entry = QLineEdit()
        self.button = QPushButton('Calculate', self)
        self.result = QLabel()

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.entry)
        vbox.addWidget(self.button)
        vbox.addWidget(self.result)
        vbox.setSpacing(10)
        vbox.setContentsMargins(10, 10, 10, 10)

        self.setLayout(vbox)

        self.button.clicked.connect(self.calculate)

        self.setWindowTitle('Alphanumeric Qabbala Calculator')
        self.setGeometry(200, 200, 250, 120)  # Adjusted window size
        self.show()

    def calculate(self):
        user_input = self.entry.text().strip()  # strip whitespace

        if not user_input:
            self.result.setText("Please enter a string.")
            return

        #if not user_input.isalpha(): # temporary, until i add logic for AQ numbers
        #    self.result.setText("Input must contain only letters.")
        #    return

        result = calculate_alphanumeric_qabbala_value(user_input)
        self.result.setText(f"'{user_input}' = AQ- {result}")

def calculate_alphanumeric_qabbala_value(user_input):

    user_input = user_input.upper()
    aq = Ciphers('Alphanumeric Qabbala')
    aq.alphanumeric_qabbala()

    value = 0
    for char in user_input: # iterate through string
        if char in aq.gematria: # check if char is in dict
            value += aq.gematria[char] # add value to total

    return value


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
