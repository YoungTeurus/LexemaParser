from typing import Dict, TypeVar, List, Tuple

from Integer import Integer
from Lexema import Lexema, splitting_lexemas

StrOrInt = TypeVar('StrOrInt', str, int)  # Тип для хранения строки или целого числа
StrLexemaList = List[str]  # Тип для хранения строки лексем
ObjLexemaList = List[Lexema]
Str_ObjLexemaDict = Dict[str, Lexema]


def unique_list(_list: list):
    # Возвращает список, который содержит только уникальные значения из _list, сохраняя порядок.
    unique_list = list()
    for item in _list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


class Parcer:

    @staticmethod
    def get_lexemas(input_string: str) -> StrLexemaList:
        """
        Проходит про строке и разбивает её на лексемы. Лексемы могут повторяться.
         См. splitting_lexemas.
        :param input_string: Строка для прохода.
        :return: Список лексем в порядке, как в строке.
        """

        def add_lexema(lex_start: int, lex_end: int):
            if lex_end - lex_start <= 0:
                # Если лексема пустое множество - не добавляем её
                return
            lexema_char = input_string[lex_start:lex_end]
            # print(f"Добавление в список лексемы '{lexema_char}'")
            # Добавление лексемы в список
            return_list.append(lexema_char)

        return_list: StrLexemaList = list()

        string_len = len(input_string)
        lex_start = 0

        for char_n, char in enumerate(input_string.replace(' ', '')):
            # print(f'Символ "{char}" - {char_n}')
            if char in splitting_lexemas:
                # print(f'Символ "{char}" является разделяющим')
                # Если символ является разделяющим, заканчиваем текущую лексему и начинаем новую
                add_lexema(lex_start, char_n)
                add_lexema(char_n, char_n+1)
                lex_start = char_n + 1
            elif char_n + 1 == string_len:
                # Если текущий символ последний
                add_lexema(lex_start, char_n + 1)

        return return_list

    @staticmethod
    def get_object_lexema_list_and_str_object_lexema_dict(unique_str_lexema_list: StrLexemaList) -> Tuple[ObjLexemaList, Str_ObjLexemaDict]:
        object_lexema_list = []
        str_object_lexema_dict = dict()
        for i, lexema in enumerate(unique_str_lexema_list):
            new_lexema = Lexema(_char=lexema, _id=i)
            object_lexema_list.append(new_lexema)  # Создаём список объектов-лексем
            str_object_lexema_dict[lexema] = new_lexema  # Создаём словарь строковая лексема - объект-лексема
        return object_lexema_list, str_object_lexema_dict

    @staticmethod
    def get_output_lexema_list(str_lexema_list: StrLexemaList, str_object_lexema_dict: Str_ObjLexemaDict):
        output_lexema_list = []
        for str_lexema in str_lexema_list:
            output_lexema_list.append(
                str_object_lexema_dict[str_lexema])  # Сопоставляем последовательность строковых

        return output_lexema_list

    @staticmethod
    def parse_string(input_string: str) -> Tuple[ObjLexemaList, ObjLexemaList]:
        """
        Осуществляет лексический разбор переданной строки, разбирая её на отдельные лексемы.
        :param input_string: Строка для разбора.
        :return: Tuple, содержащий список всех лексем и список представления исходной строки в виде
         последовательности лексем.
        """
        str_lexema_list = Parcer.get_lexemas(input_string)  # 1. Найти последовательность строковых лексем
        unique_str_lexema_list = unique_list(str_lexema_list)  # 2. Найти уникальные строковые лексемы
        # 3. Создаём список объектов-лексем
        # 4. Создаём словарь строковая лексема - объект-лексема
        object_lexema_list, str_object_lexema_dict = Parcer.get_object_lexema_list_and_str_object_lexema_dict(
            unique_str_lexema_list)
        output_lexema_list = Parcer.get_output_lexema_list(str_lexema_list, str_object_lexema_dict)

        return object_lexema_list, output_lexema_list

    # @staticmethod
    # def get_lexema_dict(lexema_list: StrLexemaList) -> LexemaDict:
    #     """
    #     Используя список лексем, возвращет словарь уникальных лексем вида:
    #         'лексема' : {id: 'int', type: 'str'}
    #     :param lexema_list: Список лексем.
    #     :return: Словарь лексем.
    #     """
    #     return_dict: LexemaDict = dict()
#
    #     unique_lexema_list = unique_list(lexema_list)
#
    #     for i, lexema in enumerate(unique_lexema_list):
    #         return_dict[lexema] = {'id': int(i), 'type': None}
#
    #     return return_dict
#
    # @staticmethod
    # def get_lexema_string(input_string: str, lexema_dict: LexemaDict) -> str:
#
    #     return_string: str = input_string
#
    #     for i, lexema in enumerate(lexema_dict):
    #         return_string = return_string.replace(lexema, '"Лексема {0}"'.format(lexema_dict[lexema]["id"]))
#
    #     return return_string
