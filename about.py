from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

fontTitle = QFont("Arial", 24)
fontText = QFont("Arial", 14)

class Help(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hakkimizda")
        self.setGeometry(200,200,450,250)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout(self)
        textTitle = QLabel("Hakkimizda")
        textHakkimizda = QLabel("Bu sayfa hakkimizda sayfasi burada bizi ile ilgili tum bilgilere ulasabilirsiniz"
                                "Bu program udemy de ogrenci egitimi icin gelistirildi ve Python derslerini icerir...")
        textTitle.setFont(fontTitle)
        textHakkimizda.setFont(fontText)
        vbox.addWidget(textTitle)
        vbox.addWidget(textHakkimizda)
        self.setLayout(vbox)