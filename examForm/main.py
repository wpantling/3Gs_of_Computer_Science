from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtCore import QUrl, Qt
import sys
import mainDesign

class GlobalMem: backURL = ['back', 'current', 'forward']

class WebViewer(QMainWindow, mainDesign.Ui_MainWindow):

 def __init__(self):
     super(self.__class__, self).__init__()
     self.setupUi(self)
     self.GoButton.clicked.connect(self.go_button)
     self.BackButton.clicked.connect(self.back_button)
     self.lineEdit.returnPressed.connect(self.go_button)

 def go_button(self):
    print("Button pressed")
    newURL = self.lineEdit.text()
    print("the New URL will be", newURL)

    if GlobalMem.backURL[1] == 'current':
        GlobalMem.backURL[1] = self.lineEdit.text()
    else:
        GlobalMem.backURL[0] = GlobalMem.backURL[1]
        GlobalMem.backURL[1] = newURL
        self.webView.setUrl(QUrl("http://" + newURL))


 def back_button(self):
    print(GlobalMem.backURL)
    self.webView.setUrl(QUrl("http://" + ''.join(GlobalMem.backURL[0])))
    self.lineEdit.setText(''.join(GlobalMem.backURL[0]))
    GlobalMem.backURL[2] = GlobalMem.backURL[0]
    GlobalMem.backURL[0] = GlobalMem.backURL[1]
    GlobalMem.backURL[1] = GlobalMem.backURL[2]


def main():
    app = QApplication(sys.argv)
    window = WebViewer()
    window.show()
    app.exec_()


if __name__ == '__main__':
 main()