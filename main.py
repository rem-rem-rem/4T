'''
Created on 3 thg 5, 2022

@author: A315-56
'''
import sys
import os
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# counter = 0
# jumper = 10

os.system("pyuic5 -x Main.ui -o REM.py")

from REM import *
from style import *
from GUI_PyQt5_Func_1 import *
     
class MAIN(Ui_MainWindow):
    def __init__(self, mainwindow):
        self.setupUi(mainwindow)

        # self.Ui_MainWindow.verticalSlider.valueChanged.connect(self.slide_it)
        
        
        self.Top_stackedWidget.setCurrentWidget(self.Top_ControlPanel)
        self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)
        self.Control_btn.setStyleSheet(Control_btn_active)

        self.slider_setting()
        self.verticalSlider.valueChanged.connect(self.slide_it)

        self.Menu_btn.clicked.connect(lambda: UIFunctions.ToggleMenu      (self, 50, 250))
        self.Control_btn.clicked.connect(lambda: UIFunctions.Select_Menu  (self, 1))
        self.Parameter_btn.clicked.connect(lambda: UIFunctions.Select_Menu(self, 2))
        self.Setting_btn.clicked.connect(lambda: UIFunctions.Select_Menu  (self, 3))

    def slider_setting(self):
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)


    def progressBarValue(self, value):
        #biểu diễn thanh tiến trình
        styleSheet = """
            border-radius:165px;
            background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(0, 0, 42, 0), stop:{STOP_2} rgba(0, 0, 42, 255))
        """
        #láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
        # dừng giá trị từ 1 đến 0

        progress = (100 - value) / 100.0
        # Láy giá trị mới
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #Ungứ dụng giá trị mới vào styleSheet
        self.label_23.setStyleSheet(newStylsheet)

    def slide_it(self, value):
        print("Tung dep trrai")
        # Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.verticalSlider.value())
        # newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue(100 - int(value))
        # self.label_17.setText(newRem)











