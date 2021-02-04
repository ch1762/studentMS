# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentinfo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

sys.path.append("../")  # 返回上层路径
from service import service


class Ui_MainWindow(QMainWindow):
    # 构造方法
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self)  # 初始化窗体设置

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(105, 8, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cboxCondition = QtWidgets.QComboBox(self.centralwidget)
        self.cboxCondition.setGeometry(QtCore.QRect(230, 8, 100, 22))
        self.cboxCondition.setObjectName("cboxCondition")
        self.cboxCondition.addItem("")
        self.cboxCondition.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 8, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(649, 3, 51, 31))
        self.btnExit.setObjectName("btnExit")
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(590, 3, 51, 31))
        self.btnQuery.setObjectName("btnQuery")
        self.tbStudent = QtWidgets.QTableWidget(self.centralwidget)
        self.tbStudent.setGeometry(QtCore.QRect(0, 40, 701, 301))
        self.tbStudent.setObjectName("tbStudent")
        self.tbStudent.setColumnCount(7)
        self.tbStudent.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbStudent.setHorizontalHeaderItem(6, item)
        self.editKey = QtWidgets.QLineEdit(self.centralwidget)
        self.editKey.setGeometry(QtCore.QRect(485, 9, 85, 20))
        self.editKey.setObjectName("editKey")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tbStudent.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbStudent.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.query()  # 窗体加载时显示所有数据
        self.btnQuery.clicked.connect(self.query)  # 绑定查询按钮的单击信号

    # 查询学生信息，并显示在表格中
    def query(self):
        self.tbStudent.setRowCount(0)  # 清空表格中的所有行
        # 获取所有学生信息
        if self.editKey.text() == "":
            result = service.query(
                "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo")
        else:
            key = self.editKey.text()  # 记录查询关键字
            # 根据学生编号查询信息
            if self.cboxCondition.currentText() == "学生编号":
                sql="select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo where stuID like '%" + key + "%'"
                result = service.query2(sql)
            # 根据学生姓名查询信息
            elif self.cboxCondition.currentText() == "学生姓名":
                sql = "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo where stuName like '%" + key + "%'"
                result = service.query2(sql)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbStudent.setRowCount(row)  # 设置表格行数
        self.tbStudent.setColumnCount(7)  # 设置表格列数
        # 设置表格的标题名称
        self.tbStudent.setHorizontalHeaderLabels(['学生编号', '学生姓名', '班级', '性别', '年龄', '家庭地址', '联系电话'])
        for i in range(row):  # 遍历行
            for j in range(self.tbStudent.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbStudent.setItem(i, j, data)  # 设置每个单元格的数据

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生信息查询"))
        self.label_2.setText(_translate("MainWindow", "选择查询列表："))
        self.cboxCondition.setItemText(0, _translate("MainWindow", "学生编号"))
        self.cboxCondition.setItemText(1, _translate("MainWindow", "学生姓名"))
        self.label_3.setText(_translate("MainWindow", "输入查询关键字："))
        self.btnExit.setText(_translate("MainWindow", "退出"))
        self.btnQuery.setText(_translate("MainWindow", "查询"))
        item = self.tbStudent.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学生编号"))
        item = self.tbStudent.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "学生姓名"))
        item = self.tbStudent.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "班级"))
        item = self.tbStudent.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tbStudent.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "年龄"))
        item = self.tbStudent.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "家庭地址"))
        item = self.tbStudent.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "联系电话"))
