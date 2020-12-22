#Designed by Camilo Quiceno, version 1.0
#At Materialise Colombia office

#Python
import os
import sys

#Pyqt
from PyQt5 import QtCore, QtGui, QtWidgets

#3Matic
import trimatic

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(663, 261)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMinimumSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../CEToolKit/Test/img/materialise_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWidget.setWindowIcon(icon)
        MainWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tab_namer = QtWidgets.QWidget()
        self.tab_namer.setObjectName("tab_namer")
        self.comboBox_type = QtWidgets.QComboBox(self.tab_namer)
        self.comboBox_type.setGeometry(QtCore.QRect(290, 30, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_type.setFont(font)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.groupBox_type_names = QtWidgets.QGroupBox(self.tab_namer)
        self.groupBox_type_names.setGeometry(QtCore.QRect(20, 20, 231, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_type_names.setFont(font)
        self.groupBox_type_names.setObjectName("groupBox_type_names")
        self.radioButton_regular_name = QtWidgets.QRadioButton(self.groupBox_type_names)
        self.radioButton_regular_name.setGeometry(QtCore.QRect(10, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_regular_name.setFont(font)
        self.radioButton_regular_name.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.radioButton_regular_name.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.radioButton_regular_name.setChecked(True)
        self.radioButton_regular_name.setObjectName("radioButton_regular_name")
        self.radioButton_production_name = QtWidgets.QRadioButton(self.groupBox_type_names)
        self.radioButton_production_name.setGeometry(QtCore.QRect(10, 80, 191, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_production_name.setFont(font)
        self.radioButton_production_name.setObjectName("radioButton_production_name")
        self.comboBox_rev = QtWidgets.QComboBox(self.tab_namer)
        self.comboBox_rev.setGeometry(QtCore.QRect(290, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_rev.setFont(font)
        self.comboBox_rev.setObjectName("comboBox_rev")
        self.comboBox_rev.addItem("")
        self.comboBox_surgery = QtWidgets.QComboBox(self.tab_namer)
        self.comboBox_surgery.setGeometry(QtCore.QRect(20, 160, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_surgery.setFont(font)
        self.comboBox_surgery.setObjectName("comboBox_surgery")
        self.comboBox_surgery.addItem("")
        self.comboBox_surgery.addItem("")
        self.comboBox_surgery.addItem("")
        self.comboBox_surgery.addItem("")
        self.pushButton_apply = QtWidgets.QPushButton(self.tab_namer)
        self.pushButton_apply.setGeometry(QtCore.QRect(500, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_apply.setFont(font)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.pushButton_cancel = QtWidgets.QPushButton(self.tab_namer)
        self.pushButton_cancel.setGeometry(QtCore.QRect(380, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.textEdit_UID = QtWidgets.QTextEdit(self.tab_namer)
        self.textEdit_UID.setGeometry(QtCore.QRect(290, 110, 51, 31))
        self.textEdit_UID.setObjectName("textEdit_UID")
        MainWidget.addTab(self.tab_namer, "")
        self.tab_wrap = QtWidgets.QWidget()
        self.tab_wrap.setObjectName("tab_wrap")
        self.comboBox_type_wrap = QtWidgets.QComboBox(self.tab_wrap)
        self.comboBox_type_wrap.setGeometry(QtCore.QRect(280, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_type_wrap.setFont(font)
        self.comboBox_type_wrap.setObjectName("comboBox_type_wrap")
        self.comboBox_type_wrap.addItem("")
        self.comboBox_type_wrap.addItem("")
        self.comboBox_type_wrap.addItem("")
        self.comboBox_type_wrap.addItem("")
        self.comboBox_type_wrap.addItem("")
        self.comboBox_type_wrap.addItem("")
        self.comboBox_type_wrap.addItem("")
        self.comboBox_type_wrap.addItem("")
        self.label_type_wrap = QtWidgets.QLabel(self.tab_wrap)
        self.label_type_wrap.setGeometry(QtCore.QRect(50, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_type_wrap.setFont(font)
        self.label_type_wrap.setObjectName("label_type_wrap")
        self.label_gap_closing_distance = QtWidgets.QLabel(self.tab_wrap)
        self.label_gap_closing_distance.setGeometry(QtCore.QRect(50, 70, 161, 21))
        self.label_gap_closing_distance.setObjectName("label_gap_closing_distance")
        self.label_smallets_detail = QtWidgets.QLabel(self.tab_wrap)
        self.label_smallets_detail.setGeometry(QtCore.QRect(50, 100, 151, 21))
        self.label_smallets_detail.setObjectName("label_smallets_detail")
        self.label_protect_thin_walls = QtWidgets.QLabel(self.tab_wrap)
        self.label_protect_thin_walls.setGeometry(QtCore.QRect(50, 130, 151, 21))
        self.label_protect_thin_walls.setObjectName("label_protect_thin_walls")
        self.label_resulting_offset = QtWidgets.QLabel(self.tab_wrap)
        self.label_resulting_offset.setGeometry(QtCore.QRect(50, 160, 151, 21))
        self.label_resulting_offset.setObjectName("label_resulting_offset")
        self.label_reduce = QtWidgets.QLabel(self.tab_wrap)
        self.label_reduce.setGeometry(QtCore.QRect(350, 70, 61, 21))
        self.label_reduce.setObjectName("label_reduce")
        self.label_preserve_sharp_features = QtWidgets.QLabel(self.tab_wrap)
        self.label_preserve_sharp_features.setGeometry(QtCore.QRect(350, 100, 191, 21))
        self.label_preserve_sharp_features.setObjectName("label_preserve_sharp_features")
        self.label_preserve_sharp_structures = QtWidgets.QLabel(self.tab_wrap)
        self.label_preserve_sharp_structures.setGeometry(QtCore.QRect(350, 130, 211, 21))
        self.label_preserve_sharp_structures.setObjectName("label_preserve_sharp_structures")
        self.pushButton_cancel_wrapper = QtWidgets.QPushButton(self.tab_wrap)
        self.pushButton_cancel_wrapper.setGeometry(QtCore.QRect(380, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_cancel_wrapper.setFont(font)
        self.pushButton_cancel_wrapper.setObjectName("pushButton_cancel_wrapper")
        self.pushButton_apply_wrapper = QtWidgets.QPushButton(self.tab_wrap)
        self.pushButton_apply_wrapper.setGeometry(QtCore.QRect(500, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_apply_wrapper.setFont(font)
        self.pushButton_apply_wrapper.setObjectName("pushButton_apply_wrapper")
        self.doubleSpinBox_gap_closing_distance = QtWidgets.QDoubleSpinBox(self.tab_wrap)
        self.doubleSpinBox_gap_closing_distance.setGeometry(QtCore.QRect(220, 70, 51, 22))
        self.doubleSpinBox_gap_closing_distance.setDecimals(1)
        self.doubleSpinBox_gap_closing_distance.setObjectName("doubleSpinBox_gap_closing_distance")
        self.doubleSpinBox_smallets_detail = QtWidgets.QDoubleSpinBox(self.tab_wrap)
        self.doubleSpinBox_smallets_detail.setGeometry(QtCore.QRect(170, 100, 51, 22))
        self.doubleSpinBox_smallets_detail.setDecimals(2)
        self.doubleSpinBox_smallets_detail.setObjectName("doubleSpinBox_smallets_detail")
        self.doubleSpinBox_resulting_offset = QtWidgets.QDoubleSpinBox(self.tab_wrap)
        self.doubleSpinBox_resulting_offset.setGeometry(QtCore.QRect(180, 160, 51, 22))
        self.doubleSpinBox_resulting_offset.setDecimals(1)
        self.doubleSpinBox_resulting_offset.setMinimum(-10)
        self.doubleSpinBox_resulting_offset.setObjectName("doubleSpinBox_resulting_offset")
        self.checkBox_protect_thin_walls = QtWidgets.QCheckBox(self.tab_wrap)
        self.checkBox_protect_thin_walls.setGeometry(QtCore.QRect(190, 130, 21, 21))
        self.checkBox_protect_thin_walls.setText("")
        self.checkBox_protect_thin_walls.setObjectName("checkBox_protect_thin_walls")
        self.checkBox_preserve_sharp_structures = QtWidgets.QCheckBox(self.tab_wrap)
        self.checkBox_preserve_sharp_structures.setGeometry(QtCore.QRect(560, 130, 21, 21))
        self.checkBox_preserve_sharp_structures.setText("")
        self.checkBox_preserve_sharp_structures.setObjectName("checkBox_preserve_sharp_structures")
        self.checkBox_preserve_sharp_features = QtWidgets.QCheckBox(self.tab_wrap)
        self.checkBox_preserve_sharp_features.setGeometry(QtCore.QRect(540, 100, 21, 21))
        self.checkBox_preserve_sharp_features.setText("")
        self.checkBox_preserve_sharp_features.setObjectName("checkBox_preserve_sharp_features")
        self.checkBox_reduce = QtWidgets.QCheckBox(self.tab_wrap)
        self.checkBox_reduce.setGeometry(QtCore.QRect(420, 70, 21, 21))
        self.checkBox_reduce.setText("")
        self.checkBox_reduce.setObjectName("checkBox_reduce")
        MainWidget.addTab(self.tab_wrap, "")

        self.retranslateUi(MainWidget)
        MainWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):

        #Tab_namer
        _translate = QtCore.QCoreApplication.translate
        #MainWidget.setWindowTitle(_translate("MainWidget", "CEToolkit"))
        self.groupBox_type_names.setTitle(_translate("MainWidget", "Type of Name"))
        self.radioButton_regular_name.setText(_translate("MainWidget", "Regular Name"))
        self.radioButton_production_name.setText(_translate("MainWidget", "Production Name"))
        self.comboBox_surgery.setItemText(0, _translate("MainWidget", "Orthognatic"))
        self.comboBox_surgery.setItemText(1, _translate("MainWidget", "Reconstruction"))
        self.comboBox_surgery.setItemText(2, _translate("MainWidget", "Models"))
        self.comboBox_surgery.setItemText(3, _translate("MainWidget", "Others"))
        self.comboBox_type.setItemText(0, _translate("MainWidget", "Part"))
        self.comboBox_rev.setItemText(0, _translate("MainWidget", "REV0"))
        self.comboBox_rev.setItemText(1, _translate("MainWidget", "REV1"))
        self.comboBox_rev.setItemText(2, _translate("MainWidget", "REV2"))
        self.comboBox_rev.setItemText(3, _translate("MainWidget", "REV3"))
        self.comboBox_rev.setItemText(4, _translate("MainWidget", "REV4"))
        self.comboBox_rev.setItemText(5, _translate("MainWidget", "REV5"))
        self.comboBox_rev.setItemText(6, _translate("MainWidget", "REV6"))

        self.pushButton_apply.setText(_translate("MainWidget", "Apply"))
        self.pushButton_cancel.setText(_translate("MainWidget", "Cancel"))
        self.textEdit_UID.setPlaceholderText(_translate("MainWidget", "UID"))
        MainWidget.setTabText(MainWidget.indexOf(self.tab_namer), _translate("MainWidget", "Namer"))

        #Tab_wrap
        self.comboBox_type_wrap.setItemText(0, _translate("MainWidget", "Wrap"))
        self.comboBox_type_wrap.setItemText(1, _translate("MainWidget", "Planned Models"))
        self.comboBox_type_wrap.setItemText(2, _translate("MainWidget", "PreOp Models"))
        self.comboBox_type_wrap.setItemText(3, _translate("MainWidget", "Sandwich Buttom"))
        self.comboBox_type_wrap.setItemText(4, _translate("MainWidget", "Lingual Wall"))
        self.comboBox_type_wrap.setItemText(5, _translate("MainWidget", "Palatal Strap"))
        self.comboBox_type_wrap.setItemText(6, _translate("MainWidget", "Strap Part"))
        self.comboBox_type_wrap.setItemText(7, _translate("MainWidget", "Large Color File"))
        self.label_type_wrap.setText(_translate("MainWidget", "Type Of Wrap"))
        self.label_gap_closing_distance.setText(_translate("MainWidget", "Gap Closing Distance:"))
        self.label_smallets_detail.setText(_translate("MainWidget", "Smallest Detail:"))
        self.label_protect_thin_walls.setText(_translate("MainWidget", "Protect Thin Walls:"))
        self.label_resulting_offset.setText(_translate("MainWidget", "Resulting Offset:"))
        self.label_reduce.setText(_translate("MainWidget", "Reduce:"))
        self.label_preserve_sharp_features.setText(_translate("MainWidget", "Preserve Sharp Features:"))
        self.label_preserve_sharp_structures.setText(_translate("MainWidget", "Preserve Surface Structures:"))
        self.pushButton_cancel_wrapper.setText(_translate("MainWidget", "Cancel"))
        self.pushButton_apply_wrapper.setText(_translate("MainWidget", "Apply"))
        MainWidget.setTabText(MainWidget.indexOf(self.tab_wrap), _translate("MainWidget", "Wraper"))

        self.pushButton_apply.setText(_translate("MainWidget", "Apply"))
        self.pushButton_cancel.setText(_translate("MainWidget", "Cancel"))

        #Namer Connections
        self.radioButton_regular_name.clicked.connect(self.radioButton_regular_name_checked) 
        self.radioButton_production_name.clicked.connect(self.radioButton_production_name_checked)
        self.comboBox_surgery.currentIndexChanged.connect(self.comboBox_surgery_changed)
        self.pushButton_apply.clicked.connect(self.pushButton_apply_clicked)
        self.pushButton_cancel.clicked.connect(self.pushButton_cancel_clicked)

        #Wrapper Connections
        self.comboBox_type_wrap.currentIndexChanged.connect(self.comboBox_type_wrap_changed)

        self.pushButton_apply_wrapper.clicked.connect(self.pushButton_apply_wrapper_clicked)
        self.pushButton_cancel_wrapper.clicked.connect(self.pushButton_cancel_clicked)

#Namer Functions
    def comboBox_type_text(self,surgery):

        self.comboBox_type.clear()

        if surgery == 'Orthognatic':
            
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
                
            self.comboBox_type.setItemText(0, "IntSplint")
            self.comboBox_type.setItemText(1, "FinalSplint")
            self.comboBox_type.setItemText(2, "GenioGuide")
            self.comboBox_type.setItemText(3, "GenioPositionGuide")

        if surgery == 'Reconstruction':

            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            
            self.comboBox_type.setItemText(0, "MandGuide")
            self.comboBox_type.setItemText(1, "FibulaGuide")
            self.comboBox_type.setItemText(2, "ScapGuide")
            self.comboBox_type.setItemText(3, "HipGuide")
            self.comboBox_type.setItemText(4, "MandPositionGuide")
            self.comboBox_type.setItemText(5, "MidfacePositionGuide")
        
        if surgery == 'Models':

            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            
            self.comboBox_type.setItemText(0, "PreopMaxModel")
            self.comboBox_type.setItemText(1, "PlannedMaxModel")
            self.comboBox_type.setItemText(2, "PreopMaxOrbitModel")
            self.comboBox_type.setItemText(3, "PlannedMaxOrbitModel")
            self.comboBox_type.setItemText(4, "PreopMandOrbitModel")
            self.comboBox_type.setItemText(5, "PlannedMandOrbitModel")
            self.comboBox_type.setItemText(6, "PreopOrbitModel")
            self.comboBox_type.setItemText(7, "PlannedOrbitModel")
            self.comboBox_type.setItemText(8, "PreopMandMaxModel")
            self.comboBox_type.setItemText(9, "PlannedMandMaxModel")
            self.comboBox_type.setItemText(10, "PreopMandModel")
            self.comboBox_type.setItemText(11, "PlannedMandModel")

        if surgery == 'Others':

            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            self.comboBox_type.addItem("")
            
            self.comboBox_type.setItemText(0, "DistrGuide")
            self.comboBox_type.setItemText(1, "DistrPositionGuide")
            self.comboBox_type.setItemText(2, "CranGuide")
            self.comboBox_type.setItemText(3, "CranShapeGuide")
            self.comboBox_type.setItemText(4, "Spacers")
            self.comboBox_type.setItemText(5, "AnaplGuide")
            self.comboBox_type.setItemText(6, "PSIImplant")
   
    def radioButton_production_name_checked(self, MainWidget): 
        _translate = QtCore.QCoreApplication.translate
        if self.comboBox_surgery.currentText() == 'Orthognatic':
            print('ortho pro')
            self.comboBox_type_text('Orthognatic')

        elif self.comboBox_surgery.currentText() == 'Reconstruction':
            print('Reconstruction pro')
            self.comboBox_type_text('Reconstruction')

        elif self.comboBox_surgery.currentText() == 'Models':
            print('Modelsc pro')
            self.comboBox_type_text('Models')
        elif self.comboBox_surgery.currentText() == 'Others':
            print('Others pro')
            self.comboBox_type_text('Others')

    def radioButton_regular_name_checked(self): 
        if self.comboBox_surgery.currentText() == 'Orthognatic':
            print('ortho reg')
            self.comboBox_type_text('Orthognatic')
        elif self.comboBox_surgery.currentText() == 'Reconstruction':
            print('Reconstruction reg')
            self.comboBox_type_text('Reconstruction')
        elif self.comboBox_surgery.currentText() == 'Models':
            print('Models reg')
            self.comboBox_type_text('Models')
        elif self.comboBox_surgery.currentText() == 'Others':
            print('Others reg')
            self.comboBox_type_text('Others')

    def comboBox_surgery_changed(self):
        
        if self.comboBox_surgery.currentText() == 'Orthognatic':
            print('ortho reg')
            self.comboBox_type_text('Orthognatic')
        elif self.comboBox_surgery.currentText() == 'Reconstruction':
                print('Reconstruction reg')
                self.comboBox_type_text('Reconstruction')
        elif self.comboBox_surgery.currentText() == 'Models':
            print('Models reg')
            self.comboBox_type_text('Models')
        elif self.comboBox_surgery.currentText() == 'Others':
            print('Others reg')
            self.comboBox_type_text('Others')

    def pushButton_apply_clicked(self):

        if self.radioButton_regular_name.isChecked():

            name = self.comboBox_type.currentText()
            version = self.comboBox_rev.currentText()
            uid = self.textEdit_UID.toPlainText()
            final_name = f'{name}_{uid}_{version}'

        if self.radioButton_production_name.isChecked():

            case_id = trimatic.get_project_filename()
            case_id = case_id.split('\\')[-1].split(".")[0]

            uid = self.textEdit_UID.toPlainText()

            if not case_id:
                case_id = 'XXX_XXX_XXX'

            print(f'EL case id es {case_id}')

            item = 'SD900.XXX'

            version = int(self.comboBox_rev.currentText().split('V')[-1]) + 1
            name = self.comboBox_type.currentText()
            build = 'build'

            final_name = f'{case_id}_{uid}_{item}_V0{version}_{name}_{build}'
        
        new_object = trimatic.duplicate(old_object)
        new_object.name = final_name
        MainWidget.close()

    def pushButton_cancel_clicked(self):
        MainWidget.close()

#Wrapper Function
    def comboBox_type_wrap_changed(self):
        if self.comboBox_type_wrap.currentText() == 'Planned Models':
            self.doubleSpinBox_gap_closing_distance.setValue(2.5)
            self.doubleSpinBox_smallets_detail.setValue(0.5)
            self.checkBox_protect_thin_walls.setChecked(False)
            self.doubleSpinBox_resulting_offset.setValue(0)
            self.checkBox_reduce.setChecked(True)
            self.checkBox_preserve_sharp_features.setChecked(True)
            self.checkBox_preserve_sharp_structures.setChecked(False)

        if self.comboBox_type_wrap.currentText() == 'PreOp Models':
            self.doubleSpinBox_gap_closing_distance.setValue(3.0)
            self.doubleSpinBox_smallets_detail.setValue(0.7)
            self.checkBox_protect_thin_walls.setChecked(False)
            self.doubleSpinBox_resulting_offset.setValue(0)
            self.checkBox_reduce.setChecked(True)
            self.checkBox_preserve_sharp_features.setChecked(False)
            self.checkBox_preserve_sharp_structures.setChecked(False)

        if self.comboBox_type_wrap.currentText() == 'Sandwich Buttom':
            self.doubleSpinBox_gap_closing_distance.setValue(1.0)
            self.doubleSpinBox_smallets_detail.setValue(0.25)
            self.checkBox_protect_thin_walls.setChecked(False)
            self.doubleSpinBox_resulting_offset.setValue(0.1)
            self.checkBox_reduce.setChecked(False)
            self.checkBox_preserve_sharp_features.setChecked(True)
            self.checkBox_preserve_sharp_structures.setChecked(True)
        
        if self.comboBox_type_wrap.currentText() == 'Lingual Wall':
            self.doubleSpinBox_gap_closing_distance.setValue(3.0)
            self.doubleSpinBox_smallets_detail.setValue(0.7)
            self.checkBox_protect_thin_walls.setChecked(False)
            self.doubleSpinBox_resulting_offset.setValue(0.3)
            self.checkBox_reduce.setChecked(True)
            self.checkBox_preserve_sharp_features.setChecked(False)
            self.checkBox_preserve_sharp_structures.setChecked(False)

        if self.comboBox_type_wrap.currentText() == 'Palatal Strap':
            self.doubleSpinBox_gap_closing_distance.setValue(0.0)
            self.doubleSpinBox_smallets_detail.setValue(0.5)
            self.checkBox_protect_thin_walls.setChecked(False)
            self.doubleSpinBox_resulting_offset.setValue(1.5)
            self.checkBox_reduce.setChecked(True)
            self.checkBox_preserve_sharp_features.setChecked(False)
            self.checkBox_preserve_sharp_structures.setChecked(False)    

        if self.comboBox_type_wrap.currentText() == 'Strap Part':
            self.doubleSpinBox_gap_closing_distance.setValue(0.0)
            self.doubleSpinBox_smallets_detail.setValue(0.7)
            self.checkBox_protect_thin_walls.setChecked(False)
            self.doubleSpinBox_resulting_offset.setValue(3)
            self.checkBox_reduce.setChecked(True)
            self.checkBox_preserve_sharp_features.setChecked(False)
            self.checkBox_preserve_sharp_structures.setChecked(False)

        if self.comboBox_type_wrap.currentText() == 'Large Color File':
            self.doubleSpinBox_gap_closing_distance.setValue(0.0)
            self.doubleSpinBox_smallets_detail.setValue(0.7)
            self.checkBox_protect_thin_walls.setChecked(False)
            self.doubleSpinBox_resulting_offset.setValue(-0.4)
            self.checkBox_reduce.setChecked(True)
            self.checkBox_preserve_sharp_features.setChecked(True)
            self.checkBox_preserve_sharp_structures.setChecked(False)

    def pushButton_apply_wrapper_clicked(self):

        gap_closing = self.doubleSpinBox_gap_closing_distance.value()
        smallest_detail = self.doubleSpinBox_smallets_detail.value()
        protect_thin_walls = self.checkBox_protect_thin_walls.isChecked()
        resulting_offset = self.doubleSpinBox_resulting_offset.value()
        reduce_param = self.checkBox_reduce.isChecked()
        preserve_sharp_features = self.checkBox_preserve_sharp_features.isChecked()
        preserve_surface_structure = self.checkBox_preserve_sharp_structures.isChecked()

        trimatic.wrap(entities=old_object, gap_closing_distance=gap_closing, smallest_detail=smallest_detail, protect_thin_walls=protect_thin_walls, resulting_offset=resulting_offset, reduce=reduce_param, preserve_sharp_features=preserve_sharp_features, preserve_surface_structure=preserve_surface_structure)

        if self.comboBox_type_wrap.currentText() != 'Wrap':
            print(f'Object wrapped as {self.comboBox_type_wrap.currentText()} parameters')

        else:
            print(f'Object wrapped as custom parameters')

        MainWidget.close()

if __name__ == "__main__":

    selection = trimatic.message_box(message="Please select the workpart" , title= "Name Changer",with_cancel=False)

    try:
        old_object = trimatic.get_selection()
        trimatic.suspend_progress()

        if old_object:
        
            app = QtWidgets.QApplication(sys.argv)
            MainWidget = QtWidgets.QTabWidget()
            ui = Ui_MainWidget()
            ui.setupUi(MainWidget)
            MainWidget.show()
            sys.exit(app.exec_())

        else:
            trimatic.message_box(message="Please select an object" , title= "Name Changer",with_cancel=False)

    except:
        print('Please select an object')