import os
import sys

os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"

from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QToolBar,
)

# HTML Industrial / Imperial
PAGINA_INICIO_HTML = """
<!DOCTYPE html>
<html lang="la">
<head>
    <meta charset="UTF-8">
    <title>OFFICINA HEPHAESTI // TERMINALE</title>
    <style>
        * {
            box-sizing: border-box;
            border-radius: 0px !important;
        }
        body {
            background-color: #080808;
            color: #d0d0d0;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            border: 8px solid #1a1a1a;
        }
        h1 {
            font-size: 2.8rem;
            color: #ff5500;
            margin-bottom: 0px;
            text-transform: uppercase;
            border-bottom: 4px solid #ff5500;
            padding-bottom: 5px;
            letter-spacing: 4px;
        }
        .status {
            color: #666;
            margin-top: 5px;
            margin-bottom: 30px;
            font-size: 0.9rem;
            font-weight: bold;
        }
        .search-box {
            display: flex;
            width: 650px;
            max-width: 90%;
            border: 3px solid #ff5500;
            background: #101010;
        }
        input[type="text"] {
            width: 100%;
            padding: 12px 15px;
            border: none;
            outline: none;
            background: transparent;
            color: #ffaa00;
            font-family: 'Courier New', monospace;
            font-size: 1.1rem;
            font-weight: bold;
        }
        button {
            background: #ff5500;
            color: #000;
            border: none;
            padding: 0 25px;
            cursor: pointer;
            font-weight: 900;
            font-family: 'Courier New', monospace;
            font-size: 1rem;
            text-transform: uppercase;
        }
        button:hover {
            background: #ff8800;
        }
        .panel-short {
            display: flex;
            gap: 10px;
            margin-top: 30px;
        }
        .shortcut {
            background: #141414;
            border: 2px solid #333;
            padding: 10px 20px;
            color: #ffaa00;
            text-decoration: none;
            font-weight: bold;
            font-size: 0.9rem;
        }
        .shortcut:hover {
            border-color: #ff5500;
            background: #ff5500;
            color: #000;
        }
    </style>
</head>
<body>
    <h1>[ OFFICINA_HEPHAESTI ]</h1>
    <div class="status">MACHINA GRAVIS // MOTOR CHROMIUM ACTIVUS</div>
    
    <form class="search-box" action="https://duckduckgo.com/" method="get">
        <input type="text" name="q" placeholder="INQUIRE IN INTERRETE..." autofocus>
        <button type="submit">SCRUTARI</button>
    </form>

    <div class="panel-short">
        <a class="shortcut" href="https://youtube.com">[YOUTUBE]</a>
        <a class="shortcut" href="https://github.com">[GITHUB]</a>
        <a class="shortcut" href="https://la.wikipedia.org">[WIKIPEDIA_LATINA]</a>
    </div>
</body>
</html>
"""


