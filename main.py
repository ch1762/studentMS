# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from service import service
from baseinfo import result,student
from query import resultinfo,studentinfo
from settings import classes,grade,subject,examkinds
from system import user

class Ui_MainWindow(QMainWindow):
    # 构造方法
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self) # 初始化窗体设置

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 583)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/appstu.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-image: url(:/newPrefix/images/main.jpg);")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiongrade = QtWidgets.QAction(MainWindow)
        self.actiongrade.setObjectName("actiongrade")
        self.actionclass = QtWidgets.QAction(MainWindow)
        self.actionclass.setObjectName("actionclass")
        self.actionsubject = QtWidgets.QAction(MainWindow)
        self.actionsubject.setObjectName("actionsubject")
        self.actionexamkinds = QtWidgets.QAction(MainWindow)
        self.actionexamkinds.setObjectName("actionexamkinds")
        self.actionstudent = QtWidgets.QAction(MainWindow)
        self.actionstudent.setObjectName("actionstudent")
        self.actionresult = QtWidgets.QAction(MainWindow)
        self.actionresult.setObjectName("actionresult")
        self.actionstudentinfo = QtWidgets.QAction(MainWindow)
        self.actionstudentinfo.setObjectName("actionstudentinfo")
        self.actionresultinfo = QtWidgets.QAction(MainWindow)
        self.actionresultinfo.setObjectName("actionresultinfo")
        self.actionuserinfo = QtWidgets.QAction(MainWindow)
        self.actionuserinfo.setObjectName("actionuserinfo")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actiongrade)
        self.menu.addAction(self.actionclass)
        self.menu.addAction(self.actionsubject)
        self.menu.addAction(self.actionexamkinds)
        self.menu_2.addAction(self.actionstudent)
        self.menu_2.addAction(self.actionresult)
        self.menu_3.addAction(self.actionstudentinfo)
        self.menu_3.addAction(self.actionresultinfo)
        self.menu_4.addAction(self.actionuserinfo)
        self.menu_4.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        self.actionexit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        datetime = QtCore.QDateTime.currentDateTime()  # 获取当前日期时间
        time = datetime.toString("yyyy-MM-dd HH:mm:ss")  # 对日期时间进行格式化
        # 状态栏中显示登录用户、登录时间，以及版权信息
        self.statusbar.showMessage("当前登录用户：" + service.userName + " | 登录时间：" + time ,0)
        # 为基础设置菜单中的QAction绑定triggered信号
        self.menu.triggered[QtWidgets.QAction].connect(self.openSet)
        # 为基本信息管理菜单中的QAction绑定triggered信号
        self.menu_2.triggered[QtWidgets.QAction].connect(self.openBase)
        # 为系统查询菜单中的QAction绑定triggered信号
        self.menu_3.triggered[QtWidgets.QAction].connect(self.openQuery)
        # 为系统管理菜单中的QAction绑定triggered信号
        self.menu_4.triggered[QtWidgets.QAction].connect(self.openSys)

    # 基础设置菜单对应槽函数
    def openSet(self,m):
        if m.text()=="年级设置":
            self.m = grade.Ui_MainWindow()  # 创建年级设置窗体对象
            self.m.show()  # 显示窗体
        elif  m.text()=="班级设置":
            self.m = classes.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "考试科目设置":
            self.m = subject.Ui_MainWindow()  # 创建考试科目设置窗体对象
            self.m.show()  # 显示窗体
        elif  m.text()=="考试类别":
            self.m = examkinds.Ui_MainWindow()  # 创建考试类别设置窗体对象
            self.m.show()  # 显示窗体

    # 基本信息管理菜单对应槽函数
    def openBase(self,m):
        if  m.text()=="学生管理":
            self.m = student.Ui_MainWindow()  # 创建学生管理窗体对象
            self.m.show()  # 显示窗体
        elif  m.text()=="成绩管理":
            self.m = result.Ui_MainWindow()  # 创建成绩管理窗体对象
            self.m.show()  # 显示窗体

    # 系统查询菜单对应槽函数
    def openQuery(self,m):
        if  m.text()=="学生信息查询":
            self.m = studentinfo.Ui_MainWindow()  # 创建学生信息查询窗体对象
            self.m.show()  # 显示窗体
        elif  m.text()=="学生成绩查询":
            self.m = resultinfo.Ui_MainWindow()  # 创建学生成绩查询窗体对象
            self.m.show()  # 显示窗体

    # 系统管理菜单对应槽函数
    def openSys(self,m):
        if  m.text()=="用户维护":
            self.m = user.Ui_MainWindow()  # 创建用户维护窗体对象
            self.m.show()  # 显示窗体

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生成绩管理系统"))
        self.menu.setTitle(_translate("MainWindow", "基础设置"))
        self.menu_2.setTitle(_translate("MainWindow", "基本信息管理"))
        self.menu_3.setTitle(_translate("MainWindow", "系统查询"))
        self.menu_4.setTitle(_translate("MainWindow", "系统管理"))
        self.actiongrade.setText(_translate("MainWindow", "年级设置"))
        self.actionclass.setText(_translate("MainWindow", "班级设置"))
        self.actionsubject.setText(_translate("MainWindow", "考试科目设置"))
        self.actionexamkinds.setText(_translate("MainWindow", "考试类别"))
        self.actionstudent.setText(_translate("MainWindow", "学生管理"))
        self.actionresult.setText(_translate("MainWindow", "成绩管理"))
        self.actionstudentinfo.setText(_translate("MainWindow", "学生信息查询"))
        self.actionresultinfo.setText(_translate("MainWindow", "学生成绩查询"))
        self.actionuserinfo.setText(_translate("MainWindow", "用户维护"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
import img_rc