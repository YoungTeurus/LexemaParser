# Указанные ниже лексемы разделяют строку на отдельные лексемы:
splitters = [
    '+', '-', '*', '/',
    '=', '(', ')', '^',
    '<', '>', ',', ';',
    '{', '}', ':=', ' ',
    '=='
]

# Указанные ниже лексемы являются операторами в исходном языке
operators = [
    'not', 'xor', 'or', 'and', '=', ':=',
    '^', '+', '-', '*', '/', '=='
]

# Указанные ниже лексемы являются константами в исходном языке
bool_consts = [
    'true', 'false'
]

INT_CONST = 'Целочисленная константа'
FLOAT_CONST = 'Вещественная константа'
BOOL_CONST = 'Булева константа'
VARIABLE = 'Переменная'
OPERATOR = 'Оператор'
SPLITTER = 'Разделитель'

possible_types = [
    INT_CONST, FLOAT_CONST, VARIABLE, OPERATOR, SPLITTER, BOOL_CONST
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

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if self.type is not None:
            if self.type == INT_CONST or self.type == FLOAT_CONST:
                return f"Константа {self.id}"
            if self.type == BOOL_CONST:
                return f"Константа {self.char}"
            if self.type == VARIABLE:
                return f"Переменная {self.id}"
            if self.type == OPERATOR or self.type == SPLITTER:
                return f"{self.char}"
        # Если тип не установлен:
        return f"'Нераспознанная лексема {self.id}'"

    def determine_lexema_type(self) -> None:
        if self.char in operators:
            self.type = OPERATOR
            return
        if self.char in splitters:
            self.type = SPLITTER
            return
        if self.char in bool_consts:
            self.type = BOOL_CONST
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
