import sys
import time
import urllib.request
from urllib.parse import urlencode
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from country import country_list
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
import webbrowser
import graphics
import geocoder
import urllib.request

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1050, 650)
        Form.setWindowIcon(QtGui.QIcon(":/icons/icons/covid-19.png"))
        Form.setStyleSheet("background-color:rgba(255,255,255,255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 311, 741))
        self.frame.setStyleSheet("background-color:#2d89ef;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 10, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/covid-19.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#fff;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_covid_info = QtWidgets.QPushButton(self.frame)
        self.btn_covid_info.setGeometry(QtCore.QRect(30, 170, 251, 51))
        self.btn_covid_info.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"QPushButton:hover{\n"
"font: 8.2pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border:1px solid #603cba;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Covid 19_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_covid_info.setIcon(icon)
        self.btn_covid_info.setIconSize(QtCore.QSize(30, 30))
        self.btn_covid_info.setObjectName("btn_covid_info")
        self.btn_comp = QtWidgets.QPushButton(self.frame)
        self.btn_comp.setGeometry(QtCore.QRect(30, 230, 251, 51))
        self.btn_comp.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"QPushButton:hover{\n"
"font: 8.2pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border:1px solid #603cba;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/compare_git_64px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_comp.setIcon(icon1)
        self.btn_comp.setIconSize(QtCore.QSize(25, 25))
        self.btn_comp.setObjectName("btn_comp")
        self.btn_hosp = QtWidgets.QPushButton(self.frame)
        self.btn_hosp.setGeometry(QtCore.QRect(30, 290, 251, 51))
        self.btn_hosp.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"QPushButton:hover{\n"
"font: 8.2pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border:1px solid #603cba;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/hospital_240px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hosp.setIcon(icon2)
        self.btn_hosp.setIconSize(QtCore.QSize(25, 25))
        self.btn_hosp.setObjectName("btn_hosp")
        self.btn_vac_info = QtWidgets.QPushButton(self.frame)
        self.btn_vac_info.setGeometry(QtCore.QRect(30, 350, 251, 51))
        self.btn_vac_info.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"QPushButton:hover{\n"
"font: 8.2pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border:1px solid #603cba;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/insulin_pen_128px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_vac_info.setIcon(icon3)
        self.btn_vac_info.setIconSize(QtCore.QSize(25, 25))
        self.btn_vac_info.setObjectName("btn_vac_info")
        self.btn_about = QtWidgets.QPushButton(self.frame)
        self.btn_about.setGeometry(QtCore.QRect(30, 410, 251, 51))
        self.btn_about.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"QPushButton:hover{\n"
"font: 8.2pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border:1px solid #603cba;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/about_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(icon4)
        self.btn_about.setObjectName("btn_about")
        self.btn_help = QtWidgets.QPushButton(self.frame)
        self.btn_help.setGeometry(QtCore.QRect(30, 470, 251, 51))
        self.btn_help.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"QPushButton:hover{\n"
"font: 8.2pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border:1px solid #603cba;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/help_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(icon5)
        self.btn_help.setObjectName("btn_help")
        self.btn_exit = QtWidgets.QPushButton(self.frame)
        self.btn_exit.setGeometry(QtCore.QRect(30, 530, 251, 51))
        self.btn_exit.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"QPushButton:hover{\n"
"font: 8.2pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border:1px solid #603cba;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/Logout_32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon6)
        self.btn_exit.setObjectName("btn_exit")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 619, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(220, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:None;\n"
"color:#fff;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 630, 311, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:None;\n"
"color:#fff;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(310, 0, 741, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.CovidInformation = QtWidgets.QWidget()
        self.CovidInformation.setObjectName("CovidInformation")
        self.frame_recovered = QtWidgets.QFrame(self.CovidInformation)
        self.frame_recovered.setGeometry(QtCore.QRect(10, 440, 220, 141))
        self.frame_recovered.setStyleSheet("#frame_recovered {\n"
"background-color: rgb(76, 217, 123);\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.frame_recovered.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered.setObjectName("frame_recovered")
        self.recovered = QtWidgets.QLabel(self.frame_recovered)
        self.recovered.setGeometry(QtCore.QRect(20, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.recovered.setFont(font)
        self.recovered.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered.setObjectName("recovered")
        self.recoveredCount = QtWidgets.QLabel(self.frame_recovered)
        self.recoveredCount.setGeometry(QtCore.QRect(10, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.recoveredCount.setFont(font)
        self.recoveredCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.recoveredCount.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recoveredCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.recoveredCount.setObjectName("recoveredCount")
        self.country = QtWidgets.QLineEdit(self.CovidInformation)
        self.country.setGeometry(QtCore.QRect(310, 179, 251, 31))
        self.country.setStyleSheet("border-color: rgb(143, 143, 143);\n"
"color:black;")
        self.country.setObjectName("country")
        self.frame_active = QtWidgets.QFrame(self.CovidInformation)
        self.frame_active.setGeometry(QtCore.QRect(250, 440, 220, 141))
        self.frame_active.setStyleSheet("\n"
"background-color: rgb(76, 181, 255);\n"
"    border-radius: 20px;")
        self.frame_active.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_active.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_active.setObjectName("frame_active")
        self.active = QtWidgets.QLabel(self.frame_active)
        self.active.setGeometry(QtCore.QRect(20, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.active.setFont(font)
        self.active.setStyleSheet("color: rgb(255, 255, 255);")
        self.active.setAlignment(QtCore.Qt.AlignCenter)
        self.active.setObjectName("active")
        self.activeCount = QtWidgets.QLabel(self.frame_active)
        self.activeCount.setGeometry(QtCore.QRect(10, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.activeCount.setFont(font)
        self.activeCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.activeCount.setStyleSheet("color: rgb(255, 255, 255);")
        self.activeCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.activeCount.setObjectName("activeCount")
        self.frame_critical = QtWidgets.QFrame(self.CovidInformation)
        self.frame_critical.setGeometry(QtCore.QRect(491, 440, 220, 141))
        self.frame_critical.setStyleSheet("background-color: rgb(144, 89, 255);\n"
"    border-radius: 20px;")
        self.frame_critical.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_critical.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_critical.setObjectName("frame_critical")
        self.critical = QtWidgets.QLabel(self.frame_critical)
        self.critical.setGeometry(QtCore.QRect(20, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.critical.setFont(font)
        self.critical.setStyleSheet("color: rgb(255, 255, 255);")
        self.critical.setAlignment(QtCore.Qt.AlignCenter)
        self.critical.setObjectName("critical")
        self.criticalCount = QtWidgets.QLabel(self.frame_critical)
        self.criticalCount.setGeometry(QtCore.QRect(10, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.criticalCount.setFont(font)
        self.criticalCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.criticalCount.setStyleSheet("color: rgb(255, 255, 255);")
        self.criticalCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.criticalCount.setObjectName("criticalCount")
        self.selectCountry = QtWidgets.QLabel(self.CovidInformation)
        self.selectCountry.setGeometry(QtCore.QRect(310, 150, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setItalic(False)
        self.selectCountry.setFont(font)
        self.selectCountry.setStyleSheet("background:None;\n"
"color:#2d89ef;")
        self.selectCountry.setObjectName("selectCountry")
        self.frame_affected = QtWidgets.QFrame(self.CovidInformation)
        self.frame_affected.setGeometry(QtCore.QRect(10, 280, 330, 141))
        self.frame_affected.setStyleSheet("#frame_affected {\n"
"    background-color: #FFB259;\n"
"    border-radius: 20px;\n"
"}")
        self.frame_affected.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_affected.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_affected.setObjectName("frame_affected")
        self.confirmed = QtWidgets.QLabel(self.frame_affected)
        self.confirmed.setGeometry(QtCore.QRect(20, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.confirmed.setFont(font)
        self.confirmed.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.confirmed.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmed.setObjectName("confirmed")
        self.confirmedCount = QtWidgets.QLabel(self.frame_affected)
        self.confirmedCount.setGeometry(QtCore.QRect(20, 80, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.confirmedCount.setFont(font)
        self.confirmedCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.confirmedCount.setStyleSheet("background:None;\n"
"color: rgb(255, 255, 255);")
        self.confirmedCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.confirmedCount.setObjectName("confirmedCount")
        self.countryFlag = QtWidgets.QLabel(self.CovidInformation)
        self.countryFlag.setGeometry(QtCore.QRect(40, 120, 250, 141))
        self.countryFlag.setStyleSheet("background:none;\n"
"border:1px solid red;\n"
"")
        self.countryFlag.setText("")
        self.countryFlag.setScaledContents(True)
        self.countryFlag.setObjectName("countryFlag")
        self.lastUpdated = QtWidgets.QLabel(self.CovidInformation)
        self.lastUpdated.setGeometry(QtCore.QRect(310, 210, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(8)
        font.setItalic(False)
        font.setKerning(True)
        self.lastUpdated.setFont(font)
        self.lastUpdated.setStyleSheet("color: rgb(143, 143, 143);")
        self.lastUpdated.setObjectName("lastUpdated")
        self.frame_deaths = QtWidgets.QFrame(self.CovidInformation)
        self.frame_deaths.setGeometry(QtCore.QRect(380, 280, 330, 141))
        self.frame_deaths.setStyleSheet("background-color: rgb(255, 89, 89);\n"
"    border-radius: 20px;")
        self.frame_deaths.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_deaths.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_deaths.setObjectName("frame_deaths")
        self.deaths = QtWidgets.QLabel(self.frame_deaths)
        self.deaths.setGeometry(QtCore.QRect(20, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.deaths.setFont(font)
        self.deaths.setStyleSheet("color: rgb(255, 255, 255);")
        self.deaths.setAlignment(QtCore.Qt.AlignCenter)
        self.deaths.setObjectName("deaths")
        self.deathsCount = QtWidgets.QLabel(self.frame_deaths)
        self.deathsCount.setGeometry(QtCore.QRect(20, 80, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.deathsCount.setFont(font)
        self.deathsCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deathsCount.setStyleSheet("color: rgb(255, 255, 255);")
        self.deathsCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.deathsCount.setObjectName("deathsCount")
        self.btn_covid_info_2 = QtWidgets.QPushButton(self.CovidInformation)
        self.btn_covid_info_2.setGeometry(QtCore.QRect(10, 20, 721, 41))
        self.btn_covid_info_2.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"")
        self.btn_covid_info_2.setIcon(icon)
        self.btn_covid_info_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_covid_info_2.setObjectName("btn_covid_info_2")
        self.stackedWidget.addWidget(self.CovidInformation)
        self.CovidInfoComparator = QtWidgets.QWidget()
        self.CovidInfoComparator.setObjectName("CovidInfoComparator")
        self.country_1 = QtWidgets.QLineEdit(self.CovidInfoComparator)
        self.country_1.setGeometry(QtCore.QRect(30, 210, 221, 31))
        self.country_1.setStyleSheet("border-color: rgb(143, 143, 143);\n"
"color:black;")
        self.country_1.setObjectName("country_1")
        self.btn_covid_info_3 = QtWidgets.QPushButton(self.CovidInfoComparator)
        self.btn_covid_info_3.setGeometry(QtCore.QRect(10, 20, 721, 41))
        self.btn_covid_info_3.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"")
        self.btn_covid_info_3.setIcon(icon1)
        self.btn_covid_info_3.setIconSize(QtCore.QSize(30, 30))
        self.btn_covid_info_3.setObjectName("btn_covid_info_3")
        self.countryFlag_1 = QtWidgets.QLabel(self.CovidInfoComparator)
        self.countryFlag_1.setGeometry(QtCore.QRect(40, 70, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.countryFlag_1.setFont(font)
        self.countryFlag_1.setStyleSheet("background:none;\n"
"border:1px solid red;\n"
"")
        self.countryFlag_1.setText("")
        self.countryFlag_1.setPixmap(QtGui.QPixmap("../../../.designer/COVID DASHBOARD[UPLOADED]/images/custom – 1.jpg"))
        self.countryFlag_1.setScaledContents(True)
        self.countryFlag_1.setObjectName("countryFlag_1")
        self.selectCountry_2 = QtWidgets.QLabel(self.CovidInfoComparator)
        self.selectCountry_2.setGeometry(QtCore.QRect(70, 170, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setItalic(False)
        self.selectCountry_2.setFont(font)
        self.selectCountry_2.setStyleSheet("background:None;\n"
"color:#2d89ef;")
        self.selectCountry_2.setObjectName("selectCountry_2")
        self.frame_recovered_3 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_3.setGeometry(QtCore.QRect(30, 250, 220, 71))
        self.frame_recovered_3.setStyleSheet("\n"
"    background-color: #FFB259;\n"
"    border-radius: 20px;\n"
"")
        self.frame_recovered_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_3.setObjectName("frame_recovered_3")
        self.recovered_4 = QtWidgets.QLabel(self.frame_recovered_3)
        self.recovered_4.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_4.setFont(font)
        self.recovered_4.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_4.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_4.setObjectName("recovered_4")
        self.confirm1 = QtWidgets.QLabel(self.frame_recovered_3)
        self.confirm1.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.confirm1.setFont(font)
        self.confirm1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.confirm1.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.confirm1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.confirm1.setObjectName("confirm1")
        self.frame_recovered_4 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_4.setGeometry(QtCore.QRect(30, 330, 220, 71))
        self.frame_recovered_4.setStyleSheet("\n"
"background-color: rgb(76, 217, 123);\n"
"    border-radius: 20px;\n"
"\n"
"")
        self.frame_recovered_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_4.setObjectName("frame_recovered_4")
        self.recovered_5 = QtWidgets.QLabel(self.frame_recovered_4)
        self.recovered_5.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_5.setFont(font)
        self.recovered_5.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_5.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_5.setObjectName("recovered_5")
        self.recover1 = QtWidgets.QLabel(self.frame_recovered_4)
        self.recover1.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.recover1.setFont(font)
        self.recover1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.recover1.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recover1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.recover1.setObjectName("recover1")
        self.frame_recovered_5 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_5.setGeometry(QtCore.QRect(30, 410, 220, 71))
        self.frame_recovered_5.setStyleSheet("background-color: rgb(255, 89, 89);\n"
"    border-radius: 20px;")
        self.frame_recovered_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_5.setObjectName("frame_recovered_5")
        self.recovered_6 = QtWidgets.QLabel(self.frame_recovered_5)
        self.recovered_6.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_6.setFont(font)
        self.recovered_6.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_6.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_6.setObjectName("recovered_6")
        self.deaths1 = QtWidgets.QLabel(self.frame_recovered_5)
        self.deaths1.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.deaths1.setFont(font)
        self.deaths1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deaths1.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.deaths1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.deaths1.setObjectName("deaths1")
        self.frame_recovered_6 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_6.setGeometry(QtCore.QRect(30, 490, 220, 71))
        self.frame_recovered_6.setStyleSheet("\n"
"background-color: rgb(76, 181, 255);\n"
"    border-radius: 20px;")
        self.frame_recovered_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_6.setObjectName("frame_recovered_6")
        self.recovered_7 = QtWidgets.QLabel(self.frame_recovered_6)
        self.recovered_7.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_7.setFont(font)
        self.recovered_7.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_7.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_7.setObjectName("recovered_7")
        self.active1 = QtWidgets.QLabel(self.frame_recovered_6)
        self.active1.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.active1.setFont(font)
        self.active1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.active1.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.active1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.active1.setObjectName("active1")
        self.frame_recovered_7 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_7.setGeometry(QtCore.QRect(30, 570, 220, 71))
        self.frame_recovered_7.setStyleSheet("background-color: rgb(144, 89, 255);\n"
"    border-radius: 20px;")
        self.frame_recovered_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_7.setObjectName("frame_recovered_7")
        self.recovered_8 = QtWidgets.QLabel(self.frame_recovered_7)
        self.recovered_8.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_8.setFont(font)
        self.recovered_8.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_8.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_8.setObjectName("recovered_8")
        self.critical1 = QtWidgets.QLabel(self.frame_recovered_7)
        self.critical1.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.critical1.setFont(font)
        self.critical1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.critical1.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.critical1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.critical1.setObjectName("critical1")
        self.frame_recovered_8 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_8.setGeometry(QtCore.QRect(500, 570, 220, 71))
        self.frame_recovered_8.setStyleSheet("background-color: rgb(144, 89, 255);\n"
"    border-radius: 20px;")
        self.frame_recovered_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_8.setObjectName("frame_recovered_8")
        self.recovered_9 = QtWidgets.QLabel(self.frame_recovered_8)
        self.recovered_9.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_9.setFont(font)
        self.recovered_9.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_9.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_9.setObjectName("recovered_9")
        self.critical2 = QtWidgets.QLabel(self.frame_recovered_8)
        self.critical2.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.critical2.setFont(font)
        self.critical2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.critical2.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.critical2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.critical2.setObjectName("critical2")
        self.frame_recovered_9 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_9.setGeometry(QtCore.QRect(500, 330, 220, 71))
        self.frame_recovered_9.setStyleSheet("\n"
"background-color: rgb(76, 217, 123);\n"
"    border-radius: 20px;\n"
"\n"
"")
        self.frame_recovered_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_9.setObjectName("frame_recovered_9")
        self.recovered_10 = QtWidgets.QLabel(self.frame_recovered_9)
        self.recovered_10.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_10.setFont(font)
        self.recovered_10.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_10.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_10.setObjectName("recovered_10")
        self.recover2 = QtWidgets.QLabel(self.frame_recovered_9)
        self.recover2.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.recover2.setFont(font)
        self.recover2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.recover2.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recover2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.recover2.setObjectName("recover2")
        self.countryFlag_2 = QtWidgets.QLabel(self.CovidInfoComparator)
        self.countryFlag_2.setGeometry(QtCore.QRect(510, 70, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.countryFlag_2.setFont(font)
        self.countryFlag_2.setStyleSheet("background:none;\n"
"border:1px solid red;\n"
"")
        self.countryFlag_2.setText("")
        self.countryFlag_2.setPixmap(QtGui.QPixmap("../../../.designer/COVID DASHBOARD[UPLOADED]/images/custom – 1.jpg"))
        self.countryFlag_2.setScaledContents(True)
        self.countryFlag_2.setObjectName("countryFlag_2")
        self.frame_recovered_10 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_10.setGeometry(QtCore.QRect(500, 250, 220, 71))
        self.frame_recovered_10.setStyleSheet("\n"
"    background-color: #FFB259;\n"
"    border-radius: 20px;\n"
"")
        self.frame_recovered_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_10.setObjectName("frame_recovered_10")
        self.recovered_11 = QtWidgets.QLabel(self.frame_recovered_10)
        self.recovered_11.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_11.setFont(font)
        self.recovered_11.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_11.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_11.setObjectName("recovered_11")
        self.confirm2 = QtWidgets.QLabel(self.frame_recovered_10)
        self.confirm2.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.confirm2.setFont(font)
        self.confirm2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.confirm2.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.confirm2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.confirm2.setObjectName("confirm2")
        self.country_2 = QtWidgets.QLineEdit(self.CovidInfoComparator)
        self.country_2.setGeometry(QtCore.QRect(500, 210, 221, 31))
        self.country_2.setStyleSheet("border-color: rgb(143, 143, 143);\n"
"color:black;")
        self.country_2.setObjectName("country_2")
        self.frame_recovered_11 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_11.setGeometry(QtCore.QRect(500, 410, 220, 71))
        self.frame_recovered_11.setStyleSheet("background-color: rgb(255, 89, 89);\n"
"    border-radius: 20px;")
        self.frame_recovered_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_11.setObjectName("frame_recovered_11")
        self.recovered_12 = QtWidgets.QLabel(self.frame_recovered_11)
        self.recovered_12.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_12.setFont(font)
        self.recovered_12.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_12.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_12.setObjectName("recovered_12")
        self.deaths2 = QtWidgets.QLabel(self.frame_recovered_11)
        self.deaths2.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.deaths2.setFont(font)
        self.deaths2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.deaths2.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.deaths2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.deaths2.setObjectName("deaths2")
        self.selectCountry_3 = QtWidgets.QLabel(self.CovidInfoComparator)
        self.selectCountry_3.setGeometry(QtCore.QRect(540, 170, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setItalic(False)
        self.selectCountry_3.setFont(font)
        self.selectCountry_3.setStyleSheet("background:None;\n"
"color:#2d89ef;")
        self.selectCountry_3.setObjectName("selectCountry_3")
        self.frame_recovered_12 = QtWidgets.QFrame(self.CovidInfoComparator)
        self.frame_recovered_12.setGeometry(QtCore.QRect(500, 490, 220, 71))
        self.frame_recovered_12.setStyleSheet("\n"
"background-color: rgb(76, 181, 255);\n"
"    border-radius: 20px;")
        self.frame_recovered_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recovered_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recovered_12.setObjectName("frame_recovered_12")
        self.recovered_13 = QtWidgets.QLabel(self.frame_recovered_12)
        self.recovered_13.setGeometry(QtCore.QRect(20, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recovered_13.setFont(font)
        self.recovered_13.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.recovered_13.setAlignment(QtCore.Qt.AlignCenter)
        self.recovered_13.setObjectName("recovered_13")
        self.active2 = QtWidgets.QLabel(self.frame_recovered_12)
        self.active2.setGeometry(QtCore.QRect(10, 40, 201, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.active2.setFont(font)
        self.active2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.active2.setStyleSheet("background:none;\n"
"color: rgb(255, 255, 255);")
        self.active2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.active2.setObjectName("active2")
        self.btn_compare = QtWidgets.QPushButton(self.CovidInfoComparator)
        self.btn_compare.setGeometry(QtCore.QRect(270, 110, 201, 51))
        self.btn_compare.setStyleSheet("QPushButton {\n"
"    color:#fff;\n"
"    border: none;\n"
"    background-color: rgba(13, 9, 36,100);\n"
"    border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(13, 9, 36,150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(13, 9, 36,100);\n"
"}")
        self.btn_compare.setIcon(icon1)
        self.btn_compare.setIconSize(QtCore.QSize(25, 25))
        self.btn_compare.setObjectName("btn_compare")
        self.confirm_ = QtWidgets.QLabel(self.CovidInfoComparator)
        self.confirm_.setGeometry(QtCore.QRect(280, 260, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_.setFont(font)
        self.confirm_.setStyleSheet("background:none;\n"
"color:black;")
        self.confirm_.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_.setObjectName("confirm_")
        self.recover_ = QtWidgets.QLabel(self.CovidInfoComparator)
        self.recover_.setGeometry(QtCore.QRect(280, 340, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.recover_.setFont(font)
        self.recover_.setStyleSheet("background:none;\n"
"color:black;")
        self.recover_.setAlignment(QtCore.Qt.AlignCenter)
        self.recover_.setObjectName("recover_")
        self.deaths_ = QtWidgets.QLabel(self.CovidInfoComparator)
        self.deaths_.setGeometry(QtCore.QRect(280, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.deaths_.setFont(font)
        self.deaths_.setStyleSheet("background:none;\n"
"color:black;")
        self.deaths_.setAlignment(QtCore.Qt.AlignCenter)
        self.deaths_.setObjectName("deaths_")
        self.active_ = QtWidgets.QLabel(self.CovidInfoComparator)
        self.active_.setGeometry(QtCore.QRect(280, 500, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.active_.setFont(font)
        self.active_.setStyleSheet("background:none;\n"
"color:black;")
        self.active_.setAlignment(QtCore.Qt.AlignCenter)
        self.active_.setObjectName("active_")
        self.critical_ = QtWidgets.QLabel(self.CovidInfoComparator)
        self.critical_.setGeometry(QtCore.QRect(280, 580, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.critical_.setFont(font)
        self.critical_.setStyleSheet("background:none;\n"
"color:black;")
        self.critical_.setAlignment(QtCore.Qt.AlignCenter)
        self.critical_.setObjectName("critical_")
        self.stackedWidget.addWidget(self.CovidInfoComparator)
        self.NearestHospital = QtWidgets.QWidget()
        self.NearestHospital.setObjectName("NearestHospital")
        self.btn_covid_info_4 = QtWidgets.QPushButton(self.NearestHospital)
        self.btn_covid_info_4.setGeometry(QtCore.QRect(10, 20, 721, 41))
        self.btn_covid_info_4.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"")
        self.btn_covid_info_4.setIcon(icon2)
        self.btn_covid_info_4.setIconSize(QtCore.QSize(30, 30))
        self.btn_covid_info_4.setObjectName("btn_covid_info_4")

        self.frame_2 = QFrame(self.NearestHospital)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 70, 721, 531))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.WebHospital = QWebEngineView(self.frame_2)
        self.WebHospital.setGeometry(QRect(0, 0, 720, 520))
        self.WebHospital.page().profile().setHttpUserAgent(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    )
        self.WebHospital.setUrl(QUrl('https://maps.google.com/'))
 

        self.btnFind = QtWidgets.QPushButton(self.NearestHospital)
        self.btnFind.setGeometry(QtCore.QRect(150, 600, 201, 41))
        self.btnFind.setStyleSheet("QPushButton {\n"
"    color:#fff;\n"
"    border: none;\n"
"    background-color: rgba(13, 9, 36,100);\n"
"    border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(13, 9, 36,150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(13, 9, 36,100);\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/find_and_replace_52px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnFind.setIcon(icon7)
        self.btnFind.setIconSize(QtCore.QSize(25, 25))
        self.btnFind.setObjectName("btnFind")
        self.btnEmergency = QtWidgets.QPushButton(self.NearestHospital)
        self.btnEmergency.setGeometry(QtCore.QRect(380, 600, 201, 41))
        self.btnEmergency.setStyleSheet("QPushButton {\n"
"    color:#fff;\n"
"    border: none;\n"
"    background-color: rgba(13, 9, 36,100);\n"
"    border-radius: 18;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(13, 9, 36,150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(13, 9, 36,100);\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/ambulance_64px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEmergency.setIcon(icon8)
        self.btnEmergency.setIconSize(QtCore.QSize(25, 25))
        self.btnEmergency.setObjectName("btnEmergency")
        self.stackedWidget.addWidget(self.NearestHospital)
        self.VaccineInformation = QtWidgets.QWidget()
        self.VaccineInformation.setObjectName("VaccineInformation")
        self.btn_covid_info_5 = QtWidgets.QPushButton(self.VaccineInformation)
        self.btn_covid_info_5.setGeometry(QtCore.QRect(10, 20, 721, 41))
        self.btn_covid_info_5.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"")
        self.btn_covid_info_5.setIcon(icon3)
        self.btn_covid_info_5.setIconSize(QtCore.QSize(30, 30))
        self.btn_covid_info_5.setObjectName("btn_covid_info_5")
        self.frame_3 = QFrame(self.VaccineInformation)
        self.frame_3.setObjectName(u"frame_2")
        self.frame_3.setGeometry(QRect(10, 70, 721, 531))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.WebVaccine = QWebEngineView(self.frame_3)
        self.WebVaccine.setGeometry(QRect(0, 0, 720, 520))
        self.WebVaccine.page().profile().setHttpUserAgent(
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    )
        self.WebVaccine.setUrl(QUrl('https://surokkha.gov.bd/'))
        self.stackedWidget.addWidget(self.VaccineInformation)
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.btn_covid_info_6 = QtWidgets.QPushButton(self.About)
        self.btn_covid_info_6.setGeometry(QtCore.QRect(10, 20, 721, 41))
        self.btn_covid_info_6.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"")
        self.btn_covid_info_6.setIcon(icon4)
        self.btn_covid_info_6.setIconSize(QtCore.QSize(30, 30))
        self.btn_covid_info_6.setObjectName("btn_covid_info_6")
        self.profile_info_1 = QLabel(self.About)
        self.profile_info_1.setObjectName(u"profile_info_1")
        self.profile_info_1.setGeometry(QRect(30, 280, 241, 51))
        font12 = QFont()
        font12.setPointSize(10)
        self.profile_info_1.setFont(font12)
        self.profile_info_1.setStyleSheet(u"color:black;")
        self.profile_info_1.setAlignment(Qt.AlignCenter)


        self.profile_info_2 = QLabel(self.About)
        self.profile_info_2.setObjectName(u"profile_info_2")
        self.profile_info_2.setGeometry(QRect(150, 280, 421, 131))
        self.profile_info_2.setFont(font12)
        self.profile_info_2.setStyleSheet(u"color:black;")
        self.profile_info_2.setAlignment(Qt.AlignCenter)

        self.profile_info_3 = QLabel(self.About)
        self.profile_info_3.setObjectName(u"profile_info_3")
        self.profile_info_3.setGeometry(QRect(480, 280, 211, 51))
        self.profile_info_3.setFont(font12)
        self.profile_info_3.setStyleSheet(u"color:black;")
        self.profile_info_3.setAlignment(Qt.AlignCenter)

        self.profile_info_4 = QLabel(self.About)
        self.profile_info_4.setObjectName(u"profile_info_4")
        self.profile_info_4.setGeometry(QRect(150, 530, 211, 51))
        self.profile_info_4.setFont(font12)
        self.profile_info_4.setStyleSheet(u"color:black;")
        self.profile_info_4.setAlignment(Qt.AlignCenter)
 
        self.profile_info_5 = QLabel(self.About)
        self.profile_info_5.setObjectName(u"profile_info_5")
        self.profile_info_5.setGeometry(QRect(370, 530, 211, 51))
        self.profile_info_5.setFont(font12)
        self.profile_info_5.setStyleSheet(u"color:black;")
        self.profile_info_5.setAlignment(Qt.AlignCenter)
        self.profile_info_6 = QLabel(self.About)
        self.profile_info_6.setObjectName(u"profile_info_6")
        self.profile_info_6.setGeometry(QRect(250, 620, 111, 21))
        font13 = QFont()
        font13.setPointSize(9)
        self.profile_info_6.setFont(font13)
        self.profile_info_6.setStyleSheet(u"color:black;")
        self.profile_info_6.setAlignment(Qt.AlignCenter)
        self.profile_6 = QLabel(self.About)
        self.profile_6.setObjectName(u"profile_6")
        self.profile_6.setGeometry(QRect(350, 620, 21, 21))
        self.profile_6.setPixmap(QPixmap(u":/icons/icons/love_96px.png"))
        self.profile_6.setScaledContents(True)
        self.profile_info_7 = QLabel(self.About)
        self.profile_info_7.setObjectName(u"profile_info_7")
        self.profile_info_7.setGeometry(QRect(370, 620, 111, 21))
        self.profile_info_7.setFont(font13)
        self.profile_info_7.setStyleSheet(u"color:black;")
        self.profile_info_7.setAlignment(Qt.AlignCenter)
        self.line_2 = QtWidgets.QFrame(self.About)
        self.line_2.setGeometry(QtCore.QRect(210, 620, 311, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.stackedWidget.addWidget(self.About)
        self.Help = QtWidgets.QWidget()
        self.Help.setObjectName("Help")
        self.btn_covid_info_7 = QtWidgets.QPushButton(self.Help)
        self.btn_covid_info_7.setGeometry(QtCore.QRect(10, 20, 721, 41))
        self.btn_covid_info_7.setStyleSheet("QPushButton{\n"

"text-align:center;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border:1px solid #99b433;\n"
"background-color:#eff4ff;\n"
"color:#9f00a7;\n"
"}\n"
"")
        self.btn_covid_info_7.setIcon(icon5)
        self.btn_covid_info_7.setIconSize(QtCore.QSize(30, 30))
        self.btn_covid_info_7.setObjectName("btn_covid_info_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.Help)
        self.textBrowser.setGeometry(QtCore.QRect(20, 80, 701, 561))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.Help)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("COVIDINFO v1.0")
        self.label_2.setText(_translate("Form", "COVIDINFO "))
        self.btn_covid_info.setText(_translate("Form", "COVID INFORMATION"))
        self.btn_comp.setText(_translate("Form", "COVID INFO COMPARATOR"))
        self.btn_hosp.setText(_translate("Form", "NEAREST HOSPITAL"))
        self.btn_vac_info.setText(_translate("Form", "VACCINE INFORMATION"))
        self.btn_about.setText(_translate("Form", "ABOUT"))
        self.btn_help.setText(_translate("Form", "HELP"))
        self.btn_exit.setText(_translate("Form", "EXIT"))
        self.label_3.setText(_translate("Form", "v1.0"))
        self.label_4.setText(_translate("Form", "Copyright (C) 2022, SIHAB SAHARIAR"))
        self.recovered.setText(_translate("Form", "Recovered"))
        self.recoveredCount.setText(_translate("Form", "0"))
        self.active.setText(_translate("Form", "Active"))
        self.activeCount.setText(_translate("Form", "0"))
        self.critical.setText(_translate("Form", "Critical"))
        self.criticalCount.setText(_translate("Form", "0"))
        self.selectCountry.setText(_translate("Form", "Search Country :"))
        self.confirmed.setText(_translate("Form", "Confirmed"))
        self.confirmedCount.setText(_translate("Form", "0"))
        self.lastUpdated.setText(_translate("Form", "last updated: 08-April-2022"))
        self.deaths.setText(_translate("Form", "Deaths"))
        self.deathsCount.setText(_translate("Form", "0"))
        self.btn_covid_info_2.setText(_translate("Form", "COVID INFORMATION"))
        self.btn_covid_info_3.setText(_translate("Form", "COVID INFO COMPARATOR"))
        self.selectCountry_2.setText(_translate("Form", "Search Country :"))
        self.recovered_4.setText(_translate("Form", "Confirmed"))
        self.confirm1.setText(_translate("Form", "0"))
        self.recovered_5.setText(_translate("Form", "Recovered"))
        self.recover1.setText(_translate("Form", "0"))
        self.recovered_6.setText(_translate("Form", "Deaths"))
        self.deaths1.setText(_translate("Form", "0"))
        self.recovered_7.setText(_translate("Form", "Active"))
        self.active1.setText(_translate("Form", "0"))
        self.recovered_8.setText(_translate("Form", "Critical"))
        self.critical1.setText(_translate("Form", "0"))
        self.recovered_9.setText(_translate("Form", "Critical"))
        self.critical2.setText(_translate("Form", "0"))
        self.recovered_10.setText(_translate("Form", "Recovered"))
        self.recover2.setText(_translate("Form", "0"))
        self.recovered_11.setText(_translate("Form", "Confirmed"))
        self.confirm2.setText(_translate("Form", "0"))
        self.recovered_12.setText(_translate("Form", "Deaths"))
        self.deaths2.setText(_translate("Form", "0"))
        self.selectCountry_3.setText(_translate("Form", "Search Country :"))
        self.recovered_13.setText(_translate("Form", "Active"))
        self.active2.setText(_translate("Form", "0"))
        self.btn_compare.setText(_translate("Form", "COMPARE"))
        self.confirm_.setText(_translate("Form", "?"))
        self.recover_.setText(_translate("Form", "?"))
        self.deaths_.setText(_translate("Form", "?"))
        self.active_.setText(_translate("Form", "?"))
        self.critical_.setText(_translate("Form", "?"))
        self.btn_covid_info_4.setText(_translate("Form", "NEAREST HOSPITAL"))
        self.btnFind.setText(_translate("Form", "FIND OUT"))
        self.btnEmergency.setText(_translate("Form", "EMERGENCY AMBULANCE"))
        self.btn_covid_info_5.setText(_translate("Form", "VACCINE INFORMATION"))
        self.btn_covid_info_6.setText(_translate("Form", "ABOUT"))
       
     
        self.profile_info_2.setText(QCoreApplication.translate("Form", u"Sihab Sahariar\n"
"Undergrad Student\n""Computer Science & Engineering | BRAC UNIVERSITY", None))
     
        
        self.profile_info_6.setText(_translate("Form", "MADE WITH"))
        self.profile_info_7.setText(_translate("Form", "OPENSOURCE"))
        self.btn_covid_info_7.setText(_translate("Form", "HELP"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">How to use this software?</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">About COVIDINFO v1.0 : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">COVIDINFO v1.0 is the beta version of this software. It was very difficult time for us during pandemic. We fought a lot to deal with this. To stay safe and protective it\'s very important to keep track of current COVID situation. Here is the solution to deal with it. In our software we have features like -</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. Real time update of COVID Information.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. Comparision of Covid Situation between two countries.  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Information of Nearest Hospital and live location view.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. Emergency Ambulance information.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5. Built-in Vaccine Information webpage to register/login for vaccination.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">6. Simple &amp; Interactive GUI.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; text-decoration: underline;\">Manual : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. To get an update of any country\'s current COVID situation , goto &quot;</span><span style=\" font-size:10pt; font-weight:600;\">COVID INFORMATION</span><span style=\" font-size:10pt;\">&quot; section and write down the country name , hit Enter.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. To compare between two country\'s information, goto &quot;</span><span style=\" font-size:10pt; font-weight:600;\">COVID INFO COMPARATOR</span><span style=\" font-size:10pt;\">&quot; section and write down the country\'s name, press Compare button.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. To find out the nearest hospital , goto </span><span style=\" font-size:10pt; font-weight:600;\">&quot;NEAREST HOSPITAL&quot;</span><span style=\" font-size:10pt;\"> section and press the Find Out buttion, same for Emergency Ambulance.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. To get vaccine information, goto &quot;</span><span style=\" font-size:10pt; font-weight:600;\">VACCINE INFORMATION</span><span style=\" font-size:10pt;\">&quot; section and follow the website.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Thank you for using this software.</span></p></body></html>"))

# Backend Start
        countries = country_list.get_country()
        completer = QCompleter(countries)
        self.country.setCompleter(completer)
        self.country_1.setCompleter(completer)
        self.country_2.setCompleter(completer)        
        self.country.editingFinished.connect(self.search)

        self.btn_covid_info.pressed.connect(self.show_covidInfo)
        self.btn_comp.pressed.connect(self.show_covidComp)
        self.btn_hosp.pressed.connect(self.show_hosp)
        self.btn_vac_info.pressed.connect(self.show_vacInfo)
        self.btn_about.pressed.connect(self.show_about)
        self.btn_help.pressed.connect(self.show_help)
        self.btn_exit.pressed.connect(self.show_exit)
        self.btnEmergency.pressed.connect(self.callAmbulance)
        self.btnFind.pressed.connect(self.findHospital)
        self.btn_compare.pressed.connect(self.compare_covid)
#Functions
    def show_covidInfo(self):
    	self.stackedWidget.setCurrentIndex(0)

    def show_covidComp(self):
    	self.stackedWidget.setCurrentIndex(1)

    def show_hosp(self):
    	self.stackedWidget.setCurrentIndex(2)

    def show_vacInfo(self):
    	self.stackedWidget.setCurrentIndex(3)

    def show_about(self):
    	self.stackedWidget.setCurrentIndex(4)

    def show_help(self):
    	self.stackedWidget.setCurrentIndex(5)

    def show_exit(self):
    	sys.exit(app.exec_())

    def callAmbulance(self):
    	msg = QMessageBox()
    	msg.setIcon(QMessageBox.Information)
    	msg.setText("Online Ambulance : +8801627669222 ")
    	msg.setWindowTitle("Ambulance Information")
    	msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    	retval = msg.exec_()
    def findHospital(self):
    	g = geocoder.ip('me')
    	lat = g.latlng[0]
    	lng = g.latlng[1]
    	url = f"https://www.google.com/maps/search/Hospital/@{lat},{lng},14z" 
    	self.WebHospital.setUrl(QUrl(url))

    def get_all(self):
        url = "https://corona.lmao.ninja/v2/all"
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

        request = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(request)
        data = json.loads(resp.read().decode("utf-8"))
        time_stamp = data['updated']
        time_stamp_ft = time.strftime('%d-%B-%Y %H:%M:%S', time.localtime(time_stamp/1000))

        self.activeCount.setText(str(data['active']))
        self.recoveredCount.setText(str(data['recovered']))
        self.confirmedCount.setText(str(data['cases']))
        self.deathsCount.setText(str(data['deaths']))
        self.criticalCount.setText(str(data['critical']))
        self.lastUpdated.setText("Last updated: " + time_stamp_ft)        

    def search(self):        
        country = urllib.parse.quote(self.country.text())
        url = f"https://corona.lmao.ninja/v2/countries/{country}"
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
        try:
	        request = urllib.request.Request(url, headers=headers)
	        resp = urllib.request.urlopen(request)
	        data = json.loads(resp.read().decode("utf-8"))
	        flag_url = data['countryInfo']['flag']
	        request = urllib.request.Request(flag_url, headers=headers)
	        flag = urllib.request.urlopen(request).read()
	        pixmap = QPixmap()
	        pixmap.loadFromData(flag)
	        time_stamp = data['updated']
	        time_stamp_ft = time.strftime('%d-%B-%Y %H:%M:%S', time.localtime(time_stamp/1000))


	        self.countryFlag.setPixmap(pixmap)
	        self.activeCount.setText(str(data['active']))
	        self.recoveredCount.setText(str(data['recovered']))
	        self.confirmedCount.setText(str(data['cases']))
	        self.deathsCount.setText(str(data['deaths']))
	        self.criticalCount.setText(str(data['critical']))
	        self.lastUpdated.setText("Last updated: " + time_stamp_ft)

        except:
	        self.activeCount.setText('ERROR')
	        self.recoveredCount.setText('ERROR')
	        self.confirmedCount.setText('ERROR')
	        self.deathsCount.setText('ERROR')
	        self.criticalCount.setText('ERROR')
	        self.lastUpdated.setText('ERROR')     	
    def compare_covid(self):        
        country1 = urllib.parse.quote(self.country_1.text())
        country2 = urllib.parse.quote(self.country_2.text())
        url1 = f"https://corona.lmao.ninja/v2/countries/{country1}"
        url2 = f"https://corona.lmao.ninja/v2/countries/{country2}"
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
        try:
	        request1 = urllib.request.Request(url1, headers=headers)
	        resp1 = urllib.request.urlopen(request1)
	        data1 = json.loads(resp1.read().decode("utf-8"))
	        flag_url1 = data1['countryInfo']['flag']
	        request1 = urllib.request.Request(flag_url1, headers=headers)
	        flag1 = urllib.request.urlopen(request1).read()
	        pixmap1 = QPixmap()
	        pixmap1.loadFromData(flag1)

	        request2 = urllib.request.Request(url2, headers=headers)
	        resp2 = urllib.request.urlopen(request2)
	        data2 = json.loads(resp2.read().decode("utf-8"))
	        flag_url2 = data2['countryInfo']['flag']
	        request2 = urllib.request.Request(flag_url2, headers=headers)
	        flag2 = urllib.request.urlopen(request2).read()
	        pixmap2 = QPixmap()
	        pixmap2.loadFromData(flag2)
	        
	        self.countryFlag_1.setPixmap(pixmap1)
	        self.active1.setText(str(data1['active']))
	        self.recover1.setText(str(data1['recovered']))
	        self.confirm1.setText(str(data1['cases']))
	        self.deaths1.setText(str(data1['deaths']))
	        self.critical1.setText(str(data1['critical']))
	        self.countryFlag_2.setPixmap(pixmap2)
	        self.active2.setText(str(data2['active']))
	        self.recover2.setText(str(data2['recovered']))
	        self.confirm2.setText(str(data2['cases']))
	        self.deaths2.setText(str(data2['deaths']))
	        self.critical2.setText(str(data2['critical']))

	        if (int(data1['active']) >int(data2['active'])):
	        	self.active_.setText(">")
	        elif (int(data1['active']) <int(data2['active'])):
	        	self.active_.setText("<")
	        else:
	        	self.active_.setText("=")

	        if (int(data1['recovered']) >int(data2['recovered'])):
	        	self.recover_.setText(">")
	        elif (int(data1['recovered']) <int(data2['recovered'])):
	        	self.recover_.setText("<")
	        else:
	        	self.recover_.setText("=")

	        if (int(data1['deaths']) >int(data2['deaths'])):
	        	self.deaths_.setText(">")
	        elif (int(data1['deaths']) <int(data2['deaths'])):
	        	self.deaths_.setText("<")
	        else:
	        	self.deaths_.setText("=")

	        if (int(data1['cases']) >int(data2['cases'])):
	        	self.confirm_.setText(">")
	        elif (int(data1['cases']) <int(data2['cases'])):
	        	self.confirm_.setText("<")
	        else:
	        	self.confirm_.setText("=")

	        if (int(data1['critical']) >int(data2['critical'])):
	        	self.critical_.setText(">")
	        elif (int(data1['critical']) <int(data2['critical'])):
	        	self.critical_.setText("<")
	        else:
	        	self.critical_.setText("=")	        	        	
        except:
	        self.active1.setText('')
	        self.recover1.setText('')
	        self.confirm1.setText('')
	        self.deaths1.setText('')
	        self.critical1.setText('')
	        self.active2.setText('')
	        self.recover2.setText('')
	        self.confirm2.setText('')
	        self.deaths2.setText('')
	        self.critical2.setText('')
	        self.active_.setText('?')
	        self.recover_.setText('?')
	        self.confirm_.setText('?')
	        self.deaths_.setText('?')
	        self.critical_.setText('?')


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False  
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    if connect() == True:
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
    else:
        print("No Connection...")
        app.quit()
    sys.exit(app.exec_())

