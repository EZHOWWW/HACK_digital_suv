# encoding: utf-8
import sys
import os
import json
import subprocess

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QUrl, QObject, Slot
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView

from form import IDR_mainwindow_ui


# заглушка питон пошелнахуй
class JsonType(str):
    def __init__(self):
        super().__init__(str.__init__())


SAVE_PATH = "./saves"
os.makedirs(SAVE_PATH, exist_ok=True)

DIRPATH = os.path.curdir

# QT
class VisuRadionIDE(QMainWindow):
    WEBAPP_PORT = 5053

    def __init__(self):
        super().__init__()

        self._setupUi()

    def _setupUi(self):
        self.ui = IDR_mainwindow_ui()
        self.ui.setupUi(self)

        self.ui.bloklyWebWidget = QWebEngineView(self)
        self.setCentralWidget(self.ui.bloklyWebWidget)
        self.ui.bloklyWebWidget.load(QUrl(f"http://localhost:{self.WEBAPP_PORT}/"))

        # self.ui.bloklyWebWidget.page().runJavaScript(
        #     "Ardublockly.generateArduino()", resultCallback=self.saveCallback
        # )

        self.ui.action_Save.triggered.connect(self.saveBlocks)
        # self.ui.action_Open.triggered.connect(self.loadBlocks)
        # self.ui.action_SaveAs.triggered.connect(self.saveAsBlocks)
        self.ui.action.triggered.connect(self.uploadToController)

    # save eqr
    def saveBlocks(self):
        self.ui.bloklyWebWidget.page().runJavaScript(
            "Ardublockly.generateArduino()", resultCallback=self.saveCallback
        )

    # save resp
    def saveCallback(self, block_data):
        try:
            save_file_path = os.path.join(SAVE_PATH, "blocks.cpp")
            with open(save_file_path, "w") as f:
                f.write(block_data)
            print("Блоки успешно сохранены.")
        except Exception as e:
            print("Ошибка при сохранении блоков:", e)

    # def loadBlocks(self):
    #     try:
    #         with open(os.path.join(SAVE_PATH, "blocks.json"), "r") as f:
    #             blocks = json.load(f)

    #         block_data_js = json.dumps(blocks)
    #         self.bloklyWebWidget.page().runJavaScript(
    #             f"""
    #             var blockData = {block_data_js};
    #             var workspace = Blockly.getMainWorkspace();
    #             var dom = Blockly.Xml.textToDom(JSON.stringify(blockData));
    #             Blockly.Xml.domToWorkspace(dom, workspace);
    #         """
    #         )

    #     except FileNotFoundError:
    #         print("Файл блоков не найден.")
    #     except Exception as e:
    #         print("Ошибка при загрузке блоков:", e)

    def uploadToController(self):
        try:
            RadionControllerService.compile(SAVE_PATH + "/bloks.cpp")
            RadionControllerService.load_to_controller(
                os.path.abspath(SAVE_PATH + "/output")
            )

        except FileNotFoundError:
            print("Файл блоков не найден. Сначала сохраните блоки.")
        except Exception as e:
            print("Ошибка при загрузке на контроллер:", e)


# TODO


class RadionControllerService:

    @staticmethod
    def compile(file_path: str | os.PathLike = 'RudionManagment') -> str:
        print(f"Компиляция файла: {file_path}")
        subprocess.run([SAVE_PATH, 'RudionManagment/Build.sh', file_path])
        return True

    @staticmethod
    def load_to_controller(build_path: str | os.PathLike = 'RudionManagment/build') -> bool:
        print(f"Загрузка кода на контроллер:\n{build_path}")
        subprocess.run(['RudionManagment/Upload.sh', build_path])
        return True



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ide = VisuRadionIDE()
    ide.show()
    sys.exit(app.exec())
