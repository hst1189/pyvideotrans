# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from videotrans.configure import config
from videotrans.util import tools


class Ui_openaittsform(object):
    def setupUi(self, openaittsform):
        self.has_done = False
        openaittsform.setObjectName("openaittsform")
        openaittsform.setWindowModality(QtCore.Qt.NonModal)
        openaittsform.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(openaittsform.sizePolicy().hasHeightForWidth())
        openaittsform.setSizePolicy(sizePolicy)
        openaittsform.setMaximumSize(QtCore.QSize(600, 600))

        v1=QtWidgets.QVBoxLayout(openaittsform)

        self.label_0 = QtWidgets.QLabel(openaittsform)
        self.label_0.setGeometry(QtCore.QRect(10, 10, 580, 35))
        self.label_0.setText(
            'OpenAI官方接口无需填写' if config.defaulelang == 'zh' else 'AIs compatible with the ChatGPT also used here')
        v1.addWidget(self.label_0)

        h1=QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel(openaittsform)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.openaitts_api = QtWidgets.QLineEdit(openaittsform)
        self.openaitts_api.setMinimumSize(QtCore.QSize(0, 35))
        self.openaitts_api.setObjectName("openaitts_api")
        h1.addWidget(self.label)
        h1.addWidget(self.openaitts_api)
        v1.addLayout(h1)

        h2=QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel(openaittsform)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.openaitts_key = QtWidgets.QLineEdit(openaittsform)
        self.openaitts_key.setMinimumSize(QtCore.QSize(0, 35))
        self.openaitts_key.setObjectName("openaitts_key")
        h2.addWidget(self.label_2)
        h2.addWidget(self.openaitts_key)
        v1.addLayout(h2)

        h3=QtWidgets.QHBoxLayout()
        self.label_3 = QtWidgets.QLabel(openaittsform)
        self.label_3.setObjectName("label_3")
        self.openaitts_model = QtWidgets.QComboBox(openaittsform)
        self.openaitts_model.setMinimumSize(QtCore.QSize(0, 35))
        self.openaitts_model.setObjectName("openaitts_model")
        h3.addWidget(self.label_3)
        h3.addWidget(self.openaitts_model)
        v1.addLayout(h3)

        self.label_allmodels = QtWidgets.QLabel(openaittsform)

        self.label_allmodels.setObjectName("label_allmodels")
        self.label_allmodels.setText(
            '填写所有可用模型，以英文逗号分隔，填写后可在上方选择' if config.defaulelang == 'zh' else 'Fill in all available models, separated by commas. After filling in, you can select them above')
        v1.addWidget(self.label_allmodels)
        self.edit_allmodels = QtWidgets.QPlainTextEdit(openaittsform)
        self.edit_allmodels.setMinimumHeight(40)
        self.edit_allmodels.setObjectName("edit_allmodels")
        v1.addWidget(self.edit_allmodels)
        
        
        v1.addWidget(QtWidgets.QLabel('角色列表' if config.defaulelang == 'zh' else 'Role list'))
        self.edit_roles = QtWidgets.QPlainTextEdit(openaittsform)
        self.edit_roles.setMinimumHeight(40)
        self.edit_roles.setObjectName("edit_roles")
        v1.addWidget(self.edit_roles)


        h4=QtWidgets.QHBoxLayout()

        self.set_openaitts = QtWidgets.QPushButton(openaittsform)
        self.set_openaitts.setMinimumSize(QtCore.QSize(0, 35))
        self.set_openaitts.setObjectName("set_openaitts")

        self.test_openaitts = QtWidgets.QPushButton(openaittsform)
        self.test_openaitts.setMinimumSize(QtCore.QSize(0, 30))
        self.test_openaitts.setObjectName("test_openaitts")

        help_btn = QtWidgets.QPushButton()
        help_btn.setMinimumSize(QtCore.QSize(0, 35))
        help_btn.setStyleSheet("background-color: rgba(255, 255, 255,0)")
        help_btn.setObjectName("help_btn")
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setText("查看填写教程" if config.defaulelang == 'zh' else "Fill out the tutorial")
        help_btn.clicked.connect(lambda: tools.open_url(url='https://pyvideotrans.com/openaitts'))

        h4.addWidget(self.set_openaitts)
        h4.addWidget(self.test_openaitts)
        h4.addWidget(help_btn)
        v1.addLayout(h4)

        self.retranslateUi(openaittsform)
        QtCore.QMetaObject.connectSlotsByName(openaittsform)

    def retranslateUi(self, openaittsform):
        openaittsform.setWindowTitle("OpenAI API TTS")
        self.label_3.setText('选择模型' if config.defaulelang == 'zh' else "Model")
        self.set_openaitts.setText('保存' if config.defaulelang == 'zh' else "Save")
        self.test_openaitts.setText('测试..' if config.defaulelang == 'zh' else "Test..")
        self.openaitts_api.setPlaceholderText(
            '若使用OpenAI官方接口，无需填写;第三方api在此填写' if config.defaulelang == 'zh' else 'If using the official OpenAI interface, there is no need to fill it out; Fill in the third-party API here')
        self.openaitts_api.setToolTip(
            '若使用OpenAI官方接口，无需填写;第三方api在此填写' if config.defaulelang == 'zh' else 'If using the official OpenAI interface, there is no need to fill it out; Fill in the third-party API here')
        self.openaitts_key.setPlaceholderText("Secret key")
        self.openaitts_key.setToolTip(
            "必须是付费账号，免费账号频率受限无法使用" if config.defaulelang == 'zh' else 'Must be a paid account, free account frequency is limited and cannot be used')
        self.label.setText("API URL")
        self.label_2.setText("SK")
