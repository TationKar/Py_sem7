# Урок 7. Функции высшего порядка
# Задача 36: Напишите функцию вывода таблицы умножения print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и 
# num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов 
# идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y)
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

#                   ВАРИАНТ ДЛЯ КОНСОЛИ НАЧАЛО
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         print(''.join(f'{elem:<5}' for elem in [operation(i, j) for j in range(1, num_columns + 1)]))

# print_operation_table(lambda x, y: x * y)
#                   ВАРИАНТ ДЛЯ КОНСОЛИ КОНЕЦ

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from ui_tbl import Ui_MainWindow

rows = 1
columns = 1
result_text = ""

class TableMult(QtWidgets.QMainWindow):
    def __init__(self):
        super(TableMult, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Таблица умножения') 
        self.ui.rows.setPlaceholderText('1')
        self.ui.clmn.setPlaceholderText('1')   

        self.ui.resButton.clicked.connect(self.TableToolPrint)

    def TableToolPrint(self):
        global rows
        global columns
        rows = int(self.ui.rows.text())
        columns = int(self.ui.clmn.text())

        def print_operation_table(operation, num_row = rows, num_columns = columns):
            global result_text

            for i in range(1, num_row+1):
                result_text+= (''.join(f'{elem:<5}' for elem in [operation(i, j) for j in range(1, num_columns+1)]))
                result_text+="\n"
            return result_text
        
        self.ui.table_res.clear
        self.ui.table_res.setPlainText(print_operation_table(lambda x, y: x * y))
        global result_text
        result_text=""


app = QtWidgets.QApplication([])
application = TableMult()
application.show()
 
sys.exit(app.exec())