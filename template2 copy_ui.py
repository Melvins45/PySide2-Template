# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template2 copy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon_rc

class Ui_Template(object):
    def setupUi(self, Template):
        if not Template.objectName():
            Template.setObjectName(u"Template")
        Template.resize(690, 496)
        icon = QIcon()
        icon.addFile(u"img/template_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Template.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Template)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(Template)
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

        self.body = QWidget(Template)
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

        self.retranslateUi(Template)

        QMetaObject.connectSlotsByName(Template)
    # setupUi

    def retranslateUi(self, Template):
        Template.setWindowTitle(QCoreApplication.translate("Template", u"Template 2", None))
        self.pushButton.setText("")
        self.template_1.setText(QCoreApplication.translate("Template", u"Template 1", None))
        self.template_2.setText(QCoreApplication.translate("Template", u"Template 2", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Template", u"Elit veniam culpa cupidatat dolore sint excepteur sint cupidatat nisi officia sunt. Anim qui laborum sunt Lorem aliquip sunt aute elit pariatur Lorem aliquip commodo. Incididunt commodo sit laboris esse esse.  Laborum minim id cillum veniam. Non anim amet adipisicing consequat. Eu dolor minim eu aute labore et magna laboris ad sit non laboris occaecat. Pariatur sit cupidatat mollit quis.  Fugiat enim reprehenderit aute ipsum eu fugiat in cupidatat reprehenderit. Veniam ea adipisicing ipsum fugiat eiusmod ipsum. Excepteur anim aute anim quis qui quis dolore voluptate et consectetur consequat cupidatat deserunt. Non nostrud velit et laboris nostrud sint commodo id sit irure. Sit quis sint consequat officia irure commodo qui qui in. Commodo tempor ipsum culpa officia ullamco aliquip mollit aute amet ipsum aliquip officia exercitation.", None))
    # retranslateUi

