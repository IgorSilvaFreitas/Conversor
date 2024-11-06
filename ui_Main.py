# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainCvzLLv.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_Conversor(object):
    def setupUi(self, Conversor):
        if not Conversor.objectName():
            Conversor.setObjectName(u"Conversor")
        Conversor.resize(847, 584)
        Conversor.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.centralwidget = QWidget(Conversor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setMaximumSize(QSize(371, 551))
        self.frame_menu.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_1 = QFrame(self.frame_menu)
        self.frame_1.setObjectName(u"frame_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_1.sizePolicy().hasHeightForWidth())
        self.frame_1.setSizePolicy(sizePolicy1)
        self.frame_1.setStyleSheet(u"")
        self.frame_1.setFrameShape(QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.pesquisar_bt = QPushButton(self.frame_1)
        self.pesquisar_bt.setObjectName(u"pesquisar_bt")
        self.pesquisar_bt.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-image: url(:icons/icons/add_circle_att.png);\n"
"	background-repeat: no-repeat;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pesquisar_bt.setIcon(icon)
        self.pesquisar_bt.setIconSize(QSize(35, 40))

        self.horizontalLayout_2.addWidget(self.pesquisar_bt)

        self.caminho_ql = QLineEdit(self.frame_1)
        self.caminho_ql.setObjectName(u"caminho_ql")
        self.caminho_ql.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.caminho_ql)


        self.verticalLayout.addWidget(self.frame_1)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.frame_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pg_inicial = QLabel(self.frame_2)
        self.pg_inicial.setObjectName(u"pg_inicial")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(100)
        sizePolicy2.setHeightForWidth(self.pg_inicial.sizePolicy().hasHeightForWidth())
        self.pg_inicial.setSizePolicy(sizePolicy2)
        self.pg_inicial.setMinimumSize(QSize(0, 0))
        self.pg_inicial.setMaximumSize(QSize(75, 100))

        self.verticalLayout_3.addWidget(self.pg_inicial)

        self.edit_inicial = QLineEdit(self.frame_2)
        self.edit_inicial.setObjectName(u"edit_inicial")
        self.edit_inicial.setMinimumSize(QSize(0, 0))
        self.edit_inicial.setMaximumSize(QSize(150, 100))
        self.edit_inicial.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.edit_inicial)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pg_final = QLabel(self.frame_2)
        self.pg_final.setObjectName(u"pg_final")
        sizePolicy2.setHeightForWidth(self.pg_final.sizePolicy().hasHeightForWidth())
        self.pg_final.setSizePolicy(sizePolicy2)
        self.pg_final.setMinimumSize(QSize(0, 0))
        self.pg_final.setMaximumSize(QSize(75, 100))

        self.verticalLayout_4.addWidget(self.pg_final)

        self.edit_final = QLineEdit(self.frame_2)
        self.edit_final.setObjectName(u"edit_final")
        self.edit_final.setMinimumSize(QSize(0, 0))
        self.edit_final.setMaximumSize(QSize(150, 100))
        self.edit_final.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.edit_final)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.frame_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(500, 16777215))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.area_sep = QLabel(self.frame_3)
        self.area_sep.setObjectName(u"area_sep")
        self.area_sep.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.area_sep)

        self.edit_area = QLineEdit(self.frame_3)
        self.edit_area.setObjectName(u"edit_area")
        self.edit_area.setMaximumSize(QSize(211, 22))
        self.edit_area.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.edit_area)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.verticalSpacer_3 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.frame_4 = QFrame(self.frame_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.form = QLabel(self.frame_4)
        self.form.setObjectName(u"form")
        self.form.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.form)

        self.stream = QRadioButton(self.frame_4)
        self.stream.setObjectName(u"stream")
        self.stream.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.stream)

        self.lattice = QRadioButton(self.frame_4)
        self.lattice.setObjectName(u"lattice")
        self.lattice.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.lattice)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer_4 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.frame_5 = QFrame(self.frame_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.salvar_bt = QPushButton(self.frame_5)
        self.salvar_bt.setObjectName(u"salvar_bt")
        self.salvar_bt.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.salvar_bt)

        self.converter_bt = QPushButton(self.frame_5)
        self.converter_bt.setObjectName(u"converter_bt")
        self.converter_bt.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.converter_bt)


        self.verticalLayout.addWidget(self.frame_5)

        self.verticalSpacer_5 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.calc_sep = QPushButton(self.frame_menu)
        self.calc_sep.setObjectName(u"calc_sep")
        self.calc_sep.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(100, 100, 100);\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.calc_sep)


        self.horizontalLayout.addWidget(self.frame_menu, 0, Qt.AlignTop)

        self.frame_table = QFrame(self.centralwidget)
        self.frame_table.setObjectName(u"frame_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_table.sizePolicy().hasHeightForWidth())
        self.frame_table.setSizePolicy(sizePolicy3)
        self.frame_table.setFrameShape(QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_table)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.frame_table)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.tableView)


        self.horizontalLayout.addWidget(self.frame_table)

        Conversor.setCentralWidget(self.centralwidget)

        self.retranslateUi(Conversor)

        QMetaObject.connectSlotsByName(Conversor)
    # setupUi

    def retranslateUi(self, Conversor):
        Conversor.setWindowTitle(QCoreApplication.translate("Conversor", u"MainWindow", None))
        self.pesquisar_bt.setText("")
        self.pg_inicial.setText(QCoreApplication.translate("Conversor", u"P\u00e1gina Inicial", None))
        self.pg_final.setText(QCoreApplication.translate("Conversor", u"P\u00e1gina Final", None))
        self.area_sep.setText(QCoreApplication.translate("Conversor", u"\u00c1rea de Separa\u00e7\u00e3o", None))
        self.form.setText(QCoreApplication.translate("Conversor", u"Formatos:", None))
        self.stream.setText(QCoreApplication.translate("Conversor", u"Stream", None))
        self.lattice.setText(QCoreApplication.translate("Conversor", u"Lattice", None))
        self.salvar_bt.setText(QCoreApplication.translate("Conversor", u"Salvar", None))
        self.converter_bt.setText(QCoreApplication.translate("Conversor", u"Converter", None))
        self.calc_sep.setText(QCoreApplication.translate("Conversor", u"Abrir regua", None))
    # retranslateUi

