import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QWidget, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt, QTime, QDateTime

'''
QMainWindow vs QWidget :
QMainWindow 자체의 layout 을 사용한다.
QHBoxlayout QVBoxlayout 같은 layout 사용못함
'''

class ExWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        # 툴팁
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        #QAction 
        exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction(QIcon('img/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+s')
        saveAction.setStatusTip('save application')

        printAction = QAction(QIcon('img/print.png'), 'Print', self)
        printAction.setShortcut('Ctrl+p')
        printAction.setStatusTip('Print application')

        editAction = QAction(QIcon('img/edit.png'), 'Edit', self)
        editAction.setShortcut('Ctrl+e')
        editAction.setStatusTip('edit application')
        
        #상태 바
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        # 메뉴 바
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # 간편 단축키(&) Alt + F 로 File 메뉴 단축키 설정
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        #툴바
        self.toolbar = self.addToolBar('MainToolBar')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(printAction)
        self.toolbar.addAction(editAction)

        # 버튼
        btn = QPushButton('Quit', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(100, 100)
        btn.resize(100,100)
        #btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        #현재 날짜 출력
        now = QDate.currentDate()
        print('default : ', now.toString())
        print('d.M.yy : ', now.toString('d.M.yy'))
        print('dd.MM.yyyy : ',now.toString('dd.MM.yyyy'))
        print('ddd.MMMM.yyyy : ', now.toString('ddd.MMMM.yyyy'))
        print('Qt.IS0Date :', now.toString(Qt.ISODate))
        print('Qt.DefaultLocaleLongDate : ', now.toString(Qt.DefaultLocaleLongDate))

        time = QTime.currentTime()
        print('default : ', time.toString)
        print('h.m.s : ', time.toString('h.m.s'))
        print('hh.mm.ss : ', time.toString('hh.mm.ss'))
        print('hh.mm.ss.zzz : ', time.toString('hh.mm.ss.zzz'))
        print('Qt.DefaultLocaleLongDate : ', time.toString(Qt.DefaultLocaleLongDate))
        print('Qt.DefaultLocaleShortDate : ', time.toString(Qt.DefaultLocaleShortDate))

        datetime = QDateTime.currentDateTime()
        print('datetime : ', datetime.toString())
        print(datetime.toString('d.M.yy hh:mm:ss'))
        print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
        print(datetime.toString(Qt.DefaultLocaleLongDate))
        print(datetime.toString(Qt.DefaultLocaleShortDate))

        self.setGeometry(400, 400, 400, 400)
        self.setWindowIcon(QIcon('img/web.png'))
        self.setWindowTitle('test Window')
        self.center()
        self.show()

    def center(self):
        # center로 창 옮기기
        # self.frameGeometry() 메서드를 이용하여 self 창의 위치와 크기 정보를 가저온다
        qr = self.frameGeometry()
        #사용하는 모니터 화면의 가운데 위치를 파악
        cp = QDesktopWidget().availableGeometry().center()
        #창의 중심위치를 화면의 중심위치로 이동한다
        qr.moveCenter(cp)
        #현재 창을 화면의 중심으로 이동했던 qr의 위치로 이동시킨다.
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExWindow()
    sys.exit(app.exec_())
