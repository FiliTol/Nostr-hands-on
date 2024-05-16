import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget
from scripts.post import posting


class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Note App')
        self.setGeometry(100, 100, 300, 200)

        self.text_input = QLineEdit(self)

        post_button = QPushButton('Post a note', self)
        post_button.clicked.connect(self.post_note)

        layout = QVBoxLayout()
        layout.addWidget(self.text_input)
        layout.addWidget(post_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        read_button = QPushButton('Read the notes', self)
        read_button.clicked.connect(self.execute_script2)
        read_button.setGeometry(50, 120, 200, 50)

    def post_note(self):
        note_text = self.text_input.text()
        posting(note_text)
        print("Posting note:", note_text)

    def execute_script2(self):
        # Add the logic to execute script2 here
        print("Executing script2")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    note_app = NoteApp()
    note_app.show()
    sys.exit(app.exec_())
