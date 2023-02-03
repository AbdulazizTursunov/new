from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
matn = ""
app = QApplication([])
oyna = QWidget()
oyna.setFixedSize(360,510)
ekran = QLineEdit(oyna)
ekran.setGeometry(15,5,337,70)
ekran.setFont(QFont("Times",20))
ekran.setPlaceholderText("0")
oyna.setWindowTitle("GILAMLI KALKULYATOR")
oyna.setStyleSheet("background-color:blue;")
ekran.setStyleSheet("background-color:lightgreen") 

def func_bir():
    global matn
    matn += "1"
    ekran.setText(matn)

def func_ikki():
    global matn
    matn += "2"
    ekran.setText(matn)

def func_uch():
    global matn
    matn += "3"
    ekran.setText(matn)

def func_tort():
    global matn
    matn += "4"
    ekran.setText(matn)

def func_besh():
    global matn
    matn += "5"
    ekran.setText(matn)

def func_olti():
    global matn
    matn += "6"
    ekran.setText(matn)

def func_yetti():
    global matn
    matn += "7"
    ekran.setText(matn)

def func_sakkiz():
    global matn
    matn += "8"
    ekran.setText(matn)

def func_toqqiz():
    global matn
    matn += "9"
    ekran.setText(matn)

def func_nol():
    global matn
    matn += "0"
    ekran.setText(matn)

def func_bol():
    global matn
    matn += "/"
    ekran.setText(matn)

def func_kop():
    global matn
    matn += "*"
    ekran.setText(matn)

def func_plus():
    global matn
    matn += "+"
    ekran.setText(matn)

def func_minus():
    global matn
    matn += "-"
    ekran.setText(matn)

def func_ac():
    global matn
    matn = ""
    ekran.setText(matn)

def func_teng():
    global matn
    ekran.setText(str(eval(matn)))

def func_clear():
    global matn
    matn = matn[:-1]
    ekran.setText(matn)

def func_foiz():
    global matn
    matn += "%"
    ekran.setText(matn)

def func_nuqta():
    global matn
    matn += ","
    ekran.setText(matn)

def func_bekor():
    global matn 
    matn += "."
    ekran.setText(matn)

tugma_c = QPushButton("AC", oyna)
tugma_c.setGeometry(15, 80, 80, 80)
tugma_c.setFont(QFont("times", 30))
tugma_c.setStyleSheet("background-color:orange; border: 2px solid black; bordor radius: 45px")
tugma_c.clicked.connect(func_ac)

tugma_clear = QPushButton("<", oyna)
tugma_clear.setGeometry(100, 80, 80, 80)
tugma_clear.setFont(QFont("times", 30))
tugma_clear.setStyleSheet("background-color:darkblue; border: 2px solid black; border radius:45 px")
tugma_clear.clicked.connect(func_clear)

tugma_foiz = QPushButton("%", oyna)
tugma_foiz.setGeometry(185, 80, 80, 80)
tugma_foiz.setFont(QFont("times", 30))
tugma_foiz.setStyleSheet("background-color:yellow; border: 2px solid black; border radius:45 px")
tugma_foiz.clicked.connect(func_foiz)


tugma_boluv = QPushButton("/", oyna)
tugma_boluv.setGeometry(270, 80, 80, 80)
tugma_boluv.setFont(QFont("times", 30))
tugma_boluv.setStyleSheet("background-color:lightgreen; border: 2px solid black; border radius:45 px")
tugma_boluv.clicked.connect(func_bol)

tugma_kop = QPushButton("x", oyna)
tugma_kop.setGeometry(270, 165, 80, 80)
tugma_kop.setFont(QFont("times", 30))
tugma_kop.setStyleSheet("background-color:green; border: 2px solid black; border radius:45 px")
tugma_kop.clicked.connect(func_kop)

tugma_minus = QPushButton("-", oyna)
tugma_minus.setGeometry(270, 250, 80, 80)
tugma_minus.setFont(QFont("times", 30))
tugma_minus.setStyleSheet("background-color:red; border: 2px solid black; border radius:45 px")
tugma_minus.clicked.connect(func_minus)

tugma_plus = QPushButton("+", oyna)
tugma_plus.setGeometry(270, 335, 80, 80)
tugma_plus.setFont(QFont("times", 30))
tugma_plus.setStyleSheet("background-color:brown; border: 2px solid black; border radius:45 px")
tugma_plus.clicked.connect(func_plus)

