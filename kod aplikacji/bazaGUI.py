# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bazaUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 654)
        MainWindow.setStyleSheet("font: 10pt \"Constantia\";\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(198, 165, 129, 255), stop:1 rgba(171, 176, 232, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setObjectName("stackedWidget")
        self.p1 = QtWidgets.QWidget()
        self.p1.setObjectName("p1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.p1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_23 = QtWidgets.QFrame(self.p1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setStyleSheet("")
        self.frame_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_10 = QtWidgets.QFrame(self.frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setStyleSheet("font: 10pt;\n"
"padding: 5pt;\n"
"background-color:rgba(206, 197, 212, 240);\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_10)
        self.frame_2.setMinimumSize(QtCore.QSize(337, 146))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QtCore.QSize(126, 144))
        self.frame_12.setMaximumSize(QtCore.QSize(126, 144))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_17 = QtWidgets.QFrame(self.frame_12)
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.frame_17)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_17)
        self.frame_8 = QtWidgets.QFrame(self.frame_12)
        self.frame_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_11 = QtWidgets.QFrame(self.frame_12)
        self.frame_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_11)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_11)
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_15)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_15)
        self.horizontalLayout_10.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QtCore.QSize(209, 144))
        self.frame_14.setMaximumSize(QtCore.QSize(209, 144))
        self.frame_14.setStyleSheet("background-color: none;\n"
"font: 9pt \"Consolas\";")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_18 = QtWidgets.QFrame(self.frame_14)
        self.frame_18.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.address = QtWidgets.QLineEdit(self.frame_18)
        self.address.setMaximumSize(QtCore.QSize(200, 30))
        self.address.setObjectName("address")
        self.gridLayout_8.addWidget(self.address, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_18)
        self.frame_9 = QtWidgets.QFrame(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.database = QtWidgets.QLineEdit(self.frame_9)
        self.database.setMaximumSize(QtCore.QSize(200, 30))
        self.database.setObjectName("database")
        self.gridLayout_4.addWidget(self.database, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_13 = QtWidgets.QFrame(self.frame_14)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.username = QtWidgets.QLineEdit(self.frame_13)
        self.username.setMaximumSize(QtCore.QSize(200, 30))
        self.username.setObjectName("username")
        self.gridLayout_3.addWidget(self.username, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_13)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.password = QtWidgets.QLineEdit(self.frame_16)
        self.password.setMaximumSize(QtCore.QSize(200, 30))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout_6.addWidget(self.password, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_16)
        self.horizontalLayout_10.addWidget(self.frame_14)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_21 = QtWidgets.QFrame(self.frame_10)
        self.frame_21.setStyleSheet("")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.loginBtn = QtWidgets.QPushButton(self.frame_21)
        self.loginBtn.setMaximumSize(QtCore.QSize(229, 91))
        self.loginBtn.setAutoFillBackground(False)
        self.loginBtn.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 75 10pt \"Constantia\";\n"
"color: white;\n"
"padding: 30px;\n"
"margin: 30px;")
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout_8.addWidget(self.loginBtn)
        self.verticalLayout.addWidget(self.frame_21)
        self.horizontalLayout_7.addWidget(self.frame_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.frame_23)
        self.stackedWidget.addWidget(self.p1)
        self.p2 = QtWidgets.QWidget()
        self.p2.setObjectName("p2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.p2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_4 = QtWidgets.QFrame(self.p2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget.setStyleSheet("background-color:none;\n"
"color:black;\n"
"font: 9pt \"Consolas\";")
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_16.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setMaximumSize(QtCore.QSize(288, 16777215))
        self.frame_7.setStyleSheet("background-color:rgba(206, 197, 212, 240);\n"
"color:black;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_29 = QtWidgets.QFrame(self.frame_7)
        self.frame_29.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_27 = QtWidgets.QFrame(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_5 = QtWidgets.QLabel(self.frame_27)
        self.label_5.setStyleSheet("font: 10pt \"Constantia\";")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.gridLayout_13.addWidget(self.label_5, 0, 0, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(self.frame_27)
        self.usernameLabel.setStyleSheet("font: 10pt \"Constantia\";")
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout_13.addWidget(self.usernameLabel, 0, 2, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_27, 0, QtCore.Qt.AlignLeft)
        self.frame_28 = QtWidgets.QFrame(self.frame_29)
        self.frame_28.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_28)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setHorizontalSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.logoutBtn = QtWidgets.QPushButton(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutBtn.sizePolicy().hasHeightForWidth())
        self.logoutBtn.setSizePolicy(sizePolicy)
        self.logoutBtn.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 75 10pt \"Constantia\";\n"
"color: white;\n"
"padding: 10px;")
        self.logoutBtn.setObjectName("logoutBtn")
        self.gridLayout_12.addWidget(self.logoutBtn, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_28, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frame_29)
        self.frame_26 = QtWidgets.QFrame(self.frame_7)
        self.frame_26.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_26)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.tableList = QtWidgets.QComboBox(self.frame_26)
        self.tableList.setStyleSheet("background-color: none;\n"
"font: 9pt \"Consolas\";")
        self.tableList.setObjectName("tableList")
        self.gridLayout_14.addWidget(self.tableList, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_26)
        self.label_4.setStyleSheet("font: 11pt \"Constantia\";")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.gridLayout_14.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_26)
        self.frame_30 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_30.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.toolBox = QtWidgets.QToolBox(self.frame_30)
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setObjectName("toolBox")
        self.AMDpage = QtWidgets.QWidget()
        self.AMDpage.setGeometry(QtCore.QRect(0, 0, 274, 209))
        self.AMDpage.setObjectName("AMDpage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.AMDpage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_33 = QtWidgets.QFrame(self.AMDpage)
        self.frame_33.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_33.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_9.setContentsMargins(60, 0, 60, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.addRowsBtn = QtWidgets.QPushButton(self.frame_33)
        self.addRowsBtn.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 75 10pt \"Constantia\";\n"
"color: white;\n"
"padding: 10px;")
        self.addRowsBtn.setObjectName("addRowsBtn")
        self.verticalLayout_9.addWidget(self.addRowsBtn)
        self.modBtn = QtWidgets.QPushButton(self.frame_33)
        self.modBtn.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 75 10pt \"Constantia\";\n"
"color: white;\n"
"padding: 10px;")
        self.modBtn.setObjectName("modBtn")
        self.verticalLayout_9.addWidget(self.modBtn)
        self.deleteRowsBtn = QtWidgets.QPushButton(self.frame_33)
        self.deleteRowsBtn.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 75 10pt \"Constantia\";\n"
