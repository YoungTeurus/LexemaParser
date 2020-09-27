from Classes.HashTableCompareFunctions import str_object_lexema_compare
from Classes.HashFunction import UniversalHashFunction_ForString
from Classes.HashTable import HashTable
from Classes.Lexema import Lexema

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # window = ParserWindow()
    # window.show()
    # app.exec_()

    hash_table_size = 255  # Длина хеш-таблицы
    hash_function = UniversalHashFunction_ForString(hash_table_size)
    hash_table = HashTable(hash_table_size, hash_function)

    str_lexemas = "how are you mate whats up bro howdy it's me your best friend flowey".split(' ')

    for i, obj in enumerate(str_lexemas):
        hash_table.insert(obj, Lexema(obj, i))

    for obj in str_lexemas:
        print(hash_table.get_value(obj, str_object_lexema_compare))
