#!/usr/bin/env python3

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
   QApplication,
   QLabel,
   QMainWindow,
   QMenuBar,
   QToolBar,
   QMenu
)

class Window(QMainWindow):
   # This is the main window (The Top Level Widget)
   def __init__(self, parent=None):
      super().__init__() # <-- Initializer
      self.setWindowTitle("Python Menus and Toolbars")
      self.resize(400, 200)
      
      self.centralWidget = QLabel("Hello, World!")
      self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
      self.setCentralWidget(self.centralWidget)
      
      self._createMenuBar()
      self._createToolBars()
      
   def _createMenuBar(self):
      menuBar = self.menuBar()
      
      # Creating menus using a QMenu object
      fileMenu = QMenu("&File", self)
      settingsMenu = QMenu("&Settings", self)
      menuBar.addMenu(fileMenu)
      menuBar.addMenu(settingsMenu)
      
      # Creating menus using a title
      editMenu = menuBar.addMenu("&Edit")
      helpMenu = menuBar.addMenu("&Help")
      
   def _createToolBars(self):
      # Using a title
      fileToolBar = self.addToolBar("File")
      
      # Using a QToolBar object
      editToolBar = QToolBar("Edit", self)
      self.addToolBar(editToolBar)
      
      # Using a QToolBar object and a toolbar area
      helpToolBar = QToolBar("Help", self)
      self.addToolBar(Qt.LeftToolBarArea, helpToolBar)
      
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec())