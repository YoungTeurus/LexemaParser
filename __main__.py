import sys
from PyQt5 import QtWidgets

from Lexema import Lexema
from ParserWindow import ParserWindow

from Parcer import Parcer, unique_list


if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # window = ParserWindow()
    # window.show()
    # app.exec_()

    input_str = "z=(x^2+1)*(y^2-1)+1"
    input_str2 = "true or false == true"

    _, _, output_lexema_list = Parcer.parse_string(input_str2)

    print(output_lexema_list)

#
    # _, output_lexema_list = Parcer.parse_string(input_str)
#
    # print(output_lexema_list)

    # str_lexema_list = Parcer.get_lexemas(input_str)  # 1. Найти последовательность строковых лексем
    # unique_str_lexema_list = unique_list(str_lexema_list)  # 2. Найти уникальные строковые лексемы
    # object_lexema_list = []
    # str_object_lexema_dict = dict()
    # for i, lexema in enumerate(unique_str_lexema_list):
    #     new_lexema = Lexema(_char=lexema, _id=i)
    #     object_lexema_list.append(new_lexema)  # 3. Создаём список объектов-лексем
    #     str_object_lexema_dict[lexema] = new_lexema  # 4. Создаём словарь строковая лексема - объект-лексема
#
    # output_lexema_list = []
    # for str_lexema in str_lexema_list:
    #     output_lexema_list.append(str_object_lexema_dict[str_lexema])  # 5. Сопоставляем последовательность строковых
    #     # лексем объектам-лексемам
#
    # print(input_str)
    # print(str_lexema_list)
    # print(unique_str_lexema_list)
#
    # print("{", end="")
    # for lex in str_object_lexema_dict:
    #     print(f"{lex}: {str(str_object_lexema_dict[lex])},", end="")
    # print("}")
#
    # for lex in output_lexema_list:
    #     print(str(lex), end="")
    # print()
