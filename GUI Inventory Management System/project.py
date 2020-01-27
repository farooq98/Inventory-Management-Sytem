from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(955, 692)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 961, 701))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.mainFrame = QtWidgets.QFrame(self.tab)
        self.mainFrame.setGeometry(QtCore.QRect(-90, -150, 1199, 831))
        self.mainFrame.setStyleSheet("#mainFrame{\n"
"background-color:rgb(143,213,233);\n"
"}\n"
"\n"
"#searchBtn:hover{\n"
"background-color: rgba(0,0,0,0.5);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"#searchBtn{\n"
"background-color: rgba(21,149,136,0.8);\n"
"\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"#searchtxtbox{\n"
"color: white;\n"
"border-radius: 1px;\n"
"background-color: transparent;\n"
"border-bottom: 1px solid white;\n"
"}\n"
"#searchframe{\n"
"background-color: rgba(21,149,136,0.5);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.productTable = QtWidgets.QTableWidget(self.mainFrame)
        self.productTable.setGeometry(QtCore.QRect(250, 260, 631, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.productTable.setFont(font)
        self.productTable.setStyleSheet("\n"
"background-color: rgba(21,149,136,0.5);\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.productTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.productTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.productTable.setShowGrid(False)
        self.productTable.setRowCount(10)
        self.productTable.setColumnCount(5)
        self.productTable.setObjectName("productTable")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.productTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.productTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.productTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.productTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.productTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.productTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.productTable.setItem(1, 1, item)
        self.productTable.horizontalHeader().setVisible(False)
        self.productTable.verticalHeader().setVisible(False)
        self.searchframe = QtWidgets.QFrame(self.mainFrame)
        self.searchframe.setGeometry(QtCore.QRect(250, 190, 631, 61))
        self.searchframe.setStyleSheet("")
        self.searchframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchframe.setObjectName("searchframe")
        self.searchtxtbox = QtWidgets.QLineEdit(self.searchframe)
        self.searchtxtbox.setGeometry(QtCore.QRect(10, 10, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchtxtbox.setFont(font)
        self.searchtxtbox.setObjectName("searchtxtbox")
        self.searchBtn = QtWidgets.QPushButton(self.searchframe)
        self.searchBtn.setGeometry(QtCore.QRect(520, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchBtn.setFont(font)
        self.searchBtn.setObjectName("searchBtn")
        self.comboBox = QtWidgets.QComboBox(self.searchframe)
        self.comboBox.setGeometry(QtCore.QRect(390, 11, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("#comboBox{\n"
"color: white;\n"
"border-radius: 1px;\n"
"background-color: transparent;\n"
"border-bottom: 1px solid white;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.mainFrame)
        self.label_13.setGeometry(QtCore.QRect(50, 180, 1021, 621))
        self.label_13.setStyleSheet("image: url(:/newPrefix/products-png-5.png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_13.raise_()
        self.productTable.raise_()
        self.searchframe.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.addtocartFrame = QtWidgets.QFrame(self.tab_4)
        self.addtocartFrame.setGeometry(QtCore.QRect(-10, -10, 981, 731))
        self.addtocartFrame.setStyleSheet("#addtocartFrame{background-color: rgb(200,199,168)}\n"
"#cartTable{\n"
"background-color: rgba(0,95,155,0.5);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"#removeframe{\n"
"background-color: rgba(162,160,108,0.5);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"#productIDlbl2{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#removeproductTxtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"#sellPrice_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#removeproductBtn{\n"
"    color: white;\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}\n"
"#removeproductBtn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(162,160,108);\n"
"}")
        self.addtocartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addtocartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addtocartFrame.setObjectName("addtocartFrame")
        self.label_6 = QtWidgets.QLabel(self.addtocartFrame)
        self.label_6.setGeometry(QtCore.QRect(330, 40, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgba(162,160,108,0.5);\n"
"    border-radius: 10px;\n"
"color:White;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.cartFrame = QtWidgets.QFrame(self.addtocartFrame)
        self.cartFrame.setGeometry(QtCore.QRect(50, 110, 321, 491))
        self.cartFrame.setStyleSheet("#cartFrame{\n"
"background-color: rgba(162,160,108,0.5);\n"
"    border-radius: 10px;\n"
"}\n"
"#customerIDlbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#productIDlbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#customerIDtxtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#productIDtxtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#datelbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#quantitytxtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#datetxtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#cat_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#addproductqtyllbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#qty_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#buyPrice_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#buyPrice_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#sellPrice_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#sellPrice_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#addtocartBtn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}\n"
"#addtocartBtn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(162,160,108);\n"
"}")
        self.cartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cartFrame.setObjectName("cartFrame")
        self.customerIDlbl = QtWidgets.QLabel(self.cartFrame)
        self.customerIDlbl.setGeometry(QtCore.QRect(30, 100, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.customerIDlbl.setFont(font)
        self.customerIDlbl.setStyleSheet("")
        self.customerIDlbl.setObjectName("customerIDlbl")
        self.customerIDtxtbox = QtWidgets.QLineEdit(self.cartFrame)
        self.customerIDtxtbox.setGeometry(QtCore.QRect(30, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.customerIDtxtbox.setFont(font)
        self.customerIDtxtbox.setStyleSheet("")
        self.customerIDtxtbox.setObjectName("customerIDtxtbox")
        self.productIDlbl = QtWidgets.QLabel(self.cartFrame)
        self.productIDlbl.setGeometry(QtCore.QRect(30, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.productIDlbl.setFont(font)
        self.productIDlbl.setObjectName("productIDlbl")
        self.productIDtxtbox = QtWidgets.QLineEdit(self.cartFrame)
        self.productIDtxtbox.setGeometry(QtCore.QRect(30, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productIDtxtbox.setFont(font)
        self.productIDtxtbox.setObjectName("productIDtxtbox")
        self.addproductqtyllbl = QtWidgets.QLabel(self.cartFrame)
        self.addproductqtyllbl.setGeometry(QtCore.QRect(30, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.addproductqtyllbl.setFont(font)
        self.addproductqtyllbl.setObjectName("addproductqtyllbl")
        self.quantitytxtbox = QtWidgets.QLineEdit(self.cartFrame)
        self.quantitytxtbox.setGeometry(QtCore.QRect(30, 240, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quantitytxtbox.setFont(font)
        self.quantitytxtbox.setObjectName("quantitytxtbox")
        self.datelbl = QtWidgets.QLabel(self.cartFrame)
        self.datelbl.setGeometry(QtCore.QRect(30, 280, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.datelbl.setFont(font)
        self.datelbl.setObjectName("datelbl")
        self.datetxtbox = QtWidgets.QLineEdit(self.cartFrame)
        self.datetxtbox.setGeometry(QtCore.QRect(30, 300, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.datetxtbox.setFont(font)
        self.datetxtbox.setReadOnly(True)
        self.datetxtbox.setObjectName("datetxtbox")
        self.addtocartBtn = QtWidgets.QPushButton(self.cartFrame)
        self.addtocartBtn.setGeometry(QtCore.QRect(50, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addtocartBtn.setFont(font)
        self.addtocartBtn.setObjectName("addtocartBtn")
        self.buyProductBtn = QtWidgets.QPushButton(self.cartFrame)
        self.buyProductBtn.setGeometry(QtCore.QRect(50, 410, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buyProductBtn.setFont(font)
        self.buyProductBtn.setStyleSheet("#buyProductBtn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}\n"
"#buyProductBtn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(162,160,108);\n"
"}")
        self.buyProductBtn.setObjectName("buyProductBtn")
        self.cartTable = QtWidgets.QTableWidget(self.addtocartFrame)
        self.cartTable.setGeometry(QtCore.QRect(400, 160, 521, 291))
        self.cartTable.setStyleSheet("background-color: rgba(162,160,108,0.5);\n"
"color: white;")
        self.cartTable.setShowGrid(False)
        self.cartTable.setRowCount(5)
        self.cartTable.setColumnCount(5)
        self.cartTable.setObjectName("cartTable")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cartTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cartTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cartTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cartTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cartTable.setItem(0, 4, item)
        self.cartTable.horizontalHeader().setVisible(False)
        self.cartTable.verticalHeader().setVisible(False)
        self.removeframe = QtWidgets.QFrame(self.addtocartFrame)
        self.removeframe.setGeometry(QtCore.QRect(400, 510, 521, 91))
        self.removeframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.removeframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.removeframe.setObjectName("removeframe")
        self.removeproductTxtbox = QtWidgets.QLineEdit(self.removeframe)
        self.removeproductTxtbox.setGeometry(QtCore.QRect(130, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.removeproductTxtbox.setFont(font)
        self.removeproductTxtbox.setObjectName("removeproductTxtbox")
        self.productIDlbl2 = QtWidgets.QLabel(self.removeframe)
        self.productIDlbl2.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.productIDlbl2.setFont(font)
        self.productIDlbl2.setObjectName("productIDlbl2")
        self.removeproductBtn = QtWidgets.QPushButton(self.removeframe)
        self.removeproductBtn.setGeometry(QtCore.QRect(140, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.removeproductBtn.setFont(font)
        self.removeproductBtn.setObjectName("removeproductBtn")
        self.emptyCartBtn = QtWidgets.QPushButton(self.removeframe)
        self.emptyCartBtn.setGeometry(QtCore.QRect(280, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.emptyCartBtn.setFont(font)
        self.emptyCartBtn.setStyleSheet("#emptyCartBtn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}\n"
"#emptyCartBtn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(162,160,108);\n"
"}")
        self.emptyCartBtn.setObjectName("emptyCartBtn")
        self.label_7 = QtWidgets.QLabel(self.addtocartFrame)
        self.label_7.setGeometry(QtCore.QRect(490, 110, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(162,160,108,0.5);\n"
"    border-radius: 10px;\n"
"color:White;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.cart_total_lbl = QtWidgets.QLabel(self.addtocartFrame)
        self.cart_total_lbl.setGeometry(QtCore.QRect(570, 460, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.cart_total_lbl.setFont(font)
        self.cart_total_lbl.setStyleSheet("background-color: rgba(162,160,108,0.5);\n"
"    border-radius: 10px;\n"
"color:White;")
        self.cart_total_lbl.setText("")
        self.cart_total_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.cart_total_lbl.setObjectName("cart_total_lbl")
        self.cartError_lbl = QtWidgets.QLabel(self.addtocartFrame)
        self.cartError_lbl.setGeometry(QtCore.QRect(-20, -40, 1091, 711))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cartError_lbl.setFont(font)
        self.cartError_lbl.setStyleSheet("image: url(:/newPrefix/ecommerce-clipart-digital-commerce-316280-8206820.png);")
        self.cartError_lbl.setText("")
        self.cartError_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.cartError_lbl.setObjectName("cartError_lbl")
        self.label_14 = QtWidgets.QLabel(self.addtocartFrame)
        self.label_14.setGeometry(QtCore.QRect(340, 620, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.cartError_lbl.raise_()
        self.label_6.raise_()
        self.cartFrame.raise_()
        self.cartTable.raise_()
        self.removeframe.raise_()
        self.label_7.raise_()
        self.cart_total_lbl.raise_()
        self.label_14.raise_()
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.ManageCustomeFrame = QtWidgets.QFrame(self.tab_7)
        self.ManageCustomeFrame.setGeometry(QtCore.QRect(-30, -10, 991, 711))
        self.ManageCustomeFrame.setStyleSheet("#ManageCustomeFrame{\n"
"background-color:rgba(53,151,212);\n"
"}")
        self.ManageCustomeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ManageCustomeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ManageCustomeFrame.setObjectName("ManageCustomeFrame")
        self.label_2 = QtWidgets.QLabel(self.ManageCustomeFrame)
        self.label_2.setGeometry(QtCore.QRect(120, 50, 821, 571))
        self.label_2.setStyleSheet("image: url(:/newPrefix/sales-manifesto-sales-pipeline-visibility-1296x678.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.manageCustomerFrame = QtWidgets.QFrame(self.ManageCustomeFrame)
        self.manageCustomerFrame.setGeometry(QtCore.QRect(60, 110, 351, 491))
        self.manageCustomerFrame.setStyleSheet("#manageCustomerFrame{\n"
"    background-color: rgba(0,95,155,0.5);\n"
"    border-radius: 10px;\n"
"}\n"
"#customerIDlbl_2{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#selectlbl_2{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#customerID_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#selectcustomercombobox_2{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#customername_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#customernametxtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#cat_combobox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#cat_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#qty_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#qty_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#gender_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#gendercombobox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#phone_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#phonetxtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#submitcustomer_btn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}\n"
"#submitcustomer_btn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,95,155);\n"
"}")
        self.manageCustomerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manageCustomerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manageCustomerFrame.setObjectName("manageCustomerFrame")
        self.customerIDlbl_2 = QtWidgets.QLabel(self.manageCustomerFrame)
        self.customerIDlbl_2.setGeometry(QtCore.QRect(30, 100, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.customerIDlbl_2.setFont(font)
        self.customerIDlbl_2.setStyleSheet("")
        self.customerIDlbl_2.setObjectName("customerIDlbl_2")
        self.customerID_txtbox = QtWidgets.QLineEdit(self.manageCustomerFrame)
        self.customerID_txtbox.setGeometry(QtCore.QRect(30, 120, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.customerID_txtbox.setFont(font)
        self.customerID_txtbox.setStyleSheet("")
        self.customerID_txtbox.setObjectName("customerID_txtbox")
        self.customername_lbl = QtWidgets.QLabel(self.manageCustomerFrame)
        self.customername_lbl.setGeometry(QtCore.QRect(30, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.customername_lbl.setFont(font)
        self.customername_lbl.setObjectName("customername_lbl")
        self.customernametxtbox = QtWidgets.QLineEdit(self.manageCustomerFrame)
        self.customernametxtbox.setGeometry(QtCore.QRect(30, 180, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.customernametxtbox.setFont(font)
        self.customernametxtbox.setObjectName("customernametxtbox")
        self.gender_lbl = QtWidgets.QLabel(self.manageCustomerFrame)
        self.gender_lbl.setGeometry(QtCore.QRect(30, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.gender_lbl.setFont(font)
        self.gender_lbl.setObjectName("gender_lbl")
        self.phone_lbl = QtWidgets.QLabel(self.manageCustomerFrame)
        self.phone_lbl.setGeometry(QtCore.QRect(30, 280, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.phone_lbl.setFont(font)
        self.phone_lbl.setObjectName("phone_lbl")
        self.phonetxtbox = QtWidgets.QLineEdit(self.manageCustomerFrame)
        self.phonetxtbox.setGeometry(QtCore.QRect(30, 300, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.phonetxtbox.setFont(font)
        self.phonetxtbox.setObjectName("phonetxtbox")
        self.gendercombobox = QtWidgets.QComboBox(self.manageCustomerFrame)
        self.gendercombobox.setGeometry(QtCore.QRect(30, 240, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gendercombobox.setFont(font)
        self.gendercombobox.setObjectName("gendercombobox")
        self.gendercombobox.addItem("")
        self.gendercombobox.addItem("")
        self.selectlbl_2 = QtWidgets.QLabel(self.manageCustomerFrame)
        self.selectlbl_2.setGeometry(QtCore.QRect(30, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.selectlbl_2.setFont(font)
        self.selectlbl_2.setObjectName("selectlbl_2")
        self.selectcustomercombobox_2 = QtWidgets.QComboBox(self.manageCustomerFrame)
        self.selectcustomercombobox_2.setGeometry(QtCore.QRect(30, 60, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectcustomercombobox_2.setFont(font)
        self.selectcustomercombobox_2.setObjectName("selectcustomercombobox_2")
        self.selectcustomercombobox_2.addItem("")
        self.selectcustomercombobox_2.addItem("")
        self.selectcustomercombobox_2.addItem("")
        self.submitcustomer_btn = QtWidgets.QPushButton(self.manageCustomerFrame)
        self.submitcustomer_btn.setGeometry(QtCore.QRect(60, 350, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submitcustomer_btn.setFont(font)
        self.submitcustomer_btn.setObjectName("submitcustomer_btn")
        self.label_8 = QtWidgets.QLabel(self.ManageCustomeFrame)
        self.label_8.setGeometry(QtCore.QRect(340, 30, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgba(0,95,155,0.5);\n"
"    border-radius: 10px;\n"
"color:White;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.customerTable = QtWidgets.QTableWidget(self.ManageCustomeFrame)
        self.customerTable.setGeometry(QtCore.QRect(440, 170, 501, 431))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.customerTable.setFont(font)
        self.customerTable.setStyleSheet("\n"
"    background-color: rgba(0,95,155,0.5);\n"
"    border-radius: 10px;\n"
"color: white;\n"
"")
        self.customerTable.setShowGrid(False)
        self.customerTable.setRowCount(10)
        self.customerTable.setColumnCount(4)
        self.customerTable.setObjectName("customerTable")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.customerTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.customerTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.customerTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.customerTable.setItem(0, 3, item)
        self.customerTable.horizontalHeader().setVisible(False)
        self.customerTable.verticalHeader().setVisible(False)
        self.searchCustomerFrame = QtWidgets.QFrame(self.ManageCustomeFrame)
        self.searchCustomerFrame.setGeometry(QtCore.QRect(440, 110, 501, 51))
        self.searchCustomerFrame.setStyleSheet("#searchCustomerFrame{\n"
"background-color: rgba(0,95,155,0.5);\n"
"    border-radius: 10px;\n"
"}")
        self.searchCustomerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchCustomerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchCustomerFrame.setObjectName("searchCustomerFrame")
        self.searchCustomerTxtbox = QtWidgets.QLineEdit(self.searchCustomerFrame)
        self.searchCustomerTxtbox.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchCustomerTxtbox.setFont(font)
        self.searchCustomerTxtbox.setStyleSheet("    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;")
        self.searchCustomerTxtbox.setObjectName("searchCustomerTxtbox")
        self.seaarchCustomerBtn = QtWidgets.QPushButton(self.searchCustomerFrame)
        self.seaarchCustomerBtn.setGeometry(QtCore.QRect(400, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seaarchCustomerBtn.setFont(font)
        self.seaarchCustomerBtn.setStyleSheet("#seaarchCustomerBtn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,95,155);\n"
"}\n"
"#seaarchCustomerBtn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}")
        self.seaarchCustomerBtn.setObjectName("seaarchCustomerBtn")
        self.searchCustomerCombobox = QtWidgets.QComboBox(self.searchCustomerFrame)
        self.searchCustomerCombobox.setGeometry(QtCore.QRect(250, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchCustomerCombobox.setFont(font)
        self.searchCustomerCombobox.setStyleSheet("    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;")
        self.searchCustomerCombobox.setObjectName("searchCustomerCombobox")
        self.searchCustomerCombobox.addItem("")
        self.searchCustomerCombobox.addItem("")
        self.searchCustomerCombobox.addItem("")
        self.searchCustomerCombobox.addItem("")
        self.customerError_lbl = QtWidgets.QLabel(self.ManageCustomeFrame)
        self.customerError_lbl.setGeometry(QtCore.QRect(280, 630, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.customerError_lbl.setFont(font)
        self.customerError_lbl.setText("")
        self.customerError_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.customerError_lbl.setObjectName("customerError_lbl")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.manageCategoriesFrame = QtWidgets.QFrame(self.tab_3)
        self.manageCategoriesFrame.setGeometry(QtCore.QRect(-10, -10, 961, 701))
        self.manageCategoriesFrame.setStyleSheet("#manageCategoriesFrame{\n"
"background-color: rgb(236,240,241);\n"
"}\n"
"#manageCatgeorieslbl{\n"
"color: black;\n"
"}\n"
"")
        self.manageCategoriesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manageCategoriesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manageCategoriesFrame.setObjectName("manageCategoriesFrame")
        self.full_frame = QtWidgets.QFrame(self.manageCategoriesFrame)
        self.full_frame.setGeometry(QtCore.QRect(50, 70, 871, 571))
        self.full_frame.setStyleSheet("#full_frame{\n"
"    background-color: rgba(99,128,135,0.6);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"#search_frame{\n"
"    background-color: rgba(75,98,103,0.5);\n"
"border-radius: 5px;\n"
"border: 1px solid black;\n"
"}\n"
"#add_frame{\n"
"    background-color: rgba(75,98,103,0.5);\n"
"border-radius: 5px;\n"
"border: 1px solid black;\n"
"}\n"
"#cat_lbl_3{\n"
"background-color: transparent;\n"
"color: white;\n"
"}\n"
"#add_lbl{\n"
"background-color: transparent;\n"
"color: white;\n"
"}\n"
"#searchcategorytxtbox{\n"
"background-color: transparent;\n"
"border: 1px;\n"
"border-bottom: 1px solid white;\n"
"color: white;\n"
"}\n"
"#cat_txtbox{\n"
"background-color: transparent;\n"
"border: 1px;\n"
"border-bottom: 1px solid white;\n"
"color: white;\n"
"}\n"
"#add_combobox{\n"
"background-color: transparent;\n"
"border: 1px;\n"
"border-bottom: 1px solid white;\n"
"color: white;\n"
"}")
        self.full_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.full_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.full_frame.setObjectName("full_frame")
        self.cat_table = QtWidgets.QTableWidget(self.full_frame)
        self.cat_table.setGeometry(QtCore.QRect(330, 130, 261, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cat_table.setFont(font)
        self.cat_table.setStyleSheet("\n"
"    background-color: rgba(75,98,103,0.8);\n"
"border-radius: 5px;\n"
"border: 1px solid black;\n"
"color: white;\n"
"")
        self.cat_table.setShowGrid(False)
        self.cat_table.setGridStyle(QtCore.Qt.SolidLine)
        self.cat_table.setRowCount(5)
        self.cat_table.setColumnCount(1)
        self.cat_table.setObjectName("cat_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cat_table.setItem(0, 0, item)
        self.cat_table.horizontalHeader().setVisible(False)
        self.cat_table.horizontalHeader().setHighlightSections(True)
        self.cat_table.verticalHeader().setVisible(False)
        self.label_4 = QtWidgets.QLabel(self.full_frame)
        self.label_4.setGeometry(QtCore.QRect(400, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.add_frame = QtWidgets.QFrame(self.full_frame)
        self.add_frame.setGeometry(QtCore.QRect(20, 420, 821, 101))
        self.add_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_frame.setObjectName("add_frame")
        self.add_combobox = QtWidgets.QComboBox(self.add_frame)
        self.add_combobox.setGeometry(QtCore.QRect(170, 50, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_combobox.setFont(font)
        self.add_combobox.setObjectName("add_combobox")
        self.add_combobox.addItem("")
        self.add_combobox.addItem("")
        self.cat_txtbox = QtWidgets.QLineEdit(self.add_frame)
        self.cat_txtbox.setGeometry(QtCore.QRect(170, 10, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cat_txtbox.setFont(font)
        self.cat_txtbox.setObjectName("cat_txtbox")
        self.add_lbl = QtWidgets.QLabel(self.add_frame)
        self.add_lbl.setGeometry(QtCore.QRect(20, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_lbl.setFont(font)
        self.add_lbl.setObjectName("add_lbl")
        self.cat_lbl_3 = QtWidgets.QLabel(self.add_frame)
        self.cat_lbl_3.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cat_lbl_3.setFont(font)
        self.cat_lbl_3.setObjectName("cat_lbl_3")
        self.search_frame = QtWidgets.QFrame(self.full_frame)
        self.search_frame.setGeometry(QtCore.QRect(20, 20, 831, 51))
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.searchcategorytxtbox = QtWidgets.QLineEdit(self.search_frame)
        self.searchcategorytxtbox.setGeometry(QtCore.QRect(20, 10, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchcategorytxtbox.setFont(font)
        self.searchcategorytxtbox.setObjectName("searchcategorytxtbox")
        self.searchcategoryBtn = QtWidgets.QPushButton(self.search_frame)
        self.searchcategoryBtn.setGeometry(QtCore.QRect(720, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchcategoryBtn.setFont(font)
        self.searchcategoryBtn.setStyleSheet("#searchcategoryBtn:hover{\n"
"background-color: rgba(0,0,0,0.8);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"#searchcategoryBtn{\n"
"background-color: rgba(0,0,0,0.5);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.searchcategoryBtn.setObjectName("searchcategoryBtn")
        self.submitcategorybtn = QtWidgets.QPushButton(self.full_frame)
        self.submitcategorybtn.setGeometry(QtCore.QRect(390, 530, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submitcategorybtn.setFont(font)
        self.submitcategorybtn.setStyleSheet("\n"
"#submitcategorybtn:hover{\n"
"background-color: rgba(0,0,0,0.8);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"#submitcategorybtn{\n"
"background-color: rgba(0,0,0,0.6);\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.submitcategorybtn.setObjectName("submitcategorybtn")
        self.manageCatgeorieslbl = QtWidgets.QLabel(self.manageCategoriesFrame)
        self.manageCatgeorieslbl.setGeometry(QtCore.QRect(350, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.manageCatgeorieslbl.setFont(font)
        self.manageCatgeorieslbl.setObjectName("manageCatgeorieslbl")
        self.label_5 = QtWidgets.QLabel(self.manageCategoriesFrame)
        self.label_5.setGeometry(QtCore.QRect(-70, -90, 1071, 761))
        self.label_5.setStyleSheet("image: url(:/newPrefix/Gated-Products.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.full_frame.raise_()
        self.manageCatgeorieslbl.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.addproductFrame = QtWidgets.QFrame(self.tab_2)
        self.addproductFrame.setGeometry(QtCore.QRect(-10, -10, 981, 691))
        self.addproductFrame.setStyleSheet("#addproductFrame{\n"
"background-color: rgb(250,205,174);\n"
"}")
        self.addproductFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.addproductFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.addproductFrame.setObjectName("addproductFrame")
        self.Product_frame = QtWidgets.QFrame(self.addproductFrame)
        self.Product_frame.setGeometry(QtCore.QRect(70, 90, 831, 521))
        self.Product_frame.setStyleSheet("#Product_frame{\n"
"    background-color: rgba(247,170,119,0.5);\n"
"    border-radius: 10px;\n"
"}\n"
"#ID_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#selectlbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#ID_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#selectcombobox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#name_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#name_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#cat_combobox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#cat_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#qty_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#qty_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#buyPrice_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#buyPrice_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#sellPrice_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#sellPrice_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"")
        self.Product_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Product_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Product_frame.setObjectName("Product_frame")
        self.ID_lbl = QtWidgets.QLabel(self.Product_frame)
        self.ID_lbl.setGeometry(QtCore.QRect(30, 90, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.ID_lbl.setFont(font)
        self.ID_lbl.setStyleSheet("")
        self.ID_lbl.setObjectName("ID_lbl")
        self.ID_txtbox = QtWidgets.QLineEdit(self.Product_frame)
        self.ID_txtbox.setGeometry(QtCore.QRect(30, 110, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ID_txtbox.setFont(font)
        self.ID_txtbox.setStyleSheet("")
        self.ID_txtbox.setObjectName("ID_txtbox")
        self.name_lbl = QtWidgets.QLabel(self.Product_frame)
        self.name_lbl.setGeometry(QtCore.QRect(30, 150, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.name_lbl.setFont(font)
        self.name_lbl.setObjectName("name_lbl")
        self.name_txtbox = QtWidgets.QLineEdit(self.Product_frame)
        self.name_txtbox.setGeometry(QtCore.QRect(30, 170, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_txtbox.setFont(font)
        self.name_txtbox.setObjectName("name_txtbox")
        self.cat_lbl = QtWidgets.QLabel(self.Product_frame)
        self.cat_lbl.setGeometry(QtCore.QRect(30, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.cat_lbl.setFont(font)
        self.cat_lbl.setObjectName("cat_lbl")
        self.qty_lbl = QtWidgets.QLabel(self.Product_frame)
        self.qty_lbl.setGeometry(QtCore.QRect(30, 270, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.qty_lbl.setFont(font)
        self.qty_lbl.setObjectName("qty_lbl")
        self.qty_txtbox = QtWidgets.QLineEdit(self.Product_frame)
        self.qty_txtbox.setGeometry(QtCore.QRect(30, 290, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qty_txtbox.setFont(font)
        self.qty_txtbox.setObjectName("qty_txtbox")
        self.buyPrice_lbl = QtWidgets.QLabel(self.Product_frame)
        self.buyPrice_lbl.setGeometry(QtCore.QRect(30, 330, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.buyPrice_lbl.setFont(font)
        self.buyPrice_lbl.setObjectName("buyPrice_lbl")
        self.buyPrice_txtbox = QtWidgets.QLineEdit(self.Product_frame)
        self.buyPrice_txtbox.setGeometry(QtCore.QRect(30, 350, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buyPrice_txtbox.setFont(font)
        self.buyPrice_txtbox.setObjectName("buyPrice_txtbox")
        self.sellPrice_lbl = QtWidgets.QLabel(self.Product_frame)
        self.sellPrice_lbl.setGeometry(QtCore.QRect(30, 390, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.sellPrice_lbl.setFont(font)
        self.sellPrice_lbl.setStyleSheet("")
        self.sellPrice_lbl.setObjectName("sellPrice_lbl")
        self.sellPrice_txtbox = QtWidgets.QLineEdit(self.Product_frame)
        self.sellPrice_txtbox.setGeometry(QtCore.QRect(30, 410, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sellPrice_txtbox.setFont(font)
        self.sellPrice_txtbox.setObjectName("sellPrice_txtbox")
        self.cat_combobox = QtWidgets.QComboBox(self.Product_frame)
        self.cat_combobox.setGeometry(QtCore.QRect(30, 230, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cat_combobox.setFont(font)
        self.cat_combobox.setObjectName("cat_combobox")
        self.selectlbl = QtWidgets.QLabel(self.Product_frame)
        self.selectlbl.setGeometry(QtCore.QRect(30, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.selectlbl.setFont(font)
        self.selectlbl.setObjectName("selectlbl")
        self.selectcombobox = QtWidgets.QComboBox(self.Product_frame)
        self.selectcombobox.setGeometry(QtCore.QRect(30, 50, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectcombobox.setFont(font)
        self.selectcombobox.setObjectName("selectcombobox")
        self.selectcombobox.addItem("")
        self.selectcombobox.addItem("")
        self.selectcombobox.addItem("")
        self.submitBtn = QtWidgets.QPushButton(self.Product_frame)
        self.submitBtn.setGeometry(QtCore.QRect(380, 460, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.submitBtn.setFont(font)
        self.submitBtn.setStyleSheet("#submitBtn{\n"
"    background-color: rgba(247,170,119,0.8);\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"#submitBtn:hover{\n"
"    background-color: rgb(244,143,77);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px\n"
"}")
        self.submitBtn.setObjectName("submitBtn")
        self.label_3 = QtWidgets.QLabel(self.addproductFrame)
        self.label_3.setGeometry(QtCore.QRect(320, 30, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("    background-color: rgba(247,170,119,0.5);\n"
"    border-radius: 10px;\n"
"color:white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.addproductError_lbl = QtWidgets.QLabel(self.addproductFrame)
        self.addproductError_lbl.setGeometry(QtCore.QRect(300, 630, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addproductError_lbl.setFont(font)
        self.addproductError_lbl.setStyleSheet("color: Green;")
        self.addproductError_lbl.setText("")
        self.addproductError_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.addproductError_lbl.setObjectName("addproductError_lbl")
        self.label = QtWidgets.QLabel(self.addproductFrame)
        self.label.setGeometry(QtCore.QRect(40, 0, 941, 671))
        self.label.setStyleSheet("image: url(:/newPrefix/slide2.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.Product_frame.raise_()
        self.label_3.raise_()
        self.addproductError_lbl.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.SalesFrame = QtWidgets.QFrame(self.tab_5)
        self.SalesFrame.setGeometry(QtCore.QRect(-11, -11, 971, 691))
        self.SalesFrame.setStyleSheet("#SalesFrame{\n"
"background-color: rgb(77,191,191)\n"
"}")
        self.SalesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SalesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SalesFrame.setObjectName("SalesFrame")
        self.label_9 = QtWidgets.QLabel(self.SalesFrame)
        self.label_9.setGeometry(QtCore.QRect(0, 10, 981, 691))
        self.label_9.setStyleSheet("image: url(:/newPrefix/Secret-Solutions-to-Effective-Sales-Conversations-Identified.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.salesserachFrame = QtWidgets.QFrame(self.SalesFrame)
        self.salesserachFrame.setGeometry(QtCore.QRect(40, 80, 891, 51))
        self.salesserachFrame.setStyleSheet("#salesserachFrame{\n"
"background-color: rgba(54,150,150,0.6);\n"
"    border-radius: 10px;\n"
"}")
        self.salesserachFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.salesserachFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.salesserachFrame.setObjectName("salesserachFrame")
        self.searchSalestxtbox = QtWidgets.QLineEdit(self.salesserachFrame)
        self.searchSalestxtbox.setGeometry(QtCore.QRect(10, 10, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchSalestxtbox.setFont(font)
        self.searchSalestxtbox.setStyleSheet("    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;")
        self.searchSalestxtbox.setObjectName("searchSalestxtbox")
        self.sales_search_btn = QtWidgets.QPushButton(self.salesserachFrame)
        self.sales_search_btn.setGeometry(QtCore.QRect(780, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sales_search_btn.setFont(font)
        self.sales_search_btn.setStyleSheet("#sales_search_btn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(49,136,136);\n"
"}\n"
"#sales_search_btn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}")
        self.sales_search_btn.setObjectName("sales_search_btn")
        self.salesSearchCombobox = QtWidgets.QComboBox(self.salesserachFrame)
        self.salesSearchCombobox.setGeometry(QtCore.QRect(580, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.salesSearchCombobox.setFont(font)
        self.salesSearchCombobox.setStyleSheet("    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;")
        self.salesSearchCombobox.setObjectName("salesSearchCombobox")
        self.salesSearchCombobox.addItem("")
        self.salesSearchCombobox.addItem("")
        self.salesSearchCombobox.addItem("")
        self.salesSearchCombobox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.SalesFrame)
        self.label_10.setGeometry(QtCore.QRect(330, 30, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("    background-color: rgba(54,150,150,0.6);\n"
"    border-radius: 10px;\n"
"color:White;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.salestable = QtWidgets.QTableWidget(self.SalesFrame)
        self.salestable.setGeometry(QtCore.QRect(40, 140, 561, 511))
        self.salestable.setStyleSheet("\n"
"    background-color: rgba(54,150,150,0.6);\n"
"    border-radius: 10px;\n"
"color: white;\n"
"")
        self.salestable.setShowGrid(False)
        self.salestable.setRowCount(10)
        self.salestable.setColumnCount(5)
        self.salestable.setObjectName("salestable")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salestable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salestable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salestable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salestable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salestable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.salestable.setItem(1, 0, item)
        self.salestable.horizontalHeader().setVisible(False)
        self.salestable.verticalHeader().setVisible(False)
        self.salesframe2 = QtWidgets.QFrame(self.SalesFrame)
        self.salesframe2.setGeometry(QtCore.QRect(610, 140, 321, 511))
        self.salesframe2.setStyleSheet("#salesframe2{\n"
"    background-color: rgba(54,150,150,0.6);\n"
"    border-radius: 10px;\n"
"}\n"
"#cost_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#total_sales_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white; \n"
"}\n"
"#cost_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#selectcustomercombobox_2{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#customername_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#total_sales_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#profit_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#profit_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#qty_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#qty_txtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#gender_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#gendercombobox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#phone_lbl{\n"
"    background-color: transparent;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"    color: white;\n"
"}\n"
"#phonetxtbox{\n"
"    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;\n"
"}\n"
"#submitcustomer_btn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}\n"
"#submitcustomer_btn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,95,155);\n"
"}")
        self.salesframe2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.salesframe2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.salesframe2.setObjectName("salesframe2")
        self.cost_lbl = QtWidgets.QLabel(self.salesframe2)
        self.cost_lbl.setGeometry(QtCore.QRect(30, 100, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.cost_lbl.setFont(font)
        self.cost_lbl.setStyleSheet("")
        self.cost_lbl.setObjectName("cost_lbl")
        self.cost_txtbox = QtWidgets.QLineEdit(self.salesframe2)
        self.cost_txtbox.setGeometry(QtCore.QRect(30, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cost_txtbox.setFont(font)
        self.cost_txtbox.setStyleSheet("")
        self.cost_txtbox.setReadOnly(True)
        self.cost_txtbox.setObjectName("cost_txtbox")
        self.total_sales_lbl = QtWidgets.QLabel(self.salesframe2)
        self.total_sales_lbl.setGeometry(QtCore.QRect(30, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.total_sales_lbl.setFont(font)
        self.total_sales_lbl.setObjectName("total_sales_lbl")
        self.total_sales_txtbox = QtWidgets.QLineEdit(self.salesframe2)
        self.total_sales_txtbox.setGeometry(QtCore.QRect(30, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total_sales_txtbox.setFont(font)
        self.total_sales_txtbox.setReadOnly(True)
        self.total_sales_txtbox.setObjectName("total_sales_txtbox")
        self.profit_lbl = QtWidgets.QLabel(self.salesframe2)
        self.profit_lbl.setGeometry(QtCore.QRect(30, 220, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.profit_lbl.setFont(font)
        self.profit_lbl.setObjectName("profit_lbl")
        self.profit_txtbox = QtWidgets.QLineEdit(self.salesframe2)
        self.profit_txtbox.setGeometry(QtCore.QRect(30, 240, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.profit_txtbox.setFont(font)
        self.profit_txtbox.setReadOnly(True)
        self.profit_txtbox.setObjectName("profit_txtbox")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.salesDetails_Frame = QtWidgets.QFrame(self.tab_6)
        self.salesDetails_Frame.setGeometry(QtCore.QRect(-10, 0, 971, 711))
        self.salesDetails_Frame.setStyleSheet("#salesDetails_Frame{\n"
"background-color: rgb(75,197,222);\n"
"}")
        self.salesDetails_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.salesDetails_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.salesDetails_Frame.setObjectName("salesDetails_Frame")
        self.salesdetailsFrame = QtWidgets.QFrame(self.salesDetails_Frame)
        self.salesdetailsFrame.setGeometry(QtCore.QRect(40, 70, 901, 51))
        self.salesdetailsFrame.setStyleSheet("#salesdetailsFrame{\n"
"    background-color: rgba(30,142,166,0.5);\n"
"    border-radius: 10px;\n"
"}")
        self.salesdetailsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.salesdetailsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.salesdetailsFrame.setObjectName("salesdetailsFrame")
        self.searchSalestxtbox_2 = QtWidgets.QLineEdit(self.salesdetailsFrame)
        self.searchSalestxtbox_2.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchSalestxtbox_2.setFont(font)
        self.searchSalestxtbox_2.setStyleSheet("    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;")
        self.searchSalestxtbox_2.setObjectName("searchSalestxtbox_2")
        self.salesdetails_search_btn = QtWidgets.QPushButton(self.salesdetailsFrame)
        self.salesdetails_search_btn.setGeometry(QtCore.QRect(780, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.salesdetails_search_btn.setFont(font)
        self.salesdetails_search_btn.setStyleSheet("#salesdetails_search_btn:hover{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"background-color: rgb(49,136,136);\n"
"}\n"
"#salesdetails_search_btn{\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"}")
        self.salesdetails_search_btn.setObjectName("salesdetails_search_btn")
        self.salesSearchCombobox_2 = QtWidgets.QComboBox(self.salesdetailsFrame)
        self.salesSearchCombobox_2.setGeometry(QtCore.QRect(250, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.salesSearchCombobox_2.setFont(font)
        self.salesSearchCombobox_2.setStyleSheet("    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;")
        self.salesSearchCombobox_2.setObjectName("salesSearchCombobox_2")
        self.salesSearchCombobox_2.addItem("")
        self.salesSearchCombobox_2.addItem("")
        self.salesSearchCombobox_2.addItem("")
        self.salesSearchCombobox_2.addItem("")
        self.salesSearchCombobox_2.addItem("")
        self.salesSearchCombobox_2.addItem("")
        self.salesSearchCombobox_2.addItem("")
        self.salesSearchCombobox_2.addItem("")
        self.salesSearchCombobox_2.addItem("")
        self.searchSalestxtbox_3 = QtWidgets.QLineEdit(self.salesdetailsFrame)
        self.searchSalestxtbox_3.setGeometry(QtCore.QRect(410, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchSalestxtbox_3.setFont(font)
        self.searchSalestxtbox_3.setStyleSheet("    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;")
        self.searchSalestxtbox_3.setObjectName("searchSalestxtbox_3")
        self.salesSearchCombobox_3 = QtWidgets.QComboBox(self.salesdetailsFrame)
        self.salesSearchCombobox_3.setGeometry(QtCore.QRect(630, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.salesSearchCombobox_3.setFont(font)
        self.salesSearchCombobox_3.setStyleSheet("    background-color: transparent;\n"
"    border: 5px;\n"
"    border-bottom: 1px solid white;\n"
"    color: white;")
        self.salesSearchCombobox_3.setObjectName("salesSearchCombobox_3")
        self.salesSearchCombobox_3.addItem("")
        self.salesSearchCombobox_3.addItem("")
        self.salesSearchCombobox_3.addItem("")
        self.salesSearchCombobox_3.addItem("")
        self.salesSearchCombobox_3.addItem("")
        self.salesSearchCombobox_3.addItem("")
        self.salesSearchCombobox_3.addItem("")
        self.salesSearchCombobox_3.addItem("")
        self.label_11 = QtWidgets.QLabel(self.salesDetails_Frame)
        self.label_11.setGeometry(QtCore.QRect(330, 20, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("    background-color: rgba(30,142,166,0.5);\n"
"    border-radius: 10px;\n"
"color:White;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.salesDetailsTable = QtWidgets.QTableWidget(self.salesDetails_Frame)
        self.salesDetailsTable.setGeometry(QtCore.QRect(40, 130, 901, 461))
        self.salesDetailsTable.setStyleSheet("\n"
"    background-color: rgba(30,142,166,0.5);\n"
"    border-radius: 10px;\n"
"color: white;\n"
"")
        self.salesDetailsTable.setShowGrid(False)
        self.salesDetailsTable.setRowCount(10)
        self.salesDetailsTable.setColumnCount(9)
        self.salesDetailsTable.setObjectName("salesDetailsTable")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesDetailsTable.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.salesDetailsTable.setItem(1, 0, item)
        self.salesDetailsTable.horizontalHeader().setVisible(False)
        self.salesDetailsTable.verticalHeader().setVisible(False)
        self.totalsalesdetails = QtWidgets.QLabel(self.salesDetails_Frame)
        self.totalsalesdetails.setGeometry(QtCore.QRect(590, 600, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.totalsalesdetails.setFont(font)
        self.totalsalesdetails.setStyleSheet("    background-color: rgba(30,142,166,0.5);\n"
"    border-radius: 10px;\n"
"color:White;")
        self.totalsalesdetails.setText("")
        self.totalsalesdetails.setAlignment(QtCore.Qt.AlignCenter)
        self.totalsalesdetails.setObjectName("totalsalesdetails")
        self.label_12 = QtWidgets.QLabel(self.salesDetails_Frame)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 951, 651))
        self.label_12.setStyleSheet("image: url(:/newPrefix/what-makes-a-good-sales-manager-blog-header-1-650x377.jpg);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_12.raise_()
        self.salesdetailsFrame.raise_()
        self.label_11.raise_()
        self.salesDetailsTable.raise_()
        self.totalsalesdetails.raise_()
        self.tabWidget.addTab(self.tab_6, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Inventory  Management System"))
        __sortingEnabled = self.productTable.isSortingEnabled()
        self.productTable.setSortingEnabled(False)
        item = self.productTable.item(0, 0)
        item.setText(_translate("Dialog", "ID"))
        item = self.productTable.item(0, 1)
        item.setText(_translate("Dialog", "Name"))
        item = self.productTable.item(0, 2)
        item.setText(_translate("Dialog", "Category"))
        item = self.productTable.item(0, 3)
        item.setText(_translate("Dialog", "Quantity"))
        item = self.productTable.item(0, 4)
        item.setText(_translate("Dialog", "Price"))
        self.productTable.setSortingEnabled(__sortingEnabled)
        self.searchtxtbox.setPlaceholderText(_translate("Dialog", "Search here"))
        self.searchBtn.setText(_translate("Dialog", "Search"))
        self.comboBox.setItemText(0, _translate("Dialog", "All"))
        self.comboBox.setItemText(1, _translate("Dialog", "ID"))
        self.comboBox.setItemText(2, _translate("Dialog", "Name"))
        self.comboBox.setItemText(3, _translate("Dialog", "Category"))
        self.comboBox.setItemText(4, _translate("Dialog", "Quantity"))
        self.comboBox.setItemText(5, _translate("Dialog", "Price"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Products"))
        self.label_6.setText(_translate("Dialog", "Manage Cart"))
        self.customerIDlbl.setText(_translate("Dialog", "Customer ID"))
        self.productIDlbl.setText(_translate("Dialog", "Product ID"))
        self.addproductqtyllbl.setText(_translate("Dialog", "Quantity"))
        self.datelbl.setText(_translate("Dialog", "Date"))
        self.addtocartBtn.setText(_translate("Dialog", "Add To Cart"))
        self.buyProductBtn.setText(_translate("Dialog", "Buy"))
        __sortingEnabled = self.cartTable.isSortingEnabled()
        self.cartTable.setSortingEnabled(False)
        item = self.cartTable.item(0, 0)
        item.setText(_translate("Dialog", "Cus ID"))
        item = self.cartTable.item(0, 1)
        item.setText(_translate("Dialog", "Prod ID"))
        item = self.cartTable.item(0, 2)
        item.setText(_translate("Dialog", "Name"))
        item = self.cartTable.item(0, 3)
        item.setText(_translate("Dialog", "Quantity"))
        item = self.cartTable.item(0, 4)
        item.setText(_translate("Dialog", "Price"))
        self.cartTable.setSortingEnabled(__sortingEnabled)
        self.removeproductTxtbox.setPlaceholderText(_translate("Dialog", "Tyoe Here"))
        self.productIDlbl2.setText(_translate("Dialog", "Product ID"))
        self.removeproductBtn.setText(_translate("Dialog", "Remove"))
        self.emptyCartBtn.setText(_translate("Dialog", "Empty"))
        self.label_7.setText(_translate("Dialog", "Cart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Add To Cart"))
        self.customerIDlbl_2.setText(_translate("Dialog", "Customer ID"))
        self.customername_lbl.setText(_translate("Dialog", "Name"))
        self.gender_lbl.setText(_translate("Dialog", "Gender"))
        self.phone_lbl.setText(_translate("Dialog", "Phone Number"))
        self.gendercombobox.setItemText(0, _translate("Dialog", "Male"))
        self.gendercombobox.setItemText(1, _translate("Dialog", "Female"))
        self.selectlbl_2.setText(_translate("Dialog", "Select"))
        self.selectcustomercombobox_2.setItemText(0, _translate("Dialog", "Add"))
        self.selectcustomercombobox_2.setItemText(1, _translate("Dialog", "Update"))
        self.selectcustomercombobox_2.setItemText(2, _translate("Dialog", "Delete"))
        self.submitcustomer_btn.setText(_translate("Dialog", "Submit"))
        self.label_8.setText(_translate("Dialog", "Manage Customer"))
        __sortingEnabled = self.customerTable.isSortingEnabled()
        self.customerTable.setSortingEnabled(False)
        item = self.customerTable.item(0, 0)
        item.setText(_translate("Dialog", "ID"))
        item = self.customerTable.item(0, 1)
        item.setText(_translate("Dialog", "Name"))
        item = self.customerTable.item(0, 2)
        item.setText(_translate("Dialog", "Gender"))
        item = self.customerTable.item(0, 3)
        item.setText(_translate("Dialog", "Phone"))
        self.customerTable.setSortingEnabled(__sortingEnabled)
        self.searchCustomerTxtbox.setPlaceholderText(_translate("Dialog", "Search Here"))
        self.seaarchCustomerBtn.setText(_translate("Dialog", "Search"))
        self.searchCustomerCombobox.setItemText(0, _translate("Dialog", "ID"))
        self.searchCustomerCombobox.setItemText(1, _translate("Dialog", "Name"))
        self.searchCustomerCombobox.setItemText(2, _translate("Dialog", "Gender"))
        self.searchCustomerCombobox.setItemText(3, _translate("Dialog", "Phone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "Manage Customer"))
        __sortingEnabled = self.cat_table.isSortingEnabled()
        self.cat_table.setSortingEnabled(False)
        self.cat_table.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Dialog", "Categories"))
        self.add_combobox.setItemText(0, _translate("Dialog", "Add"))
        self.add_combobox.setItemText(1, _translate("Dialog", "Delete"))
        self.cat_txtbox.setPlaceholderText(_translate("Dialog", "Name"))
        self.add_lbl.setText(_translate("Dialog", "Add/Delete"))
        self.cat_lbl_3.setText(_translate("Dialog", "Category Name"))
        self.searchcategorytxtbox.setPlaceholderText(_translate("Dialog", "Search Here"))
        self.searchcategoryBtn.setText(_translate("Dialog", "Search"))
        self.submitcategorybtn.setText(_translate("Dialog", "Submit"))
        self.manageCatgeorieslbl.setText(_translate("Dialog", "Manage Categories"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Manage Categories"))
        self.ID_lbl.setText(_translate("Dialog", "ID"))
        self.name_lbl.setText(_translate("Dialog", "Name"))
        self.cat_lbl.setText(_translate("Dialog", "Category"))
        self.qty_lbl.setText(_translate("Dialog", "Quantity"))
        self.buyPrice_lbl.setText(_translate("Dialog", "Buying Price"))
        self.sellPrice_lbl.setText(_translate("Dialog", "Selling Price"))
        self.selectlbl.setText(_translate("Dialog", "Select"))
        self.selectcombobox.setItemText(0, _translate("Dialog", "Add"))
        self.selectcombobox.setItemText(1, _translate("Dialog", "Update"))
        self.selectcombobox.setItemText(2, _translate("Dialog", "Delete"))
        self.submitBtn.setText(_translate("Dialog", "Submit"))
        self.label_3.setText(_translate("Dialog", "Manage Products"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Manage Products"))
        self.searchSalestxtbox.setPlaceholderText(_translate("Dialog", "Search Here"))
        self.sales_search_btn.setText(_translate("Dialog", "Search"))
        self.salesSearchCombobox.setItemText(0, _translate("Dialog", "All"))
        self.salesSearchCombobox.setItemText(1, _translate("Dialog", "Order ID"))
        self.salesSearchCombobox.setItemText(2, _translate("Dialog", "Customer ID"))
        self.salesSearchCombobox.setItemText(3, _translate("Dialog", "Date"))
        self.label_10.setText(_translate("Dialog", "Sales"))
        __sortingEnabled = self.salestable.isSortingEnabled()
        self.salestable.setSortingEnabled(False)
        item = self.salestable.item(0, 0)
        item.setText(_translate("Dialog", "Date"))
        item = self.salestable.item(0, 1)
        item.setText(_translate("Dialog", "Order ID"))
        item = self.salestable.item(0, 2)
        item.setText(_translate("Dialog", "Customer ID"))
        item = self.salestable.item(0, 3)
        item.setText(_translate("Dialog", "Cost"))
        item = self.salestable.item(0, 4)
        item.setText(_translate("Dialog", "Bill"))
        self.salestable.setSortingEnabled(__sortingEnabled)
        self.cost_lbl.setText(_translate("Dialog", "Cost"))
        self.total_sales_lbl.setText(_translate("Dialog", "Sales"))
        self.profit_lbl.setText(_translate("Dialog", "Profit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Sales"))
        self.searchSalestxtbox_2.setPlaceholderText(_translate("Dialog", "Search Here"))
        self.salesdetails_search_btn.setText(_translate("Dialog", "Search"))
        self.salesSearchCombobox_2.setItemText(0, _translate("Dialog", "Date"))
        self.salesSearchCombobox_2.setItemText(1, _translate("Dialog", "Order ID"))
        self.salesSearchCombobox_2.setItemText(2, _translate("Dialog", "Customer ID"))
        self.salesSearchCombobox_2.setItemText(3, _translate("Dialog", "Customer Name"))
        self.salesSearchCombobox_2.setItemText(4, _translate("Dialog", "Customer Phone"))
        self.salesSearchCombobox_2.setItemText(5, _translate("Dialog", "Product ID"))
        self.salesSearchCombobox_2.setItemText(6, _translate("Dialog", "Product Name"))
        self.salesSearchCombobox_2.setItemText(7, _translate("Dialog", "Cast"))
        self.salesSearchCombobox_2.setItemText(8, _translate("Dialog", "Price"))
        self.searchSalestxtbox_3.setPlaceholderText(_translate("Dialog", "Search Here"))
        self.salesSearchCombobox_3.setItemText(0, _translate("Dialog", "Date"))
        self.salesSearchCombobox_3.setItemText(1, _translate("Dialog", "Order ID"))
        self.salesSearchCombobox_3.setItemText(2, _translate("Dialog", "Cust ID"))
        self.salesSearchCombobox_3.setItemText(3, _translate("Dialog", "Customer Name"))
        self.salesSearchCombobox_3.setItemText(4, _translate("Dialog", "Customer Phone"))
        self.salesSearchCombobox_3.setItemText(5, _translate("Dialog", "Product ID"))
        self.salesSearchCombobox_3.setItemText(6, _translate("Dialog", "Cost"))
        self.salesSearchCombobox_3.setItemText(7, _translate("Dialog", "Price"))
        self.label_11.setText(_translate("Dialog", "Sales Details"))
        __sortingEnabled = self.salesDetailsTable.isSortingEnabled()
        self.salesDetailsTable.setSortingEnabled(False)
        item = self.salesDetailsTable.item(0, 0)
        item.setText(_translate("Dialog", "Date"))
        item = self.salesDetailsTable.item(0, 1)
        item.setText(_translate("Dialog", "Order ID"))
        item = self.salesDetailsTable.item(0, 2)
        item.setText(_translate("Dialog", "Cust ID"))
        item = self.salesDetailsTable.item(0, 3)
        item.setText(_translate("Dialog", "Cust Name"))
        item = self.salesDetailsTable.item(0, 4)
        item.setText(_translate("Dialog", "Phone"))
        item = self.salesDetailsTable.item(0, 5)
        item.setText(_translate("Dialog", "Product ID"))
        item = self.salesDetailsTable.item(0, 6)
        item.setText(_translate("Dialog", "Prod Name"))
        item = self.salesDetailsTable.item(0, 7)
        item.setText(_translate("Dialog", "Cost"))
        item = self.salesDetailsTable.item(0, 8)
        item.setText(_translate("Dialog", "Price"))
        self.salesDetailsTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Sales Details"))
        
        # Product Form Getting Data from database
        self.getProductData("select ID,Name,Category,Quantity,Selling_price from products")
        
        # Search Product in Product Form
        self.searchBtn.clicked.connect(self.searchProduct)
        
        # Category Form getting Category data from databse
        self.getCategoryData("select * from category")
        
        # Category Form submit Button Onclick function
        self.submitcategorybtn.clicked.connect(self.AddCategoryBtnClick)
        
        # Search Category in Category form
        self.searchcategoryBtn.clicked.connect(self.searchCategory)
        
        # Add Product Form Getting Categories Data from databse
        self.getCategoryDatainCombobox()
        
        # Add Product Form Submit Button OnClick Function
        self.submitBtn.clicked.connect(self.addProductBtnClick)
        
        # Add Customer Form Submit Button OnClick Funxction
        self.submitcustomer_btn.clicked.connect(self.AddCustomerBtn)
        
        # Customer Form getting Customer Data from databse
        self.getCustomerData("select * from customer")
        
        # Search Customer in Customer Form
        self.seaarchCustomerBtn.clicked.connect(self.searchCustomer)
        
        # Setting Current date in Cart Form
        self.datetxtbox.setText(str(date.today()))
        
        # Cart Form ADd to Cart Button OnClick Function
        self.addtocartBtn.clicked.connect(self.cartBtnClick)
        
        # Cart Form Deleting Previous Data from cart
        self.emptyCartBtnClick()
        
        # Getting data from cart just to check for previous values
        self.getCartData("select customerID,productID,productName,Quantity,Selling_Price from cart")
        
        # Cart Form Emtry Cart button to delete All the data from cart
        self.emptyCartBtn.clicked.connect(self.emptyCartBtnClick)
        
        # Cart Form Removing data from Cart in Cart form
        self.removeproductBtn.clicked.connect(self.removeCartBtnClick)
        
        # Cart Form Buy Products Button OnClick Function
        self.buyProductBtn.clicked.connect(self.buyProductCartBtnClick)
        
        # Sales Tab getting data in sales table from database
        self.getSalesData("select order_date,orderID,customerID,buying_price,selling_price from sales")
        
        # Search Sales in Sales Tab
        self.sales_search_btn.clicked.connect(self.searchSales)
        
        #Sales Details Tab gettind Sales_details from database
        self.getSalesDetailsData("select * from sales_details")
        
        
    # Datbase Connection in Constructor to be used throughout the class
    def __init__(self):
        import sqlite3
        self.db = sqlite3.connect("inventory.db")
        self.crr = self.db.cursor()
    
    # Functions For Getting,Updating and Sending Data To Database
    def addProductBtnClick(self):
        selcom = self.selectcombobox.currentText()
        if selcom == "Add":
            selid=self.ID_txtbox.text()
            selname=self.name_txtbox.text()
            selcat=self.cat_combobox.currentText()
            selqua=self.qty_txtbox.text()
            selbuy=self.buyPrice_txtbox.text()
            selse=self.sellPrice_txtbox.text()
            if selname == "" or selcat == "" or selqua == "" or selbuy == "" or selse == "" or selid == "":
                self.addproductError_lbl.setText("Please Provide all the Details")
            else:
                sql="insert into products(ID,Name,Category,Quantity,Buying_price,Selling_price)values('%s','%s','%s','%s','%s','%s')"%(selid,selname,selcat,selqua,selbuy,selse)
                self.crr.execute(sql)
                self.db.commit()
                self.getProductData("select ID,Name,Category,Quantity,Selling_price from products")
                self.ID_txtbox.setText("")
                self.name_txtbox.setText("")
                self.qty_txtbox.setText("")
                self.buyPrice_txtbox.setText("")
                self.sellPrice_txtbox.setText("")
                self.addproductError_lbl.setText("Product Added")
            
        if selcom == "Update":
            pro_id = self.ID_txtbox.text()
            if pro_id != "":
                self.crr.execute("select * from products where ID='%s'"%(pro_id))
                res = self.crr.fetchall()
                if res == []:
                    self.addproductError_lbl.setText("Invalid Product ID")
                else:
                    selname = self.name_txtbox.text()
                    selcat = self.cat_combobox.currentText()
                    selqua = self.qty_txtbox.text()
                    selbuy = self.buyPrice_txtbox.text()
                    selse = self.sellPrice_txtbox.text()
                    if selname == "":
                        selname = res[0][1]
                    if selcat == "":
                        selcat = res[0][2]
                    if selqua == "":
                        selqua = res[0][3]
                    if selbuy == "":
                        selbuy = res[0][4]
                    if selse == "":
                        selse = res[0][5]
                    self.crr.execute("update products set Name='%s',Category='%s',Quantity='%s',Buying_price='%s',Selling_price='%s' where ID='%s'"%(selname,selcat,selqua,selbuy,selse,pro_id))
                    self.db.commit()
                    self.addproductError_lbl.setText("Product Details Updated")
                    self.getProductData("select ID,Name,Category,Quantity,Selling_price from products")
            else:
                self.addproductError_lbl.setText("Please Enter Product ID")
                
        if selcom == "Delete":
            pro_id = self.ID_txtbox.text()
            if pro_id == "":
                self.addproductError_lbl.setText("Please Enter Product ID")
            else:
                self.crr.execute("select ID from products where ID='%s'"%(pro_id))
                res = self.crr.fetchall()
                if res == []:
                    self.addproductError_lbl.setText("Invalid Product ID")
                else:
                    self.crr.execute("Delete from products where ID='%s'"%(pro_id))
                    self.db.commit()
                    self.addproductError_lbl.setText("Product Delete")
                    self.getProductData("select ID,Name,Category,Quantity,Selling_price from products")
    
    def getProductData(self,sql):
        self.crr.execute(sql)
        res = self.crr.fetchall()
        self.productTable.setRowCount(1)
        for row_number in range(len(res)):
            self.productTable.insertRow(row_number+1)
            for column_number in range(len(res[row_number])):
                self.productTable.setItem(row_number+1,column_number,QtWidgets.QTableWidgetItem(str(res[row_number][column_number])))
        
    def searchProduct(self):
        txt = self.searchtxtbox.text()+"%"
        Valcom = self.comboBox.currentText()
        if Valcom == "All":
            sql= "select ID,Name,Category,Quantity,Selling_price from products"
        else:
            sql = "select ID,Name,Category,Quantity,Selling_price from products where %s like '%s'"%(Valcom,txt)
        self.getProductData(sql)
        
    def AddCategoryBtnClick(self):
        ValCom = self.add_combobox.currentText()
        txt = self.cat_txtbox.text()
        if ValCom == "Add" and txt != "":
            self.crr.execute("select * from category where category='%s'"%(txt))
            res = self.crr.fetchall()
            if res == []:
                self.crr.execute("insert into category(category) values('%s')"%(txt))
                self.db.commit()
                self.getCategoryData("select * from category")
                #self.getCategoryDatainCombobox()
        if ValCom == "Delete" and txt != "":
            self.crr.execute("select * from category where category='%s'"%(txt))
            res = self.crr.fetchall()
            if res != []:
                self.crr.execute("delete from category where category='%s'"%(txt))
                self.db.commit()
                self.getCategoryData("select * from category") 
                #self.getCategoryDatainCombobox()
                
    def getCategoryData(self,sql):
        self.crr.execute(sql)
        res = self.crr.fetchall()
        self.cat_table.setRowCount(0)
        for row_number in range(len(res)):
            self.cat_table.insertRow(row_number)
            for column_number in range(len(res[row_number])):
                self.cat_table.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(res[row_number][column_number])))
        
    def searchCategory(self):
        txt = self.searchcategorytxtbox.text()
        if txt == "":
            sql = "select * from category"
        else:
            sql = "select * from category where category like '%s'"%(txt+"%")
        self.getCategoryData(sql)
        
    def getCategoryDatainCombobox(self):
            self.crr.execute("select * from category")
            resitems = self.crr.fetchall()
            lstitems = []
            for i in resitems:
                for j in i:
                    lstitems.append(j)
            self.cat_combobox.addItems(lstitems)
        
    def AddCustomerBtn(self):
        sel = self.selectcustomercombobox_2.currentText()
        if sel == "Add":
            ID = self.customerID_txtbox.text()
            name = self.customernametxtbox.text()
            gender = self.gendercombobox.currentText()
            phone = self.phonetxtbox.text()
            if ID == "" or name == "" or gender == "" or phone == "":
                self.customerError_lbl.setText("Please Provide All the Details")
            else:
                self.crr.execute("insert into customer(ID,Name,Gender,Phone) values('%s','%s','%s','%s')"%(ID,name,gender,phone))
                self.db.commit()
                self.customerError_lbl.setText("Customer Added")
                self.getCustomerData("select * from customer")
                
        if sel == "Update":
            ID = self.customerID_txtbox.text()
            if ID == "":
                self.customerError_lbl.setText("Please Enter ID")
            else:
                self.crr.execute("select * from customer where ID='%s'"%(ID))
                res = self.crr.fetchall()
                if res == []:
                    self.customerError_lbl.setText("Invalid ID")
                else:
                    name = self.customernametxtbox.text()
                    gender = self.gendercombobox.currentText()
                    phone = self.phonetxtbox.text()
                    if name == "":
                        name = res[0][1]
                    if gender == "":
                        gender = res[0][2]
                    if phone == "":
                        phone = res[0][3]
                    self.crr.execute("update customer set Name='%s', Gender='%s', Phone='%s' where ID='%s'"%(name,gender,phone,ID))
                    self.db.commit()
                    self.customerError_lbl.setText("Customer Details Updated")
                    self.getCustomerData("select * from customer")
                    
        if sel == "Delete":
            ID = self.customerID_txtbox.text()
            if ID == "":
                self.customerError_lbl.setText("Please Enter ID")
            else:
                self.crr.execute("select * from customer where ID='%s'"%(ID))
                res = self.crr.fetchall()
                if res == []:
                    self.customerError_lbl.setText("Invalid ID")
                else:
                    self.crr.execute("delete from customer where ID='%s'"%(ID))
                    self.db.commit()
                    self.customerError_lbl.setText("Customer Deleted")
                    self.getCustomerData("select * from customer")
    
    def getCustomerData(self,sql):
        self.crr.execute(sql)
        res = self.crr.fetchall()
        self.customerTable.setRowCount(1)
        for row_number in range(len(res)):
            self.customerTable.insertRow(row_number+1)
            for column_number in range(len(res[row_number])):
                self.customerTable.setItem(row_number+1,column_number,QtWidgets.QTableWidgetItem(str(res[row_number][column_number])))
    
    def searchCustomer(self):
        txt = self.searchCustomerTxtbox.text()+"%"
        ValCom = self.searchCustomerCombobox.currentText()
        if ValCom == "All":
            sql = "select * from customer"
        else:
            sql = "select * from customer where %s like '%s'"%(ValCom,txt)
        self.getCustomerData(sql)
    
    def cartBtnClick(self):
        cust_id = self.customerIDtxtbox.text()
        prod_id = self.productIDtxtbox.text()
        quantity = self.quantitytxtbox.text()
        date = self.datetxtbox.text()
        self.crr.execute("select Name from customer where ID='%s'"%(cust_id))
        res = self.crr.fetchall()
        self.crr.execute("select Name,Selling_price,Buying_price from products where ID='%s'"%(prod_id))
        res1 = self.crr.fetchall()
        if res == [] or res1 == [] or quantity == "":
            if res == [] and res1 == []:
                self.label_14.setText("Invalid Customer and Product ID")
            elif res == []:
                self.label_14.setText("Invalid Customer ID")
            elif res1 == []:
                self.label_14.setText("Invalid Product ID")
            elif quantity == "":
                self.label_14.setText("Please Enter Quantity")
        else:
            prod_name = res1[0][0]
            sel_price = int(res1[0][1])*int(quantity)
            buy_price = int(res1[0][2])*int(quantity)
            order_date = self.datetxtbox.text()
            self.crr.execute("select Quantity from products where ID='%s'"%(prod_id))
            res = self.crr.fetchall()
            if int(quantity) <= int(res[0][0]):
                self.crr.execute("insert into cart(order_date,customerID,productID,productName,Quantity,Selling_Price,Buying_Price) values('%s','%s','%s','%s','%s','%s','%s')"%(order_date,cust_id,prod_id,prod_name,quantity,sel_price,buy_price))
                self.db.commit()
                current_qty = int(res[0][0])-int(quantity)
                self.crr.execute("update products set Quantity='%s' where ID='%s'"%(current_qty,prod_id))
                self.customerIDtxtbox.setReadOnly(True)
                self.productIDtxtbox.setText("")
                self.quantitytxtbox.setText("")
                self.getCartData("select customerID,productID,productName,Quantity,Selling_Price from cart")
                self.cartTotalLbl()
            else:
                self.label_14.setText("We do not have enough Quantity in Stock")

    def getCartData(self,sql):
        self.crr.execute(sql)
        res = self.crr.fetchall()
        self.cartTable.setRowCount(1)
        for row_number in range(len(res)):
            self.cartTable.insertRow(row_number+1)
            for column_number in range(len(res[row_number])):
                self.cartTable.setItem(row_number+1,column_number,QtWidgets.QTableWidgetItem(str(res[row_number][column_number])))

    def emptyCartBtnClick(self):
        self.crr.execute("drop table if exists cart")
        self.db.commit()
        self.crr.execute("""create table if not exists cart(
                            order_date date not null,
                            customerID varchar(50) not null,
                            productID varchar(50) not null,
                            productName varchar(50) not null,
                            Quantity int not null,
                            Selling_Price int not null,
                            Buying_Price int not null)""")
        self.db.commit()
        self.customerIDtxtbox.setReadOnly(False)
        self.getCartData("select customerID,productID,productName,Quantity,Selling_Price from cart")
        self.cartTotalLbl()
        self.db.rollback()
        
    def removeCartBtnClick(self):
        ID = self.removeproductTxtbox.text()
        self.crr.execute("select * from cart where productID='%s'"%(ID))
        res = self.crr.fetchall()
        if res == []:
            self.label_14.setText("Product does not exists in cart")
        else:
            self.crr.execute("delete from cart where productID='%s'"%(ID))
            self.db.commit()
            self.getCartData("select customerID,productID,productName,Quantity,Selling_Price from cart")
            self.removeproductTxtbox.setText("")
            self.cartTotalLbl()
            self.crr.execute("select * from cart")
            res = self.crr.fetchall()
            if res == []:
                self.customerIDtxtbox.setReadOnly(False)
                self.db.rollback()
            
    def cartTotalLbl(self):
        total_sales = 0
        self.crr.execute("select Selling_Price from cart")
        res = self.crr.fetchall()
        for i in res:
            for j in i:
                total_sales += int(j)
                
        self.cart_total_lbl.setText("Rs "+str(total_sales))
        
        total_costofGoods = 0
        self.crr.execute("select Buying_Price from cart")
        res = self.crr.fetchall()
        for i in res:
            for j in i:
                total_costofGoods += int(j)
                
        return [total_sales,total_costofGoods]
        
    def buyProductCartBtnClick(self):
        date = self.datetxtbox.text()
        cust_id = self.customerIDtxtbox.text()
        prod_id = self.productIDtxtbox.text()
        total = self.cartTotalLbl()
        total_sales = total[0]
        total_cost = total[1]
        cus_id = self.customerIDtxtbox.text()
        self.crr.execute("insert into sales(order_date,customerID,buying_price,selling_price) values('%s','%s','%s','%s')"%(date,cus_id,total_cost,total_sales))
        self.db.commit()
        self.crr.execute("select orderID from sales")
        order = self.crr.fetchall()
        if order == []:
            order_id = 1
        else:
            order_id = order[len(order)-1][0]
        self.crr.execute("select * from cart")
        res = self.crr.fetchall()
        self.crr.execute("select Name, Phone from customer where ID='%s'"%(res[0][1]))
        custDetail = self.crr.fetchall()
        print(res)
        for i in range(len(res)):
            self.crr.execute("""insert into sales_details(order_date,orderID,customerID,customerName,customerPhone,productID,
                             productName,buying_price,selling_price) 
                             values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(res[i][0],order_id,res[i][1],custDetail[0][0],custDetail[0][1],res[i][2],res[i][3],res[i][5],res[i][6]))
        
        self.db.commit()
        self.customerIDtxtbox.setReadOnly(False)
        self.customerIDtxtbox.setText("")
        self.emptyCartBtnClick()
        self.cartTotalLbl()
        self.getProductData("select ID,Name,Category,Quantity,Selling_price from products")
        self.getSalesData("select order_date,orderID,customerID,buying_price,selling_price from sales")
        self.getSalesDetailsData("select * from sales_details")
        
    def getSalesData(self,sql):
        self.crr.execute(sql)
        res = self.crr.fetchall()
        self.salestable.setRowCount(1)
        for row_number in range(len(res)):
            self.salestable.insertRow(row_number+1)
            for column_number in range(len(res[row_number])):
                self.salestable.setItem(row_number+1,column_number,QtWidgets.QTableWidgetItem(str(res[row_number][column_number])))
        self.salesProfictCalculate(sql)
        
    def salesProfictCalculate(self,sql):
        self.crr.execute(sql)
        res = self.crr.fetchall()
        cost = 0
        sales = 0
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j == 3:
                    cost += int(res[i][j])
                if j == 4:
                    sales += int(res[i][j])
        self.cost_txtbox.setText("Rs "+str(cost))
        self.total_sales_txtbox.setText("Rs "+str(sales))
        self.profit_txtbox.setText("Rs "+str(sales-cost))
        
    def searchSales(self):
        ValCom = self.salesSearchCombobox.currentText()
        txt = self.searchSalestxtbox.text()
        if ValCom == "Customer ID":
            ValCom = "customerID"
        if ValCom == "Order ID":
            ValCom = "orderID"
        if ValCom == "Date":
            ValCom = "order_date"
            self.searchSalestxtbox.setPlaceholderText("YYYY-MM-DD")
        if ValCom == "All":
            sql = "select order_date,orderID,customerID,buying_price,selling_price from sales"
        else:
            sql = "select order_date,orderID,customerID,buying_price,selling_price from sales where %s='%s'"%(ValCom,txt)
        try:
            self.getSalesData(sql)
        except:
            pass
        
    def getSalesDetailsData(self,sql):
        self.crr.execute(sql)
        res = self.crr.fetchall()
        self.salesDetailsTable.setRowCount(1)
        for row_number in range(len(res)):
            self.salesDetailsTable.insertRow(row_number+1)
            for column_number in range(len(res[row_number])):
                self.salesDetailsTable.setItem(row_number+1,column_number,QtWidgets.QTableWidgetItem(str(res[row_number][column_number])))
        
import projectimages

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

