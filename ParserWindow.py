from Classes.HashFunction import UniversalHashFunction_ForString
from Classes.HashTable import HashTable
from Classes.Parcer import Parcer
from UIs import ParserWindowUI3
from PyQt5 import QtWidgets


class ParserWindow(QtWidgets.QMainWindow, ParserWindowUI3.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_ParseInput.clicked.connect(self.parse_string_action)

    def parse_string_action(self) -> None:
        self.textBrowser_Log.clear()

        input_string = self.textEdit_InputText.toPlainText()
        if len(input_string) <= 0:
            self.textBrowser_Log.append("Строка для парса пуста!")
            return

        object_lexema_list, hash_table, output_lexema_list = Parcer.parse_string(input_string)

        output_str = ""
        for lexema in output_lexema_list:
            output_str += str(lexema) + " "

        self.textBrowser_Log.append("Строка успешно распарсена!")

        self.tableWidget_LexemasOut.clear()
        self.tableWidget_LexemasOut.setRowCount(len(object_lexema_list))
        self.tableWidget_LexemasOut.setColumnCount(3)
        self.tableWidget_LexemasOut.setHorizontalHeaderLabels(["Id лексемы", "Лексема", "Тип лексемы"])
        for i, lexema in enumerate(object_lexema_list):
            # Id лексемы
            self.tableWidget_LexemasOut.setItem(i, 0, QtWidgets.QTableWidgetItem(str(lexema.id)))
            # Лексема
            self.tableWidget_LexemasOut.setItem(i, 1, QtWidgets.QTableWidgetItem(lexema.char))
            # Тип лексемы
            self.tableWidget_LexemasOut.setItem(i, 2, QtWidgets.QTableWidgetItem(lexema.type))

        self.textBrowser_OutLexemas.setText(output_str)

        self.tableWidget_OutHashTable.clear()
        self.tableWidget_OutHashTable.setRowCount(0)
        self.tableWidget_OutHashTable.setColumnCount(2)
        self.tableWidget_OutHashTable.setHorizontalHeaderLabels(["Ключ в таблице", "Объект"])
        actual_row = 0
        for i, item in enumerate(hash_table.get_table()):
            if item is not None:
                self.tableWidget_OutHashTable.setRowCount(self.tableWidget_OutHashTable.rowCount() + 1)
                self.tableWidget_OutHashTable.setItem(actual_row, 0, QtWidgets.QTableWidgetItem(str(i)))
                self.tableWidget_OutHashTable.setItem(actual_row, 1, QtWidgets.QTableWidgetItem(str(item)))
                actual_row += 1

