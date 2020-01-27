from PyQt5 import QtCore, QtGui, QtWidgets
from project import Ui_Dialog

class Ui_Dialog2(object):
    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(778, 408)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 801, 441))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("#frame{\n"
"background-image: url(:/newPrefix/Login Image.jpg);\n"
"}\n"
"#frame_2{\n"
"background-color: rgba(0,95,155,0.5);\n"
"border-radius: 10px;\n"
"}\n"
"#signInGroupBox{\n"
"color: white;\n"
"}\n"
"#userlbl{\n"
"color: white;\n"
"}\n"
"#passwordlbl{\n"
"color: white;\n"
"}\n"
"#usertxtbox{\n"
"color: white;\n"
"border-radius: 1px;\n"
"background-color: transparent;\n"
"border-bottom: 1px solid white\n"
"}\n"
"#passwordtxtbox{\n"
"background-color: transparent;\n"
"color: white;\n"
"border-radius: 1px;\n"
"border-bottom: 1px solid white\n"
"}\n"
"#signinBtn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}\n"
"#signinBtn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,95,155);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(400, 30, 341, 371))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.signInGroupBox = QtWidgets.QGroupBox(self.frame_2)
        self.signInGroupBox.setGeometry(QtCore.QRect(40, 50, 261, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signInGroupBox.setFont(font)
        self.signInGroupBox.setObjectName("signInGroupBox")
        self.usertxtbox = QtWidgets.QLineEdit(self.signInGroupBox)
        self.usertxtbox.setGeometry(QtCore.QRect(20, 80, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usertxtbox.setFont(font)
        self.usertxtbox.setObjectName("usertxtbox")
        self.passwordtxtbox = QtWidgets.QLineEdit(self.signInGroupBox)
        self.passwordtxtbox.setGeometry(QtCore.QRect(20, 150, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordtxtbox.setFont(font)
        self.passwordtxtbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordtxtbox.setObjectName("passwordtxtbox")
        self.userlbl = QtWidgets.QLabel(self.signInGroupBox)
        self.userlbl.setGeometry(QtCore.QRect(20, 50, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.userlbl.setFont(font)
        self.userlbl.setObjectName("userlbl")
        self.passwordlbl = QtWidgets.QLabel(self.signInGroupBox)
        self.passwordlbl.setGeometry(QtCore.QRect(20, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.passwordlbl.setFont(font)
        self.passwordlbl.setObjectName("passwordlbl")
        self.signInerrorLbl = QtWidgets.QLabel(self.signInGroupBox)
        self.signInerrorLbl.setGeometry(QtCore.QRect(20, 186, 221, 20))
        self.signInerrorLbl.setText("")
        self.signInerrorLbl.setObjectName("signInerrorLbl")
        self.signinBtn = QtWidgets.QPushButton(self.frame_2)
        self.signinBtn.setGeometry(QtCore.QRect(40, 280, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signinBtn.setFont(font)
        self.signinBtn.setObjectName("signinBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.signinBtn.clicked.connect(self.loginClick)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign In"))
        self.signInGroupBox.setTitle(_translate("Dialog", "Sign In"))
        self.userlbl.setText(_translate("Dialog", "Username"))
        self.passwordlbl.setText(_translate("Dialog", "Password"))
        self.signinBtn.setText(_translate("Dialog", "Sign In"))
    
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        Dialog.hide()
        
    def loginClick(self):
        import sqlite3
        db = sqlite3.connect("inventory.db")
        crr = db.cursor()
        crr.execute("select * from login where username='%s'"%(self.usertxtbox.text()))
        res = crr.fetchall()
        if self.usertxtbox.text() == "" or self.passwordtxtbox.text() == "":
            self.signInerrorLbl.setText("Please Enter Username and Password")
            self.signInerrorLbl.setStyleSheet("color: red;\n")
            self.userlbl.setStyleSheet("color: red;\n")
            self.usertxtbox.setStyleSheet("border: 1px solid red;color: red;")
            self.passwordlbl.setStyleSheet("color: red;\n")
            self.passwordtxtbox.setStyleSheet("border: 1px solid red;color: red;")
        else:
            if res == []:
                self.signInerrorLbl.setText("Incorrect Username Or Password")
                self.signInerrorLbl.setStyleSheet("color: red;\n")
                self.userlbl.setStyleSheet("color: red;\n")
                self.usertxtbox.setStyleSheet("border: 1px solid red;color: red;")
                self.passwordlbl.setStyleSheet("color: red;\n")
                self.passwordtxtbox.setStyleSheet("border: 1px solid red;color: red;")
            else:
                user = res[0][0]
                password = res[0][1]
                if user == self.usertxtbox.text() and password == self.passwordtxtbox.text():
                    self.openWindow()
                else:
                    self.userlbl.setStyleSheet("color: white;\n")
                    self.usertxtbox.setStyleSheet("border: 1px solid white;color: white;")
                    self.passwordlbl.setStyleSheet("color: red;\n")
                    self.passwordtxtbox.setStyleSheet("border: 1px solid red;color: red;")
                    self.signInerrorLbl.setText("Incorrect Password")
                    self.signInerrorLbl.setStyleSheet("color: red;\n")

import login

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi2(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

