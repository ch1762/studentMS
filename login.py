# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys  # 导入sys模块
import main
from service import service

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        MainWindow.resize(360, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 360, 80))
        self.label.setStyleSheet("border-image: url(:/newPrefix/images/login.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.editName = QtWidgets.QLineEdit(self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(195, 100, 140, 20))
        self.editName.setObjectName("editName")
        self.editPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.editPwd.setGeometry(QtCore.QRect(195, 130, 140, 20))
        self.editPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPwd.setObjectName("editPwd")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 130, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(200, 160, 60, 25))
        self.btnLogin.setObjectName("btnLogin")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(270, 160, 60, 25))
        self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close) # 关闭登录窗体
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 输入密码后按回车键执行登录操作
        self.editPwd.editingFinished.connect(self.openMain)
        # 单击“登录”按钮执行登录操作
        self.btnLogin.clicked.connect(self.openMain)

    # 打开主窗体
    def openMain(self):
        service.userName=self.editName.text() # 全局变量，记录用户名
        self.userPwd=self.editPwd.text() # 记录用户密码
        if service.userName != "" and self.userPwd != "": # 判断用户名和密码不为空
            # 根据用户名和密码查询数据
            result=service.query("select * from tb_user where userName = %s and userPwd = %s",service.userName,self.userPwd)
            if len(result)>0: # 如果查询结果大于0，说明存在该用户，可以登录
                self.m = main.Ui_MainWindow()  # 创建主窗体对象
                self.m.show()  # 显示主窗体
                MainWindow.hide() # 隐藏当前的登录窗体
            else:
                self.editName.setText("") # 清空用户名文本
                self.editPwd.setText("") # 清空密码文本框
                QMessageBox.warning(None, '警告', '请输入正确的用户名和密码！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入用户名和密码！', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "系统登录"))
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密  码："))
        self.btnLogin.setText(_translate("MainWindow", "登录"))
        self.btnExit.setText(_translate("MainWindow", "退出"))
import img_rc

# 主方法
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程
