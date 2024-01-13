from PyQt5 import QtCore, QtGui, QtWidgets
from connect import *
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QApplication


cursor, conn = connect()


# 图书管理员界面
class Ui_bookadmin(object):
    def setupUi(self, bookadmin):
        # 主界面
        bookadmin.setObjectName("bookadmin")
        bookadmin.resize(846, 796)
        # 主界面下的大框架
        self.tabWidget = QtWidgets.QTabWidget(bookadmin)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 811, 761))
        self.tabWidget.setObjectName("tabWidget")

        # 创建选项卡“查询读者信息”
        # 创建选项卡
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # 垂直布局2
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # 垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # 水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 选项卡“查询读者信息”是标签2的父窗口
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        # 选项卡“查询读者信息”是文本框 “卡号” 的父窗口
        self.readerid = QtWidgets.QLineEdit(self.tab)
        self.readerid.setObjectName("readerid")
        self.horizontalLayout.addWidget(self.readerid)

        # 选项卡“查询读者信息”是标签的父窗口
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # 选项卡“查询读者信息”是文本框 “姓名” 的父窗口
        self.readername = QtWidgets.QLineEdit(self.tab)
        self.readername.setObjectName("readername")
        self.horizontalLayout.addWidget(self.readername)
        # 选项卡“查询读者信息”是标签3 的父窗口
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        # 选项卡“查询读者信息”是文本框 “单位” 的父窗口
        self.unit = QtWidgets.QLineEdit(self.tab)
        self.unit.setObjectName("unit")
        self.horizontalLayout.addWidget(self.unit)

        # 水平布局是垂直布局的父窗口
        self.verticalLayout.addLayout(self.horizontalLayout)

        # 创建垂直布局2
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # 创建“查询”按钮 设置尺寸政策
        self.select = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select.sizePolicy().hasHeightForWidth())
        self.select.setSizePolicy(sizePolicy)
        self.select.setObjectName("select")

        # 在水平布局2添加“查询”按钮
        self.horizontalLayout_2.addWidget(self.select)

        # 创建“显示所有”按钮 设置尺寸政策
        self.selectall = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectall.sizePolicy().hasHeightForWidth())
        self.selectall.setSizePolicy(sizePolicy)
        self.selectall.setObjectName("selectall")

        # 在水平布局2添加“显示所有”按钮
        self.horizontalLayout_2.addWidget(self.selectall)

        # 水平布局2是垂直布局的父窗口
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # 创建表格，选项卡“查询读者信息”是父窗口
        self.readerinfors = QtWidgets.QTableWidget(self.tab)
        self.readerinfors.setObjectName("readerinfors")
        #6列 卡号、姓名、性别、单位、人员类别、密码
        self.readerinfors.setColumnCount(6)
        self.readerinfors.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfors.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfors.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfors.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfors.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfors.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfors.setHorizontalHeaderItem(5, item)

        # 表格是垂直布局的父窗口
        self.verticalLayout.addWidget(self.readerinfors)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        #将tab添加到tabWidget大框架
        self.tabWidget.addTab(self.tab, "")


        # 创建选项卡2“管理借书证”
        # 创建选项卡
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        # 创建小部件
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(10, 10, 701, 691))
        self.widget.setObjectName("widget")

        # 第一行
        # 创建垂直布局7
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        # 创建水平布局19
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        # 创建水平布局20
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        # 创建标签15 水平布局20
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_20.addWidget(self.label_15)

        # 创建“卡号”文本框 水平布局20 水平布局19
        self.readerid = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readerid.sizePolicy().hasHeightForWidth())
        self.readerid.setSizePolicy(sizePolicy)
        self.readerid.setObjectName("readerid")
        self.horizontalLayout_20.addWidget(self.readerid)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)

        # 创建水平布局21
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        # 创建标签16 水平布局2
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_21.addWidget(self.label_16)

        # 创建“姓名”文本框 水平布局21 水平布局19
        self.readname = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readname.sizePolicy().hasHeightForWidth())
        self.readname.setSizePolicy(sizePolicy)
        self.readname.setObjectName("readname")
        self.horizontalLayout_21.addWidget(self.readname)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_21)

        # 创建水平布局22
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")

        # 创建标签17 水平布局22
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_22.addWidget(self.label_17)

        # 创建“单位”文本框 水平布局22 水平布局19
        self.unit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit.sizePolicy().hasHeightForWidth())
        self.unit.setSizePolicy(sizePolicy)
        self.readname.setObjectName("unit")
        self.horizontalLayout_22.addWidget(self.unit)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_22)


        # 创建水平布局23
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")

        # 创建标签18 水平布局23
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_23.addWidget(self.label_18)

        # 创建“性别选项” 水平布局23 水平布局19 垂直布局7
        self.sex = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sex.sizePolicy().hasHeightForWidth())
        self.sex.setSizePolicy(sizePolicy)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.horizontalLayout_23.addWidget(self.sex)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_23)
        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        # 第二行
        # 创建水平布局24
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")

        # 创建水平布局25
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")

        # 创建标签19 水平布局25
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_25.addWidget(self.label_19)

        # 创建“人员类别”选项 水平布局25 水平布局24
        self.readtype = QtWidgets.QComboBox(self.widget)
        self.readtype.setObjectName("readtype")
        self.readtype.addItem("")
        self.readtype.addItem("")
        self.horizontalLayout_25.addWidget(self.readtype)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_25)

        # 创建水平布局26
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        # 创建标签20 水平布局26
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_26.addWidget(self.label_20)

        # 创建“密码”文本框 水平布局26 水平布局 24
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setObjectName("password")
        self.horizontalLayout_26.addWidget(self.password)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_26)

        # 创建水平布局27
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")

        # 创建标签21 水平布局27 水平布局24
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_27.addWidget(self.label_21)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_27)

        # 水平布局28
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")

        # 创建标签22 水平布局28 水平布局24 垂直布局7
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_28.addWidget(self.label_22)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_28)
        self.verticalLayout_7.addLayout(self.horizontalLayout_24)

        # 创建水平布局29
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")

        # 添加
        self.addr = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addr.sizePolicy().hasHeightForWidth())
        self.addr.setSizePolicy(sizePolicy)
        self.addr.setObjectName("addr")
        self.horizontalLayout_29.addWidget(self.addr)

        # 修改
        self.alterr = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alterr.sizePolicy().hasHeightForWidth())
        self.alterr.setSizePolicy(sizePolicy)
        self.alterr.setObjectName("alterr")
        self.horizontalLayout_29.addWidget(self.alterr)

        # 删除
        self.deleter = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleter.sizePolicy().hasHeightForWidth())
        self.deleter.setSizePolicy(sizePolicy)
        self.deleter.setObjectName("deleter")
        self.horizontalLayout_29.addWidget(self.deleter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_29)

        # 创建表格控件
        self.readerinfos = QtWidgets.QTableWidget(self.widget)
        self.readerinfos.setObjectName("readerinfos")
        self.readerinfos.setColumnCount(6)
        self.readerinfos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.readerinfos.setHorizontalHeaderItem(5, item)
        self.verticalLayout_7.addWidget(self.readerinfos)
        self.tabWidget.addTab(self.tab_2,"")

        # 选项卡“管理书籍信息”
        # 创建选项卡3
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        # 创建垂直布局5
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        # 创建垂直布局3
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # 第一行
        # 创建水平布局13
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        # 创建水平布局3
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # 创建标签4 水平布局3
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)

        # 创建文本框“书号”  水平布局3 水平布局13
        self.bookid = QtWidgets.QLineEdit(self.tab_3)
        self.bookid.setObjectName("bookid")
        self.horizontalLayout_3.addWidget(self.bookid)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_3)

        # 创建水平布局5
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # 创建标签5 水平布局5
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)

        # 创建文本框“类别”  水平布局5 水平布局13
        self.booktype = QtWidgets.QLineEdit(self.tab_3)
        self.booktype.setObjectName("booktype")
        self.horizontalLayout_5.addWidget(self.booktype)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_5)

        # 创建水平布局12
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        # 创建标签6 水平布局12
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)

        # 创建文本框“书名”  水平布局12 水平布局13
        self.bookname = QtWidgets.QLineEdit(self.tab_3)
        self.bookname.setObjectName("bookname")
        self.horizontalLayout_12.addWidget(self.bookname)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        # 创建水平布局8
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        # 创建标签7 水平布局8
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)

        # 创建文本框“出版社”  水平布局8 水平布局13 垂直布局3
        self.publisher = QtWidgets.QLineEdit(self.tab_3)
        self.publisher.setObjectName("publisher")
        self.horizontalLayout_8.addWidget(self.publisher)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        #第二行
        # 创建水平布局14
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        # 创建水平布局4
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # 创建标签8 水平布局4
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)

        # 创建文本框“出版年份”  水平布局4 水平布局14 垂直布局3
        self.year = QtWidgets.QLineEdit(self.tab_3)
        self.year.setObjectName("year")
        self.horizontalLayout_4.addWidget(self.year)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_4)

        # 创建水平布局6
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # 创建标签9 水平布局6
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)

        # 创建文本框“作者”  水平布局6 水平布局14
        self.author = QtWidgets.QLineEdit(self.tab_3)
        self.author.setObjectName("author")
        self.horizontalLayout_6.addWidget(self.author)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)

        # 创建水平布局10
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        # 创建标签12 水平布局10
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)

        # 创建文本框“价格”  水平布局10 水平布局14
        self.price = QtWidgets.QLineEdit(self.tab_3)
        self.price.setObjectName("price")
        self.horizontalLayout_10.addWidget(self.price)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_10)

        # 创建水平布局9
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        # 创建标签11 水平布局9
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)

        # 创建文本框“在馆册数”  水平布局9 水平布局14
        self.stock = QtWidgets.QLineEdit(self.tab_3)
        self.stock.setObjectName("stock")
        self.horizontalLayout_9.addWidget(self.stock)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        # 第三行
        # 创建水平布局17
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")

        # 创建水平布局15
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")

        # 创建水平布局7
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        # 创建标签10 水平布局7
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)

        # 创建文本框“馆藏册数”  水平布局7 水平布局15
        self.totalnum = QtWidgets.QLineEdit(self.tab_3)
        self.totalnum.setObjectName("totalnum")
        self.horizontalLayout_7.addWidget(self.totalnum)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_7)

        # 创建水平布局11
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # 创建标签13 水平布局11
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_15)

        # 创建水平布局16
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")

        # 创建“添加”按钮 水平布局 16
        self.addbook = QtWidgets.QPushButton(self.tab_3)
        self.addbook.setObjectName("addbook")
        self.horizontalLayout_16.addWidget(self.addbook)

        # 创建“删除”按钮 水平布局 16
        self.deletebook = QtWidgets.QPushButton(self.tab_3)
        self.deletebook.setObjectName("deletebook")
        self.horizontalLayout_16.addWidget(self.deletebook)

        # 创建“修改”按钮 水平布局 16
        self.alterbook = QtWidgets.QPushButton(self.tab_3)
        self.alterbook.setObjectName("alterbook")
        self.horizontalLayout_16.addWidget(self.alterbook)

        #水平布局16 水平布局17 垂直布局3
        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        # 添加表格控件“bookinfos”
        self.bookinfos = QtWidgets.QTableWidget(self.tab_3)
        self.bookinfos.setObjectName("bookinfos")
        self.bookinfos.setColumnCount(9)
        self.bookinfos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookinfos.setHorizontalHeaderItem(8, item)
        #表格 垂直布局3 垂直布局5
        self.verticalLayout_3.addWidget(self.bookinfos)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        # 标签2“管理图书信息”添加到大框架
        self.tabWidget.addTab(self.tab_3, "")

        # 选项卡3“借阅/归还审批”
        # 选项卡3
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        # 添加表格控件“iteminfo”
        self.iteminfo = QtWidgets.QTableWidget(self.tab_4)
        self.iteminfo.setGeometry(QtCore.QRect(80, 40, 421, 631))
        self.iteminfo.setObjectName("iteminfo")

        self.iteminfo.setColumnCount(6)
        self.iteminfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.iteminfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.iteminfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.iteminfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.iteminfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.iteminfo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.iteminfo.setHorizontalHeaderItem(5, item)

        #创建小部件layoutWidget
        self.layoutWidget = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget.setGeometry(QtCore.QRect(610, 160, 95, 301))
        self.layoutWidget.setObjectName("layoutWidget")

        # 创建垂直布局 4
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # 创建按钮“批准” 垂直布局4
        self.yes = QtWidgets.QPushButton(self.layoutWidget)
        self.yes.setObjectName("yes")
        self.verticalLayout_4.addWidget(self.yes)

        # 创建按钮“驳回” 垂直布局4
        self.no = QtWidgets.QPushButton(self.layoutWidget)
        self.no.setObjectName("no")
        self.verticalLayout_4.addWidget(self.no)

        # 创建按钮“刷新” 垂直布局4
        self.refresh = QtWidgets.QPushButton(self.layoutWidget)
        self.refresh.setObjectName("refresh")
        self.verticalLayout_4.addWidget(self.refresh)

        # 标签3“借阅/归还审批”添加到大框架
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(bookadmin)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(bookadmin)

        self.show_all_books()
        self.selectall.clicked.connect(self.show_all_readers)
        self.select.clicked.connect(self.readerselect)
        self.addbook.clicked.connect(self.add_book)
        self.deletebook.clicked.connect(self.drop_book)
        self.alterbook.clicked.connect(self.update_book)

        # 使bookinfos中鼠标点击操作选中的是一行而不是一格
        self.bookinfos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 使bookinfos中鼠标双击行的时候不可直接更改
        self.bookinfos.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.bookinfos.activated.connect(self.displayinfo)

        self.show_all_items()
        # 使iteminfo中鼠标点击操作选中的是一行而不是一格
        self.iteminfo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 使iteminfo中鼠标双击行的时候不可直接更改
        self.iteminfo.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.yes.clicked.connect(self.pizhun)
        self.no.clicked.connect(self.bohui)
        self.refresh.clicked.connect(self.show_all_items)

        self.addr.clicked.connect(self.addreader)
        self.alterr.clicked.connect(self.alterreader)
        self.deleter.clicked.connect(self.deletereader)

    def retranslateUi(self, bookadmin):
        # 中文翻译
        _translate = QtCore.QCoreApplication.translate
        bookadmin.setWindowTitle(_translate("bookadmin", "图书管理员系统"))
        # 查询读者信息
        self.label_2.setText(_translate("bookadmin", "卡号"))
        self.label.setText(_translate("bookadmin", "姓名"))
        self.label_3.setText(_translate("bookadmin", "单位"))
        self.select.setText(_translate("bookadmin", "查询"))
        self.selectall.setText(_translate("bookadmin", "显示所有"))
        item = self.readerinfors.horizontalHeaderItem(0)
        item.setText(_translate("bookadmin", "卡号"))
        item = self.readerinfors.horizontalHeaderItem(1)
        item.setText(_translate("bookadmin", "姓名"))
        item = self.readerinfors.horizontalHeaderItem(2)
        item.setText(_translate("bookadmin", "性别"))
        item = self.readerinfors.horizontalHeaderItem(3)
        item.setText(_translate("bookadmin", "类型"))
        item = self.readerinfors.horizontalHeaderItem(4)
        item.setText(_translate("bookadmin", "单位"))
        item = self.readerinfors.horizontalHeaderItem(5)
        item.setText(_translate("bookadmin", "密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("bookadmin", "查询借书证信息"))

        # 管理读者信息
        # 上方界面
        self.label_15.setText(_translate("systemadmin", "卡号"))
        self.label_16.setText(_translate("systemadmin", "姓名"))
        self.label_17.setText(_translate("systemadmin", "单位"))
        self.label_18.setText(_translate("systemadmin", "性别"))
        self.sex.setItemText(0, _translate("systemadmin", "男"))
        self.sex.setItemText(1, _translate("systemadmin", "女"))
        self.label_19.setText(_translate("systemadmin", "人员类别"))
        self.readtype.setItemText(0, _translate("systemadmin", "学生"))
        self.readtype.setItemText(1, _translate("systemadmin", "教师"))
        self.label_20.setText(_translate("systemadmin", "密码"))
        self.addr.setText(_translate("systemadmin", "添加"))
        self.alterr.setText(_translate("systemadmin", "修改"))
        self.deleter.setText(_translate("systemadmin", "删除"))
        # 下方界面
        item = self.readerinfos.horizontalHeaderItem(0)
        item.setText(_translate("systemadmin", "卡号"))
        item = self.readerinfos.horizontalHeaderItem(1)
        item.setText(_translate("systemadmin", "姓名"))
        item = self.readerinfos.horizontalHeaderItem(2)
        item.setText(_translate("systemadmin", "性别"))
        item = self.readerinfos.horizontalHeaderItem(3)
        item.setText(_translate("systemadmin", "人员类别"))
        item = self.readerinfos.horizontalHeaderItem(4)
        item.setText(_translate("systemadmin", "单位"))
        item = self.readerinfos.horizontalHeaderItem(5)
        item.setText(_translate("systemadmin", "密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("systemadmin", "管理借书证信息"))


        # 管理书籍信息
        # 上方界面
        self.label_4.setText(_translate("bookadmin", "书号"))
        self.label_5.setText(_translate("bookadmin", "类别"))
        self.label_6.setText(_translate("bookadmin", "书名"))
        self.label_7.setText(_translate("bookadmin", "出版社"))
        self.label_8.setText(_translate("bookadmin", "出版年份"))
        self.label_9.setText(_translate("bookadmin", "作者"))
        self.label_12.setText(_translate("bookadmin", "价格"))
        self.label_11.setText(_translate("bookadmin", "在馆册数"))
        self.label_10.setText(_translate("bookadmin", "馆藏册数"))
        self.addbook.setText(_translate("bookadmin", "添加"))
        self.deletebook.setText(_translate("bookadmin", "删除"))
        self.alterbook.setText(_translate("bookadmin", "修改"))
        # 下方查询结果页面
        item = self.bookinfos.horizontalHeaderItem(0)
        item.setText(_translate("bookadmin", "书号"))
        item = self.bookinfos.horizontalHeaderItem(1)
        item.setText(_translate("bookadmin", "类别"))
        item = self.bookinfos.horizontalHeaderItem(2)
        item.setText(_translate("bookadmin", "书名"))
        item = self.bookinfos.horizontalHeaderItem(3)
        item.setText(_translate("bookadmin", "出版社"))
        item = self.bookinfos.horizontalHeaderItem(4)
        item.setText(_translate("bookadmin", "出版年份"))
        item = self.bookinfos.horizontalHeaderItem(5)
        item.setText(_translate("bookadmin", "作者"))
        item = self.bookinfos.horizontalHeaderItem(6)
        item.setText(_translate("bookadmin", "价格"))
        item = self.bookinfos.horizontalHeaderItem(7)
        item.setText(_translate("bookadmin", "在馆册数"))
        item = self.bookinfos.horizontalHeaderItem(8)
        item.setText(_translate("bookadmin", "馆藏册数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("bookadmin", "管理书籍信息"))

        # 借阅、归还审批
        item = self.iteminfo.horizontalHeaderItem(0)
        item.setText(_translate("bookadmin", "卡号"))
        item = self.iteminfo.horizontalHeaderItem(1)
        item.setText(_translate("bookadmin", "书号"))
        item = self.iteminfo.horizontalHeaderItem(2)
        item.setText(_translate("bookadmin", "借书时间"))
        item = self.iteminfo.horizontalHeaderItem(3)
        item.setText(_translate("bookadmin", "还书时间"))
        item = self.iteminfo.horizontalHeaderItem(4)
        item.setText(_translate("bookadmin", "状态"))
        self.yes.setText(_translate("bookadmin", "批准"))
        self.no.setText(_translate("bookadmin", "驳回"))
        self.refresh.setText(_translate("bookadmin", "刷新"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("bookadmin", "借阅/归还审批"))

    # 一、管理借书证（读者）
    # 01 显示所有的借书证
    def show_all_readers(self):
        sql = "select * from card"
        res = cursor.execute(sql)  # 返回表中元组个数赋值给res
        readerinfo = cursor.fetchall()  # 以嵌套元组的形式获取表中元组
        # print(readerinfo)
        self.readerinfors.setRowCount(res)
        for i in range(res):
            reader = readerinfo[i]
            readerid = QTableWidgetItem(reader[0])
            readername = QTableWidgetItem(reader[1])
            readersex = QTableWidgetItem(reader[2])
            readertype = QTableWidgetItem(reader[3])
            readerunit = QTableWidgetItem(reader[4])
            password=QTableWidgetItem(reader[5])

            self.readerinfors.setItem(i, 0, readerid)
            self.readerinfors.setItem(i, 1, readername)
            self.readerinfors.setItem(i, 2, readersex)
            self.readerinfors.setItem(i, 3, readertype)
            self.readerinfors.setItem(i, 4, readerunit)
            self.readerinfors.setItem(i, 5, password)

    # 02 选择读者（鼠标双击或输入）
    def readerselect(self):
        readerid = self.readerid.text()
        readername = self.readername.text()
        readerunit = self.unit.text()
        abc = 0
        if readerid:
            readerid = ' `账号`="%s"' % (readerid)
            abc = 1
        if readername:
            if abc == 1:
                readername = ' and `姓名`="%s"' % (readername)
            else:
                readername = ' `姓名`="%s"' % (readername)
                abc = 1
        if readerunit:
            if abc == 1:
                readerunit = ' and `单位`="%s"' % (readerunit)
            else:
                readerunit = ' `单位`="%s"' % (readerunit)
        sql0 = 'select * from card where'
        sql1 = readerid + readername + readerunit
        sql = sql0 + sql1
        if sql1:
            res = cursor.execute(sql)
            if res:
                readerinfo = cursor.fetchall()  # 返回一堆元组组成的元组
                self.readerinfors.setRowCount(res)
                for i in range(res):
                    reader = readerinfo[i]
                    readerid = QTableWidgetItem(reader[0])
                    readername = QTableWidgetItem(reader[1])
                    readersex = QTableWidgetItem(reader[2])
                    readertype = QTableWidgetItem(reader[3])
                    readerunit = QTableWidgetItem(reader[4])
                    password = QTableWidgetItem(reader[5])
                    self.readerinfors.setItem(i, 0, readerid)
                    self.readerinfors.setItem(i, 1, readername)
                    self.readerinfors.setItem(i, 2, readersex)
                    self.readerinfors.setItem(i, 3, readertype)
                    self.readerinfors.setItem(i, 4, readerunit)
                    self.readerinfors.setItem(i, 5, password)
            else:
                QMessageBox.warning(self, "警告", "没有符合条件的读者！", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "至少输入一项读者信息！", QMessageBox.Yes)

    # 03 添加借书证
    def addreader(self):
        id = self.readerid.text()
        name = self.readname.text()
        rsex = self.sex.currentText()
        rtype = self.readtype.currentText()
        runit = self.unit.text()
        password = self.password.text()


        sql = 'SELECT * FROM card WHERE `卡号`="%s"' % id
        res = cursor.execute(sql)
        if res:
            QMessageBox.warning(self, "警告", "该读者ID已被占用！", QMessageBox.Yes)
        else:
            value = (id, name, rsex, rtype, runit,password)
            sql = 'INSERT INTO `card` (`卡号`,`姓名`,`性别`,`人员类别`,`单位`,`密码`) VALUES ("%s","%s","%s","%s","%s","%s");' % value
            cursor.execute(sql)
            conn.commit()
            QMessageBox.warning(self, "提示", "添加成功！", QMessageBox.Yes)
            self.getreadersinfo()

    # 04 修改读者信息
    def alterreader(self):
        id = self.readerid.text()
        name = self.readname.text()
        rsex = self.sex.currentText()
        rtype = self.readtype.currentText()
        runit = self.unit.text()
        password = self.password.text()


        value = (name, rsex, rtype, runit,password,id)
        sql = 'UPDATE `card` SET `姓名`="%s",`性别`="%s",`人员类别`="%s",`单位`="%s",`密码`="%s" WHERE `卡号`="%s"' % value
        cursor.execute(sql)
        conn.commit()
        QMessageBox.warning(self, "提示", "修改成功！", QMessageBox.Yes)
        self.getreadersinfo()

    # 05 删除读者信息
    def deletereader(self):
        res = QMessageBox.warning(self, "警告", "即将删除, 确定？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.Yes:
            id = self.readerid.text()
            sql = 'DELETE FROM card WHERE `卡号`="%s"' % id
            cursor.execute(sql)
            conn.commit()
            QMessageBox.warning(self, "提示", "删除成功！", QMessageBox.Yes)
            self.getreadersinfo()


    #二、管理图书
    # 01 显示所有图书信息
    def show_all_books(self):
        sql = 'SELECT * FROM book'
        res = cursor.execute(sql)
        books = cursor.fetchall()
        self.bookinfos.setRowCount(res)
        for i in range(res):
            book = books[i]
            self.bookinfos.setItem(i, 0, QTableWidgetItem(book[0]))
            self.bookinfos.setItem(i, 1, QTableWidgetItem(book[1]))
            self.bookinfos.setItem(i, 2, QTableWidgetItem(book[2]))
            self.bookinfos.setItem(i, 3, QTableWidgetItem(book[3]))
            self.bookinfos.setItem(i, 4, QTableWidgetItem(str(book[4])))
            self.bookinfos.setItem(i, 5, QTableWidgetItem(book[5]))
            self.bookinfos.setItem(i, 6, QTableWidgetItem(str(book[6])))
            self.bookinfos.setItem(i, 7, QTableWidgetItem(str(book[7])))
            self.bookinfos.setItem(i, 8, QTableWidgetItem(str(book[8])))


    # 02 添加图书
    def add_book(self):
        bookid = self.bookid.text()
        booktype = self.booktype.text()
        bookname = self.bookname.text()
        publisher = self.publisher.text()
        year=self.year.text()
        author = self.author.text()
        price = self.price.text()

        try:
            totalnum = int(self.totalnum.text())
            stock = int(self.stock.text())
            if price != '':
                price = float(price)
                if bookid and booktype and bookname and publisher and year and price and stock and totalnum:
                    sql = 'insert into `book`(`书号`,`类别`,`书名`,`出版社`,`出版年份`,`作者`,`价格`,`在馆册数`,`馆藏册数`) values ("%s","%s","%s","%s","%s","%s","%.2f","%d","%d")' % (
                    bookid,booktype,bookname,publisher,year,author,price,stock,totalnum)
                    cursor.execute(sql)
                    conn.commit()
                    self.show_all_books()
                else:
                    QMessageBox.warning(self, "警告", "请补全书目信息！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "请补全书目信息！", QMessageBox.Yes)
        except (pymysql.err.IntegrityError, ValueError):
            QMessageBox.warning(self, "警告", "书目信息错误！", QMessageBox.Yes)

    # 03 删除图书
    def drop_book(self):
        s = self.bookinfos.currentRow()  # 通过获取第几行（从0开始）
        bookid = self.bookinfos.item(s, 0).text()
        sql = 'delete from book where `书号`="%s"' % (bookid)
        cursor.execute(sql)
        conn.commit()
        self.show_all_books()

    # 04 显示修改后的图书信息
    def displayinfo(self):
        s = self.bookinfos.currentRow()
        self.bookid.setText(self.bookinfos.item(s, 0).text())
        self.booktype.setText(self.bookinfos.item(s, 1).text())
        self.bookname.setText(self.bookinfos.item(s, 2).text())
        self.publisher.setText(self.bookinfos.item(s, 3).text())
        self.year.setText(self.bookinfos.item(s, 4).text())
        self.author.setText(self.bookinfos.item(s, 5).text())
        self.price.setText(self.bookinfos.item(s, 6).text())
        self.stock.setText(self.bookinfos.item(s, 7).text())
        self.totalnum.setText(self.bookinfos.item(s, 8).text())

    # 05 修改图书
    def update_book(self):
        bookid = self.bookid.text()
        booktype = self.booktype.text()
        bookname = self.bookname.text()
        publisher = self.publisher.text()
        year=self.year.text()
        author = self.author.text()
        price = self.price.text()

        try:
            totalnum = int(self.totalnum.text())
            stock = int(self.stock.text())
            if price != '':
                price = float(price)
                if bookid and booktype and bookname and publisher and year and price and stock and totalnum:
                    sql = 'UPDATE book SET `书号`="%s",`类别`="%s",`书名`="%s",`出版社`="%s",`出版年份`="%s",`作者`="%s",`价格`="%.2f",`在馆册数`="%d",`馆藏册数`="%d" WHERE `书号`="%s"' %(
                    bookid,booktype,bookname,publisher,year,author,price,stock,totalnum, bookid)
                    cursor.execute(sql)
                    conn.commit()
                    self.show_all_books()
                else:
                    QMessageBox.warning(self, "警告", "请补全书目信息！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "警告", "请补全书目信息！", QMessageBox.Yes)
        except (pymysql.err.IntegrityError, ValueError):
            QMessageBox.warning(self, "警告", "书目信息错误！", QMessageBox.Yes)

    # 三、借阅归还审批功能
    # 01 显示所有待审批信息
    def show_all_items(self):
        sql = 'SELECT * FROM `record`'
        res = cursor.execute(sql)
        records = cursor.fetchall()
        self.iteminfo.setRowCount(res)
        for i in range(res):
            record = records[i]
            self.iteminfo.setItem(i, 0, QTableWidgetItem(record[0]))
            self.iteminfo.setItem(i, 1, QTableWidgetItem(record[1]))
            if record[2] is not None:
                self.iteminfo.setItem(i, 2, QTableWidgetItem(record[2].strftime('%Y-%m-%d %H:%M:%S')))
            else:
                self.iteminfo.setItem(i, 2, QTableWidgetItem(''))

            if record[3] is not None:
                self.iteminfo.setItem(i, 3, QTableWidgetItem(record[3].strftime('%Y-%m-%d %H:%M:%S')))
            else:
                self.iteminfo.setItem(i, 3, QTableWidgetItem(''))
            # self.iteminfo.setItem(i, 3, QTableWidgetItem(record[3]))
            self.iteminfo.setItem(i, 4, QTableWidgetItem('通过' if record[5] == 10 else '等待审核'))
            # self.iteminfo.setItem(i, 5, QTableWidgetItem(record[5]))


    # 02 批准借阅请求
    def pizhun(self):

        s = self.iteminfo.currentRow()  # 通过获取第几行（从0开始）
        bookid= self.iteminfo.item(s, 0).text()
        cardid = self.iteminfo.item(s, 1).text()
        btime = self.iteminfo.item(s, 2).text()
        rtime = self.iteminfo.item(s, 3).text()
        

        if btime != '':
            sql1 = 'UPDATE `record` SET `状态`= "%s" WHERE `书号`="%s" and `卡号`="%s" and `状态`="%s" and `借书日期` is not null' % (10, bookid, cardid, 1)
            cursor.execute(sql1)
            conn.commit()

            sql2 = 'UPDATE book set `在馆册数`=`在馆册数`-1 where `书号`="%s"' % (bookid)
            cursor.execute(sql2)
            conn.commit()
        elif rtime != '':
            sql1 = 'UPDATE `record` SET `状态`= "%s" WHERE `书号`="%s" and `卡号`="%s" and `状态`="%s" and `还书日期` is not null' % (10, bookid, cardid, 1)
            cursor.execute(sql1)
            conn.commit()

            sql4 = 'UPDATE book set `在馆册数`=`在馆册数`+1 where `书号`="%s"' % (bookid)
            cursor.execute(sql4)
            conn.commit()
        QMessageBox.warning(self, "提示", "审核请求成功！", QMessageBox.Yes)
        self.show_all_items()

    # 03 驳回借阅请求
    def bohui(self):
        s = self.iteminfo.currentRow()  # 通过获取第几行（从0开始）
        bookid = self.iteminfo.item(s, 0).text()
        cardid = self.iteminfo.item(s, 1).text()
        sql = 'delete from record where `书号`="%s" and `卡号`="%s" and `状态`= 1' % (bookid, cardid)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        QMessageBox.warning(self, "提示", "驳回借阅请求成功！", QMessageBox.Yes)
        self.show_all_items()
        
    def getreadersinfo(self):
        pass
