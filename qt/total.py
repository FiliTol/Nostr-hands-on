import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel
from scripts.post import posting
from scripts.one_query import querying
import asyncio


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('NostrApp')

        # Left vertical layout
        left_layout = QVBoxLayout()

        # Top left horizontal layout
        top_left_layout = QHBoxLayout()
        self.input_text = QLineEdit()
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_text)
        top_left_layout.addWidget(self.input_text)
        top_left_layout.addWidget(self.submit_button)

        # Bottom left horizontal layout
        bottom_left_layout = QHBoxLayout()
        self.bottom_button = QPushButton('Show Text')
        self.bottom_button.clicked.connect(self.show_text)
        bottom_left_layout.addWidget(self.bottom_button)

        left_layout.addLayout(top_left_layout)
        left_layout.addLayout(bottom_left_layout)

        # Right vertical layout
        self.output_text = QTextEdit()

        # Main horizontal layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.output_text)

        self.setLayout(main_layout)

        self.show()

    def submit_text(self):
        note_text = self.input_text.text()
        posting(note_text)

    async def show_text(self):
        querying()
        await self.output_text.append()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