"color: white;\n"
"padding: 10px;")
        self.deleteRowsBtn.setObjectName("deleteRowsBtn")
        self.verticalLayout_9.addWidget(self.deleteRowsBtn)
        self.verticalLayout_6.addWidget(self.frame_33)
        self.toolBox.addItem(self.AMDpage, "")
        self.viewPage = QtWidgets.QWidget()
        self.viewPage.setGeometry(QtCore.QRect(0, 0, 274, 209))
        self.viewPage.setObjectName("viewPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.viewPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.viewPage)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.clientViewBtn = QtWidgets.QPushButton(self.frame_3)
        self.clientViewBtn.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 75 10pt \"Constantia\";\n"
"color: white;\n"
"padding: 10px;")
        self.clientViewBtn.setObjectName("clientViewBtn")
        self.verticalLayout_10.addWidget(self.clientViewBtn)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.toolBox.addItem(self.viewPage, "")
        self.processPage = QtWidgets.QWidget()
        self.processPage.setGeometry(QtCore.QRect(0, 0, 274, 209))
        self.processPage.setObjectName("processPage")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.processPage)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_6 = QtWidgets.QFrame(self.processPage)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.deleteProcBtn = QtWidgets.QPushButton(self.frame_6)
        self.deleteProcBtn.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 75 10pt \"Constantia\";\n"
"color: white;\n"
"padding: 10px;")
        self.deleteProcBtn.setObjectName("deleteProcBtn")
        self.verticalLayout_11.addWidget(self.deleteProcBtn)
        self.freeSlotsProcBtn = QtWidgets.QPushButton(self.frame_6)
        self.freeSlotsProcBtn.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 75 10pt \"Constantia\";\n"
"color: white;\n"
"padding: 10px;")
        self.freeSlotsProcBtn.setObjectName("freeSlotsProcBtn")
        self.verticalLayout_11.addWidget(self.freeSlotsProcBtn)
        self.horizontalLayout_9.addWidget(self.frame_6)
        self.toolBox.addItem(self.processPage, "")
        self.horizontalLayout_6.addWidget(self.toolBox)
        self.verticalLayout_4.addWidget(self.frame_30)
        self.frame_32 = QtWidgets.QFrame(self.frame_7)
        self.frame_32.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_32.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_32)
        self.label_8.setStyleSheet("font: 11pt \"Constantia\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.recentHistory = QtWidgets.QTextBrowser(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentHistory.sizePolicy().hasHeightForWidth())
        self.recentHistory.setSizePolicy(sizePolicy)
        self.recentHistory.setMaximumSize(QtCore.QSize(352, 200))
        self.recentHistory.setStyleSheet("background-color: none;\n"
"font: 8pt \"Consolas\";")
        self.recentHistory.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.recentHistory.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.recentHistory.setObjectName("recentHistory")
        self.verticalLayout_8.addWidget(self.recentHistory)
        self.verticalLayout_4.addWidget(self.frame_32, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_4.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight)
        self.gridLayout_11.addWidget(self.frame_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.p2)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Centrum sportowe Rujner"))
        self.label.setText(_translate("MainWindow", "Adres bazy danych:"))
        self.label_7.setText(_translate("MainWindow", "Nazwa bazy danych:"))
        self.label_2.setText(_translate("MainWindow", "Użytkownik:"))
        self.label_3.setText(_translate("MainWindow", "Hasło:"))
        self.loginBtn.setText(_translate("MainWindow", "Połącz"))
        self.label_5.setText(_translate("MainWindow", "Zalogowany jako: "))
        self.usernameLabel.setText(_translate("MainWindow", "usernameText"))
        self.logoutBtn.setText(_translate("MainWindow", "Wyloguj"))
        self.label_4.setText(_translate("MainWindow", "Tabele:"))
        self.addRowsBtn.setText(_translate("MainWindow", "Dodaj"))
        self.modBtn.setText(_translate("MainWindow", "Modyfikuj"))
        self.deleteRowsBtn.setText(_translate("MainWindow", "Usuń"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.AMDpage), _translate("MainWindow", "Główne operacje"))
        self.clientViewBtn.setText(_translate("MainWindow", "Rozpiska klientów"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.viewPage), _translate("MainWindow", "Widoki"))
        self.deleteProcBtn.setText(_translate("MainWindow", "Usuń stare profile"))
        self.freeSlotsProcBtn.setText(_translate("MainWindow", "Pokaż wolne miejsca"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.processPage), _translate("MainWindow", "Procedury"))
        self.label_8.setText(_translate("MainWindow", "Historia operacji:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())