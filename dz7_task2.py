# Урок 7. Функции высшего порядка
# Задание 1 необязательное Сделайте локальный чат-бот 
# с внешним хранилищем. Тема чат-бота - любая вам интересная.


#                   ВАРИАНТ ДЛЯ КОНСОЛИ НАЧАЛО
from random import *
import json

def load():
    with open("films.json","r", encoding="utf-8") as fh:
        global films 
        films = json.load(fh)
    print("Фильмотека была успешно загружена из films.json")

def save():
    with open("films.json","w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii="False"))
    print("Фильмотека успешно сохранена в файле films.json")

try:
    load()
except:
    films=[]
    films.append("Чужой")
    films.append("Назад в будущее")
    films.append("Пятый элемент")
    films.append("Начало")
    films.append("Интерстеллар")

while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот фильмотека начал свою работу")
    elif command == "/stop":
        save()
        print("Бот закончил свою работу. Буду рад видет Вас снова!")
        break
    elif command == "/all":
        print("Текущий список фильмов:")
        print(', '.join(elem for elem in films))
    elif command == "/add":
        films.append(input("Введите название фильма: "))
        print(f"Фильм ''{films[-1]}'' добавлен в список")
        save()
    elif command == "/help":
        print("Список команд:")
        print("/start   Начало работы бота")
        print("/stop    Остановка бота")
        print("/all     Вывод текущего списка фильмов")
        print("/add     Добавление нового фильма в список")
        print("/delete  Удалить фильм из списка")
        print("/random  Выбрать случайный фильм из списка")
        print("/save    Сохранить список")
        print("/load    Загрузить список")
        print("/help    Вывод данного списка комманд")
    elif command == "/delete":
        delFilm = input("Введите название фильма, который надо удалить из списка: ")
        '''
        if delFilm in films:
            films.remove(delFilm)
            print(f"Фильм ''{delFilm}'' удален из списка")
        else:
            print(f"Фильм ''{delFilm}'' отсутствует в списке")
        '''
        try:
            films.remove(delFilm)
            print(f"Фильм ''{delFilm}'' удален из списка")
        except:
            print(f"Фильм ''{delFilm}'' отсутствует в списке")
        save()
    elif command == "/random":
        print("Случайный выбор!")
        # print(films[randint(0, len(films)-1)])  #вариант
        print(choice(films))
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Такой команды нет. Изучите, пожалуйста, руководство пользователя. Команда /help")

#                   ВАРИАНТ ДЛЯ КОНСОЛИ КОНЕЦ


# from random import *
# import json
# import sys
# from functools import reduce
# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtGui import QIcon
# from ui_bot import Ui_MainWindow

# command="/start"

# class BotTool(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(BotTool, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.init_UI()
    
#     def init_UI(self):
#         self.setWindowTitle('Чат-бот о фильмах')   
#         global command
#         command == "/start"
#         self.ui.startButton.clicked.connect(self.startBot)
#         # self.ui.sendButton.clicked.connect(self.comandChoice)

#         self.lineEdit.setDisabled(True)
#         self.top_btn.clicked.connect(self.inputFunc)
#         self.lineEdit.returnPressed.connect(self.process)

#     def inputFunc(self):
#         self.lineEdit.setDisabled(False)
#         # self.textBrowser.setText("Welcome to #1 button. what do you want to do?")

#     def process(self):
#         global command
#         command = self.lineEdit.text()
#         if command == "":
#             self.textBrowser.append("Ok i will leave you alone")
#             #self.close()
#         else:
#             self.textBrowser.append("say what?")
#         self.lineEdit.clear()


#     def comandChoice(self):
#         global command

#         command = self.ui.lineEdit.text()
        

#     def startBot(self):
#         # print("BOT: Бот фильмотека начал свою работу")
#         self.ui.textEdit.setText("BOT: Бот фильмотека начал свою работу")

#     def load():
#         with open("films.json","r", encoding="utf-8") as fh:
#             global films 
#             films = json.load(fh)
#         print("Фильмотека была успешно загружена из films.json")

#     def save():
#         with open("films.json","w", encoding="utf-8") as fh:
#             fh.write(json.dumps(films, ensure_ascii="False"))
#         print("Фильмотека успешно сохранена в файле films.json")

#     try:
#         load()
#     except:
#         films=[]
#         films.append("Чужой")
#         films.append("Назад в будущее")
#         films.append("Пятый элемент")
#         films.append("Начало")
#         films.append("Интерстеллар")

#     def botProcess(self):
#         global command
        
#         while True:
#             if command == "/start":
#                 self.ui.textEdit.setText("BOT: Бот фильмотека начал свою работу")
#                 # print("Бот фильмотека начал свою работу")
#             elif command == "/stop":
#                 self.save()
#                 print("Бот закончил свою работу. Буду рад видет Вас снова!")
#                 break
#             elif command == "/all":
#                 print("Текущий список фильмов:")
#                 print(', '.join(elem for elem in films))
#             elif command == "/add":
#                 films.append(input("Введите название фильма: "))
#                 print(f"Фильм ''{films[-1]}'' добавлен в список")
#                 self.save()
#             elif command == "/help":
#                 print("Список команд:")
#                 print("/start   Начало работы бота")
#                 print("/stop    Остановка бота")
#                 print("/all     Вывод текущего списка фильмов")
#                 print("/add     Добавление нового фильма в список")
#                 print("/delete  Удалить фильм из списка")
#                 print("/random  Выбрать случайный фильм из списка")
#                 print("/save    Сохранить список")
#                 print("/load    Загрузить список")
#                 print("/help    Вывод данного списка комманд")
#             elif command == "/delete":
#                 delFilm = input("Введите название фильма, который надо удалить из списка: ")
#                 '''
#                 if delFilm in films:
#                     films.remove(delFilm)
#                     print(f"Фильм ''{delFilm}'' удален из списка")
#                 else:
#                     print(f"Фильм ''{delFilm}'' отсутствует в списке")
#                 '''
#                 try:
#                     films.remove(delFilm)
#                     print(f"Фильм ''{delFilm}'' удален из списка")
#                 except:
#                     print(f"Фильм ''{delFilm}'' отсутствует в списке")
#                 self.save()
#             elif command == "/random":
#                 print("Случайный выбор!")
#                 # print(films[randint(0, len(films)-1)])  #вариант
#                 print(choice(films))
#             elif command == "/save":
#                 self.save()
#             elif command == "/load":
#                 self.load()
#             else:
#                 print("Такой команды нет. Изучите, пожалуйста, руководство пользователя. Команда /help")

# app = QtWidgets.QApplication([])
# application = BotTool()
# application.show()
 
# sys.exit(app.exec())