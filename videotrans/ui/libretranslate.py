# run again.  Do not edit this file unless you know what you are doing.

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from videotrans.configure import config
from videotrans.util import tools


class Ui_libretranslateform(object):
    def setupUi(self, libretranslateform):
        self.has_done = False
        libretranslateform.setObjectName("libretranslateform")
        libretranslateform.setWindowModality(QtCore.Qt.NonModal)
        libretranslateform.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(libretranslateform.sizePolicy().hasHeightForWidth())
        libretranslateform.setSizePolicy(sizePolicy)
        libretranslateform.setMaximumSize(QtCore.QSize(500, 300))

        self.verticalLayout = QtWidgets.QVBoxLayout(libretranslateform)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        
        
        self.label = QtWidgets.QLabel(libretranslateform)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.address = QtWidgets.QLineEdit(libretranslateform)
        self.address.setMinimumSize(QtCore.QSize(320, 35))
        self.address.setObjectName("address")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.address)
        
        self.label2 = QtWidgets.QLabel(libretranslateform)
        self.label2.setMinimumSize(QtCore.QSize(100, 35))
        self.label2.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.label2.setObjectName("label2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label2)
        self.key = QtWidgets.QLineEdit(libretranslateform)
        self.key.setMinimumSize(QtCore.QSize(320, 35))
        self.key.setObjectName("key")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.key)
        
        
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.formLayout_3)
        
        self.set = QtWidgets.QPushButton(libretranslateform)
        self.set.setMinimumSize(QtCore.QSize(0, 35))
        self.set.setObjectName("set")

        self.test = QtWidgets.QPushButton(libretranslateform)
        self.test.setObjectName("test")

        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText("查看填写教程" if config.defaulelang == 'zh' else "Fill out the tutorial")
        help_btn.clicked.connect(lambda: tools.open_url(url='https://pyvideotrans.com/libretranslate'))

        h1=QtWidgets.QHBoxLayout()
        h1.addWidget(self.set)
        h1.addWidget(self.test)
        h1.addWidget(help_btn)

        self.verticalLayout.addLayout(h1)


        self.retranslateUi(libretranslateform)
        QtCore.QMetaObject.connectSlotsByName(libretranslateform)

    def retranslateUi(self, libretranslateform):
        libretranslateform.setWindowTitle("LibreTranslate")
        self.label.setText("API URL")
        self.label2.setText("API Key")
        self.key.setPlaceholderText('填写密钥，不存在为空即可' if config.defaulelang == 'zh' else 'Input your libretranslate key ')
        self.address.setPlaceholderText('API URL')
        self.set.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.test.setText('测试' if config.defaulelang == 'zh' else "Test")
