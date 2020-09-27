from typing import Dict, TypeVar, List, Tuple

from Classes.HashFunction import UniversalHashFunction_ForString
from Classes.HashTable import HashTable
from Classes.HashTableCompareFunctions import str_object_lexema_compare
from Classes.Lexema import Lexema, splitters

StrOrInt = TypeVar('StrOrInt', str, int)  # Тип для хранения строки или целого числа
StrLexemaList = List[str]  # Тип для хранения строки лексем
ObjLexemaList = List[Lexema]
OutObjLexemaList = ObjLexemaList
Str_ObjLexemaDict = Dict[str, Lexema]


DEFAULT_HASH_TABLE_SIZE = 255


def unique_list(_list: list):
    # Возвращает список, который содержит только уникальные значения из _list, сохраняя порядок.
    unique_list = list()
    for item in _list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


class Parcer:
    @staticmethod
    def prepare_string(input_string: str) -> str:
        """
        Метод подготавливает исходную строку для прохода парсера.
        Убирает все переносы строк.
        :param input_string: Исходная строка.
        :return: Изменённая строка.
        """
        return_str = input_string.replace("\n", "")
        # Заготовка для расширения.
        return return_str

    @staticmethod
    def get_lexemas(input_string: str) -> StrLexemaList:
        """
        Проходит про строке и разбивает её на лексемы. Лексемы могут повторяться.
         См. splitting_lexemas.
        :param input_string: Строка для прохода.
        :return: Список лексем в порядке, как в строке.
        """

        def is_start_of_any_reserved_lexema(char: str) -> bool:
            # Возвращает True, если переданная строка является началом любого оператора.
            for operator in splitters:
                if operator.startswith(char):
                    return True
            return False

        def is_any_reserved_lexema(char: str) -> bool:
            # Возвращает True, если переданная строка является любым оператором или разделителем.
            for operator in splitters:
                if char == operator:
                    return True
            return False

        return_list: StrLexemaList = list()

        string_len = len(input_string)

        lex_start = 0

        while lex_start < string_len:
            not_reserved_lexema = True
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
                            not_reserved_lexema = False
                        # Если лексема прерывается, начинаем обрабатывать её как обычную лексему
                        break
            if not_reserved_lexema:
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

        return return_list

    @staticmethod
    def get_object_lexema_list_and_str_object_lexema_hash_table(unique_str_lexema_list: StrLexemaList
                                                                ) -> Tuple[ObjLexemaList, HashTable]:
        """
        Возвращает два объекта: список объектов-лексем и словарь типа "строковая лексема - объект-лексема".
        :param unique_str_lexema_list: Список уникальных лексем
        :return: Tuple из двух элементов: списка объектов-лексем и хеш-таблицы, содержащей объекты-лексемы.
        """
        hash_table_size = DEFAULT_HASH_TABLE_SIZE  # Длина хеш-таблицы
        hash_function = UniversalHashFunction_ForString(hash_table_size)
        hash_table = HashTable(hash_table_size, hash_function)

        object_lexema_list = []
        for i, str_lexema in enumerate(unique_str_lexema_list):
            obj_lexema = Lexema(_char=str_lexema, _id=i)
            object_lexema_list.append(obj_lexema)  # Создаём список объектов-лексем
            hash_table.insert(str_lexema, obj_lexema)  # Добавляем в хеш-таблицу лексемы
        return object_lexema_list, hash_table

    @staticmethod
    def get_output_lexema_list(str_lexema_list: StrLexemaList, hash_table: HashTable):
        output_lexema_list = []
        for str_lexema in str_lexema_list:
            output_lexema_list.append(
                # Сопоставляем последовательность строковых лексем и лексем-объектов
                hash_table.get_value(str_lexema, str_object_lexema_compare)
            )

        return output_lexema_list

    @staticmethod
    def parse_string(input_string: str) -> Tuple[ObjLexemaList, HashTable, OutObjLexemaList]:
        """
        Осуществляет лексический разбор переданной строки, разбирая её на отдельные лексемы.
        :param input_string: Строка для разбора.
        :return: Tuple, содержащий список всех лексем, хеш-таблицу типа "строковая лексема - объект-лексема"
         и список представления исходной строки в виде последовательности лексем.
        """
        input_string = Parcer.prepare_string(input_string)  # 0. Убрать все переносы строк

        str_lexema_list = Parcer.get_lexemas(input_string)  # 1. Найти последовательность строковых лексем
        unique_str_lexema_list = unique_list(str_lexema_list)  # 2. Найти уникальные строковые лексемы
        # 3. Создаём список объектов-лексем
        # 4. Создаём словарь строковая лексема - объект-лексема
        object_lexema_list, hash_table = Parcer.get_object_lexema_list_and_str_object_lexema_hash_table(
            unique_str_lexema_list)
        output_lexema_list = Parcer.get_output_lexema_list(str_lexema_list, hash_table)

        return object_lexema_list, hash_table, output_lexema_list
