from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import pyqtgraph as pg
# import the function from utils.py
from FunctionsOOP import SignalProcessor

# import UI file
FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "Equalizer-All.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)

        # Create an instance of SignalProcessor
        self.signal_processor = SignalProcessor(self)

        # Add your custom logic and functionality here
        self.Handle_Buttons()
        self.tabWidget.setCurrentIndex(0)

    def Handle_Buttons(self):
        # self.pushButton.clicked.connect(self.signal_processor.load_signal)
        # self.pushButton_57.clicked.connect(self.signal_processor.load_signal)
        # self.pushButton_22.clicked.connect(self.signal_processor.load_signal)
        # self.pushButton_27.clicked.connect(self.signal_processor.load_signal)
        #
        # self.pushButton_2.clicked.connect(self.apply_equalizer_handler)
        self.tabWidget.currentChanged.connect(self.tab_changed_handler)

    def apply_equalizer_handler(self):
        freq_ranges, magnitude, phases, freqs, time = self.signal_processor.get_freq_components(self.signal_processor.signal)
        self.signal_processor.apply_equalizer_uniform(freq_ranges, magnitude, phases, freqs, time)

    def tab_changed_handler(self, index):
        if index == 0:
            print("First tab clicked")
            # self.pushButton.clicked.connect(self.signal_processor.load_signal)
            self.pushButton.clicked.connect(lambda: self.signal_processor.load_signal(graph=self.graphicsView))

            self.pushButton_2.clicked.connect(self.apply_equalizer_handler)



        elif index == 1:
            print("Second tab clicked")
            # self.pushButton_57.clicked.connect(self.signal_processor.load_signal)
            self.pushButton_57.clicked.connect(lambda: self.signal_processor.load_signal(graph=self.graphicsView_56))




        elif index == 2:
            print("Third tab clicked")
            # self.pushButton_22.clicked.connect(self.signal_processor.load_signal)
            self.pushButton_22.clicked.connect(lambda: self.signal_processor.load_signal(graph=self.graphicsView_21))




        elif index == 3:
            print("Fourth tab clicked")
            # self.pushButton_27.clicked.connect(self.signal_processor.load_signal)
            self.pushButton_27.clicked.connect(lambda: self.signal_processor.load_signal(graph=self.graphicsView_26))



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()