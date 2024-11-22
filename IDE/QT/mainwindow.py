# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class RIDEBlocksWebEng:
    def __init__(self, engview, url):
        self.engview = engview
        self.engview.load(QUrl(url))
class RIDESchemeWebEng:
    def __init__(self, engview, url):
        self.engview = engview
        self.engview.load(QUrl(url))
class RadionIDE(QMainWindow):
    def __init__(self,url1, url2 parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.blockswebeng = RIDEBlocksWebEng(self.ui.BlockswebEngineView, 'http://ardublock.ru/app/')
        self.schemewebeng = RIDESchemeWebEng(self.ui.SchemewebEngineView, 'http://ardublock.ru/aliexpress/')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = RadionIDE(sys.argv[1], sys.argv[2])

    widget.show()
    sys.exit(app.exec())
