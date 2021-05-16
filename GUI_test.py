from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import urllib.request
from urllib.request import Request, urlopen
from Corona_Tracker import CoronaTracker
data = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 400)
        MainWindow.setStyleSheet("background-color:#1d1d1d;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 110, 120, 120))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(90, 120, 256, 192))
        self.textBrowser.setStyleSheet(u"color:#fff;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 40, 251, 41))
        self.lineEdit.setStyleSheet(u"color: #fff;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 40, 93, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color:#fff;\n"
"border: 1px solid white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"background-color:rgb(255,220,180)\n"
"}\n"
"QPushButt:Pressed{\n"
"background-color:rgba(255,220,180,160)\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("CoronaTracker GUI")
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.pushButton.clicked.connect(self.go)
       
    def go(self):
        self.textBrowser.setText("")
        #self.load_flag()
        self.load_data()

    def load_flag(self):
        url_flag = data_json['countryInfo']
        flag = (url_flag['flag'])
        print(flag)
        req = Request(flag, headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(data)
        self.label.setPixmap(pixmap)
        self.label.show()


    def load_data(self):
        global data_json
        country = self.lineEdit.text()
        try:
                CoronaTrack = CoronaTracker(country)
                CoronaTrack.loadData()
                data_json = CoronaTrack.data_json
		   
                xx = self.textBrowser.toPlainText()
                for x,y in data_json.items():
                        xx+=str(x)+"-"+str(y)+'\n'
 


                self.textBrowser.setText(xx)
                self.load_flag()
        except :
                self.textBrowser.setText("Could not Found")
                self.label.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
