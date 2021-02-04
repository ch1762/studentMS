# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classes.ui'
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
        self.editName = QtWidgets.QLineEdit(self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(300, 235, 80, 20))
        self.editName.setObjectName("editName")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(310, 260, 50, 30))
        self.btnExit.setObjectName("btnExit")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(130, 260, 50, 30))
        self.btnEdit.setObjectName("btnEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 235, 80, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(7, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(40, 260, 50, 30))
        self.btnAdd.setObjectName("btnAdd")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(220, 260, 50, 30))
        self.btnDel.setObjectName("btnDel")
        self.tbClass = QtWidgets.QTableWidget(self.centralwidget)
        self.tbClass.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.tbClass.setObjectName("tbClass")
        self.tbClass.setColumnCount(3)
        self.tbClass.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbClass.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbClass.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbClass.setHorizontalHeaderItem(2, item)
        self.editID = QtWidgets.QLineEdit(self.centralwidget)
        self.editID.setGeometry(QtCore.QRect(100, 235, 80, 20))
        self.editID.setObjectName("editID")
        self.editID.setValidator(QtGui.QIntValidator(0, 9999))
        self.cboxGrade = QtWidgets.QComboBox(self.centralwidget)
        self.cboxGrade.setGeometry(QtCore.QRect(100, 205, 70, 22))
        self.cboxGrade.setObjectName("cboxGrade")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 235, 80, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bindGrade() # 绑定年级下拉列表
        self.tbClass.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbClass.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.query()  # 窗体加载时显示所有数据
        self.tbClass.itemClicked.connect(self.getItem)  # 获取选中的单元格数据
        self.btnAdd.clicked.connect(self.add)  # 绑定添加按钮的单击信号
        self.btnEdit.clicked.connect(self.edit)  # 绑定修改按钮的单击信号
        self.btnDel.clicked.connect(self.delete)  # 绑定删除按钮的单击信号

    # 查询班级信息，并显示在表格中
    def query(self):
        self.tbClass.setRowCount(0)  # 清空表格中的所有行
        result = service.query("select classID,gradeName,className from v_classinfo")  # 调用服务类中的公共方法执行查询语句
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbClass.setRowCount(row)  # 设置表格行数
        self.tbClass.setColumnCount(3)  # 设置表格列数
        # 设置表格的标题名称
        self.tbClass.setHorizontalHeaderLabels(['班级编号', '所属年级','班级名称'])
        for i in range(row):  # 遍历行
            for j in range(self.tbClass.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbClass.setItem(i, j, data)  # 设置每个单元格的数据

    # 获取所有年级，显示在下拉列表中
    def bindGrade(self):
        result=service.query("select gradeName from tb_grade") # 从年级表中查询数据
        for i in result: # 遍历查询结果
            self.cboxGrade.addItem(i[0]) # 在下拉列表中显示年级

    # 获取选中的表格内容
    def getItem(self, item):
        if item.column() == 0:  # 如果单击的是第一列
            self.select = item.text()  # 获取单击的单元格文本
            self.editID.setText(self.select)  # 显示在班级编号文本框中

    # 判断要添加的记录是否存在
    def getName(self, cid,name):
        # 根据年级编号和班级名查询数据
        result = service.query("select * from tb_class where gradeID =%s and className = %s", cid,name)
        return len(result) # 返回查询结果的记录

    # 添加班级信息
    def add(self):
        classID = self.editID.text()  # 记录输入的班级编号
        className = self.editName.text()  # 记录输入的班级名称
        if self.cboxGrade.currentText() !="": # 如果选择了年级
            # 获取年级对应的ID
            result=service.query("select gradeID from tb_grade where gradeName=%s",self.cboxGrade.currentText())
            if len(result)>0: # 如果结果大于0
                gradeID=result[0] # 记录选择的年级对应的ID
                if classID != "" and className != "":  # 判断班级编号和班级名称不为空
                    if self.getName(gradeID,className) > 0: # 判断已经存在该记录
                        self.editName.setText("") # 清空班级文本框
                        QMessageBox.information(None, '提示', '您要添加的班级已经存在，请重新输入！', QMessageBox.Ok)
                    else:
                        # 执行添加语句
                        result = service.exec("insert into tb_class(classID,gradeID,className) values (%s,%s,%s)", (classID, gradeID,className))
                        if result > 0:  # 如果结果大于0，说明添加成功
                            self.query()  # 在表格中显示最新数据
                            QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请先添加年级！', QMessageBox.Ok)

    # 修改班级信息
    def edit(self):
        try:
            if self.select != "":  # 判断是否选择了要修改的数据
                className = self.editName.text()  # 记录修改的班级名称
                if self.cboxGrade.currentText() != "": # 如果选择了年级
                    # 获取年级对应的ID
                    result = service.query("select gradeID from tb_grade where gradeName=%s", self.cboxGrade.currentText())
                    if len(result) > 0: # 如果结果大于0
                        gradeID = result[0] # 记录选择的年级对应的ID
                        if className != "":  # 判断班级名称不为空
                            if self.getName(gradeID,className) > 0: # 判断已经存在该记录
                                self.editName.setText("") # 清空班级文本框
                                QMessageBox.information(None, '提示', '您要修改的班级已经存在，请重新输入！', QMessageBox.Ok)
                            else:
                                # 执行修改操作
                                result = service.exec("update tb_class set gradeID=%s , className= %s where classID=%s",
                                                      (gradeID,className, self.select))
                                if result > 0:  # 如果结果大于0，说明修改成功
                                    self.query()  # 在表格中显示最新数据
                                    QMessageBox.information(None, '提示', '信息修改成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要修改的数据！', QMessageBox.Ok)

    # 删除班级信息
    def delete(self):
        try:
            if self.select != "":  # 判断是否选择了要删除的数据
                # 执行删除操作
                result = service.exec("delete from tb_class where classID= %s", (self.select,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                    QMessageBox.information(None, '提示', '信息删除成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要删除的数据！', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "班级设置"))
        self.btnExit.setText(_translate("MainWindow", "退出"))
        self.btnEdit.setText(_translate("MainWindow", "修改"))
        self.label_3.setText(_translate("MainWindow", "班级名称："))
        self.label_2.setText(_translate("MainWindow", "选择年级："))
        self.btnAdd.setText(_translate("MainWindow", "添加"))
        self.btnDel.setText(_translate("MainWindow", "删除"))
        item = self.tbClass.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "班级编号"))
        item = self.tbClass.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "年级编号"))
        item = self.tbClass.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "班级名称"))
        self.label_4.setText(_translate("MainWindow", "班级编号："))
