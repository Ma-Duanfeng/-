from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")#整体菜单框
        Login.setWindowModality(QtCore.Qt.ApplicationModal)
        Login.resize(700, 400)
        # setGeometry左右，上下，宽度，高度
        self.label = QtWidgets.QLabel(Login)#“用户登录”
        self.label.setGeometry(QtCore.QRect(300, 20, 180, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.user = QtWidgets.QLabel(Login)#“用户”
        self.user.setGeometry(QtCore.QRect(160, 100, 65, 41))
        self.user.setObjectName("user")

        self.password = QtWidgets.QLabel(Login)#“密码”
        self.password.setGeometry(QtCore.QRect(160, 150, 65, 41))
        self.password.setObjectName("password")

        self.identify = QtWidgets.QLabel(Login)#“身份类别”
        self.identify.setGeometry(QtCore.QRect(140, 200, 150, 41))
        self.identify.setObjectName("identify")

        self.userline = QtWidgets.QLineEdit(Login)#用户框
        self.userline.setGeometry(QtCore.QRect(290, 100, 200, 40))
        self.userline.setObjectName("userline")

        self.pwline = QtWidgets.QLineEdit(Login)#密码框
        self.pwline.setGeometry(QtCore.QRect(290, 150, 200, 40))
        self.pwline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwline.setObjectName("pwline")

        self.idbox = QtWidgets.QComboBox(Login)#身份类别子目录框
        self.idbox.setGeometry(QtCore.QRect(290, 200, 200, 40))
        self.idbox.setObjectName("idbox")
        self.idbox.addItem("")
        self.idbox.addItem("")

        self.loginbt = QtWidgets.QPushButton(Login)
        self.loginbt.setGeometry(QtCore.QRect(250, 270, 93, 28))
        self.loginbt.setObjectName("loginbt")

        self.exitbt = QtWidgets.QPushButton(Login)
        self.exitbt.setGeometry(QtCore.QRect(420, 270, 93, 28))
        self.exitbt.setObjectName("exitbt")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "df图书馆管理系统"))
        self.label.setText(
            _translate("Login", "<html><head/><body><p><span style=\" font-size:16pt;\">用户登录</span></p></body></html>"))
        self.user.setText(
            _translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">用户id</span></p></body></html>"))
        self.password.setText(
            _translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">密码</span></p></body></html>"))
        self.identify.setText(
            _translate("Login", "<html><head/><body><p><span style=\" font-size:12pt;\">身份类型</span></p></body></html>"))
        self.idbox.setItemText(0, _translate("Login", "读者"))
        self.idbox.setItemText(1, _translate("Login", "图书管理员"))
        self.loginbt.setText(_translate("Login", "登录"))
        self.exitbt.setText(_translate("Login", "退出"))






