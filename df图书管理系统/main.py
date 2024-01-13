
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from login import Ui_Login
from reader import Ui_Reader
from connect import *
from BookAdmin import Ui_bookadmin

# 链接数据库
cursor, conn = connect()


class Readerui(QtWidgets.QMainWindow, Ui_Reader):
    def __init__(self, parent=None):
        super(Readerui, self).__init__(parent)
        self.setupUi(self)

class bookadminui(QtWidgets.QMainWindow, Ui_bookadmin):
    def __init__(self, admin_name, parent=None):
        super(bookadminui, self).__init__(parent)
        self.setupUi(self)
        self.admin_name = admin_name
       


# 程序首页（登录界面）
class MyMainForm(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.exitbt.clicked.connect(self.exit)
        self.loginbt.clicked.connect(self.login)

    # 退出
    def exit(self):
        rec_code = QMessageBox.question(self, "确认", "您确认要退出吗？", QMessageBox.Yes | QMessageBox.No)
        if rec_code != 65536:
            self.close()

    # 登陆
    def login(self):
        
        ID = self.userline.text()
        PW = self.pwline.text()
        if ID == '' or PW == '':
            QMessageBox.warning(self, "警告", "请输入用户名/密码", QMessageBox.Yes)
        else:
            # 读者登录
            if self.idbox.currentText() == '读者':
                sql = 'select * from card where `卡号` = "%s" and `密码`="%s"' % (ID, PW)
                res = cursor.execute(sql)
                if res:
                    self.read = Readerui()
                    self.read.show()
                    self.close()
                    pass
                else:
                    QMessageBox.warning(self, "警告", "密码错误，请重新输入！", QMessageBox.Yes)
            # 图书管理员登录
            elif self.idbox.currentText() == '图书管理员':
                sql = 'select * from admin where `管理员账号` = "%s" and `密码`="%s"' % (ID, PW)
                res = cursor.execute(sql)
                # cursor.close()
                # conn.close()
                # 进行判断
                if res:
                    self.bookadmin = bookadminui(ID)
                    self.bookadmin.show()
                    self.close()
                    pass
                else:
                    QMessageBox.warning(self, "警告", "密码错误，请重新输入！", QMessageBox.Yes)



app = QApplication(sys.argv)
myWin = MyMainForm()
myWin.show()
sys.exit(app.exec_())
