# Указанные ниже лексемы разделяют строку на отдельные лексемы:
splitting_lexemas = [
    '+', '-', '*', '/',
    '=', '(', ')', '^',
    '<', '>', ',', ';',
    '{', '}'
]

INT_CONST = 'Целочисленная константа'
FLOAT_CONST = 'Вещественная константа'
VARIABLE = 'Переменная'
OPEARATOR = 'Оператор/разделитель'

possible_types = [
    INT_CONST, FLOAT_CONST, VARIABLE, OPEARATOR
]


class Lexema:

    char: str = None  # Строковое представление лексемы
    id: int = None  # Id лексемы
    type: str = None  # Тип лексемы

    def __init__(self, _char: str = None, _id: int = None):
        self.char = _char
        self.id = _id

        if self.char is not None:
            self.determine_lexema_type()

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.char in splitting_lexemas:
            return self.char
        if self.id is not None:
            return f"'Лексема {self.id}'"
        else:
            return f"'Лексема {self.char}'"

    def determine_lexema_type(self):
        if self.char in splitting_lexemas:
            self.type = OPEARATOR
            return
        try:
            _ = int(self.char)
            self.type = INT_CONST
            return
        except ValueError:
            pass
        try:
            _ = float(self.char)
            self.type = FLOAT_CONST
            return
        except ValueError:
            pass
        self.type = VARIABLE
