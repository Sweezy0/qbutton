import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
verdana_font=QFont("Verdana",15)
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Başlık")
        self.setGeometry(400,100,600,400)
        self.arayuz()
    
    def arayuz(self):
        self.yazi=QLabel("Giriş Ekranına Hoş Geldiniz", self)
        self.yazi.setFont(verdana_font)
        self.yazi.move(200,150)

        self.buton_giris=QPushButton("Giriş",self)
        self.buton_giris.setFont(verdana_font)
        self.buton_giris.move(200,200)
        self.buton_giris.clicked.connect(self.fonksiyon_giris)

        self.buton_cikis=QPushButton("Çıkış",self)
        self.buton_cikis.setFont(verdana_font)
        self.buton_cikis.move(300,200)
        self.buton_cikis.clicked.connect(self.fonksiyon_cikis)
        
        self.show()
    
    def fonksiyon_giris(self):
        self.yazi.resize(180,30)
        self.yazi.setText("Giriş butonuna basıldı")
        self.setWindowTitle("Giriş butonu aktif")
        self.buton_cikis.close()
    
    def fonksiyon_cikis(self):
        self.yazi.resize(200,30)
        self.yazi.setText("Çıkış butonuna basıldı")
        self.setWindowTitle("Çıkış butonu aktif")
        self.buton_giris.close()

uygulama=QApplication(sys.argv)
pencere=Pencere()
sys.exit(uygulama.exec_())