# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
sys.path.append("../") # 返回上层路径
from service import service

class Ui_MainWindow(QMainWindow):
    # 构造方法
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self) # 初始化窗体设置

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbUser = QtWidgets.QTableWidget(self.centralwidget)
        self.tbUser.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.tbUser.setObjectName("tbUser")
        self.tbUser.setColumnCount(2)
        self.tbUser.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(1, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 220, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.editName = QtWidgets.QLineEdit(self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(100, 220, 80, 20))
        self.editName.setObjectName("editID")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.editPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.editPwd.setGeometry(QtCore.QRect(300, 220, 80, 20))
        self.editPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPwd.setObjectName("editName")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(40, 260, 50, 30))
        self.btnAdd.setObjectName("btnAdd")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(130, 260, 50, 30))
        self.btnEdit.setObjectName("btnEdit")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(220, 260, 50, 30))
        self.btnDel.setObjectName("btnDel")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(310, 260, 50, 30))
        self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close) # 关闭窗口
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tbUser.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbUser.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.query() # 窗体加载时显示所有数据
        self.tbUser.itemClicked.connect(self.getItem) # 获取选中的单元格数据
        self.btnAdd.clicked.connect(self.add) # 绑定添加按钮的单击信号
        self.btnEdit.clicked.connect(self.edit) # 绑定修改按钮的单击信号
        self.btnDel.clicked.connect(self.delete) # 绑定删除按钮的单击信号

    # 查询用户信息，并显示在表格中
    def query(self):
        self.tbUser.setRowCount(0) # 清空表格中的所有行
        result = service.query("select * from tb_user") # 调用服务类中的公共方法执行查询语句
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbUser.setRowCount(row)  # 设置表格行数
        self.tbUser.setColumnCount(2)  # 设置表格列数
        # 设置表格的标题名称
        self.tbUser.setHorizontalHeaderLabels(['用户名称', '用户密码'])
        for i in range(row):  # 遍历行
            for j in range(self.tbUser.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbUser.setItem(i, j, data) # 设置每个单元格的数据

    # 获取选中的表格内容
    def getItem(self, item):
        if item.column() == 0:  # 如果单击的是第一列
            self.select = item.text() # 获取单击的单元格文本
            self.editName.setText(self.select) # 显示在用户名称文本框中

    # 添加用户信息
    def add(self):
        userName = self.editName.text() # 记录输入的用户名
        userPwd = self.editPwd.text() # 记录输入的用户密码
        if userName != "" and userPwd != "": # 判断用户名和密码不为空
            # 执行添加语句
            result=service.exec("insert into tb_user(userName,userPwd) values (%s,%s)",(userName,userPwd))
            if result>0:  # 如果结果大于0，说明添加成功
                self.query() # 在表格中显示最新数据
                QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)

    # 修改用户信息
    def edit(self):
        try:
            if self.select!="": # 判断是否选择了要修改的数据
                userPwd = self.editPwd.text() # 记录修改的用户密码
                if userPwd != "": # 判断密码不为空
                    # 执行修改操作
                    result=service.exec("update tb_user set userPwd= %s where userName=%s",(userPwd,self.select))
                    if result>0: # 如果结果大于0，说明修改成功
                        self.query() # 在表格中显示最新数据
                        QMessageBox.information(None, '提示', '信息修改成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要修改的数据！', QMessageBox.Ok)

    # 删除用户信息
    def delete(self):
        try:
            if self.select!="": # 判断是否选择了要删除的数据
                # 执行删除操作
                result=service.exec("delete from tb_user where userName= %s",(self.select,))
                if result>0: # 如果结果大于0，说明删除成功
                    self.query() # 在表格中显示最新数据
                    QMessageBox.information(None, '提示', '信息删除成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要删除的数据！', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户信息维护"))
        item = self.tbUser.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "用户名"))
        item = self.tbUser.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "密码"))
        self.label_3.setText(_translate("MainWindow", "用户密码："))
        self.label_2.setText(_translate("MainWindow", "用户名称："))
        self.btnAdd.setText(_translate("MainWindow", "添加"))
        self.btnEdit.setText(_translate("MainWindow", "修改"))
        self.btnDel.setText(_translate("MainWindow", "删除"))
        self.btnExit.setText(_translate("MainWindow", "退出"))
