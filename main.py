import ciphers
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

        aq = ciphers.AlphanumericQabbala()
        result = aq.calculate(user_input)
        self.result.setText(f"'{user_input}' = AQ - {result}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
