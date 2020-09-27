import math
import random


class IHashFunction:
    def hash(self, obj: object) -> int:
        return 0


# noinspection PyPep8Naming
class UniversalHashFunction_ForString(IHashFunction):
    """
    Универсальная хеш-функция для строк.
    """
    _C: float = None
    _hash_table_size: int = None

    def __init__(self, hash_table_size: int):
        self._C = random.random()
        self._hash_table_size = hash_table_size

    def hash(self, string: str) -> int:
        if not type(string) == str:
            raise TypeError(f"Функция хеширования предназначена только для типа str, было передано"
                            f" {string.__class__}!")
        _sum: int = 0
        for i, char in enumerate(string):
            _sum += ord(char) * (i // 13)

        return math.floor(self._hash_table_size *
                          ((self._C * _sum) % 1)
                          )