class HefestoBrowser(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("HEPHAESTUS // NAVIGATOR IMPERIALIS 🗿")
    self.setGeometry(100, 100, 1280, 720)

    self.tabs = QTabWidget()
    self.tabs.setDocumentMode(True)
    self.tabs.setTabsClosable(True)
    self.tabs.tabCloseRequested.connect(self.cerrar_pestana)
    self.tabs.currentChanged.connect(self.cambio_de_pestana)
    self.setCentralWidget(self.tabs)

    navbar = QToolBar("GUBERNATIO")
    self.addToolBar(navbar)

    btn_atras = QPushButton("[ RETRO ]")
    btn_atras.clicked.connect(self.navegar_atras)
    navbar.addWidget(btn_atras)

    btn_adelante = QPushButton("[ PORRO ]")
    btn_adelante.clicked.connect(self.navegar_adelante)
    navbar.addWidget(btn_adelante)

    btn_recargar = QPushButton("[ RENOVARE ]")
    btn_recargar.clicked.connect(self.recargar_pagina)
    navbar.addWidget(btn_recargar)

    btn_home = QPushButton("[ DOMUS ]")
    btn_home.clicked.connect(self.ir_a_inicio)
    navbar.addWidget(btn_home)

    btn_nueva_tab = QPushButton("[ + ]")
    btn_nueva_tab.clicked.connect(lambda: self.crear_nueva_pestana())
    navbar.addWidget(btn_nueva_tab)

    self.url_bar = QLineEdit()
    self.url_bar.setPlaceholderText("SCRIBE URL VEL INQUISITIONEM...")
    self.url_bar.returnPressed.connect(self.cargar_url)
    navbar.addWidget(self.url_bar)

    self.aplicar_estilo_tosco()
    self.crear_nueva_pestana(label="TABULA_I")

  def aplicar_estilo_tosco(self):
    estilo = """
            * {
                border-radius: 0px;
                font-family: 'Consolas', 'Courier New', monospace;
            }
            QMainWindow {
                background-color: #050505;
            }
            QToolBar {
                background-color: #111111;
                border-bottom: 4px solid #ff5500;
                padding: 4px;
                spacing: 4px;
            }
            QPushButton {
                background-color: #1a1a1a;
                color: #ffaa00;
                border: 2px solid #333333;
                padding: 6px 10px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #ff5500;
                color: #000000;
                border-color: #ff8800;
            }
            QLineEdit {
                background-color: #080808;
                color: #00ff66;
                border: 2px solid #ff5500;
                padding: 6px 10px;
                font-size: 13px;
                font-weight: bold;
            }
            QTabWidget::pane {
                border: 2px solid #1a1a1a;
            }
            QTabBar::tab {
                background-color: #0a0a0a;
                color: #666666;
                border: 2px solid #222222;
                border-bottom: none;
                padding: 6px 14px;
                font-weight: bold;
                font-size: 11px;
            }
            QTabBar::tab:selected {
                background-color: #181818;
                color: #ff5500;
                border: 2px solid #ff5500;
                border-bottom: none;
            }
            QTabBar::tab:hover {
                background-color: #222222;
                color: #ffffff;
            }
        """
    self.setStyleSheet(estilo)

  def crear_nueva_pestana(self, qurl=None, label="NOVUM_TAB"):
    browser = QWebEngineView()

    if qurl is None:
      browser.setHtml(PAGINA_INICIO_HTML)
    else:
      browser.setUrl(qurl)

    i = self.tabs.addTab(browser, label)
    self.tabs.setCurrentIndex(i)

    browser.urlChanged.connect(
        lambda q, browser=browser: self.actualizar_url(q, browser)
    )
    browser.loadFinished.connect(
        lambda _, i=i, browser=browser: self.tabs.setTabText(
            self.tabs.indexOf(browser),
            f"[{browser.page().title()[:12].upper()}]"
            if browser.page().title()
            else "[OFFICINA]",
        )
    )

  def cerrar_pestana(self, index):
    if self.tabs.count() > 1:
      self.tabs.removeTab(index)

  def cambio_de_pestana(self, index):
    if index >= 0:
      browser_actual = self.tabs.widget(index)
      if browser_actual:
        url_texto = browser_actual.url().toString()
        if url_texto == "about:blank" or not url_texto:
          self.url_bar.setText("")
        else:
          self.url_bar.setText(url_texto)

  def cargar_url(self):
    texto = self.url_bar.text().strip()
    browser_actual = self.tabs.currentWidget()

    if not browser_actual:
      return

    if "." in texto and " " not in texto:
      if not texto.startswith("http://") and not texto.startswith("https://"):
        texto = "https://" + texto
      browser_actual.setUrl(QUrl(texto))
    else:
      url_busqueda = f"https://duckduckgo.com/?q={texto.replace(' ', '+')}"
      browser_actual.setUrl(QUrl(url_busqueda))

  def ir_a_inicio(self):
    browser_actual = self.tabs.currentWidget()
    if browser_actual:
      browser_actual.setHtml(PAGINA_INICIO_HTML)
      self.url_bar.setText("")

  def actualizar_url(self, q, browser=None):
    if browser == self.tabs.currentWidget():
      url_str = q.toString()
      if url_str != "about:blank":
        self.url_bar.setText(url_str)

  def navegar_atras(self):
    if self.tabs.currentWidget():
      self.tabs.currentWidget().back()

  def navegar_adelante(self):
    if self.tabs.currentWidget():
      self.tabs.currentWidget().forward()

  def recargar_pagina(self):
    if self.tabs.currentWidget():
      self.tabs.currentWidget().reload()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = HefestoBrowser()
  window.show()
  window.raise_()
  window.activateWindow()
  sys.exit(app.exec())