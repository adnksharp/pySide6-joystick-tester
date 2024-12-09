# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(361, 325)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.ax = QLCDNumber(Widget)
        self.ax.setObjectName(u"ax")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ax.sizePolicy().hasHeightForWidth())
        self.ax.setSizePolicy(sizePolicy)
        self.ax.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.ax.setFrameShape(QFrame.Shape.NoFrame)
        self.ax.setSmallDecimalPoint(False)
        self.ax.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.ax)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.ay = QLCDNumber(Widget)
        self.ay.setObjectName(u"ay")
        sizePolicy.setHeightForWidth(self.ay.sizePolicy().hasHeightForWidth())
        self.ay.setSizePolicy(sizePolicy)
        self.ay.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.ay.setFrameShape(QFrame.Shape.NoFrame)
        self.ay.setSmallDecimalPoint(False)
        self.ay.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.ay)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.di = QLCDNumber(Widget)
        self.di.setObjectName(u"di")
        sizePolicy.setHeightForWidth(self.di.sizePolicy().hasHeightForWidth())
        self.di.setSizePolicy(sizePolicy)
        self.di.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.di.setSmallDecimalPoint(False)
        self.di.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.di)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Joystick", None))
        self.label.setText(QCoreApplication.translate("Widget", u"X:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Y:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"SW:", None))
    # retranslateUi

