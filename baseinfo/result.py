# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
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
        MainWindow.resize(766, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(7, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cboxKinds = QtWidgets.QComboBox(self.centralwidget)
        self.cboxKinds.setGeometry(QtCore.QRect(80, 10, 69, 22))
        self.cboxKinds.setObjectName("cboxKinds")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(317, 9, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cboxClass = QtWidgets.QComboBox(self.centralwidget)
        self.cboxClass.setGeometry(QtCore.QRect(390, 9, 69, 22))
        self.cboxClass.setObjectName("cboxClass")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(710, 3, 51, 31))
        self.btnExit.setObjectName("btnExit")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(650, 3, 51, 31))
        self.btnDel.setObjectName("btnDel")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(530, 3, 51, 31))
        self.btnAdd.setObjectName("btnAdd")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(590, 3, 51, 31))
        self.btnEdit.setObjectName("btnEdit")
        self.btnQuery = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuery.setGeometry(QtCore.QRect(470, 3, 51, 31))
        self.btnQuery.setObjectName("btnQuery")
        self.tbResult = QtWidgets.QTableWidget(self.centralwidget)
        self.tbResult.setGeometry(QtCore.QRect(0, 40, 761, 301))
        self.tbResult.setObjectName("tbResult")
        self.tbResult.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tbResult.setHorizontalHeaderItem(6, item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(303, 353, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(473, 355, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(643, 356, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.editResult = QtWidgets.QLineEdit(self.centralwidget)
        self.editResult.setGeometry(QtCore.QRect(687, 356, 71, 20))
        self.editResult.setObjectName("editResult")
        self.cboxGrade = QtWidgets.QComboBox(self.centralwidget)
        self.cboxGrade.setGeometry(QtCore.QRect(233, 10, 69, 22))
        self.cboxGrade.setObjectName("cboxGrade")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(160, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.cboxStuName = QtWidgets.QComboBox(self.centralwidget)
        self.cboxStuName.setGeometry(QtCore.QRect(380, 353, 69, 22))
        self.cboxStuName.setObjectName("cboxStuName")
        self.cboxSubject = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSubject.setGeometry(QtCore.QRect(550, 354, 69, 22))
        self.cboxSubject.setObjectName("cboxSubject")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bindGrade()  # 绑定年级下拉列表
        self.bindCbox()  # 绑定考试科目、类别和姓名下拉列表
        self.cboxGrade.currentIndexChanged.connect(self.bindClass)  # 根据年级绑定班级列表
        self.cboxClass.currentIndexChanged.connect(self.bindStuName)  # 显示指定班的所有学生
        self.tbResult.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbResult.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.query()  # 窗体加载时显示所有数据
        self.tbResult.itemClicked.connect(self.getItem)  # 获取选中的单元格数据
        self.btnQuery.clicked.connect(self.query)  # 绑定刷新按钮的单击信号
        self.btnAdd.clicked.connect(self.add)  # 绑定添加按钮的单击信号
        self.btnEdit.clicked.connect(self.edit)  # 绑定修改按钮的单击信号
        self.btnDel.clicked.connect(self.delete)  # 绑定删除按钮的单击信号

    # 查询学生成绩信息，并显示在表格中
    def query(self):
        self.tbResult.setRowCount(0)  # 清空表格中的所有行
        kindname=self.cboxKinds.currentText() # 记录选择的考试类别
        gradename = self.cboxGrade.currentText()  # 记录选择的年级
        classname = self.cboxClass.currentText()  # 记录选择的班级
        if kindname=="所有":
            if gradename == "所有":
                if classname=="所有" or classname=="":
                    # 获取所有学生的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo")
                else:
                    # 获取指定班级的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where className=%s",
                        classname)
            else:
                if classname == "所有":
                    # 获取指定年级的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where gradeName=%s",
                        gradename)
                else:
                    # 获取指定年级指定班的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where gradeName=%s and className=%s",
                        gradename,classname)
        else:
            if gradename == "所有":
                if classname=="所有" or classname=="":
                    # 获取指定考试类别的所有学生成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s",kindname)
                else:
                    # 获取指定考试类别的指定班级的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s and className=%s",
                        kindname,classname)
            else:
                if classname == "所有":
                    # 获取指定考试类别的指定年级的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s and gradeName=%s",
                        kindname,gradename)
                else:
                    # 获取指定考试类别的指定年级指定班的成绩信息
                    result = service.query(
                        "select ID,stuID,stuName,CONCAT(gradeName,className),subName,kindName,result from v_resultinfo where kindName=%s and gradeName=%s and className=%s",
                        kindname,gradename,classname)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbResult.setRowCount(row)  # 设置表格行数
        self.tbResult.setColumnCount(7)  # 设置表格列数
        # 设置表格的标题名称
        self.tbResult.setHorizontalHeaderLabels(['编号', '学生编号', '学生姓名', '班级', '科目', '种类', '成绩'])
        for i in range(row):  # 遍历行
            for j in range(self.tbResult.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbResult.setItem(i, j, data)  # 设置每个单元格的数据

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
                               self.cboxGrade.currentText())  # 从班级视图中查询数据
        for i in result:  # 遍历查询结果
            self.cboxClass.addItem(i[0])  # 在下拉列表中显示年级

    # 显示所有考试类别、考试科目和学生姓名
    def bindCbox(self):
        self.cboxKinds.addItem("所有")  # 设置考试类别的默认首选项
        result = service.query("select kindName from tb_examkinds")  # 从考试类别表中查询数据
        for i in result:  # 遍历查询结果
            self.cboxKinds.addItem(i[0])  # 在下拉列表中显示考试类别
        self.cboxSubject.addItem("所有")  # 设置考试科目的默认首选项
        result = service.query("select subName from tb_subject")  # 从考试科目表中查询数据
        for i in result:  # 遍历查询结果
            self.cboxSubject.addItem(i[0])  # 在下拉列表中显示考试科目
        result = service.query("select stuName from tb_student")  # 从学生信息表中查询数据
        for i in result:  # 遍历查询结果
            self.cboxStuName.addItem(i[0])  # 在下拉列表中显示所有学生姓名

    def bindStuName(self):
        self.cboxStuName.clear()  # 清空列表
        result = service.query("select stuName from v_studentinfo where gradeName=%s and className=%s",
                               self.cboxGrade.currentText(), self.cboxClass.currentText())  # 从学生信息视图中查询数据
        for i in result:  # 遍历查询结果
            self.cboxStuName.addItem(i[0])  # 在下拉列表中显示指定班的学生姓名

    # 获取选中的表格内容
    def getItem(self, item):
        if item.column()==0: # 如果单击的是第一列
            self.select = item.text()  # 获取单击的单元格文本
            # 根据编号查询成绩信息
            result = service.query("select * from v_resultinfo where ID=%s", self.select)
            self.cboxKinds.setCurrentText(result[0][3])  # 显示考试类别
            self.cboxGrade.setCurrentText(result[0][6])  # 显示年级
            self.cboxClass.setCurrentText(result[0][5])  # 显示班级
            self.cboxStuName.setCurrentText(result[0][2])  # 显示学生姓名
            self.cboxSubject.setCurrentText(result[0][4])  # 显示考试科目
            self.editResult.setText(str(result[0][7]))  # 显示学生分数

    # 判断要添加的记录是否存在
    def getScore(self, sid, kindid, subid):
        # 根据年级编号和班级名查询数据
        result = service.query("select * from tb_result where stuID =%s and kindID=%s and subID=%s", sid, kindid, subid)
        return len(result)  # 返回查询结果的记录

    # 添加学生成绩信息
    def add(self):
        subname = self.cboxSubject.currentText()  # 记录考试科目
        kindname = self.cboxKinds.currentText()  # 记录考试类别
        gradename = self.cboxGrade.currentText()  # 记录年级
        classname = self.cboxClass.currentText()  # 记录班级
        stuname = self.cboxStuName.currentText()  # 记录学生姓名
        score = self.editResult.text()  # 记录输入的分数
        if kindname != "所有":  # 如果选择了考试类别
            # 获取选择的考试类别对应ID
            result = service.query("select kindID from tb_examkinds where kindName=%s", kindname)
            if len(result) > 0:
                kindID = result[0]
                if subname != "所有":  # 如果选择了考试科目
                    # 获取选择的考试科目对应ID
                    result = service.query("select subID from tb_subject where subName=%s", subname)
                    if len(result) > 0:
                        subID = result[0]
                        if stuname != "":  # 如果选择了学生姓名
                            # 获取学生对应的ID
                            result = service.query(
                                "select stuID from v_studentinfo where gradeName=%s and className=%s and stuName=%s",
                                gradename, classname, stuname)
                            if len(result) > 0:  # 如果结果大于0
                                stuID = result[0]  # 记录选择的学生对应的ID
                                if self.getScore(stuID, kindID, subID) <= 0:  # 判断是否已经存在相同记录
                                    if score != "":  # 如果输入了分数
                                        # 执行添加语句
                                        result = service.exec(
                                            "insert into tb_result(stuID,kindID,subID,result) values (%s,%s,%s,%s)",
                                            (stuID, kindID, subID, score))
                                        if result > 0:  # 如果结果大于0，说明添加成功
                                            self.query()  # 在表格中显示最新数据
                                            QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
                                    else:
                                        QMessageBox.warning(None, '警告', '请输入分数！', QMessageBox.Ok)
                                else:
                                    QMessageBox.warning(None, '警告', '该学生成绩记录已经存在，请核查！', QMessageBox.Ok)
                        else:
                            QMessageBox.warning(None, '警告', '请先选择学生！', QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, '警告', '请先选择考试科目！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请先选择考试类别！', QMessageBox.Ok)

    # 修改学生成绩信息
    def edit(self):
        try:
            if self.select != "":  # 判断是否选择了要修改的数据
                ID = self.select  # 记录要修改的编号
                score = self.editResult.text()  # 记录成绩
                # 执行修改操作
                result = service.exec("update tb_result set result=%s where ID=%s", (score, ID))
                if result > 0:  # 如果结果大于0，说明修改成功
                    self.query()  # 在表格中显示最新数据
                    QMessageBox.information(None, '提示', '信息修改成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要修改的数据！', QMessageBox.Ok)

    # 删除学生成绩信息
    def delete(self):
        try:
            if self.select != "":  # 判断是否选择了要删除的数据
                # 执行删除操作
                result = service.exec("delete from tb_result where ID= %s", (self.select,))
                if result > 0:  # 如果结果大于0，说明删除成功
                    self.query()  # 在表格中显示最新数据
                    QMessageBox.information(None, '提示', '信息删除成功！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要删除的数据！', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "成绩管理"))
        self.label_2.setText(_translate("MainWindow", "考试种类："))
        self.label_3.setText(_translate("MainWindow", "选择班级："))
        self.btnExit.setText(_translate("MainWindow", "退出"))
        self.btnDel.setText(_translate("MainWindow", "删除"))
        self.btnAdd.setText(_translate("MainWindow", "添加"))
        self.btnEdit.setText(_translate("MainWindow", "修改"))
        self.btnQuery.setText(_translate("MainWindow", "刷新"))
        item = self.tbResult.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "编号"))
        item = self.tbResult.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "学生编号"))
        item = self.tbResult.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "学生姓名"))
        item = self.tbResult.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "班级"))
        item = self.tbResult.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "科目"))
        item = self.tbResult.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "种类"))
        item = self.tbResult.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "成绩"))
        self.label_4.setText(_translate("MainWindow", "学生姓名："))
        self.label_5.setText(_translate("MainWindow", "考试科目："))
        self.label_6.setText(_translate("MainWindow", "成绩："))
        self.label_10.setText(_translate("MainWindow", "选择年级："))
