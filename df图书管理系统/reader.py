import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from connect import *
from PyQt5.QtCore import *

cursor, conn = connect()  # 连接数据库


# 读者界面设计

class Ui_Reader(object):
    # 创建UI
    #主窗口界面
    def setupUi(self, Reader):
        Reader.setObjectName("Reader")
        Reader.resize(1000, 950)

        # 创建一个QTabWidget并将Reader设置为其父窗口
        self.readertab = QtWidgets.QTabWidget(Reader)
        self.readertab.setGeometry(QtCore.QRect(20, 11, 900, 850))
        self.readertab.setObjectName("readertab")

        # 创建一个为“borrowbook”（借书）的空白页面
        self.borrowbook = QtWidgets.QWidget()
        self.borrowbook.setObjectName("borrowbook")

        # 创建一个QWidget并将"borrowbook" widget设置为其父窗口
        self.layoutWidget = QtWidgets.QWidget(self.borrowbook)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 800, 750))
        self.layoutWidget.setObjectName("layoutWidget")

        # 创建一个垂直布局，并将layoutWidget设置为其父窗口
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 创建一个水平布局，用于水平排列小部件
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 创建一个QLabel，并将layoutWidget设置为其父窗口
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        # 将QLabel添加到水平布局中
        self.horizontalLayout.addWidget(self.label)

        # 创建一个QLineEdit(输入文本框)，并将layoutWidget设置为其父窗口
        self.borrowbookid = QtWidgets.QLineEdit(self.layoutWidget)
        self.borrowbookid.setObjectName("borrowbookid")
        self.horizontalLayout.addWidget(self.borrowbookid)

        # 创建一个“借书查询”的QPushButton，并将layoutWidget设置为其父窗口
        self.borrowcheckbt = QtWidgets.QPushButton(self.layoutWidget)
        self.borrowcheckbt.setObjectName("borrowcheckbt")
        # 将QPushButton添加到水平布局中
        self.horizontalLayout.addWidget(self.borrowcheckbt)

        # 将水平布局添加到名为“verticalLayout_2”垂直布局中
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # 创建一个“borrowtable”的表格控件，放在layoutWidget里面
        self.borrowtable = QtWidgets.QTableWidget(self.layoutWidget)
        # 禁用鼠标跟踪
        self.borrowtable.setMouseTracking(False)
        # 设置编辑触发方式：在按下键盘按键时触发编辑
        self.borrowtable.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        # 设置选择行为：在选择时整行被选中
        self.borrowtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.borrowtable.setObjectName("borrowtable")
        # 9列表格
        self.borrowtable.setColumnCount(9)
        # 1行表格
        self.borrowtable.setRowCount(1)
        # 创建一个表格对象
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowtable.setHorizontalHeaderItem(8, item)
        # 将表格添加到垂直布局“verticalLayout_2”中
        self.verticalLayout_2.addWidget(self.borrowtable)
        # 学号&提交
        # 创建水平布局10
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        # 创建水平布局11
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # 创建标签8 水平布局11
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)

        # 创建文本框“卡号”  水平布局11 水平布局10
        self.cardid = QtWidgets.QLineEdit(self.layoutWidget)
        self.cardid.setObjectName("cardid")
        self.horizontalLayout_11.addWidget(self.cardid)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        # 创建水平布局12
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        # 创建标签9 水平布局12
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)

        # 创建按钮  水平布局12 水平布局10
        self.borrowokbt = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.borrowokbt.sizePolicy().hasHeightForWidth())
        self.borrowokbt.setSizePolicy(sizePolicy)
        self.borrowokbt.setObjectName("borrowokbt")

        self.horizontalLayout_12.addWidget(self.borrowokbt)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_12)

        # 创建水平布局13
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        # 创建标签10 水平布局13
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.readertab.addTab(self.borrowbook, "")

        #创建一个名为“returnbook”（还书）的空白页面
        self.returnbook = QtWidgets.QWidget()
        self.returnbook.setObjectName("returnbook")

        # 在 returnbook 页面中创建一个名为 layoutWidget1 的小部件（上一个layoutWidget部件是借书界面下的部件）
        self.layoutWidget1 = QtWidgets.QWidget(self.returnbook)
        self.layoutWidget1.setGeometry(QtCore.QRect(9, 9, 311, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")

        # 在 layoutWidget1 上创建一个水平布局 horizontalLayout_3
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # 在 horizontalLayout_3 上添加一个标签 returnbo
        self.returnbo = QtWidgets.QLabel(self.layoutWidget1)
        self.returnbo.setObjectName("returnbo")
        self.horizontalLayout_3.addWidget(self.returnbo)

        # 在 horizontalLayout_3 上添加一个文本框 returnbookid
        self.returnbookid = QtWidgets.QLineEdit(self.layoutWidget1)
        self.returnbookid.setObjectName("returnbookid")
        self.horizontalLayout_3.addWidget(self.returnbookid)

        # 在 horizontalLayout_3 上添加一个按钮 returnbookbt
        self.returnbookbt = QtWidgets.QPushButton(self.layoutWidget1)
        # 创建一个尺寸策略对象，固定宽度和高度，不拉伸
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnbookbt.sizePolicy().hasHeightForWidth())
        self.returnbookbt.setSizePolicy(sizePolicy)
        self.returnbookbt.setObjectName("returnbookbt")
        self.horizontalLayout_3.addWidget(self.returnbookbt)
        # 将 returnbook 页面添加到readertabb的QTabWidget 中
        self.readertab.addTab(self.returnbook, "")

        # 创建一个名为checkbook（查询图书信息）的空白页面
        self.checkbook = QtWidgets.QWidget()
        self.checkbook.setObjectName("checkbook")

        # 在查询图书信息页面中创建一个表格控件tableWidget
        self.tableWidget = QtWidgets.QTableWidget(self.checkbook)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 651, 471))
        self.tableWidget.setObjectName("tableWidget")
        # 设置表格的编辑触发方式和选择行为
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # 9列查询图书
        self.tableWidget.setColumnCount(9)#9列查询所有图书界面
        # 设置表格的行数为 5
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)

        # 在 checkbook 页面中创建一个小部件 widget（上面的查询框架）
        self.widget = QtWidgets.QWidget(self.checkbook)
        self.widget.setGeometry(QtCore.QRect(13, 13, 641, 162))
        self.widget.setObjectName("widget")
        # 在 widget 上创建一个水平布局 horizontalLayout_9
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        # 在 horizontalLayout_9 上创建一个垂直布局 verticalLayout_4
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # 在 verticalLayout_4 上创建一个水平布局4
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #在widge下创建标签label3，并加入水平布局
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        # 文本框“书号”，并加入垂直布局
        self.bookid = QtWidgets.QLineEdit(self.widget)
        self.bookid.setObjectName("bookid")
        self.horizontalLayout_4.addWidget(self.bookid)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        #创建水平布局5
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # 在widge下创建标签4，并加入水平布局
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        #文本框“书名”，并加入垂直布局
        self.bookname = QtWidgets.QLineEdit(self.widget)
        self.bookname.setObjectName("bookname")
        self.horizontalLayout_5.addWidget(self.bookname)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        # 创建水平布局6，来构建“作者”查询
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.author = QtWidgets.QLineEdit(self.widget)
        self.author.setObjectName("author")
        self.horizontalLayout_6.addWidget(self.author)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        # 创建水平布局7，来构建“类别”查询
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.type = QtWidgets.QLineEdit(self.widget)
        self.type.setObjectName("type")
        self.horizontalLayout_7.addWidget(self.type)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        # 创建水平布局8，来构建“出版社”查询
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.publisher = QtWidgets.QLineEdit(self.widget)
        self.publisher.setObjectName("pubulisher")
        self.horizontalLayout_8.addWidget(self.publisher)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        # 在 horizontalLayout_9 上添加 verticalLayout_4
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        # 创建一个垂直布局 verticalLayout，其中包含按钮 pushButton 和 checkbt
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        #创建一个按钮pushButton
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        # 创建一个按钮checkbt
        self.checkbt = QtWidgets.QPushButton(self.widget)
        self.checkbt.setObjectName("checkbt")
        self.verticalLayout.addWidget(self.checkbt)
        # 在 horizontalLayout_9 上添加 verticalLayout
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        # 将 checkbook 页面添加到大的主界面中
        self.readertab.addTab(self.checkbook, "")

        # 重新设置用户界面的文本，主要用于本地化或刷新界面显示
        self.retranslateUi(Reader)
        # 设置当前显示的标签页为索引为0的标签页
        self.readertab.setCurrentIndex(0)
        # 通过 Qt 的元对象系统连接槽函数，确保相关的槽函数在事件发生时被调用
        QtCore.QMetaObject.connectSlotsByName(Reader)

        # 连接相关槽函数
        # 01 借书连接到borrowidcheck函数
        self.borrowcheckbt.clicked.connect(self.borrowidcheck)
        # 02 提交借书连接到submit函数
        self.borrowokbt.clicked.connect(self.submit)
        # 03 还书连接到ReturnBook函数
        self.returnbookbt.clicked.connect(self.ReturnBook)
        # 04 查询所有图书连接到selectallbook函数
        self.pushButton.clicked.connect(self.selectallbook)
        # 05 查询图书连接到selectbook函数
        self.checkbt.clicked.connect(self.selectbook)

