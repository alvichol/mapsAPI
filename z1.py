import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.delta = '0.002'
        self.initUI()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.delta = float(self.delta) - float(self.delta) / 2
            self.delta = str(self.delta)
            self.imageUp()
        if event.key() == Qt.Key_Down:
            self.delta = float(self.delta) + float(self.delta) / 2
            self.delta = str(self.delta)
            self.imageUp()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Первая программа')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 600)
        self.imageUp()

    def imageUp(self):
        api_server = "http://static-maps.yandex.ru/1.x/"
        lon = "37.530887"
        lat = "55.703118"
        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([self.delta, self.delta]),
            "l": "map"
        }
        response = requests.get(api_server, params=params)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap('map.png')
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
