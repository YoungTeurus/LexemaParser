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
    input_str2 = "( a xor  b ) == "

    _, _, output_lexema_list = Parcer.parse_string(input_str2)

    print(output_lexema_list)
