# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
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
        MainWindow.resize(705, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(96, 9, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cboxGrade = QtWidgets.QComboBox(self.centralwidget)
        self.cboxGrade.setGeometry(QtCore.QRect(169, 9, 69, 22))
        self.cboxGrade.setObjectName("cboxGrade")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(256, 9, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cboxClass = QtWidgets.QComboBox(self.centralwidget)
        self.cboxClass.setGeometry(QtCore.QRect(329, 9, 69, 22))
        self.cboxClass.setObjectName("cboxClass")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(649, 3, 51, 31))
        self.btnExit.setObjectName("btnExit")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(589, 3, 51, 31))
        self.btnDel.setObjectName("btnDel")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(469, 3, 51, 31))
        self.btnAdd.setObjectName("btnAdd")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(529, 3, 51, 31))
        self.btnEdit.setObjectName("btnEdit")
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(409, 3, 51, 31))
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(123, 353, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.editID = QtWidgets.QLineEdit(self.centralwidget)
        self.editID.setGeometry(QtCore.QRect(197, 353, 71, 20))
        self.editID.setObjectName("editID")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(293, 353, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.editName = QtWidgets.QLineEdit(self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(367, 353, 71, 20))
        self.editName.setObjectName("editName")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(463, 353, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.editAge = QtWidgets.QLineEdit(self.centralwidget)
        self.editAge.setGeometry(QtCore.QRect(507, 353, 71, 20))
        self.editAge.setObjectName("editAge")
        self.editAge.setValidator(QtGui.QIntValidator(0,99)) # 控制年龄在1到99之间
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(597, 353, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cboxSex = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSex.setGeometry(QtCore.QRect(647, 353, 51, 22))
        self.cboxSex.setObjectName("cboxSex")
        self.cboxSex.addItem("")
        self.cboxSex.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(123, 383, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.editPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.editPhone.setGeometry(QtCore.QRect(197, 383, 121, 20))
        self.editPhone.setObjectName("editPhone")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(343, 383, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.editAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.editAddress.setGeometry(QtCore.QRect(417, 383, 281, 20))
        self.editAddress.setObjectName("editAddress")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(29, 346, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bindGrade()  # 绑定年级下拉列表
        self.cboxGrade.currentIndexChanged.connect(self.bindClass)  # 根据年级绑定班级列表
        self.tbStudent.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbStudent.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.query()  # 窗体加载时显示所有数据
        self.tbStudent.itemClicked.connect(self.getItem)  # 获取选中的单元格数据
        self.btnQuery.clicked.connect(self.query)  # 绑定刷新按钮的单击信号
        self.btnAdd.clicked.connect(self.add)  # 绑定添加按钮的单击信号
        self.btnEdit.clicked.connect(self.edit)  # 绑定修改按钮的单击信号
        self.btnDel.clicked.connect(self.delete)  # 绑定删除按钮的单击信号

    # 查询学生信息，并显示在表格中
    def query(self):
        self.tbStudent.setRowCount(0)  # 清空表格中的所有行
        gname = self.cboxGrade.currentText()  # 记录选择的年级
        cname = self.cboxClass.currentText()  # 记录选择的班级
        # 获取所有学生信息
        if gname == "所有":
            result = service.query("select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo")
        # 获取指定年级学生信息
        elif gname != "所有" and cname == "所有":
            result = service.query(
                "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo where gradeName=%s", gname)
        # 获取指定年级指定班的学生信息
        elif gname != "所有" and cname != "所有":
            result = service.query(
                "select stuID,stuName,CONCAT(gradeName,className),sex,age,address,phone from v_studentinfo where gradeName=%s and className=%s",
                gname, cname)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbStudent.setRowCount(row)  # 设置表格行数
        self.tbStudent.setColumnCount(7)  # 设置表格列数
        # 设置表格的标题名称
        self.tbStudent.setHorizontalHeaderLabels(['学生编号', '学生姓名', '班级', '性别', '年龄', '家庭地址', '联系电话'])
        for i in range(row):  # 遍历行
            for j in range(self.tbStudent.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbStudent.setItem(i, j, data)  # 设置每个单元格的数据

    # 获取所有年级，显示在下拉列表中
    def bindGrade(self):
        self.cboxGrade.addItem("所有")
        result = service.query("select gradeName from tb_grade")  # 从年级表中查询数据
        for i in result:  # 遍历查询结果
            self.cboxGrade.addItem(i[0])  # 在下拉列表中显示年级

    # 根据年级获取相应班级，显示在下拉列表中
    def bindClass(self):
        self.cboxClass.clear()  # 清空列表
        self.cboxClass.addItem("所有")  # 增加首选项
        result = service.query("select className from v_classinfo where gradeName=%s",
                               self.cboxGrade.currentText())  # 从年级视图中查询数据
        for i in result:  # 遍历查询结果
            self.cboxClass.addItem(i[0])  # 在下拉列表中显示班级

    # 获取选中的表格内容
    def getItem(self, item):
        if item.column() == 0:  # 如果单击的是第一列
            self.select = item.text()  # 获取单击的单元格文本
            self.editID.setText(self.select)  # 显示在学生编号文本框中
            # 根据学生编号查询学生信息
            result = service.query("select * from v_studentinfo where stuID=%s",item.text())
            self.editName.setText(result[0][1]) # 显示学生姓名
            self.editAge.setText(str(result[0][2])) # 显示年龄
            self.editPhone.setText(result[0][4]) # 显示电话
            self.editAddress.setText(result[0][5]) # 显示地址
            self.cboxSex.setCurrentText(result[0][3]) # 显示性别

    # 判断要添加的记录是否存在
    def getName(self, sid):
        # 根据年级编号和班级名查询数据
        result = service.query("select * from tb_student where stuID =%s", sid)
        return len(result)  # 返回查询结果的记录

    # 添加学生信息
    def add(self):
        stuID = self.editID.text()  # 记录学生编号
        stuName = self.editName.text()  # 记录学生姓名
        age = self.editAge.text()  # 记录年龄
        sex = self.cboxSex.currentText()  # 记录性别
        phone = self.editPhone.text()  # 记录电话
        address = self.editAddress.text()  # 记录地址
        if self.cboxGrade.currentText() != "" and self.cboxGrade.currentText() != "所有":  # 如果选择了年级
            # 获取年级对应的ID
            result = service.query("select gradeID from tb_grade where gradeName=%s", self.cboxGrade.currentText())
            if len(result) > 0:  # 如果结果大于0
                gradeID = result[0]  # 记录选择的年级对应的ID
                if self.cboxClass.currentText() != "" and self.cboxClass.currentText() != "所有":  # 如果选择了班级
                    # 获取班级对应的ID
                    result = service.query("select classID from tb_class where gradeID=%s and className=%s", gradeID,
                                           self.cboxClass.currentText())
                    if len(result) > 0:  # 如果结果大于0
                        classID = result[0]  # 记录选择的班级对应的ID
                        if stuID != "" and stuName != "":  # 判学生编号和学生姓名不为空
                            if self.getName(stuID) > 0:  # 判断已经存在该记录
                                self.editID.setText("")  # 清空学生编号文本框
                                QMessageBox.information(None, '提示', '您要添加的学生编号已经存在，请重新输入！', QMessageBox.Ok)
                            else:
                                # 执行添加语句
                                result = service.exec(
                                        "insert into tb_student(stuID,stuName,classID,gradeID,age,sex,phone,address) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (stuID, stuName, classID, gradeID, age, sex, phone, address))
                                if result > 0:  # 如果结果大于0，说明添加成功
                                    self.query()  # 在表格中显示最新数据
                                    QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请先添加年级！', QMessageBox.Ok)

    # 修改学生信息
    def edit(self):
        try:
            if self.select != "":  # 判断是否选择了要修改的数据
                stuID = self.select  # 记录要修改的学生编号
                age = self.editAge.text()  # 记录年龄
                sex = self.cboxSex.currentText()  # 记录性别
                phone = self.editPhone.text()  # 记录电话
                address = self.editAddress.text()  # 记录地址
                # 执行修改操作
                result = service.exec("update tb_student set age=%s ,sex= %s,phone= %s,address= %s where stuID=%s",
                                      (age, sex, phone, address, stuID))
                if result > 0:  # 如果结果大于0，说明修改成功
                    self.query()  # 在表格中显示最新数据
                    QMessageBox.information(None, '提示', '信息修改成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要修改的数据！', QMessageBox.Ok)

    # 删除学生信息
    def delete(self):
        try:
            if self.select != "":  # 判断是否选择了要删除的数据
                # 执行删除操作
                result = service.exec("delete from tb_student where stuID= %s", (self.select,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                    QMessageBox.information(None, '提示', '信息删除成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要删除的数据！', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生信息管理"))
        self.label_2.setText(_translate("MainWindow", "所属年级："))
        self.label_3.setText(_translate("MainWindow", "所属班级："))
        self.btnExit.setText(_translate("MainWindow", "退出"))
        self.btnDel.setText(_translate("MainWindow", "删除"))
        self.btnAdd.setText(_translate("MainWindow", "添加"))
        self.btnEdit.setText(_translate("MainWindow", "修改"))
        self.btnQuery.setText(_translate("MainWindow", "刷新"))
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
        self.label_4.setText(_translate("MainWindow", "学生编号："))
        self.label_5.setText(_translate("MainWindow", "学生姓名："))
        self.label_6.setText(_translate("MainWindow", "年龄："))
        self.label_7.setText(_translate("MainWindow", "性别："))
        self.cboxSex.setItemText(0, _translate("MainWindow", "男"))
        self.cboxSex.setItemText(1, _translate("MainWindow", "女"))
        self.label_8.setText(_translate("MainWindow", "联系电话："))
        self.label_9.setText(_translate("MainWindow", "家庭地址："))
        self.label.setText(_translate("MainWindow", "信息设置"))
