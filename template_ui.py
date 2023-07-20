# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_Termplate(object):
    def setupUi(self, Termplate):
        if not Termplate.objectName():
            Termplate.setObjectName(u"Termplate")
        Termplate.resize(690, 496)
        self.verticalLayout = QVBoxLayout(Termplate)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(Termplate)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.header)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(u"border-image: url(img/template_icon.png);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(217, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.template_1 = QPushButton(self.header)
        self.template_1.setObjectName(u"template_1")
        font = QFont()
        font.setPointSize(14)
        self.template_1.setFont(font)
        self.template_1.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.template_1)

        self.template_2 = QPushButton(self.header)
        self.template_2.setObjectName(u"template_2")
        self.template_2.setFont(font)
        self.template_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.template_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 5)

        self.verticalLayout.addWidget(self.header)

        self.body = QWidget(Termplate)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QHBoxLayout(self.body)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(162, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.plainTextEdit = QPlainTextEdit(self.body)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font1 = QFont()
        font1.setPointSize(12)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(217, 217, 217);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.horizontalSpacer_2 = QSpacerItem(162, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.body)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Termplate)

        QMetaObject.connectSlotsByName(Termplate)
    # setupUi

    def retranslateUi(self, Termplate):
        Termplate.setWindowTitle(QCoreApplication.translate("Termplate", u"Template", None))
        self.pushButton.setText("")
        self.template_1.setText(QCoreApplication.translate("Termplate", u"Template 1", None))
        self.template_2.setText(QCoreApplication.translate("Termplate", u"Template 2", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Termplate", u"In eiusmod deserunt labore voluptate mollit qui veniam est. Sint dolore nulla ullamco dolore occaecat eiusmod incididunt commodo veniam anim minim exercitation qui. Dolore ex incididunt aliquip velit dolore id cupidatat irure.  Irure incididunt cillum ipsum in ipsum laboris consectetur veniam laboris sint laborum. Lorem excepteur ullamco sint labore pariatur proident. Cillum enim ut non ad cupidatat sunt aute ullamco aute minim.  Consectetur voluptate in exercitation ad aute amet. Cupidatat dolore nisi in eu in veniam minim sunt nostrud excepteur mollit fugiat culpa. Quis Lorem velit Lorem qui excepteur. Culpa nostrud ad adipisicing laborum labore fugiat est. Magna exercitation id culpa duis amet nostrud duis qui occaecat proident est. Dolore incididunt aliquip qui amet veniam ut incididunt labore reprehenderit quis. Velit magna cillum laborum eiusmod cillum officia occaecat enim minim ullamco pariatur.", None))
    # retranslateUi

