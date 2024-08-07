from PySide6.QtCore import Qt, Slot, QUrl, QStringListModel, QModelIndex
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QLabel, QMenu, QPushButton, QFileDialog, QListView, QLineEdit, QRadioButton, QMessageBox
from PySide6.QtGui import QAction

import sys, os, can

from view.can_log_converter import Ui_MainWindow

class AboutWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(300, 100)
        self.setWindowTitle('About')
        layout = QVBoxLayout()

        label_version = QLabel('can_log_converter v1.0 by can-bus.io')
        label_version.setStyleSheet('font-size: 14px;')
        layout.addWidget(label_version)

        label_thanks = QLabel('Thanks to:')
        label_thanks.setStyleSheet('font-size: 16px; font-weight: bold;')
        layout.addWidget(label_thanks)

        label_to = QLabel('pyside6, pyinstaller, python-can, asammdf')
        label_to.setStyleSheet('font-size: 14px;')
        layout.addWidget(label_to)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.resize(800, 600)
    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.inputFilesModel = QStringListModel()
        self.findChild(QListView, 'inputFilesList').setModel(self.inputFilesModel)

        self.findChild(QRadioButton, 'rbtn_asc').toggled.connect(lambda checked: self.setTargetSfx(checked,'.asc'))
        self.findChild(QRadioButton, 'rbtn_blf').toggled.connect(lambda checked: self.setTargetSfx(checked,'.blf'))
        self.findChild(QRadioButton, 'rbtn_csv').toggled.connect(lambda checked: self.setTargetSfx(checked,'.csv'))
        self.findChild(QRadioButton, 'rbtn_db').toggled.connect(lambda checked: self.setTargetSfx(checked,'.db'))
        self.findChild(QRadioButton, 'rbtn_log').toggled.connect(lambda checked: self.setTargetSfx(checked,'.log'))
        self.findChild(QRadioButton, 'rbtn_mf4').toggled.connect(lambda checked: self.setTargetSfx(checked,'.mf4'))
        self.findChild(QRadioButton, 'rbtn_trc').toggled.connect(lambda checked: self.setTargetSfx(checked,'.trc'))

        self.findChild(QAction, 'action_load').triggered.connect(self.loadInputFiles)
        self.findChild(QAction, 'action_exit').triggered.connect(self.exit)
        self.findChild(QAction, 'action_ad').triggered.connect(self.openAd)
        self.findChild(QAction, 'action_about').triggered.connect(self.showAbout)
        self.findChild(QPushButton, 'pbtn_setTargetDir').clicked.connect(self.setTargetDir)
        self.findChild(QPushButton, 'pbtn_loadInputFiles').clicked.connect(self.loadInputFiles)
        self.findChild(QPushButton, 'pbtn_convert').clicked.connect(self.convert)

    def setTargetDir(self):
        dir_name = QFileDialog.getExistingDirectory(
            self,
            'Select OutPut Folder',
            '',
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )

        if dir_name:
            self.findChild(QLineEdit, 'outputDir').setText(dir_name)

    def loadInputFiles(self):
        file_names, _ = QFileDialog.getOpenFileNames(
            self,
            'Select Input Files',
            '',
            'CAN Log Files (*.asc *.blf *.csv *.db *.log *.mf4 *.trc)'
        )

        if file_names:
            self.inputFilesModel.setStringList([])
            self.inputFilesModel.setStringList(file_names)

    def convert(self):
        model = self.inputFilesModel
        rows = model.rowCount(QModelIndex())
        if self.findChild(QLineEdit, 'outputDir').text() == '':
            QMessageBox.information(None, '提示', '请选择输出文件夹')
            return

        if not hasattr(self, 'targetSfx'):
            QMessageBox.information(None, '提示', '请选择目标文件类型')
            return

        if rows == 0:
            QMessageBox.information(None, '提示', '请选择待转换文件')
            return

        for row in range(rows):
            index = model.index(row, 0)
            f = model.data(index)
            name, sfx = os.path.splitext(os.path.basename(f))
            if sfx != self.targetSfx:
                rmd = 'rb'
                if sfx == '.asc' or sfx == '.csv' or sfx == '.log' or sfx == '.trc':
                    rmd = 'r'
                wmd = 'wb'
                if self.targetSfx == '.asc' or self.targetSfx == '.csv' or self.targetSfx == '.log' or self.targetSfx == '.trc':
                    wmd = 'w'

                targetFile = os.path.join(self.findChild(QLineEdit, 'outputDir').text(),name+self.targetSfx)

                if sfx == '.asc':
                    load_fcn = self.load_asc
                elif sfx == '.blf':
                    load_fcn = self.load_blf
                elif sfx == '.csv':
                    load_fcn = self.load_csv
                elif sfx == '.db':
                    load_fcn = self.load_db
                elif sfx == '.log':
                    load_fcn = self.load_log
                elif sfx == '.mf4':
                    load_fcn = self.load_mf4
                elif sfx == '.trc':
                    load_fcn = self.load_trc

                if self.targetSfx == '.asc':
                    convert_to_fcn = self.convert_to_asc
                elif self.targetSfx == '.blf':
                    convert_to_fcn = self.convert_to_blf
                elif self.targetSfx == '.csv':
                    convert_to_fcn = self.convert_to_csv
                elif self.targetSfx == '.db':
                    convert_to_fcn = self.convert_to_db
                elif self.targetSfx == '.log':
                    convert_to_fcn = self.convert_to_log
                elif self.targetSfx == '.mf4':
                    convert_to_fcn = self.convert_to_mf4
                elif self.targetSfx == '.trc':
                    convert_to_fcn = self.convert_to_trc

                self.converting(f, rmd, targetFile, load_fcn, convert_to_fcn)
            QMessageBox.information(None, '提示', '处理完毕!')

    def converting(self, f, rmd, targetFile, load_fcn, convert_to_fcn):
        with open(f, rmd) as f_in:
            log_in = load_fcn(f, f_in)
            convert_to_fcn(log_in, targetFile)

    def load_asc(self, f, f_in):
        return can.io.ASCReader(f_in)
    def load_blf(self, f, f_in):
        return can.io.BLFReader(f_in)
    def load_csv(self, f, f_in):
        return can.io.CSVReader(f_in)
    def load_db(self, f, f_in):
        return can.io.SqliteReader(f)
    def load_log(self, f, f_in):
        return can.io.CanutilsLogReader(f_in)
    def load_mf4(self, f, f_in):
        return can.io.MF4Reader(f_in)
    def load_trc(self, f, f_in):
        return can.io.TRCReader(f_in)

    def convert_to_asc(self,log_in, targetFile):
        with open(targetFile, 'w', encoding='utf-8') as f_out:
            log_out = can.io.ASCWriter(f_out, channel=1)
            for msg in log_in:
                log_out.on_message_received(msg)
            log_out.stop()
    def convert_to_blf(self,log_in, targetFile):
        with open(targetFile, 'wb') as f_out:
            log_out = can.io.BLFWriter(f_out)
            for msg in log_in:
                log_out.on_message_received(msg)
            log_out.stop()
    def convert_to_csv(self,log_in, targetFile):
        with open(targetFile, 'w', encoding='utf-8') as f_out:
            log_out = can.io.CSVWriter(f_out)
            for msg in log_in:
                log_out.on_message_received(msg)
            log_out.stop()
    def convert_to_db(self,log_in, targetFile):
        log_out = can.io.SqliteWriter(targetFile)
        for msg in log_in:
            log_out.on_message_received(msg)
        log_out.stop()
    def convert_to_log(self,log_in, targetFile):
        with open(targetFile, 'w', encoding='utf-8') as f_out:
            log_out = can.io.CanutilsLogWriter(f_out)
            for msg in log_in:
                log_out.on_message_received(msg)
            log_out.stop()
    def convert_to_mf4(self,log_in, targetFile):
        with open(targetFile, 'wb') as f_out:
            log_out = can.io.MF4Writer(f_out)
            for msg in log_in:
                log_out.on_message_received(msg)
            log_out.stop()
    def convert_to_trc(self,log_in, targetFile):
        with open(targetFile, 'w', encoding='utf-8') as f_out:
            log_out = can.io.TRCWriter(f_out)
            for msg in log_in:
                log_out.on_message_received(msg)
            log_out.stop()

    def exit(self):
        app.quit()

    @Slot()
    def openAd(self):
        url = QUrl('https://can-bus.io')
        from PySide6.QtGui import QDesktopServices
        QDesktopServices.openUrl(url)

    def showAbout(self):
        about = AboutWindow(self)
        about.exec()

    def setTargetSfx(self,checked,sfx):
        if checked:
            self.targetSfx = sfx

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
