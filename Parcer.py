from typing import Dict, TypeVar, List, Tuple

from Integer import Integer
from Lexema import Lexema, splitters, operators

StrOrInt = TypeVar('StrOrInt', str, int)  # Тип для хранения строки или целого числа
StrLexemaList = List[str]  # Тип для хранения строки лексем
ObjLexemaList = List[Lexema]
OutObjLexemaList = ObjLexemaList
Str_ObjLexemaDict = Dict[str, Lexema]


def unique_list(_list: list):
    # Возвращает список, который содержит только уникальные значения из _list, сохраняя порядок.
    unique_list = list()
    for item in _list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


class Parcer:
    all_reserved_lexemas: List[str] = None

    @staticmethod
    def build_all_possible_lexemas() -> None:
        if Parcer.all_reserved_lexemas is None:
            Parcer.all_reserved_lexemas = list()
            Parcer.all_reserved_lexemas.extend(splitters)
            Parcer.all_reserved_lexemas.extend(operators)

    @staticmethod
    def get_lexemas(input_string: str) -> StrLexemaList:
        """
        Проходит про строке и разбивает её на лексемы. Лексемы могут повторяться.
         См. splitting_lexemas.
        :param input_string: Строка для прохода.
        :return: Список лексем в порядке, как в строке.
        """

        # def add_lexema(lex_start: int, lex_end: int):
        #     if lex_end - lex_start <= 0:
        #         # Если лексема пустое множество - не добавляем её
        #         return
        #     lexema_char = input_string[lex_start:lex_end]
        #     # print(f"Добавление в список лексемы '{lexema_char}'")
        #     # Добавление лексемы в список
        #     return_list.append(lexema_char)

        # def is_start_of_any_lexemas(char: str) -> bool:
        #     # Возвращает True, если переданная строка является началом любой предопределённой
        #     # лексемы.
        #     for lexema in Parcer.all_possible_lexemas:
        #         if lexema.startswith(char):
        #             return True
        #     return False
        #
        # def is_any_lexema(char: str) -> bool:
        #     # Возвращает True, если переданная строка совпадает с любой предопределённой лексемой.
        #     for lexema in Parcer.all_possible_lexemas:
        #         if lexema == char:
        #             return True
        #     return False

        # Parcer.build_all_possible_lexemas()

        def is_start_of_any_reserved_lexema(char: str) -> bool:
            # Возвращает True, если переданная строка является началом любого оператора.
            for operator in Parcer.all_reserved_lexemas:
                if operator.startswith(char):
                    return True
            return False

        def is_any_reserved_lexema(char: str) -> bool:
            # Возвращает True, если переданная строка является любым оператором или разделителем.
            for operator in Parcer.all_reserved_lexemas:
                if char == operator:
                    return True
            return False

        Parcer.build_all_possible_lexemas()

        return_list: StrLexemaList = list()

        string_len = len(input_string)

        lex_start = 0

        while lex_start < string_len:
            current_lexema = input_string[lex_start]
            # Если встретили отдельный пробел, просто пропускаем его:
            if current_lexema == ' ':
                lex_start += 1
                continue
            # Если новая лексема начинается с символа, который есть у опреатора:
            if is_start_of_any_reserved_lexema(current_lexema):
                # Начинаем искать конец оператора
                next_char_i = lex_start + 1
                while next_char_i < string_len:
                    next_char = input_string[next_char_i]
                    if is_start_of_any_reserved_lexema(current_lexema + next_char):
                        # Если вместе со следующим символом лексе всё ещё является зарезервированной...
                        current_lexema += next_char
                        next_char_i += 1
                        lex_start += 1
                    else:
                        if is_any_reserved_lexema(current_lexema):
                            # Если уже составили сплиттер, прекращаем обход
                            break
                        # TODO: избежать повторения кода.
                        # Если лексема прерывается, начинаем обрабатывать её как обычную лексему
                        # next_char_i = lex_start + 1
                        # Если это обычная лексема:
                        while next_char_i < string_len and (next_char := input_string[next_char_i]) not in splitters:
                            # Пока не встретили сплиттер
                            current_lexema += next_char
                            next_char_i += 1
                            lex_start += 1
                        break
            else:
                next_char_i = lex_start + 1
                # Если это обычная лексема:
                while next_char_i < string_len and (next_char := input_string[next_char_i]) not in splitters:
                    # Пока не встретили сплиттер
                    current_lexema += next_char
                    next_char_i += 1
                    lex_start += 1
            # Когда дошли до конца лексемы
            lex_start += 1
            return_list.append(current_lexema)

        # current_index = 0
        # was_last_lexema_operator = True
        #
        # while True:
        #     # Текущий символ:
        #     current_char = input_string[current_index]
        #     # Является ли очередной символ началом какого-либо оператора?
        #     if is_start_of_any_lexemas(current_char):
        #         # Да
        #         # Занести в список лексем
        #         # return_list.append(current_char)
        #         while True:
        #             # Если текущий набор символов + следующий символ - одна из предопределённых лексем?
        #             if is_start_of_any_lexemas(current_char + input_string[current_index+1]):
        #                 # Да
        #                 current_char += input_string[current_index+1]
        #                 current_index += 1
        #             # Нет
        #             break
        #         if is_any_lexema(current_char):
        #             was_last_lexema_operator = True
        #             continue
        #     # Нет
        #
        #     # Является ли последняя лексема оператором?
        #     if was_last_lexema_operator:
        #         # Да
        #         # Создаём новую лексему
        #         return_list.append(current_char)
        #         was_last_lexema_operator = False
        #         pass
        #     else:
        #         # Нет
        #         # Добавляем текущий символ к прошлому
        #         return_list[len(return_list)-1] += current_char
        #
        #     current_index += 1  # Переход к следующему символу

        return return_list

    @staticmethod
    def get_object_lexema_list_and_str_object_lexema_dict(unique_str_lexema_list: StrLexemaList) -> Tuple[
        ObjLexemaList, Str_ObjLexemaDict]:
        """
        Возвращает два объекта: список объектов-лексем и словарь типа "строковая лексема - объект-лексема".
        :param unique_str_lexema_list: Список уникальных лексем
        :return: Tuple из двух элементов: списка объектов-лексем и словаря типа "строковая лексема - объект-лексема".
        """
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
    def parse_string(input_string: str) -> Tuple[ObjLexemaList, Str_ObjLexemaDict, OutObjLexemaList]:
        """
        Осуществляет лексический разбор переданной строки, разбирая её на отдельные лексемы.
        :param input_string: Строка для разбора.
        :return: Tuple, содержащий список всех лексем, словарь типа "строковая лексема - объект-лексема"
         и список представления исходной строки в виде последовательности лексем.
        """
        str_lexema_list = Parcer.get_lexemas(input_string)  # 1. Найти последовательность строковых лексем
        unique_str_lexema_list = unique_list(str_lexema_list)  # 2. Найти уникальные строковые лексемы
        # 3. Создаём список объектов-лексем
        # 4. Создаём словарь строковая лексема - объект-лексема
        object_lexema_list, str_object_lexema_dict = Parcer.get_object_lexema_list_and_str_object_lexema_dict(
            unique_str_lexema_list)
        output_lexema_list = Parcer.get_output_lexema_list(str_lexema_list, str_object_lexema_dict)

        return object_lexema_list, str_object_lexema_dict, output_lexema_list

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
