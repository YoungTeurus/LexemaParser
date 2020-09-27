from Classes.Lexema import Lexema


def default_compare(stored_value: object, compared_value: object) -> bool:
    """
    Простейшее сравнение.
    :param stored_value: Хранимое значение в хеш-таблице.
    :param compared_value: Значение, с которым сравнивается stored_value.
    :return: True, если stored_value и compared_value совпадают. Иначе - False.
    """
    if stored_value is None:
        return False
    return stored_value == compared_value


def str_object_lexema_compare(stored_value: Lexema, compared_value: str) -> bool:
    """
    Сравнение строковой лексемы и объекта-лексемы.
    :param stored_value: Лексема-объект.
    :param compared_value: Строковая лексема.
    :return: True, если лексема-объект содержит строковую лексему в char.
    """
    if stored_value is None:
        return False
    return stored_value.char == compared_value
