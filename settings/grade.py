# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grade.ui'
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
        self.tbGrade = QtWidgets.QTableWidget(self.centralwidget)
        self.tbGrade.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.tbGrade.setObjectName("tbGrade")
        self.tbGrade.setColumnCount(2)
        self.tbGrade.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbGrade.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbGrade.setHorizontalHeaderItem(1, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 220, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.editID = QtWidgets.QLineEdit(self.centralwidget)
        self.editID.setGeometry(QtCore.QRect(100, 220, 80, 22))
        self.editID.setObjectName("editID")
        self.editID.setValidator(QtGui.QIntValidator(0, 9999))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.editName = QtWidgets.QLineEdit(self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(300, 220, 80, 22))
        self.editName.setObjectName("editName")
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
        self.btnExit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tbGrade.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbGrade.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.query()  # 窗体加载时显示所有数据
        self.tbGrade.itemClicked.connect(self.getItem)  # 获取选中的单元格数据
        self.btnAdd.clicked.connect(self.add)  # 绑定添加按钮的单击信号
        self.btnEdit.clicked.connect(self.edit)  # 绑定修改按钮的单击信号
        self.btnDel.clicked.connect(self.delete)  # 绑定删除按钮的单击信号

    # 查询年级信息，并显示在表格中
    def query(self):
        self.tbGrade.setRowCount(0)  # 清空表格中的所有行
        result = service.query("select * from tb_grade")  # 调用服务类中的公共方法执行查询语句
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbGrade.setRowCount(row)  # 设置表格行数
        self.tbGrade.setColumnCount(2)  # 设置表格列数
        # 设置表格的标题名称
        self.tbGrade.setHorizontalHeaderLabels(['年级编号', '年级名称'])
        for i in range(row):  # 遍历行
            for j in range(self.tbGrade.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbGrade.setItem(i, j, data)  # 设置每个单元格的数据

    # 获取选中的表格内容
    def getItem(self, item):
        if item.column() == 0:  # 如果单击的是第一列
            self.select = item.text()  # 获取单击的单元格文本
            self.editID.setText(self.select)  # 显示在文本框中

    def getName(self,name):
        result = service.query("select * from tb_grade where gradeName = %s", name)
        return len(result)

    # 添加年级信息
    def add(self):
        gradeID = self.editID.text()  # 记录输入的年级编号
        gradeName = self.editName.text()  # 记录输入的年级名称
        if gradeID != "" and gradeName != "":  # 判断年级编号和年级名称不为空
            if self.getName(gradeName)>0:
                self.editName.setText("")
                QMessageBox.information(None, '提示', '您要添加的年级已经存在，请重新输入！', QMessageBox.Ok)
            else:
                # 执行添加语句
                result = service.exec("insert into tb_grade(gradeID,gradeName) values (%s,%s)", (gradeID, gradeName))
                if result > 0:  # 如果结果大于0，说明添加成功
                    self.query()  # 在表格中显示最新数据
                    QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)

    # 修改年级信息
    def edit(self):
        try:
            if self.select != "":  # 判断是否选择了要修改的数据
                gradeName = self.editName.text()  # 记录修改的年级名称
                if gradeName != "":  # 判断年级名称不为空
                    if self.getName(gradeName) > 0:
                        self.editName.setText("")
                        QMessageBox.information(None, '提示', '您要修改的年级已经存在，请重新输入！', QMessageBox.Ok)
                    else:
                        # 执行修改操作
                        result = service.exec("update tb_grade set gradeName= %s where gradeID=%s", (gradeName, self.select))
                        if result > 0:  # 如果结果大于0，说明修改成功
                            self.query()  # 在表格中显示最新数据
                            QMessageBox.information(None, '提示', '信息修改成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要修改的数据！', QMessageBox.Ok)

    # 删除年级信息
    def delete(self):
        try:
            if self.select != "":  # 判断是否选择了要删除的数据
                # 执行删除年级操作
                result = service.exec("delete from tb_grade where gradeID= %s", (self.select,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                # 删除年级下的所有班级
                result = service.exec("delete from tb_class where gradeID= %s", (self.select,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                QMessageBox.information(None, '提示', '信息删除成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要删除的数据！', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "年级设置"))
        item = self.tbGrade.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "年级编号"))
        item = self.tbGrade.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "年级名称"))
        self.label_3.setText(_translate("MainWindow", "年级名称："))
        self.label_2.setText(_translate("MainWindow", "年级编号："))
        self.btnAdd.setText(_translate("MainWindow", "添加"))
        self.btnEdit.setText(_translate("MainWindow", "修改"))
        self.btnDel.setText(_translate("MainWindow", "删除"))
        self.btnExit.setText(_translate("MainWindow", "退出"))
