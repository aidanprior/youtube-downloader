# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\youtube_downloader\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\youtube_downloader\\data/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.url_layout = QtWidgets.QHBoxLayout()
        self.url_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.url_layout.setObjectName("url_layout")
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.url_layout.addWidget(self.url_label)
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.url_input.setFont(font)
        self.url_input.setObjectName("url_input")
        self.url_layout.addWidget(self.url_input)
        self.download_now_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.download_now_button.setFont(font)
        self.download_now_button.setObjectName("download_now_button")
        self.url_layout.addWidget(self.download_now_button)
        self.verticalLayout.addLayout(self.url_layout)
        self.download_status_layout = QtWidgets.QHBoxLayout()
        self.download_status_layout.setObjectName("download_status_layout")
        self.download_filename_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_filename_label.sizePolicy().hasHeightForWidth())
        self.download_filename_label.setSizePolicy(sizePolicy)
        self.download_filename_label.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.download_filename_label.setFont(font)
        self.download_filename_label.setIndent(0)
        self.download_filename_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.download_filename_label.setObjectName("download_filename_label")
        self.download_status_layout.addWidget(self.download_filename_label)
        self.download_progressbar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.download_progressbar.setFont(font)
        self.download_progressbar.setProperty("value", 0)
        self.download_progressbar.setTextVisible(True)
        self.download_progressbar.setInvertedAppearance(False)
        self.download_progressbar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.download_progressbar.setObjectName("download_progressbar")
        self.download_status_layout.addWidget(self.download_progressbar)
        self.speed_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_label.sizePolicy().hasHeightForWidth())
        self.speed_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.speed_label.setFont(font)
        self.speed_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.speed_label.setObjectName("speed_label")
        self.download_status_layout.addWidget(self.speed_label)
        self.eta_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eta_label.sizePolicy().hasHeightForWidth())
        self.eta_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.eta_label.setFont(font)
        self.eta_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.eta_label.setObjectName("eta_label")
        self.download_status_layout.addWidget(self.eta_label)
        self.verticalLayout.addLayout(self.download_status_layout)
        self.downloaded_list = QtWidgets.QListWidget(self.centralwidget)
        self.downloaded_list.setObjectName("downloaded_list")
        self.verticalLayout.addWidget(self.downloaded_list)
        self.options_layout = QtWidgets.QHBoxLayout()
        self.options_layout.setObjectName("options_layout")
        self.options_left_layout = QtWidgets.QVBoxLayout()
        self.options_left_layout.setObjectName("options_left_layout")
        self.options_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options_label.sizePolicy().hasHeightForWidth())
        self.options_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.options_label.setFont(font)
        self.options_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.options_label.setAlignment(QtCore.Qt.AlignCenter)
        self.options_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.options_label.setObjectName("options_label")
        self.options_left_layout.addWidget(self.options_label)
        self.download_folder_layout = QtWidgets.QHBoxLayout()
        self.download_folder_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.download_folder_layout.setObjectName("download_folder_layout")
        self.download_folder_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_folder_label.sizePolicy().hasHeightForWidth())
        self.download_folder_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.download_folder_label.setFont(font)
        self.download_folder_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.download_folder_label.setObjectName("download_folder_label")
        self.download_folder_layout.addWidget(self.download_folder_label)
        self.download_folder_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.download_folder_input.setFont(font)
        self.download_folder_input.setObjectName("download_folder_input")
        self.download_folder_layout.addWidget(self.download_folder_input)
        self.download_folder_browse_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.download_folder_browse_button.setFont(font)
        self.download_folder_browse_button.setObjectName("download_folder_browse_button")
        self.download_folder_layout.addWidget(self.download_folder_browse_button)
        self.options_left_layout.addLayout(self.download_folder_layout)
        self.plist_input_file_layout = QtWidgets.QHBoxLayout()
        self.plist_input_file_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.plist_input_file_layout.setObjectName("plist_input_file_layout")
        self.plist_input_file_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plist_input_file_label.sizePolicy().hasHeightForWidth())
        self.plist_input_file_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.plist_input_file_label.setFont(font)
        self.plist_input_file_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plist_input_file_label.setObjectName("plist_input_file_label")
        self.plist_input_file_layout.addWidget(self.plist_input_file_label)
        self.plists_file_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.plists_file_input.setFont(font)
        self.plists_file_input.setObjectName("plists_file_input")
        self.plist_input_file_layout.addWidget(self.plists_file_input)
        self.plists_file_browse_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.plists_file_browse_button.setFont(font)
        self.plists_file_browse_button.setObjectName("plists_file_browse_button")
        self.plist_input_file_layout.addWidget(self.plists_file_browse_button)
        self.options_left_layout.addLayout(self.plist_input_file_layout)
        self.ffmpeg_bin_layout = QtWidgets.QHBoxLayout()
        self.ffmpeg_bin_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.ffmpeg_bin_layout.setObjectName("ffmpeg_bin_layout")
        self.ffmpeg_bin_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ffmpeg_bin_label.sizePolicy().hasHeightForWidth())
        self.ffmpeg_bin_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.ffmpeg_bin_label.setFont(font)
        self.ffmpeg_bin_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.ffmpeg_bin_label.setObjectName("ffmpeg_bin_label")
        self.ffmpeg_bin_layout.addWidget(self.ffmpeg_bin_label)
        self.ffmpeg_bin_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ffmpeg_bin_input.setFont(font)
        self.ffmpeg_bin_input.setObjectName("ffmpeg_bin_input")
        self.ffmpeg_bin_layout.addWidget(self.ffmpeg_bin_input)
        self.ffmpeg_bin_browse_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.ffmpeg_bin_browse_button.setFont(font)
        self.ffmpeg_bin_browse_button.setObjectName("ffmpeg_bin_browse_button")
        self.ffmpeg_bin_layout.addWidget(self.ffmpeg_bin_browse_button)
        self.options_left_layout.addLayout(self.ffmpeg_bin_layout)
        self.template_layout = QtWidgets.QHBoxLayout()
        self.template_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.template_layout.setObjectName("template_layout")
        self.template_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.template_label.sizePolicy().hasHeightForWidth())
        self.template_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.template_label.setFont(font)
        self.template_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.template_label.setObjectName("template_label")
        self.template_layout.addWidget(self.template_label)
        self.template_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.template_input.setFont(font)
        self.template_input.setObjectName("template_input")
        self.template_layout.addWidget(self.template_input)
        self.options_left_layout.addLayout(self.template_layout)
        self.load_save_options_layout = QtWidgets.QHBoxLayout()
        self.load_save_options_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.load_save_options_layout.setObjectName("load_save_options_layout")
        self.save_options_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_options_button.sizePolicy().hasHeightForWidth())
        self.save_options_button.setSizePolicy(sizePolicy)
        self.save_options_button.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.save_options_button.setFont(font)
        self.save_options_button.setObjectName("save_options_button")
        self.load_save_options_layout.addWidget(self.save_options_button)
        self.load_options_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_options_button.sizePolicy().hasHeightForWidth())
        self.load_options_button.setSizePolicy(sizePolicy)
        self.load_options_button.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.load_options_button.setFont(font)
        self.load_options_button.setObjectName("load_options_button")
        self.load_save_options_layout.addWidget(self.load_options_button)
        self.options_left_layout.addLayout(self.load_save_options_layout)
        self.options_layout.addLayout(self.options_left_layout)
        self.options_right_layout = QtWidgets.QVBoxLayout()
        self.options_right_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.options_right_layout.setObjectName("options_right_layout")
        self.archive_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.archive_checkbox.setFont(font)
        self.archive_checkbox.setObjectName("archive_checkbox")
        self.options_right_layout.addWidget(self.archive_checkbox)
        self.mp3_convert_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.mp3_convert_checkbox.setFont(font)
        self.mp3_convert_checkbox.setObjectName("mp3_convert_checkbox")
        self.options_right_layout.addWidget(self.mp3_convert_checkbox)
        self.plist_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.plist_checkbox.setFont(font)
        self.plist_checkbox.setObjectName("plist_checkbox")
        self.options_right_layout.addWidget(self.plist_checkbox)
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setObjectName("update_button")
        self.options_right_layout.addWidget(self.update_button)
        self.options_layout.addLayout(self.options_right_layout)
        self.verticalLayout.addLayout(self.options_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.url_label.setText(_translate("MainWindow", "Youtube URL: "))
        self.download_now_button.setText(_translate("MainWindow", "Go"))
        self.download_filename_label.setText(_translate("MainWindow", "Not Downloading"))
        self.speed_label.setText(_translate("MainWindow", "0.00 kB/s"))
        self.eta_label.setText(_translate("MainWindow", "ETA: 00:00"))
        self.options_label.setText(_translate("MainWindow", "Options:"))
        self.download_folder_label.setText(_translate("MainWindow", "Download Folder:"))
        self.download_folder_browse_button.setText(_translate("MainWindow", "Browse"))
        self.plist_input_file_label.setText(_translate("MainWindow", "Multi-Playlist Config:"))
        self.plists_file_browse_button.setText(_translate("MainWindow", "Browse"))
        self.ffmpeg_bin_label.setText(_translate("MainWindow", "FFmpeg Bin:"))
        self.ffmpeg_bin_browse_button.setText(_translate("MainWindow", "Browse"))
        self.template_label.setText(_translate("MainWindow", "Template:"))
        self.save_options_button.setText(_translate("MainWindow", "Save Options"))
        self.save_options_button.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.load_options_button.setText(_translate("MainWindow", "Load Options"))
        self.archive_checkbox.setText(_translate("MainWindow", "Use Archive"))
        self.mp3_convert_checkbox.setText(_translate("MainWindow", "Convert to mp3"))
        self.plist_checkbox.setText(_translate("MainWindow", "Download Playlist"))
        self.update_button.setText(_translate("MainWindow", " Update Program"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