tugma_barobar = QPushButton("=", oyna)
tugma_barobar.setGeometry(270, 420, 80, 80)
tugma_barobar.setFont(QFont("times", 30))
tugma_barobar.setStyleSheet("background-color:orange; border: 2px solid black; border radius:15 px")
tugma_barobar.clicked.connect(func_teng)

tugma_nuqta = QPushButton(",", oyna)
tugma_nuqta.setGeometry(185, 420, 80, 80)
tugma_nuqta.setFont(QFont("times", 30))
tugma_nuqta.setStyleSheet("background-color:brown; border: 2px solid black; border radius:45 px")
tugma_nuqta.clicked.connect(func_nuqta)

tugma_nol = QPushButton("0", oyna)
tugma_nol.setGeometry(100, 420, 80, 80)
tugma_nol.setFont(QFont("times", 30))
tugma_nol.setStyleSheet("background-color:red; border: 2px solid black; border radius:45 px")
tugma_nol.clicked.connect(func_nol)


tugma_nuqta = QPushButton(".", oyna)
tugma_nuqta.setGeometry(15, 420, 80, 80)
tugma_nuqta.setFont(QFont("times", 30))
tugma_nuqta.setStyleSheet("background-color:green; border: 2px solid black; border radius:45 px")
tugma_nuqta.clicked.connect(func_bekor)

tugma_bir = QPushButton("1", oyna)
tugma_bir.setGeometry(15, 335, 80, 80)
tugma_bir.setFont(QFont("times", 30))
tugma_bir.setStyleSheet("background-color:lightgreen; border: 2px solid black; border radius:45 px")
tugma_bir.clicked.connect(func_bir)

tugma_ikki = QPushButton("2", oyna)
tugma_ikki.setGeometry(100, 335, 80, 80)
tugma_ikki.setFont(QFont("times", 30))
tugma_ikki.setStyleSheet("background-color:green; border: 2px solid black; border radius:45 px")
tugma_ikki.clicked.connect(func_ikki)


tugma_uch = QPushButton("3", oyna)
tugma_uch.setGeometry(185, 335, 80, 80)
tugma_uch.setFont(QFont("times", 30))
tugma_uch.setStyleSheet("background-color:red; border: 2px solid black; border radius:45 px")
tugma_uch.clicked.connect(func_uch)


tugma_tort = QPushButton("4", oyna)
tugma_tort.setGeometry(15, 250, 80, 80)
tugma_tort.setFont(QFont("times", 30))
tugma_tort.setStyleSheet("background-color:yellow; border: 2px solid black; border radius:45 px")
tugma_tort.clicked.connect(func_tort)


tugma_besh = QPushButton("5", oyna)
tugma_besh.setGeometry(100, 250, 80, 80)
tugma_besh.setFont(QFont("times", 30))
tugma_besh.setStyleSheet("background-color:lightgreen; border: 2px solid black; border radius:45 px")
tugma_besh.clicked.connect(func_besh)

tugma_olti = QPushButton("6", oyna)
tugma_olti.setGeometry(185, 250, 80, 80)
tugma_olti.setFont(QFont("times", 30))
tugma_olti.setStyleSheet("background-color:green; border: 2px solid black; border radius:45 px")
tugma_olti.clicked.connect(func_olti)


tugma_yetti = QPushButton("7", oyna)
tugma_yetti.setGeometry(15, 165, 80, 80)
tugma_yetti.setFont(QFont("times", 30))
tugma_yetti.setStyleSheet("background-color:darkblue; border: 2px solid black; border radius:45 px")
tugma_yetti.clicked.connect(func_yetti)


tugma_sakkiz = QPushButton("8", oyna)
tugma_sakkiz.setGeometry(100, 165, 80, 80)
tugma_sakkiz.setFont(QFont("times", 30))
tugma_sakkiz.setStyleSheet("background-color:yellow; border: 2px solid black; border radius:45 px")
tugma_sakkiz.clicked.connect(func_sakkiz)

tugma_toqqiz = QPushButton("9", oyna)
tugma_toqqiz.setGeometry(185, 165, 80, 80)
tugma_toqqiz.setFont(QFont("times", 30))
tugma_toqqiz.setStyleSheet("background-color:lightgreen; border: 2px solid black; border radius:45 px")
tugma_toqqiz.clicked.connect(func_toqqiz)


oyna.show()
app.exec_()


