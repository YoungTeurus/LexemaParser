import math
import random
from typing import Optional

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # window = ParserWindow()
    # window.show()
    # app.exec_()

    hash_table_size = 255  # Длина хеш-таблицы

    _hash_C = random.random()

    def hash_fun(input_str: str) -> int:
        if not type(input_str) == str:
            raise TypeError(f"Функция хеширования предназначена только для типа str, было передано"
                            f" {input_str.__class__}!")
        _sum: int = 0
        for char in input_str:
            _sum += ord(char)

        return math.floor(hash_table_size * ((_hash_C * _sum) % 1))

    hash_table = [None for x in range(hash_table_size)]

    def add_to_hash_table(item_to_add: str) -> int:
        # Пытается добавить item_to_add в хеш-таблицу, и при успехе возвращает индекс добавленного элемента.
        # Возбуждает исключение в случае неудачи.
        calculated_hash = hash_fun(item_to_add)
        if hash_table[calculated_hash] is None:
            hash_table[calculated_hash] = item_to_add
            return calculated_hash
        elif hash_table[calculated_hash] != item_to_add:
            # Если ячейка занята чем-то, кроме этого же элемента, начинаем двигаться по таблице далее,
            # ища свободную ячейку.
            actual_hash = calculated_hash + 1
            while hash_table[actual_hash] is not None:
                actual_hash = (actual_hash + 1) % hash_table_size
                if actual_hash == calculated_hash:
                    raise Exception("В хеш-таблице не осталось свободного места!")
            hash_table[actual_hash] = item_to_add
            return actual_hash

    def get_from_hash_table(item_to_get: str) -> Optional[int]:
        # Пытается найти индекс item_to-get в хеш-таблице, и при успехе возвращает его.
        # Возвращает None, если элемент не был найден
        calculated_hash = hash_fun(item_to_get)
        if hash_table[calculated_hash] is None:
            return None
        if hash_table[calculated_hash] == item_to_get:
            return calculated_hash
        actual_hash = calculated_hash + 1
        while hash_table[actual_hash] != item_to_get:
            actual_hash = (actual_hash + 1) % hash_table_size
            if actual_hash == calculated_hash:
                return None
        return actual_hash


    sample_1 = "x"
    sample_2 = "xor"
    sample_3 = "2.8"

    print(add_to_hash_table(sample_1))
    print(add_to_hash_table(sample_2))
    print(add_to_hash_table(sample_3))

    print(get_from_hash_table(sample_1))
    print(get_from_hash_table(sample_2))
    print(get_from_hash_table(sample_3))
