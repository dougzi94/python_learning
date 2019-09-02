import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setWindowTitle('calculator')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        keyboard = []
        
        button_1 = QPushButton('1')
        button_2 = QPushButton('2')
        button_3 = QPushButton('3')

        
        grid.addWidget(button_1, 0, 1)
        grid.addWidget(button_2, 0, 2)
        grid.addWidget(button_3, 0, 3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = calculator()
    sys.exit(app.exec_())