#ui界面窗口
    def retranslateUi(self, Reader):
        # 获取Qt翻译模块的翻译函数
        _translate = QtCore.QCoreApplication.translate
        #设置窗口标题
        Reader.setWindowTitle(_translate("Reader", "读者系统"))
        #设置不同元素的文本标签
        self.label.setText(_translate("Reader", "书名"))
        self.borrowcheckbt.setText(_translate("Reader", "查询"))
        #借书界面
        item = self.borrowtable.verticalHeaderItem(0)
        item.setText(_translate("Reader", "1"))
        item = self.borrowtable.horizontalHeaderItem(0)
        item.setText(_translate("Reader", "书号"))
        item = self.borrowtable.horizontalHeaderItem(1)
        item.setText(_translate("Reader", "类别"))
        item = self.borrowtable.horizontalHeaderItem(2)
        item.setText(_translate("Reader", "书名"))
        item = self.borrowtable.horizontalHeaderItem(3)
        item.setText(_translate("Reader", "出版社"))
        item = self.borrowtable.horizontalHeaderItem(4)
        item.setText(_translate("Reader", "出版年份"))
        item = self.borrowtable.horizontalHeaderItem(5)
        item.setText(_translate("Reader", "作者"))
        item = self.borrowtable.horizontalHeaderItem(6)
        item.setText(_translate("Reader", "价格"))
        item = self.borrowtable.horizontalHeaderItem(7)
        item.setText(_translate("Reader", "在馆册数"))
        item = self.borrowtable.horizontalHeaderItem(8)
        item.setText(_translate("Reader", "馆藏册数"))
        self.label_8.setText(_translate("Reader", "学号"))
        self.borrowokbt.setText(_translate("Reader", "提交"))
        self.readertab.setTabText(self.readertab.indexOf(self.borrowbook), _translate("Reader", "借书"))

        #还书界面
        self.returnbo.setText(_translate("Reader", "书号"))
        self.returnbookbt.setText(_translate("Reader", "还书"))
        self.readertab.setTabText(self.readertab.indexOf(self.returnbook), _translate("Reader", "还书"))

        # 查询图书信息上方界面
        self.label_3.setText(_translate("Reader", "书名"))
        self.label_4.setText(_translate("Reader", "书号"))
        self.label_5.setText(_translate("Reader", "作者"))
        self.label_6.setText(_translate("Reader", "类别"))
        self.label_7.setText(_translate("Reader", "出版社"))
        self.pushButton.setText(_translate("Reader", "查询所有"))
        self.checkbt.setText(_translate("Reader", "查询"))
        self.readertab.setTabText(self.readertab.indexOf(self.checkbook), _translate("Reader", "查询图书信息"))

        # 查询图书信息下方界面
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Reader", "书号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Reader", "类别"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Reader", "书名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Reader", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Reader", "出版年份"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Reader", "作者"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Reader", "价格"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Reader", "在馆册数"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Reader", "馆藏册数"))



    # 01 借书信息查询
    def borrowidcheck(self):
        bookin = self.borrowbookid.text()
        sql = 'select * from book where `书号`="%s" or `书名`="%s"' % (bookin, bookin)
        res = cursor.execute(sql)
        bookinfo = cursor.fetchall()
        n = len(bookinfo)
        self.borrowtable.setRowCount(n)
        for i in range(n):
            book = bookinfo[i]
            bookid = QTableWidgetItem(book[0])
            booktype=QTableWidgetItem(book[1])
            bookname = QTableWidgetItem(book[2])
            publisher = QTableWidgetItem(book[3])
            year = QTableWidgetItem(str(book[4]))
            author = QTableWidgetItem((book[5]))
            price = QTableWidgetItem(str(book[6]))
            bookstock = QTableWidgetItem(str(book[7]))
            booknumber = QTableWidgetItem(str(book[8]))
            self.borrowtable.setItem(i, 0, bookid)
            self.borrowtable.setItem(i, 1, booktype)
            self.borrowtable.setItem(i, 2, bookname)
            self.borrowtable.setItem(i, 3, publisher)
            self.borrowtable.setItem(i, 4, author)
            self.borrowtable.setItem(i, 5, year)
            self.borrowtable.setItem(i, 6, price)
            self.borrowtable.setItem(i, 7, bookstock)
            self.borrowtable.setItem(i, 8, booknumber)


    # 02 提交借书申请
    def submit(self):
        s = self.borrowtable.currentRow()
        if s == -1:
            QMessageBox.warning(self, "警告", "请点击想借阅的书！", QMessageBox.Yes)
        else:
            remain = int(self.borrowtable.item(s, 7).text())
            if remain == 0:
                QMessageBox.warning(self, "警告", "这本书已经借光啦！", QMessageBox.Yes)
            else:
                b_id = self.borrowtable.item(s, 0).text()
                cardid=self.cardid.text()
                borrowtime = time.strftime("%Y-%m-%d", time.localtime())

                sql = 'INSERT INTO record(`书号`, `卡号`, `借书日期`) VALUES ("%s","%s","%s")' % (b_id, cardid, borrowtime)
                print(sql)
                cursor.execute(sql)

                conn.commit()
                QMessageBox.warning(self, "提示", "提交成功！", QMessageBox.Yes)


    # 03 提交还书申请
    def ReturnBook(self):
        bookid = self.returnbookid.text()
        sql = 'SELECT * FROM book where `书号`="%s"' % (bookid)
        res = cursor.execute(sql)
        if res:
            cardid = self.cardid.text()
            returntime = time.strftime("%Y-%m-%d", time.localtime())
            sql = 'INSERT INTO record (`书号`,`卡号`,`还书日期`) VALUES ("%s","%s","%s")' % (bookid, cardid, returntime)
            cursor.execute(sql)

            conn.commit()
            QMessageBox.warning(self, "提示", "提交成功！", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "书号输入错误！请重新输入！", QMessageBox.Yes)


    # 04 查询所有书籍
    def selectallbook(self):
        sql = 'SELECT * FROM book'
        cursor.execute(sql)
        books = cursor.fetchall()
        booknumber = len(books)
        self.tableWidget.setRowCount(booknumber)
        for i in range(booknumber):
            book = books[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(book[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(book[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(book[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(book[3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(book[4])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(book[5]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(book[6])))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(book[7])))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(str(book[8])))



    # 05 条件查询书籍
    def selectbook(self):
        bookname = self.bookid.text()
        bookid = self.bookname.text()
        bookauthor = self.author.text()
        booktype = self.type.text()
        publisher = self.publisher.text()
        an = 0
        if bookname:
            bookname = ' `书名`="%s"' % bookname
            an = 1
        if bookid:
            if an == 1:
                bookid = ' and `书号`="%s"' % bookid
            else:
                bookid = ' `书号`="%s"' % bookid
                an = 1
        if bookauthor:
            if an == 1:
                bookauthor = 'and `作者`="%s"' % bookauthor
            else:
                bookauthor = ' `作者`="%s"' % bookauthor
                an = 1
        if booktype:
            if an == 1:
                booktype = ' and `类别`="%s"' % booktype
            else:
                booktype = ' `类别`="%s"' % booktype
                an = 1
        if publisher:
            if an == 1:
                publisher = ' and `出版社`="%s"' % publisher
            else:
                publisher = ' `出版社`="%s"' % publisher
        sql1 = 'SELECT * FROM book'
        if an:
            sql1 += ' where'
        sql = sql1 + bookname + bookid + bookauthor + booktype + publisher
        res = cursor.execute(sql)
        books = cursor.fetchall()
        if res:
            booknumber = len(books)
            self.tableWidget.setRowCount(booknumber)
            for i in range(booknumber):
                book = books[i]
                self.tableWidget.setItem(i, 0, QTableWidgetItem(book[0]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(book[1]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(book[2]))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(book[3]))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(book[4])))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(book[5]))
                self.tableWidget.setItem(i, 6, QTableWidgetItem(str(book[6])))
                self.tableWidget.setItem(i, 7, QTableWidgetItem(str(book[7])))
                self.tableWidget.setItem(i, 8, QTableWidgetItem(str(book[8])))
        else:
            QMessageBox.warning(self, "警告", "没有符合条件的书！", QMessageBox.Yes)




