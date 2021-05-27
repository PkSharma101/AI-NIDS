from PyQt5 import QtCore, QtGui, QtWidgets
from joblib import load
import numpy as np
import sklearn
import _thread

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 775)
        MainWindow.setMinimumSize(QtCore.QSize(600, 775))
        MainWindow.setMaximumSize(QtCore.QSize(600, 775))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 9, 571, 171))
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 30, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 80, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 30, 89, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 30, 89, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 80, 89, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(410, 80, 89, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 130, 89, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(70, 130, 89, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(340, 130, 89, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 650, 581, 81))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 551, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 170, 221, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("flowchart.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Intrusion Detection System Prototype"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Select the Record"))
        self.pushButton.setText(_translate("MainWindow", "Normal - 1"))
        self.pushButton.clicked.connect(lambda: self.predict(1))
        self.pushButton_2.setText(_translate("MainWindow", "DoS"))
        self.pushButton_2.clicked.connect(lambda: self.predict(2))
        self.pushButton_3.setText(_translate("MainWindow", "Fuzzers"))
        self.pushButton_3.clicked.connect(lambda: self.predict(3))
        self.pushButton_4.setText(_translate("MainWindow", "Exploits"))
        self.pushButton_4.clicked.connect(lambda: self.predict(4))
        self.pushButton_5.setText(_translate("MainWindow", "Analysis"))
        self.pushButton_5.clicked.connect(lambda: self.predict(5))
        self.pushButton_6.setText(_translate("MainWindow", "Backdoors"))
        self.pushButton_6.clicked.connect(lambda: self.predict(6))
        self.pushButton_7.setText(_translate("MainWindow", "Generic"))
        self.pushButton_7.clicked.connect(lambda: self.predict(7))
        self.pushButton_8.setText(_translate("MainWindow", "Worms"))
        self.pushButton_8.clicked.connect(lambda: self.predict(8))
        self.pushButton_9.setText(_translate("MainWindow", "Shellcode"))
        self.pushButton_9.clicked.connect(lambda: self.predict(9))
        self.pushButton_11.setText(_translate("MainWindow", "Normal - 2"))
        self.pushButton_11.clicked.connect(lambda: self.predict(10))
        self.pushButton_10.setText(_translate("MainWindow", "Recon"))
        self.pushButton_10.clicked.connect(lambda: self.predict(11))
        self.groupBox_3.setTitle(_translate("MainWindow", "Prediction Result"))
        self.label_2.setText(_translate("MainWindow", "The Record is predicted as : N/A"))


    def getrecord(self,index):
        # Add 11 records in th data  list with number as mentioned on the button above
        # current enty is dummy just to show what to enter.
        data = [np.array([7.49090137e-03, 1.13000000e+02, 9.39319932e-04, 5.44563442e-04,
       3.71975764e-05, 1.82841162e-05, 3.33738259e-05, 9.96078431e-01,
       9.96047431e-01, 1.62518956e-06, 1.91491241e-04, 3.76010528e-04,
       1.81587071e-04, 7.95706372e-04, 1.31036713e-03, 1.62810844e-03,
       2.50015522e-04, 1.00000000e+00, 5.67209802e-01, 4.60351363e-01,
       1.00000000e+00, 3.35947078e-02, 2.20488610e-02, 1.95419387e-02,
       3.52393617e-02, 3.00000000e-02, 0.00000000e+00, 0.00000000e+00,
       6.82539683e-01, 1.66666667e-01, 3.38983051e-02, 3.38983051e-02,
       2.63157895e-02, 6.34920635e-01, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 3.33333333e-02, 6.29032258e-01, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
        np.array([2.02463370e-03, 1.13000000e+02, 5.63591959e-04, 3.63042294e-04,
       1.79718628e-05, 1.17345820e-05, 7.40874898e-05, 9.88235294e-01,
       1.00395257e+00, 2.68772621e-06, 4.08016962e-04, 0.00000000e+00,
       0.00000000e+00, 4.04859244e-04, 1.45048671e-04, 2.03375915e-05,
       2.55410695e-05, 1.00000000e+00, 1.44768330e-01, 5.12827661e-01,
       1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       2.85904255e-02, 2.86666667e-02, 0.00000000e+00, 0.00000000e+00,
       1.58730159e-02, 0.00000000e+00, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 1.58730159e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.66666667e-02, 1.61290323e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
       np.array([5.30211764e-03, 1.13000000e+02, 9.39319932e-04, 5.44563442e-04,
       2.11761484e-04, 1.82841162e-05, 4.71509799e-05, 9.96078431e-01,
       9.96047431e-01, 1.30604988e-05, 2.70541328e-04, 3.76010528e-04,
       1.81587071e-04, 4.93697416e-04, 1.02851021e-03, 1.02638864e-03,
       1.77702299e-04, 1.00000000e+00, 2.20780139e-01, 2.17696171e-01,
       1.00000000e+00, 2.09406602e-02, 6.56194333e-03, 2.00937046e-02,
       2.02127660e-01, 3.00000000e-02, 0.00000000e+00, 0.00000000e+00,
       1.74603175e-01, 1.66666667e-01, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 1.58730159e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.66666667e-02, 4.83870968e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
        np.array([6.62480788e-01, 1.11000000e+02, 1.87863986e-03, 1.45216918e-03,
       1.13543164e-04, 1.47364519e-04, 8.80528997e-07, 2.43137255e-01,
       9.96047431e-01, 5.91794842e-08, 1.95743210e-05, 7.52021057e-04,
       7.26348284e-04, 3.48615953e-02, 4.57779579e-02, 1.88231036e-01,
       2.07946757e-02, 1.00000000e+00, 6.51572756e-02, 4.57754364e-02,
       1.00000000e+00, 3.75664830e-02, 3.10305480e-02, 1.48287101e-02,
       5.45212766e-02, 9.00000000e-02, 0.00000000e+00, 0.00000000e+00,
       7.93650794e-02, 1.66666667e-01, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 1.58730159e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.66666667e-02, 4.83870968e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
        np.array([1.08317020e-02, 1.13000000e+02, 1.31504791e-03, 3.44890180e-03,
       5.11292529e-05, 2.86637634e-03, 7.84733718e-05, 2.43137255e-01,
       9.96047431e-01, 1.59360514e-06, 2.41856155e-02, 3.76010528e-04,
       3.08698021e-03, 8.31778148e-04, 2.67285558e-04, 4.13975294e-05,
       2.99607212e-03, 1.00000000e+00, 3.30128233e-01, 7.16524666e-01,
       1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       3.45744681e-02, 7.37333333e-01, 0.00000000e+00, 0.00000000e+00,
       6.82539683e-01, 1.66666667e-01, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 3.17460317e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.66666667e-02, 9.67741935e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
         np.array([1.08317020e-02, 1.13000000e+02, 1.31504791e-03, 3.44890180e-03,
       5.11292529e-05, 2.86637634e-03, 7.84733718e-05, 2.43137255e-01,
       9.96047431e-01, 1.59360514e-06, 2.41856155e-02, 3.76010528e-04,
       3.08698021e-03, 8.31778148e-04, 2.67285558e-04, 4.13975294e-05,
       2.99607212e-03, 1.00000000e+00, 3.30128233e-01, 7.16524666e-01,
       1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       3.45744681e-02, 7.37333333e-01, 0.00000000e+00, 0.00000000e+00,
       6.82539683e-01, 1.66666667e-01, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 3.17460317e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.66666667e-02, 9.67741935e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
       np.array([1.96717036e-02, 1.11000000e+02, 9.39319932e-04, 7.26084589e-04,
       9.11131646e-05, 2.41514072e-05, 1.44030930e-05, 9.96078431e-01,
       9.96047431e-01, 1.51564096e-06, 1.00914765e-04, 3.76010528e-04,
       1.81587071e-04, 2.18366968e-03, 2.67417791e-03, 5.52932662e-03,
       4.58542587e-04, 1.00000000e+00, 5.21508023e-01, 5.02365960e-01,
       1.00000000e+00, 3.87503222e-02, 3.08222914e-02, 1.66028289e-02,
       8.71010638e-02, 2.93333333e-02, 7.63358779e-03, 0.00000000e+00,
       3.17460317e-02, 1.66666667e-01, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 1.58730159e-02, 0.00000000e+00, 0.00000000e+00,
       6.25000000e-02, 5.00000000e-02, 1.61290323e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
         np.array([1.08317020e-02, 1.13000000e+02, 1.31504791e-03, 3.44890180e-03,
       5.11292529e-05, 2.86637634e-03, 7.84733718e-05, 2.43137255e-01,
       9.96047431e-01, 1.59360514e-06, 2.41856155e-02, 3.76010528e-04,
       3.08698021e-03, 8.31778148e-04, 2.67285558e-04, 4.13975294e-05,
       2.99607212e-03, 1.00000000e+00, 3.30128233e-01, 7.16524666e-01,
       1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       3.45744681e-02, 7.37333333e-01, 0.00000000e+00, 0.00000000e+00,
       6.82539683e-01, 1.66666667e-01, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 3.17460317e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.66666667e-02, 9.67741935e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
        np.array([2.66666716e-07, 1.17000000e+02, 1.87863986e-04, 0.00000000e+00,
       1.36530430e-05, 0.00000000e+00, 6.25000000e-02, 9.96078431e-01,
       0.00000000e+00, 9.30144222e-03, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 2.66622265e-07, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       6.51595745e-02, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       1.58730159e-02, 3.33333333e-01, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 1.58730159e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.66666667e-02, 1.61290323e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 0.00000000e+00,
       0.00000000e+00]),
       
        np.array([1.21478000e-01, 1.13000000e+02, 6.00000000e+00, 4.00000000e+00,2.58000000e+02, 1.72000000e+02, 7.40874900e+01, 2.52000000e+02,2.54000000e+02, 1.41589424e+04, 8.49536523e+03, 0.00000000e+00,0.00000000e+00, 2.42956000e+01, 8.37500000e+00, 3.01775470e+01,1.18306040e+01, 2.55000000e+02, 6.21772692e+08, 2.20253363e+09,2.55000000e+02, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,4.30000000e+01, 4.30000000e+01, 0.00000000e+00, 0.00000000e+00,1.00000000e+00, 0.00000000e+00, 1.00000000e+00, 1.00000000e+00,1.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,0.00000000e+00, 1.00000000e+00, 1.00000000e+00, 0.00000000e+00,0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,0.00000000e+00]),
        np.array([3.33333394e-08, 1.19000000e+02, 1.87863986e-04, 0.00000000e+00,
       9.61285682e-06, 0.00000000e+00, 5.00000000e-01, 9.96078431e-01,
       0.00000000e+00, 5.23917970e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 3.33277831e-08, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       4.58776596e-02, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       1.58730159e-02, 3.33333333e-01, 1.69491525e-02, 1.69491525e-02,
       2.63157895e-02, 6.34920635e-02, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 3.33333333e-02, 1.61290323e-02, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
       0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 0.00000000e+00,
       0.00000000e+00])
        ]
        try :
            record = data[index-1]
        except:
            record = ""
            print("Out of index")
        return record

    def predict(self,index):
        self.label_2.setText("Processing.....")
        _thread.start_new_thread( self.predict1,(index,))

    def predict1(self,index):
        prediction = "" 
        classes = np.array(['Analysis', 'Backdoor', 'DoS', 'Exploits', 'Fuzzers', 'Generic','Normal', 'Reconnaissance', 'Shellcode', 'Worms'], dtype=object)
        model_path = "model/"
        clf = load(model_path+'Binary-clf.joblib') 
        mclf = load(model_path+'Multi-clf.joblib') 
        record = self.getrecord(index)
        print("Record is : ",record)
        if clf.predict([record]) == 0:
            prediction = "Normal-1"
        else:
            multi_pred_value = mclf.predict([record])
            if multi_pred_value == 6:
                prediction = "Normal-2"
            else:
                prediction = classes[multi_pred_value][0]

        #prediction = str(index)
        self.label_2.setText("The Record is predicted as : "+prediction)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
