import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.rabbit = QPixmap("images/rabbit.jpg")
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([
            QPoint(70,100), QPoint(100,110), QPoint(130,100), QPoint(100,150),
        ])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(0,127,0))
        p.drawPie(50,150,100,100,0,180 * 16)
        p.drawPolygon([
            QPoint(50,200), QPoint(150,200), QPoint(100,400),
        ])
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

    

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing 1")
        self.rabbit = QPixmap("images/rabbit.jpg")
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(10,10,10))
        p.setBrush(QColor(20,127,0))
        p.drawPolygon([
            QPoint(200,40), QPoint(160,110), QPoint(100,100),
        ])


        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(0,127,0))
        p.drawPie(50,150,100,100,0,180 * 16)
        p.drawPolygon([
            QPoint(50,200), QPoint(150,200), QPoint(100,400),
        ])
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

class Simple_drawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple GitHub Drawing 3")
        self.rabbit = QPixmap("images/rabbit.jpg")
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(10,10,10))
        p.setBrush(QColor(20,127,0))
        p.drawPolygon([
            QPoint(210,140), QPoint(60,10), QPoint(30,90),QPoint(20,20)
        ])


        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(30,127,20))
        p.drawPie(50,150,100,100,0,180 * 16)
        p.drawPolygon([
            QPoint(50,200), QPoint(150,200), QPoint(100,400),
        ])
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()


def main():
    app = QApplication(sys.argv)
    # w = Simple_drawing_window()
    # w1 = Simple_drawing_window1()
    w3 = Simple_drawing_window3()
    # w.show()
    # w1.show()
    w3.show()
    return app.exec()
    


    

if __name__ == "__main__":
    sys.exit(main())