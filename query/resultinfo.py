# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultinfo.ui'
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
        MainWindow.resize(762, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cboxKinds = QtWidgets.QComboBox(self.centralwidget)
        self.cboxKinds.setGeometry(QtCore.QRect(395, 10, 69, 22))
        self.cboxKinds.setObjectName("cboxKinds")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(709, 3, 51, 31))
        self.btnExit.setObjectName("btnExit")
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(649, 3, 51, 31))
        self.btnQuery.setObjectName("btnQuery")
        self.tbResult = QtWidgets.QTableWidget(self.centralwidget)
        self.tbResult.setGeometry(QtCore.QRect(0, 40, 761, 301))
        self.tbResult.setObjectName("tbResult")
        self.tbResult.setColumnCount(6)
        self.tbResult.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbResult.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbResult.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbResult.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbResult.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbResult.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbResult.setHorizontalHeaderItem(5, item)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.cboxSubject = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSubject.setGeometry(QtCore.QRect(557, 9, 69, 22))
        self.cboxSubject.setObjectName("cboxSubject")
        self.editName = QtWidgets.QLineEdit(self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(190, 10, 100, 20))
        self.editName.setObjectName("editName")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(45, 10, 125, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tbResult.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbResult.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.bindCbox() # 窗体加载时绑定考试类别和考试科目下拉列表
        self.query()  # 窗体加载时显示所有数据
        self.btnQuery.clicked.connect(self.query)  # 绑定查询按钮的单击信号

    def bindCbox(self):
        self.cboxKinds.addItem("所有") # 设置考试类别的默认首选项
        result = service.query("select kindName from tb_examkinds")  # 从考试类别中查询数据
        for i in result:  # 遍历查询结果
            self.cboxKinds.addItem(i[0])  # 在下拉列表中显示考试类别
        self.cboxSubject.addItem("所有")  # 设置考试科目的默认首选项
        result = service.query("select subName from tb_subject")  # 从考试科目中查询数据
        for i in result:  # 遍历查询结果
            self.cboxSubject.addItem(i[0])  # 在下拉列表中显示考试科目

    # 查询成绩信息，并显示在表格中
    def query(self):
        self.tbResult.setRowCount(0)  # 清空表格中的所有行
        stuname=self.editName.text() # 记录查询的学生姓名
        kindname=self.cboxKinds.currentText() # 记录选择的考试类别
        subname=self.cboxSubject.currentText() # 记录选择的考试科目
        if stuname == "":
            if kindname=="所有":
                if subname=="所有":
                    # 查询所有成绩信息
                    result = service.query(
                        "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo")
                else:
                    # 根据考试科目查询成绩信息
                    result = service.query(
                        "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where subName=%s",subname)
            else:
                # 根据考试类别查询成绩信息
                result = service.query(
                    "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s",kindname)
        else:
            if kindname == "所有":
                if subname == "所有":
                    # 根据学生姓名查询成绩信息
                    result = service.query2(
                        "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where stuName like '%" + stuname + "%'")
                else:
                    # 根据学生姓名和考试科目查询成绩信息
                    result = service.query2(
                        "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where stuName like '%" + stuname + "%' and subName='" + subname + "'")
            else:
                # 根据学生姓名、考试科目和考试类别查询成绩信息
                result = service.query2(
                    "select stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where stuName like '%" + stuname + "%' and subName='" + subname + "' and kindName='" + kindname + "'")
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbResult.setRowCount(row)  # 设置表格行数
        self.tbResult.setColumnCount(6)  # 设置表格列数
        # 设置表格的标题名称
        self.tbResult.setHorizontalHeaderLabels(['学生编号', '学生姓名', '班级', '科目', '种类', '成绩'])
        for i in range(row):  # 遍历行
            for j in range(self.tbResult.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbResult.setItem(i, j, data)  # 设置每个单元格的数据

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生成绩查询"))
        self.label_2.setText(_translate("MainWindow", "考试种类："))
        self.btnExit.setText(_translate("MainWindow", "退出"))
        self.btnQuery.setText(_translate("MainWindow", "查询"))
        item = self.tbResult.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学生编号"))
        item = self.tbResult.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "学生姓名"))
        item = self.tbResult.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "班级"))
        item = self.tbResult.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "科目"))
        item = self.tbResult.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "种类"))
        item = self.tbResult.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "成绩"))
        self.label_5.setText(_translate("MainWindow", "考试科目："))
        self.label_7.setText(_translate("MainWindow", "输入学生姓名："))
