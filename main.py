import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from layout import *


class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)

    def onTestBtnClicked(self):
        qb = QMessageBox()
        qb.information(self, 'test', 'test2', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWidget()
    myWin.show()
    sys.exit(app.exec_())
