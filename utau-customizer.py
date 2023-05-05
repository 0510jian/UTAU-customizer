# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import glob
import os
from tkinter import *
from tkinter import filedialog

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication  # 창닫기
from PyQt5.QtGui import QIcon  # 아이콘 넣기
from PyQt5.QtWidgets import QFileDialog  # 파일 경로 설정
from PyQt5.QtWidgets import QWidget


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 280)
        MainWindow.setMinimumSize(QtCore.QSize(500, 280))
        MainWindow.setMaximumSize(QtCore.QSize(500, 280))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.utau = QtWidgets.QLabel(self.centralwidget)
        self.utau.setGeometry(QtCore.QRect(250, 0, 241, 31))
        self.utau.setObjectName("utau")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.length = QtWidgets.QWidget()
        self.length.setObjectName("length")
        self.label_2 = QtWidgets.QLabel(self.length)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 101, 21))
        self.label_2.setObjectName("label_2")
        self.OPEN_1 = QtWidgets.QPushButton(self.length)
        self.OPEN_1.setGeometry(QtCore.QRect(120, 10, 91, 21))
        self.OPEN_1.setObjectName("OPEN_1")
        self.ADDRESS_1 = QtWidgets.QTextEdit(self.length)
        self.ADDRESS_1.setGeometry(QtCore.QRect(20, 40, 191, 171))
        self.ADDRESS_1.setObjectName("ADDRESS_1")
        self.label_3 = QtWidgets.QLabel(self.length)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 131, 21))
        self.label_3.setObjectName("label_3")
        self.SAVE_NAME_1 = QtWidgets.QLineEdit(self.length)
        self.SAVE_NAME_1.setGeometry(QtCore.QRect(240, 40, 211, 21))
        self.SAVE_NAME_1.setObjectName("SAVE_NAME_1")
        self.label_4 = QtWidgets.QLabel(self.length)
        self.label_4.setGeometry(QtCore.QRect(240, 80, 131, 21))
        self.label_4.setObjectName("label_4")
        self.LENGTH_1 = QtWidgets.QLineEdit(self.length)
        self.LENGTH_1.setGeometry(QtCore.QRect(240, 110, 211, 20))
        self.LENGTH_1.setObjectName("LENGTH_1")
        self.CREATE_1 = QtWidgets.QPushButton(self.length)
        self.CREATE_1.setGeometry(QtCore.QRect(240, 160, 211, 23))
        self.CREATE_1.setObjectName("CREATE_1")
        self.QUIT_1 = QtWidgets.QPushButton(self.length)
        self.QUIT_1.setGeometry(QtCore.QRect(240, 190, 211, 23))
        self.QUIT_1.setObjectName("QUIT_1")
        self.tabWidget.addTab(self.length, "")
        self.alias = QtWidgets.QWidget()
        self.alias.setObjectName("alias")
        self.label_5 = QtWidgets.QLabel(self.alias)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 131, 21))
        self.label_5.setObjectName("label_5")
        self.SAVE_NAME_2 = QtWidgets.QLineEdit(self.alias)
        self.SAVE_NAME_2.setGeometry(QtCore.QRect(20, 130, 191, 21))
        self.SAVE_NAME_2.setObjectName("SAVE_NAME_2")
        self.OPEN_2 = QtWidgets.QPushButton(self.alias)
        self.OPEN_2.setGeometry(QtCore.QRect(120, 10, 91, 21))
        self.OPEN_2.setObjectName("OPEN_2")
        self.ADDRESS_2 = QtWidgets.QTextEdit(self.alias)
        self.ADDRESS_2.setGeometry(QtCore.QRect(20, 40, 191, 61))
        self.ADDRESS_2.setObjectName("ADDRESS_2")
        self.label_6 = QtWidgets.QLabel(self.alias)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 101, 21))
        self.label_6.setObjectName("label_6")
        self.CREATE_2 = QtWidgets.QPushButton(self.alias)
        self.CREATE_2.setGeometry(QtCore.QRect(240, 190, 91, 23))
        self.CREATE_2.setObjectName("CREATE_2")
        self.QUIT_2 = QtWidgets.QPushButton(self.alias)
        self.QUIT_2.setGeometry(QtCore.QRect(350, 190, 101, 23))
        self.QUIT_2.setObjectName("QUIT_2")
        self.MENU_2 = QtWidgets.QGroupBox(self.alias)
        self.MENU_2.setGeometry(QtCore.QRect(20, 160, 191, 51))
        self.MENU_2.setObjectName("MENU_2")
        self.D_BUTTON_2 = QtWidgets.QRadioButton(self.MENU_2)
        self.D_BUTTON_2.setGeometry(QtCore.QRect(130, 20, 51, 21))
        self.D_BUTTON_2.setObjectName("D_BUTTON_2")
        self.C_BUTTON_2 = QtWidgets.QRadioButton(self.MENU_2)
        self.C_BUTTON_2.setGeometry(QtCore.QRect(70, 20, 51, 21))
        self.C_BUTTON_2.setObjectName("C_BUTTON_2")
        self.N_BUTTON_2 = QtWidgets.QRadioButton(self.MENU_2)
        self.N_BUTTON_2.setGeometry(QtCore.QRect(10, 20, 51, 21))
        self.N_BUTTON_2.setObjectName("N_BUTTON_2")
        self.N_2 = QtWidgets.QGroupBox(self.alias)
        self.N_2.setGeometry(QtCore.QRect(240, 10, 211, 51))
        self.N_2.setObjectName("N_2")
        self.N_ALIAS = QtWidgets.QLineEdit(self.N_2)
        self.N_ALIAS.setGeometry(QtCore.QRect(10, 20, 191, 21))
        self.N_ALIAS.setObjectName("N_ALIAS")
        self.C_2 = QtWidgets.QGroupBox(self.alias)
        self.C_2.setGeometry(QtCore.QRect(240, 70, 211, 51))
        self.C_2.setObjectName("C_2")
        self.label_8 = QtWidgets.QLabel(self.C_2)
        self.label_8.setGeometry(QtCore.QRect(100, 10, 16, 41))
        self.label_8.setObjectName("label_8")
        self.C_ALIAS1 = QtWidgets.QLineEdit(self.C_2)
        self.C_ALIAS1.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.C_ALIAS1.setObjectName("C_ALIAS1")
        self.C_ALIAS2 = QtWidgets.QLineEdit(self.C_2)
        self.C_ALIAS2.setGeometry(QtCore.QRect(120, 20, 81, 21))
        self.C_ALIAS2.setObjectName("C_ALIAS2")
        self.D_2 = QtWidgets.QGroupBox(self.alias)
        self.D_2.setGeometry(QtCore.QRect(240, 130, 211, 51))
        self.D_2.setObjectName("D_2")
        self.D_ALIAS = QtWidgets.QLineEdit(self.D_2)
        self.D_ALIAS.setGeometry(QtCore.QRect(10, 20, 191, 21))
        self.D_ALIAS.setObjectName("D_ALIAS")
        self.tabWidget.addTab(self.alias, "")
        self.convert = QtWidgets.QWidget()
        self.convert.setObjectName("convert")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.convert)
        self.tabWidget_2.setGeometry(QtCore.QRect(6, 10, 461, 211))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 191, 16))
        self.label_11.setObjectName("label_11")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(230, 110, 241, 16))
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(10, 160, 131, 16))
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(10, 140, 191, 16))
        self.label_12.setObjectName("label_12")
        self.OPEN_3 = QtWidgets.QPushButton(self.tab_3)
        self.OPEN_3.setGeometry(QtCore.QRect(110, 10, 91, 21))
        self.OPEN_3.setObjectName("OPEN_3")
        self.ADDRESS_3 = QtWidgets.QTextEdit(self.tab_3)
        self.ADDRESS_3.setGeometry(QtCore.QRect(10, 40, 191, 71))
        self.ADDRESS_3.setObjectName("ADDRESS_3")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(230, 130, 241, 16))
        self.label_15.setObjectName("label_15")
        self.SAVE_NAME_3 = QtWidgets.QLineEdit(self.tab_3)
        self.SAVE_NAME_3.setGeometry(QtCore.QRect(390, 10, 51, 21))
        self.SAVE_NAME_3.setObjectName("SAVE_NAME_3")
        self.to_crazy_1 = QtWidgets.QPushButton(self.tab_3)
        self.to_crazy_1.setGeometry(QtCore.QRect(230, 70, 211, 23))
        self.to_crazy_1.setObjectName("to_crazy_1")
        self.to_hiragana_1 = QtWidgets.QPushButton(self.tab_3)
        self.to_hiragana_1.setGeometry(QtCore.QRect(230, 40, 211, 23))
        self.to_hiragana_1.setObjectName("to_hiragana_1")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(230, 10, 151, 21))
        self.label_9.setObjectName("label_9")
        self.QUIT_3 = QtWidgets.QPushButton(self.tab_3)
        self.QUIT_3.setGeometry(QtCore.QRect(230, 160, 211, 21))
        self.QUIT_3.setObjectName("QUIT_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.ADDRESS_4 = QtWidgets.QTextEdit(self.tab_4)
        self.ADDRESS_4.setGeometry(QtCore.QRect(10, 40, 191, 131))
        self.ADDRESS_4.setObjectName("ADDRESS_4")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_10.setObjectName("label_10")
        self.OPEN_4 = QtWidgets.QPushButton(self.tab_4)
        self.OPEN_4.setGeometry(QtCore.QRect(110, 10, 91, 21))
        self.OPEN_4.setObjectName("OPEN_4")
        self.to_crazy_2 = QtWidgets.QPushButton(self.tab_4)
        self.to_crazy_2.setGeometry(QtCore.QRect(230, 100, 211, 23))
        self.to_crazy_2.setObjectName("to_crazy_2")
        self.to_hiragana_2 = QtWidgets.QPushButton(self.tab_4)
        self.to_hiragana_2.setGeometry(QtCore.QRect(230, 70, 211, 23))
        self.to_hiragana_2.setObjectName("to_hiragana_2")
        self.QUIT_4 = QtWidgets.QPushButton(self.tab_4)
        self.QUIT_4.setGeometry(QtCore.QRect(230, 150, 211, 21))
        self.QUIT_4.setObjectName("QUIT_4")
        self.SAVE_NAME_4 = QtWidgets.QLineEdit(self.tab_4)
        self.SAVE_NAME_4.setGeometry(QtCore.QRect(230, 30, 191, 21))
        self.SAVE_NAME_4.setObjectName("SAVE_NAME_4")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(230, 10, 131, 21))
        self.label_16.setObjectName("label_16")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.convert, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # =====================================================================#
        MainWindow.setWindowIcon(QIcon('myang.png'))

        self.OPEN_1.clicked.connect(self.pushOpen_1)
        self.OPEN_2.clicked.connect(self.pushOpen_2)
        self.OPEN_3.clicked.connect(self.pushOpen_3)
        self.OPEN_4.clicked.connect(self.pushOpen_4)
        self.QUIT_1.clicked.connect(QCoreApplication.instance().quit)
        self.QUIT_2.clicked.connect(QCoreApplication.instance().quit)
        self.QUIT_3.clicked.connect(QCoreApplication.instance().quit)
        self.QUIT_4.clicked.connect(QCoreApplication.instance().quit)
        self.CREATE_1.clicked.connect(self.start_1)
        self.CREATE_2.clicked.connect(self.start_2)
        self.to_crazy_1.clicked.connect(self.start_3_to_crazy)
        self.to_hiragana_1.clicked.connect(self.start_3_to_hiragana)
        self.to_crazy_2.clicked.connect(self.start_4_to_crazy)
        self.to_hiragana_2.clicked.connect(self.start_4_to_hiragana)
        # =====================================================================#

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UTAU customizer 1.0"))
        self.utau.setText(_translate("MainWindow", "문의     ▶     0510jian@gmail.com"))
        self.label_2.setText(_translate("MainWindow", "변경할 UST 파일"))
        self.OPEN_1.setText(_translate("MainWindow", "UST 파일 선택"))
        self.label_3.setText(_translate("MainWindow", "변경 후 저장할 파일명"))
        self.label_4.setText(_translate("MainWindow", "변경할 길이 (n배)"))
        self.CREATE_1.setText(_translate("MainWindow", "생성"))
        self.QUIT_1.setText(_translate("MainWindow", "프로그램 종료"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.length), _translate("MainWindow", "노트길이"))
        self.label_5.setText(_translate("MainWindow", "변경 후 저장할 파일명"))
        self.OPEN_2.setText(_translate("MainWindow", "oto 파일 선택"))
        self.label_6.setText(_translate("MainWindow", "변경할 oto 파일"))
        self.CREATE_2.setText(_translate("MainWindow", "생성"))
        self.QUIT_2.setText(_translate("MainWindow", "프로그램 종료"))
        self.MENU_2.setTitle(_translate("MainWindow", "에일리어스"))
        self.D_BUTTON_2.setText(_translate("MainWindow", "삭제"))
        self.C_BUTTON_2.setText(_translate("MainWindow", "변경"))
        self.N_BUTTON_2.setText(_translate("MainWindow", "생성"))
        self.N_2.setTitle(_translate("MainWindow", "에일리어스 생성"))
        self.C_2.setTitle(_translate("MainWindow", "에일리어스 변경"))
        self.label_8.setText(_translate("MainWindow", "→"))
        self.D_2.setTitle(_translate("MainWindow", "에일리어스 삭제"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alias), _translate("MainWindow", "에일리어스"))
        self.label_11.setText(_translate("MainWindow", "경로로 지정한 곳의 파일명이 바로"))
        self.label_7.setText(_translate("MainWindow", "변경할 폴더"))
        self.label_14.setText(_translate("MainWindow", "버튼을 누르고 변환이 끝날 때까지"))
        self.label_13.setText(_translate("MainWindow", "복사본을 만들어주세요"))
        self.label_12.setText(_translate("MainWindow", "변경되는 형식이니, 반드시 사전에"))
        self.OPEN_3.setText(_translate("MainWindow", "폴더 선택"))
        self.label_15.setText(_translate("MainWindow", "잠시 기다려주세요 ✧*.◟(ˊ▽ˋ)◞.*✧"))
        self.to_crazy_1.setText(_translate("MainWindow", "히라가나(あ) → 뷁어(궇)"))
        self.to_hiragana_1.setText(_translate("MainWindow", "뷁어(궇) → 히라가나(あ)"))
        self.label_9.setText(_translate("MainWindow", "변경할 확장자(ex.wav, frq)"))
        self.QUIT_3.setText(_translate("MainWindow", "프로그램 종료"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "파일명 변환"))
        self.label_10.setText(_translate("MainWindow", "변경할 oto 파일"))
        self.OPEN_4.setText(_translate("MainWindow", "oto 파일 선택"))
        self.to_crazy_2.setText(_translate("MainWindow", "히라가나(あ) → 뷁어(궇)"))
        self.to_hiragana_2.setText(_translate("MainWindow", "뷁어(궇) → 히라가나(あ)"))
        self.QUIT_4.setText(_translate("MainWindow", "프로그램 종료"))
        self.label_16.setText(_translate("MainWindow", "변경 후 저장할 파일명"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "oto.ini 변환"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.convert), _translate("MainWindow", "궇↔あ"))


    def pushOpen_1(self): #파일 선택
        inFname = QFileDialog.getOpenFileName(self.length, 'Open file', '', 'UST파일(*.ust)')
        self.ADDRESS_1.setText(inFname[0])

    def pushOpen_2(self): #파일 선택
        inFname = QFileDialog.getOpenFileName(self.alias, 'Open file', '', 'oto.ini파일(*.ini)')
        self.ADDRESS_2.setText(inFname[0])

    def pushOpen_3(self): #파일 선택
        root = Tk()
        root.dirName = filedialog.askdirectory()
        self.ADDRESS_3.setText(root.dirName)

    def pushOpen_4(self):
        inFname = QFileDialog.getOpenFileName(self.alias, 'Open file', '', 'oto.ini파일(*.ini)')
        self.ADDRESS_4.setText(inFname[0])

    def start_1(self):
        outFname = str(self.SAVE_NAME_1.text())

        if '.ust' in outFname:
            pass
        else:
            outFname += '.ust'

        LENGTH = float(self.LENGTH_1.text())
        inFname = str(self.ADDRESS_1.toPlainText())

        inFp = open(inFname, 'r')
        outFp = open(outFname, 'w')

        while True:
            inStr = inFp.readline()
            if not inStr:
                break

            if 'Tempo=' in inStr:
                tempo, tempoNum = inStr.split('=')
                finalTempo = float(tempoNum) * LENGTH
                out = 'Tempo=' + str(finalTempo) + '\n'
                outFp.write(out)
            elif 'Length=' in inStr:
                length, lengthNum = inStr.split('=')
                finalLength = float(lengthNum) * LENGTH
                out = 'Length=' + str(finalLength) + '\n'
                outFp.write(out)
            else:
                outFp.write(inStr)

        inFp.close()
        outFp.close()

    def start_2(self):
        outFname = str(self.SAVE_NAME_2.text())

        if '.ini' in outFname:
            pass
        else:
            outFname += '.ini'

        inFname = str(self.ADDRESS_2.toPlainText())

        inFp = open(inFname, 'r')
        outFp = open(outFname, 'w')

        if self.N_BUTTON_2.isChecked():
            alias = str(self.N_ALIAS.text())

            while True:
                inStr = inFp.readline()
                if not inStr:
                    break

                reclist, oto = inStr.split('=')
                ali, num1, num2, num3, num4, num5 = oto.split(',')

                final_alias = ali + alias
                out = reclist + '=' + final_alias + ',' + num1 + ',' + num2 + ',' + num3 + ',' + num4 + ',' + num5
                outFp.write(out)

        elif self.C_BUTTON_2.isChecked():
            alias = str(self.C_ALIAS1.text())
            new_alias = str(self.C_ALIAS2.text())

            while True:
                inStr = inFp.readline()
                if not inStr:
                    break

                reclist, oto = inStr.split('=')
                ali, num1, num2, num3, num4, num5 = oto.split(',')

                if alias in ali:
                    final_alias = ali.replace(alias, new_alias)
                else:
                    final_alias = ali

                out = reclist + '=' + final_alias + ',' + num1 + ',' + num2 + ',' + num3 + ',' + num4 + ',' + num5
                outFp.write(out)

        elif self.D_BUTTON_2.isChecked():
            alias = str(self.D_ALIAS.text())

            while True:
                inStr = inFp.readline()
                if not inStr:
                    break

                reclist, oto = inStr.split('=')
                ali, num1, num2, num3, num4, num5 = oto.split(',')

                if alias in ali:
                    final_alias = ali.replace(alias, '')
                else:
                    final_alias = ali

                out = reclist + '=' + final_alias + ',' + num1 + ',' + num2 + ',' + num3 + ',' + num4 + ',' + num5
                outFp.write(out)

        inFp.close()
        outFp.close()

    def start_3_to_crazy(self):
        inFname = str(self.ADDRESS_3.toPlainText())
        TYPE = str(self.SAVE_NAME_3.text())
        if '.' in TYPE:
            TYPE = TYPE.replace('.', '')
        ROOT = inFname + '/*.' + TYPE

        B = ['궇', '궋', '궎', '궑', '궓', '궆', '궊', '궍', '궏', '궒', '궔', '궖', '궘', '궚', '궞',
             '궕', '궗', '궙', '궛', '궟', '궠', '궢', '궥', '궧', '궩', '궡', '궣', '궦', '궨', '궪',
             '궫', '궭', '궰', '궲', '궴', '궬', '궮', '궱', '궳', '궵', '궶', '궸', '궹', '궺', '궻',
             '궼', '궿', '귅', '귉', '귌', '궽', '귂', '귆', '귊', '귍', '궾', '귃', '귇', '귋', '귎',
             '귏', '귒', '귔', '귕', '귖', '귘', '귚', '귝', '귗', '귙', '귛', '귞', '귟', '귡', '귢', '귣',
             '귦', '귧', '귨', '귩', '귪', '궯', '귥',
             '귺', '귻', '귽', '귾', '긂', '긃', '긄', '긅', '긆', '긇', '긊', '긌', '긎', '긏', '긐',
             '긑', '긒', '긓', '긕', '긖', '긗', '긘', '긙', '긚', '긛', '긜', '긝', '긞', '긟', '긠',
             '긡', '긢', '긣', '긤', '긥', '긦', '긧', '긨', '긩', '긪', '긫', '긬', '긭', '긮', '긯',
             '긲', '긳', '긵', '긶', '긹', '긻', '긼', '긽', '긾', '긿', '깂', '깄', '깇', '깈', '깉',
             '깋', '깏', '깑', '깒', '깓', '깕', '깗', '깘', '깙', '깚', '깛', '깞', '깢', '깣', '뫃']
        H = ['あ', 'い', 'う', 'え', 'お', 'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ', 'か', 'き', 'く', 'け', 'こ',
             'が', 'ぎ', 'ぐ', 'げ', 'ご', 'さ', 'し', 'す', 'せ', 'そ', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
             'た', 'ち', 'つ', 'て', 'と', 'だ', 'ぢ', 'づ', 'で', 'ど', 'な', 'に', 'ぬ', 'ね', 'の',
             'は', 'ひ', 'ふ', 'へ', 'ほ', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
             'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ゃ', 'ゅ', 'ょ', 'ら', 'り', 'る', 'れ', 'ろ',
             'わ', 'ゐ', 'ゑ', 'を', 'ん', 'っ', 'ゎ',
             'ア', 'ィ', 'イ', 'ゥ', 'ウ', 'ェ', 'エ', 'ォ', 'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ',
             'ケ', 'ゲ', 'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ', 'ヂ', 'ッ', 'ツ', 'ヅ',
             'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ',
             'フ', 'ブ', 'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'メ', 'モ', 'ャ', 'ヤ', 'ュ', 'ユ', 'ョ', 'ヨ',
             'ラ', 'リ', 'ル', 'レ', 'ロ', 'ヮ', 'ワ', 'ヰ', 'ヱ', 'ヲ', 'ン', 'ヴ', 'ヵ', 'ヶ', '息']

        for i in range(158):
            fpath = ROOT

            for fpath in glob.glob(fpath):
                fpath_r = fpath.replace(H[i], B[i])
                os.rename(fpath, fpath_r)

    def start_3_to_hiragana(self):
        inFname = str(self.ADDRESS_3.toPlainText())
        TYPE = str(self.SAVE_NAME_3.text())
        if '.' in TYPE:
            TYPE = TYPE.replace('.', '')
        ROOT = inFname + '/*.' + TYPE

        B = ['궇', '궋', '궎', '궑', '궓', '궆', '궊', '궍', '궏', '궒', '궔', '궖', '궘', '궚', '궞',
             '궕', '궗', '궙', '궛', '궟', '궠', '궢', '궥', '궧', '궩', '궡', '궣', '궦', '궨', '궪',
             '궫', '궭', '궰', '궲', '궴', '궬', '궮', '궱', '궳', '궵', '궶', '궸', '궹', '궺', '궻',
             '궼', '궿', '귅', '귉', '귌', '궽', '귂', '귆', '귊', '귍', '궾', '귃', '귇', '귋', '귎',
             '귏', '귒', '귔', '귕', '귖', '귘', '귚', '귝', '귗', '귙', '귛', '귞', '귟', '귡', '귢', '귣',
             '귦', '귧', '귨', '귩', '귪', '궯', '귥',
             '귺', '귻', '귽', '귾', '긂', '긃', '긄', '긅', '긆', '긇', '긊', '긌', '긎', '긏', '긐',
             '긑', '긒', '긓', '긕', '긖', '긗', '긘', '긙', '긚', '긛', '긜', '긝', '긞', '긟', '긠',
             '긡', '긢', '긣', '긤', '긥', '긦', '긧', '긨', '긩', '긪', '긫', '긬', '긭', '긮', '긯',
             '긲', '긳', '긵', '긶', '긹', '긻', '긼', '긽', '긾', '긿', '깂', '깄', '깇', '깈', '깉',
             '깋', '깏', '깑', '깒', '깓', '깕', '깗', '깘', '깙', '깚', '깛', '깞', '깢', '깣', '뫃']
        H = ['あ', 'い', 'う', 'え', 'お', 'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ', 'か', 'き', 'く', 'け', 'こ',
             'が', 'ぎ', 'ぐ', 'げ', 'ご', 'さ', 'し', 'す', 'せ', 'そ', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
             'た', 'ち', 'つ', 'て', 'と', 'だ', 'ぢ', 'づ', 'で', 'ど', 'な', 'に', 'ぬ', 'ね', 'の',
             'は', 'ひ', 'ふ', 'へ', 'ほ', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
             'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ゃ', 'ゅ', 'ょ', 'ら', 'り', 'る', 'れ', 'ろ',
             'わ', 'ゐ', 'ゑ', 'を', 'ん', 'っ', 'ゎ',
             'ア', 'ィ', 'イ', 'ゥ', 'ウ', 'ェ', 'エ', 'ォ', 'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ',
             'ケ', 'ゲ', 'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ', 'ヂ', 'ッ', 'ツ', 'ヅ',
             'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ',
             'フ', 'ブ', 'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'メ', 'モ', 'ャ', 'ヤ', 'ュ', 'ユ', 'ョ', 'ヨ',
             'ラ', 'リ', 'ル', 'レ', 'ロ', 'ヮ', 'ワ', 'ヰ', 'ヱ', 'ヲ', 'ン', 'ヴ', 'ヵ', 'ヶ', '息']

        for i in range(158):
            fpath = ROOT

            for fpath in glob.glob(fpath):
                fpath_r = fpath.replace(B[i], H[i])
                os.rename(fpath, fpath_r)

    def start_4_to_crazy(self):
        inFname = str(self.ADDRESS_4.toPlainText())
        outFname = str(self.SAVE_NAME_4.text())

        if '.ini' in outFname:
            pass
        else:
            outFname += '.ini'

        inFp = open(inFname, 'r')
        outFp = open(outFname, 'w')

        B = ['궇', '궋', '궎', '궑', '궓', '궆', '궊', '궍', '궏', '궒', '궔', '궖', '궘', '궚', '궞',
             '궕', '궗', '궙', '궛', '궟', '궠', '궢', '궥', '궧', '궩', '궡', '궣', '궦', '궨', '궪',
             '궫', '궭', '궰', '궲', '궴', '궬', '궮', '궱', '궳', '궵', '궶', '궸', '궹', '궺', '궻',
             '궼', '궿', '귅', '귉', '귌', '궽', '귂', '귆', '귊', '귍', '궾', '귃', '귇', '귋', '귎',
             '귏', '귒', '귔', '귕', '귖', '귘', '귚', '귝', '귗', '귙', '귛', '귞', '귟', '귡', '귢', '귣',
             '귦', '귧', '귨', '귩', '귪', '궯', '귥',
             '귺', '귻', '귽', '귾', '긂', '긃', '긄', '긅', '긆', '긇', '긊', '긌', '긎', '긏', '긐',
             '긑', '긒', '긓', '긕', '긖', '긗', '긘', '긙', '긚', '긛', '긜', '긝', '긞', '긟', '긠',
             '긡', '긢', '긣', '긤', '긥', '긦', '긧', '긨', '긩', '긪', '긫', '긬', '긭', '긮', '긯',
             '긲', '긳', '긵', '긶', '긹', '긻', '긼', '긽', '긾', '긿', '깂', '깄', '깇', '깈', '깉',
             '깋', '깏', '깑', '깒', '깓', '깕', '깗', '깘', '깙', '깚', '깛', '깞', '깢', '깣', '뫃']
        H = ['あ', 'い', 'う', 'え', 'お', 'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ', 'か', 'き', 'く', 'け', 'こ',
             'が', 'ぎ', 'ぐ', 'げ', 'ご', 'さ', 'し', 'す', 'せ', 'そ', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
             'た', 'ち', 'つ', 'て', 'と', 'だ', 'ぢ', 'づ', 'で', 'ど', 'な', 'に', 'ぬ', 'ね', 'の',
             'は', 'ひ', 'ふ', 'へ', 'ほ', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
             'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ゃ', 'ゅ', 'ょ', 'ら', 'り', 'る', 'れ', 'ろ',
             'わ', 'ゐ', 'ゑ', 'を', 'ん', 'っ', 'ゎ',
             'ア', 'ィ', 'イ', 'ゥ', 'ウ', 'ェ', 'エ', 'ォ', 'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ',
             'ケ', 'ゲ', 'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ', 'ヂ', 'ッ', 'ツ', 'ヅ',
             'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ',
             'フ', 'ブ', 'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'メ', 'モ', 'ャ', 'ヤ', 'ュ', 'ユ', 'ョ', 'ヨ',
             'ラ', 'リ', 'ル', 'レ', 'ロ', 'ヮ', 'ワ', 'ヰ', 'ヱ', 'ヲ', 'ン', 'ヴ', 'ヵ', 'ヶ', '息']

        while True:
            inStr = inFp.readline()
            if not inStr:
                break

            for i in range(158):
                inStr = inStr.replace(H[i], B[i])

            outFp.write(inStr)

    def start_4_to_hiragana(self):
        inFname = str(self.ADDRESS_4.toPlainText())
        outFname = str(self.SAVE_NAME_4.text())

        if '.ini' in outFname:
            pass
        else:
            outFname += '.ini'

        inFp = open(inFname, 'r')
        outFp = open(outFname, 'w')

        B = ['궇', '궋', '궎', '궑', '궓', '궆', '궊', '궍', '궏', '궒', '궔', '궖', '궘', '궚', '궞',
             '궕', '궗', '궙', '궛', '궟', '궠', '궢', '궥', '궧', '궩', '궡', '궣', '궦', '궨', '궪',
             '궫', '궭', '궰', '궲', '궴', '궬', '궮', '궱', '궳', '궵', '궶', '궸', '궹', '궺', '궻',
             '궼', '궿', '귅', '귉', '귌', '궽', '귂', '귆', '귊', '귍', '궾', '귃', '귇', '귋', '귎',
             '귏', '귒', '귔', '귕', '귖', '귘', '귚', '귝', '귗', '귙', '귛', '귞', '귟', '귡', '귢', '귣',
             '귦', '귧', '귨', '귩', '귪', '궯', '귥',
             '귺', '귻', '귽', '귾', '긂', '긃', '긄', '긅', '긆', '긇', '긊', '긌', '긎', '긏', '긐',
             '긑', '긒', '긓', '긕', '긖', '긗', '긘', '긙', '긚', '긛', '긜', '긝', '긞', '긟', '긠',
             '긡', '긢', '긣', '긤', '긥', '긦', '긧', '긨', '긩', '긪', '긫', '긬', '긭', '긮', '긯',
             '긲', '긳', '긵', '긶', '긹', '긻', '긼', '긽', '긾', '긿', '깂', '깄', '깇', '깈', '깉',
             '깋', '깏', '깑', '깒', '깓', '깕', '깗', '깘', '깙', '깚', '깛', '깞', '깢', '깣', '뫃']
        H = ['あ', 'い', 'う', 'え', 'お', 'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ', 'か', 'き', 'く', 'け', 'こ',
             'が', 'ぎ', 'ぐ', 'げ', 'ご', 'さ', 'し', 'す', 'せ', 'そ', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
             'た', 'ち', 'つ', 'て', 'と', 'だ', 'ぢ', 'づ', 'で', 'ど', 'な', 'に', 'ぬ', 'ね', 'の',
             'は', 'ひ', 'ふ', 'へ', 'ほ', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
             'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ゃ', 'ゅ', 'ょ', 'ら', 'り', 'る', 'れ', 'ろ',
             'わ', 'ゐ', 'ゑ', 'を', 'ん', 'っ', 'ゎ',
             'ア', 'ィ', 'イ', 'ゥ', 'ウ', 'ェ', 'エ', 'ォ', 'オ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ',
             'ケ', 'ゲ', 'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ', 'ヂ', 'ッ', 'ツ', 'ヅ',
             'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ',
             'フ', 'ブ', 'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'メ', 'モ', 'ャ', 'ヤ', 'ュ', 'ユ', 'ョ', 'ヨ',
             'ラ', 'リ', 'ル', 'レ', 'ロ', 'ヮ', 'ワ', 'ヰ', 'ヱ', 'ヲ', 'ン', 'ヴ', 'ヵ', 'ヶ', '息']

        while True:
            inStr = inFp.readline()

            if not inStr:
                break

            for i in range(158):
                inStr = inStr.replace(B[i], H[i])

            outFp.write(inStr)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())