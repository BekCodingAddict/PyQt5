import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel,QWidget,QListWidgetItem,QPushButton,QVBoxLayout,QListWidget,QHBoxLayout

class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Button {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        text_widget = QLabel("PlaceHolder")
        button = QPushButton("Load Image")
        button.move(400,400)
        button2=QPushButton("Save")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        content_layout.addWidget(button2)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication()

    w = Widget()
    w.setGeometry(0,0,400,400)

    w.show()

    with open("C:\\Users\\titan\OneDrive\\Desktop\\PyQt5\\Styling_Withgets\\style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())