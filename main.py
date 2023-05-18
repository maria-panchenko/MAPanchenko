from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sqlite3

Form, Window = uic.loadUiType("zayavki.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def podacha_zayavki():
    print(form.plainTextEdit.toPlainText())
    print(form.plainTextEdit_2.toPlainText())
    print(form.plainTextEdit_3.toPlainText())
    print(form.plainTextEdit_4.toPlainText())
    print(form.plainTextEdit_5.toPlainText())
    fio = form.plainTextEdit.toPlainText()
    telefon = form.plainTextEdit_2.toPlainText()
    marka = form.plainTextEdit_3.toPlainText()
    model = form.plainTextEdit_4.toPlainText()
    polomka = form.plainTextEdit_5.toPlainText()
    base(fio, telefon, marka, model, polomka)


form.pushButton.clicked.connect(podacha_zayavki)



def base(fio,telefon, marka, model, polomka):
    con = sqlite3.connect("base_klient.db")
    cur = con.cursor()
    query1 = """ INSERT INTO klient 
    VALUES (:fio, :telefon, :marka, :model, :polomka)"""
    cur.execute(query1, {'fio': fio, 'telefon': telefon, 'marka': marka, 'model': model, 'polomka': polomka})
    con.commit()

app.exec()
