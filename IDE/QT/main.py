# encoding: utf-8
import sys
import os
import json

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QUrl, QObject, Slot
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineWidgets import QWebEngineView

from IDE.QT.form import IDR_mainwindow_ui


# заглушка питон пошелнахуй
class JsonType(str):
    def __init__(self):
        super().__init__(str.__init__())


SAVE_PATH = "./saves/"
os.makedirs(SAVE_PATH, exist_ok=True)


class ArdublocklyWebServer(BaseHTTPRequestHandler):
    basepath = "/Users/ihi/PROG/HACK_digital_suv/IDE/QT/ardublockly"

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)


    def _send_response(self, status, content_type, content):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

    def do_GET(self):
        try:
            if self.path == "/" or self.path == "/index.html":
                try:
                    with open(f"{self.basepath}/ardublockly/index.html", "r", encoding="utf-8") as f:
                        # content = 
                        self._send_response(200, "text/html", f.read())
                except FileNotFoundError:
                    self._send_response(404, "application/json", json.dumps({"error": "index.html not found"}))
            elif self.path.endswith(".css"):
                self._send_static_file("text/css")
            elif self.path.endswith(".js"):
                self._send_static_file("application/javascript")
            elif self.path.endswith(".png") or self.path.endswith(".jpg"):
                self._send_static_file("image/png" if self.path.endswith(".png") else "image/jpeg")
        except Exception as e:
            self._send_response(404, "application/json", json.dumps({"error" : "unknown path"}))
        # else:
            # self._send_response(404, "application/json", json.dumps({"error": "Неизвестный путь"}))

    def do_POST(self):
        if self.path == "/save":
            try:
                block_data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                with open(os.path.join(SAVE_PATH, "blocks.json"), "w", encoding="utf-8") as f:
                    json.dump(block_data, f, indent=4)
                self._send_response(200, "application/json", json.dumps({"success": True}))
            except json.JSONDecodeError:
                self._send_response(400, "application/json", json.dumps({"error": "Ошибка в формате данных JSON"}))
            except Exception as e:
                self._send_response(500, "application/json", json.dumps({"error": str(e)}))
        else:
            self._send_response(404, "application/json", json.dumps({"error": "Неизвестный путь"}))

    def _send_static_file(self, content_type: str):
        try:
            # file_path = os.path.join(self.basepath, self.path.lstrip("/"))
            with open(f"{self.basepath}/{self.path}", "rb") as f:
                self.send_response(200)
                self.send_header("Content-Type", content_type)
                self.end_headers()
                self.wfile.write(f.read())
        except FileNotFoundError:
            self._send_response(404, "application/json", json.dumps({"error": "Файл не найден"}))



# QT
class VisuRadionIDE(QMainWindow):
    WEBAPP_PORT = 8572

    def __init__(self):
        super().__init__()
        self.setupServer(self.WEBAPP_PORT)

        self._setupUi()


    def _setupUi(self):
        self.ui = IDR_mainwindow_ui()
        self.ui.setupUi(self)

        self.ui.bloklyWebWidget = QWebEngineView(self)
        self.setCentralWidget(self.ui.bloklyWebWidget)
        self.ui.bloklyWebWidget.load(
            QUrl(f"http://localhost:{self.WEBAPP_PORT}/")
        )

        self.ui.bloklyWebWidget.page().runJavaScript(
            "document.querySelectorAll('body > *:not(#divBody)').forEach(el => el.style.display = 'none');"
        )

        self.ui.action_Save.triggered.connect(self.saveBlocks)
        self.ui.action_Open.triggered.connect(self.loadBlocks)
        self.ui.action_SaveAs.triggered.connect(self.saveAsBlocks)
        self.ui.action.triggered.connect(self.uploadToController)

    def setupServer(self, port: int):
        self.server = HTTPServer(("localhost", port), ArdublocklyWebServer)
        server_thread = threading.Thread(target=self.server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print(f"Сервер запущен на http://localhost:{port}")


    def saveBlocks(self):
        self.bloklyWebWidget.page().runJavaScript(
            "Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);", self.saveCallback
        )

    def saveCallback(self, block_data):
        try:
            block_json = json.dumps(block_data)
            save_file_path = os.path.join(SAVE_PATH, "blocks.json")
            with open(save_file_path, "w") as f:
                f.write(block_json)
            print("Блоки успешно сохранены.")
        except Exception as e:
            print("Ошибка при сохранении блоков:", e)

    def loadBlocks(self):
        try:
            with open(os.path.join(SAVE_PATH, "blocks.json"), "r") as f:
                blocks = json.load(f)

            block_data_js = json.dumps(blocks)
            self.bloklyWebWidget.page().runJavaScript(
                f"""
                var blockData = {block_data_js};
                var workspace = Blockly.getMainWorkspace();
                var dom = Blockly.Xml.textToDom(JSON.stringify(blockData));
                Blockly.Xml.domToWorkspace(dom, workspace);
            """
            )

        except FileNotFoundError:
            print("Файл блоков не найден.")
        except Exception as e:
            print("Ошибка при загрузке блоков:", e)

    def saveAsBlocks(self):
        self.saveCallback(os.path.join(SAVE_PATH, "blocks_new.json"))

    def uploadToController(self):
        try:
            with open(os.path.join(SAVE_PATH, "blocks.json"), "r") as f:
                blocks = json.load(f)

            arduino_code = RadionControllerService.compile(blocks) 
            is_load_success = RadionControllerService.load_to_controller(arduino_code)

        except FileNotFoundError:
            print("Файл блоков не найден. Сначала сохраните блоки.")
        except Exception as e:
            print("Ошибка при загрузке на контроллер:", e)


# TODO : тут нужно прописать логику для компиляции и загрузки на контроллер
class RadionControllerService:

    @staticmethod
    def compile(file_path: str | os.PathLike) -> str:
        print(f"Компиляция файла: {file_path}")
        arduino_code = "ABOBOA"
        return arduino_code

    @staticmethod
    def load_to_controller(arduino_code: str) -> bool:
        print(f"Загрузка кода на контроллер:\n{arduino_code}")
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ide = VisuRadionIDE()
    ide.show()
    sys.exit(app.exec())