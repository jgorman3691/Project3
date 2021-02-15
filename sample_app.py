#!/usr/bin/env python3

import sys
from functools import partial
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt
# from importlib_resources import qrc_resources
from PyQt5.QtWidgets import (
   QApplication,
   QLabel,
   QMainWindow,
   QMenuBar,
   QToolBar,
   QAction,
   QSpinBox,
   QComboBox,
   QStatusBar,
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

      self._createActions()
      self._createMenuBars()
      self._createToolBars()
      self._createContextMenu()
      self._createStatusBar()
      # self.contextMenuEvent(self.event)
      self._connectActions()

   def newFile(self):
      # Logic for new file goes here
      self.centralWidget.setText("<b>File > New...</b> clicked")

   def openFile(self):
      # Logic for open file goes here
      self.centralWidget.setText("<b>File > Open...</b> clicked")

   def saveFile(self):
      # Logic for save file goes here
      self.centralWidget.setText("<b>File > Save...</b> clicked")

   def copyContent(self):
      # Logic for copying goes here
      self.centralWidget.setText("<b>Edit > Copy...</b> clicked")

   def pasteContent(self):
      # Logic for pasting goes here
      self.centralWidget.setText("<b>Edit > Paste...</b> clicked")

   def cutContent(self):
      # Logic for cutting goes here
      self.centralWidget.setText("<b>Edit > Cut...</b> clicked")

   def helpContent(self):
      # Logic for launching help goes here
      self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

   def about(self):
      # Logic for showing about dialog content goes here
      self.centralWidget.setText("<b>Help > About...</b> clicked")

   def rgbaSettings(self):
      # Logic for RGBA settings here
      self.centralWidget.setText("<b>Settings > RGBA...</b> clicked")

   def hsloSettings(self):
      # Logic for HSLO settings here
      self.centralWidget.setText("<b>Settings > HSLO...</b> clicked")

   def gammaSettings(self):
      # Logic for Gamma settings here
      self.centralWidget.setText("<b>Settings > Gamma...</b> clicked")

   def highPassSounds(self):
      # Logic for High Pass here
      self.centralWidget.setText("<b>Settings > Sounds > High Pass...</b> clicked")

   def lowPassSounds(self):
      # Logic for Low Pass here
      self.centralWidget.setText("<b>Settings > Sounds > Low Pass...</b> clicked")

   def bandPassSounds(self):
      # Logic for Band Pass here
      self.centralWidget.setText("<b>Settings > Sounds > Band Pass...</b> clicked")

   def spectralAnalyzerSounds(self):
      # Logic for FFT here
      self.centralWidget.setText("<b>Settings > Sounds > Spectral Analyzer...</b> clicked")


   def populateOpenRecent(self):
      # Step 1: Remove the old options from the menu
      self.openRecentMenu.clear()

      # Step 2: Dynamically create the actions
      actions = []
      filenames = [f"File-{n}" for n in range(5)]
      for filename in filenames:
            action = QAction(filename, self)
            action.triggered.connect(partial(self.openRecentFile, filename))
            actions.append(action)

      # Step 3: Add the actions to the menu
      self.openRecentMenu.addActions(actions)

   def openRecentFile(self, filename):
      # Logic for opening a recent file here
      self.centralWidget.setText(f"<b>File > Open Recent > {filename}</b> opened...")


   def _createMenuBars(self):
      menuBar = self.menuBar()

      # Creating menus using a QMenu object
      fileMenu = QMenu("&File", self)
      menuBar.addMenu(fileMenu)
      fileMenu.addAction(self.newAction)
      fileMenu.addAction(self.openAction)

      # Adding an "Open Recent" submenu
      self.openRecentMenu = fileMenu.addMenu("Open Recent")
      fileMenu.addAction(self.saveAction)
      fileMenu.addSeparator()
      fileMenu.addAction(self.exitAction)

      settingsMenu = menuBar.addMenu("&Settings")
      settingsMenu.addAction(self.rgbaAction)
      settingsMenu.addAction(self.hsloAction)
      settingsMenu.addAction(self.gammaAction)
      settingsMenu.addSeparator()
      soundsMenu = settingsMenu.addMenu("Sounds")
      soundsMenu.addAction(self.highPassAction)
      soundsMenu.addAction(self.lowPassAction)
      soundsMenu.addAction(self.bandPassAction)
      soundsMenu.addAction(self.spectralAnalyzerAction)

      # For when I can find Icons
      # self.newAction.setIcon(QIcon(":file-new.svg"))
      # self.openAction = QAction(QIcon(":file-open.svg"), "&Open...", self)
      # self.saveAction = QAction(QIcon(":file-save.svg"), "&Save", self)
      # self.copyAction = QAction(QIcon(":edit-copy.svg"), "&Copy", self)
      # self.pasteAction = QAction(QIcon(":edit-paste.svg"), "&Paste", self)
      # self.cutAction = QAction(QIcon(":edit-cut.svg"), "C&ut", self)
      # Creating menus using a title

      # Adding to the Edit menu
      editMenu = menuBar.addMenu("&Edit")
      editMenu.addAction(self.cutAction)
      editMenu.addAction(self.copyAction)
      editMenu.addAction(self.pasteAction)
      editMenu.addSeparator()

      # Adding a Find and Replace submenu to the Edit menu
      findMenu = editMenu.addMenu("Find and Replace")
      findMenu.addAction("Find...")
      findMenu.addAction("Replace...")

      # Adding to the help menu
      helpMenu = menuBar.addMenu("&Help")
      helpMenu.addAction(self.helpContentAction)
      helpMenu.addAction(self.aboutAction)

      # Using an icon and a title
      # helpMenu = menuBar.addMenu("&Help")

   def _createToolBars(self):
      # Using a title
      fileToolBar = self.addToolBar("File")

      # Using a QToolBar object
      editToolBar = QToolBar("Edit", self)
      self.addToolBar(editToolBar)
      editToolBar.addSeparator()
      self.fontSizeSpinBox = QSpinBox()
      self.fontSizeSpinBox.setFocusPolicy(Qt.NoFocus)
      editToolBar.addWidget(self.fontSizeSpinBox)

      # Using a QToolBar object and a toolbar area
      # helpToolBar = QToolBar("Help", self)
      # self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

   def _createActions(self):
      # Creating actions using the constructor QAction(parent)
      self.newAction = QAction(self)
      self.newAction.setText("&New")

      # Creating Actions using the second constructor (parent, text)
      self.openAction = QAction("&Open...", self)
      self.saveAction = QAction("&Save", self)
      self.exitAction = QAction("&Exit", self)
      self.rgbaAction = QAction("&RGBA", self)
      self.hsloAction = QAction("&HSLO", self)
      self.gammaAction = QAction("&Gamma", self)
      self.highPassAction = QAction("&High Pass", self)
      self.lowPassAction = QAction("&Low Pass", self)
      self.bandPassAction = QAction("&Band Pass", self)
      self.spectralAnalyzerAction = QAction("&Spectral Analyzer", self)
      self.copyAction = QAction("&Copy", self)
      self.pasteAction = QAction("&Paste", self)
      self.cutAction = QAction("&Cut", self)
      self.helpContentAction = QAction("&Help Content", self)
      self.aboutAction = QAction("&About", self)

      self.newAction.setShortcut("Ctrl+N")
      self.openAction.setShortcut("Ctrl+O")
      self.saveAction.setShortcut("Ctrl+S")
      self.exitAction.setShortcut("Alt+F4")
      self.rgbaAction.setShortcut("Ctrl+R")
      self.hsloAction.setShortcut("Ctrl+H")
      self.gammaAction.setShortcut("Ctrl+G")
      self.highPassAction.setShortcut("Alt+H")
      self.lowPassAction.setShortcut("Alt+L")
      self.bandPassAction.setShortcut("Alt+B")
      self.spectralAnalyzerAction.setShortcut("Ctrl+Alt+A")
      self.copyAction.setShortcut(QKeySequence.Copy)
      self.pasteAction.setShortcut(QKeySequence.Paste)
      self.cutAction.setShortcut(QKeySequence.Cut)
      self.helpContentAction.setShortcut("Alt+Shift+H")
      self.aboutAction.setShortcut("Alt+Shift+A")

      # Creating/Adding Help Tips
      newTip = "Create a new file"
      openTip = "Open a file"
      saveTip = "Save a file"
      exitTip = "Exit the program"
      copyTip = "Copy the selected item to the clipboard"
      cutTip = "Brit Milah"
      pasteTip = "Paste the contents of the clipboard"

      # Adding the help tips
      self.newAction.setStatusTip(newTip)
      self.newAction.setToolTip(newTip)
      self.openAction.setStatusTip(openTip)
      self.openAction.setToolTip(openTip)
      self.saveAction.setStatusTip(saveTip)
      self.saveAction.setToolTip(saveTip)
      self.exitAction.setStatusTip(exitTip)
      self.exitAction.setToolTip(exitTip)
      self.copyAction.setStatusTip(copyTip)
      self.copyAction.setToolTip(copyTip)
      self.cutAction.setStatusTip(cutTip)
      self.cutAction.setToolTip(cutTip)
      self.pasteAction.setStatusTip(pasteTip)
      self.pasteAction.setToolTip(pasteTip)




   def _createContextMenu(self):
      # Setting the Context Menu policy
      self.centralWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
      # Here we create a separator action
      separator = QAction(self)
      separator.setSeparator(True)
      # Now we get to populate the widget with actions
      self.centralWidget.addAction(self.newAction)
      self.centralWidget.addAction(self.openAction)
      self.centralWidget.addAction(self.saveAction)
      self.centralWidget.addAction(self.cutAction)
      self.centralWidget.addAction(separator)
      self.centralWidget.addAction(self.copyAction)
      self.centralWidget.addAction(self.pasteAction)
   """
   def contextMenuEvent(self, event):
      # Here we create a menu object with the central widget as parent
      menu = QMenu(self.centralWidget)
      
      # Now we get to populate the menu with actions!
      
      menu.addAction(self.newAction)
      menu.addAction(self.openAction)
      menu.addAction(self.saveAction)
      menu.addAction(self.copyAction)
      menu.addAction(self.pasteAction)
      menu.addAction(self.cutAction)
      
      # Now we launch the menu
      menu.exec(event.globalPos())
      """

   def _createStatusBar(self):
      self.statusbar = self.statusBar()

      # Adding a temporary message
      self.statusbar.showMessage("Ready", 3000)

      # Adding Permanent Messages
      self.wclabel = QLabel(f"{self.getWordCount()} words")
      self.statusbar.addPermanentWidget(self.wclabel)
      self.smnlabel = QLabel(f"{self.sayMyName()}")
      self.statusbar.addPermanentWidget(self.smnlabel)

   def getWordCount(self):
      # Logic for word count goes here
      return 42

   def sayMyName(self):
      # Logic for User Name goes here
      return "Jed S. Gorman"

   def _connectActions(self):
      # Connect File actions
      self.newAction.triggered.connect(self.newFile)
      self.openAction.triggered.connect(self.openFile)
      self.saveAction.triggered.connect(self.saveFile)
      self.exitAction.triggered.connect(self.close)

      # Connect Settings actions
      self.rgbaAction.triggered.connect(self.rgbaSettings)
      self.hsloAction.triggered.connect(self.hsloSettings)
      self.gammaAction.triggered.connect(self.gammaSettings)
      self.highPassAction.triggered.connect(self.highPassSounds)
      self.lowPassAction.triggered.connect(self.lowPassSounds)
      self.bandPassAction.triggered.connect(self.bandPassSounds)
      self.spectralAnalyzerAction.triggered.connect(self.spectralAnalyzerSounds)

      # Connect Edit actions
      self.copyAction.triggered.connect(self.copyContent)
      self.pasteAction.triggered.connect(self.pasteContent)
      self.cutAction.triggered.connect(self.cutContent)

      # Connect Help actions
      self.helpContentAction.triggered.connect(self.helpContent)
      self.aboutAction.triggered.connect(self.about)

      # Adding a dynamic menu
      self.openRecentMenu.aboutToShow.connect(self.populateOpenRecent)



if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec())
