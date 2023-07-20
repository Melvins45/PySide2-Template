import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import (QFile, QIODevice)
from PySide2.QtUiTools import QUiLoader
import constants as gc
    
def load_ui(file_name:str) -> QWidget:
    """Load an ui file in a QWidget and return it

    Args:
        file_name (str): The name of the specified ui file

    Returns:
        QWidget: The resulted QWidget
    """    
    ui_page_file = QFile(gc.PAGES[file_name])
    if not ui_page_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {file_name} : {ui_page_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_page_file)
    ui_page_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    return window  

def load_py(file_name:str) -> QWidget:
    """Load python compiled ui file in QWidget

    Args:
        file_name (str): The name of the compiled python file from ui file

    Returns:
        QWidget: The resulted QWidget
    """    
    class _Window(QWidget):
        def __init__(self, parent=None):
            super(_Window, self).__init__(parent)

            self.m_ui = gc.PAGES_UI[file_name]
            self.m_ui.setupUi(self)
    return _Window()