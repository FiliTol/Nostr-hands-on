import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel, \
    QMessageBox
from scripts.post import posting, view_pubkey
from scripts.one_query import querying
from scripts.relay import test_relay
from scripts.qrcode_generator import set_qr_label
import asyncio


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.relay = "ws://192.168.1.94:808"
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('NostrApp')

        # Left vertical layout
        left_layout = QVBoxLayout()

        # QR code tests
        qrcode_left_layout = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 200, 200)
        set_qr_label(self.label, view_pubkey())
        qrcode_left_layout.addWidget(self.label)

        # Top left horizontal layout
        top_left_layout = QHBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setText("ws://192.168.1.94:808")
        self.text_edit.setFixedHeight(30)
        self.text_edit.setFixedWidth(160)
        top_left_layout.addWidget(self.text_edit)
        self.button = QPushButton("Test relay")
        self.button.setFixedHeight(30)
        self.button.setFixedWidth(100)
        self.button.clicked.connect(self.show_popup)
        top_left_layout.addWidget(self.button)

        # Center left horizontal layout
        center_left_layout = QHBoxLayout()
        self.input_text = QLineEdit()
        self.input_text.setFixedHeight(500)
        self.input_text.setAlignment(Qt.AlignTop)
        self.submit_button = QPushButton('Submit')
        self.submit_button.setFixedHeight(30)
        self.submit_button.setFixedWidth(100)
        self.submit_button.clicked.connect(self.submit_text)
        center_left_layout.addWidget(self.input_text)
        center_left_layout.addWidget(self.submit_button)

        # Bottom left horizontal layout
        bottom_left_layout = QHBoxLayout()
        self.bottom_button = QPushButton('Show Text')
        self.bottom_button.setFixedHeight(30)
        self.bottom_button.setFixedWidth(100)
        self.bottom_button.clicked.connect(self.show_text)
        bottom_left_layout.addWidget(self.bottom_button)

        left_layout.addLayout(qrcode_left_layout)
        left_layout.addLayout(top_left_layout)
        left_layout.addLayout(center_left_layout)
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
        posting(note_text, self.relay)
        self.input_text.clear()

    def show_text(self):
        self.output_text.clear()
        result = querying(self.relay)
        for r in result:
            self.output_text.append("[" + str(r[0]) + "] " + str(r[3]))

    def show_popup(self):
        self.relay = self.text_edit.toPlainText()
        result = asyncio.run(test_relay(self.relay))

        msg = QMessageBox()
        msg.setText(result)
        msg.exec_()
