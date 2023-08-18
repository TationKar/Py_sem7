# Урок 7. Функции высшего порядка
# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает 
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 

#                   ВАРИАНТ ДЛЯ КОНСОЛИ НАЧАЛО
# from functools import reduce
# def vowcounter(symbols):
#     def vow(str):
#         return reduce(lambda x, y:x+y, list(map(str.lower().count, symbols)))
#     return vow
# vowels = "аеёийоуэюя"
# rithm = input("Введите стихотворение Винни, на русском языке: ",).split()
# vc = vowcounter(vowels)
# vowcount=list(map(lambda item: vc(item), rithm))
# print("Парам пам-пам") if len(set(vowcount))==1 else print("Пам парам")
#                   ВАРИАНТ ДЛЯ КОНСОЛИ КОНЕЦ


import sys
from functools import reduce
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from ui_Winnie import Ui_MainWindow

def vowcounter(symbols):
    def vow(str):
        return reduce(lambda x, y:x+y, list(map(str.lower().count, symbols)))
    return vow

class WinniePooh(QtWidgets.QMainWindow):
    def __init__(self):
        super(WinniePooh, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Поэзия Виини-Пуха') 
        self.ui.input_text.setPlaceholderText('Введите стихотворение')     
        self.ui.pushButton.clicked.connect(self.rithmTool)

    def rithmTool(self):

        vowels = "аеёийоуэюя"
        input_text = self.ui.input_text.text()
        rithm = input_text.split()
        vc = vowcounter(vowels)
        vowcount=list(map(lambda item: vc(item), rithm))
        if len(set(vowcount))==1:
            self.ui.result.setText(str("Парам пам-пам"))
        else:
            self.ui.result.setText(str("Пам парам"))

app = QtWidgets.QApplication([])
application = WinniePooh()
application.show()
 
sys.exit(app.exec())