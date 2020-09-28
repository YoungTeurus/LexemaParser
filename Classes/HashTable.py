from typing import List, Optional, Callable
from Classes.HashTableCompareFunctions import default_compare
from Classes.HashFunction import IHashFunction


class HashTable:
    """
    Класс хеш-тиблицы, предназначенной для вставки и получения объектов с лучшей сложностью O(1).
    Используются универсальные хеш-ключи и открытая адрессация, как метод устранения коллизий.
    """
    _table_size: int = None
    _table: List[Optional[object]] = None
    _hash_function: IHashFunction = None

    def __init__(self, size: int, hash_function: IHashFunction):
        """
        Инициализирует хеш-таблицу, создавая массив размером size.
        Для всех последующих действий используется функция hash_function.
        :param size: Размер хеш-таблицы.
        :param hash_function: Хеш-функция.
        """
        self._table_size = size
        self._table = [None for x in range(size)]
        self._hash_function = hash_function

    def insert(self, key: object,
               value: object = None,
               # compare_func: Callable[[object, object], bool] = default_compare
               ) -> Optional[int]:
        """
        Вставляет объект в хеш-таблицу.
        В сложном случае: поиск по хеш-табилце происходит по key, осуществляется вставка value, используется функция
         compare_func для проверки объектов хещ-таблицы на соответствие value.
        В случае, если хеш-таблица полна, возвращается None, и объект не добавляется.
        :param key: Ключ для хеширования. Заносится в таблицу, если не указано value.
        :param value: (Необязательно) Объект, заносимый в хеш-таблицу вместо key.
      # :param compare_func: (Необязательно) Функция, с помощью которой проверяется соответствие хранимых объектов в
      #  хеш-таблице с value.
        :return: Возвращает индекс вставленного элемента в случае нахождения свободного места, или None,
         если хеш-таблица полна.
        """
        inserted_value = key if value is None else value

        calculated_hash = self._hash_function.hash(key)
        if self._table[calculated_hash] is None:
            self._table[calculated_hash] = inserted_value
            return calculated_hash
        elif not default_compare(self._table[calculated_hash], inserted_value):
            # Если ячейка занята чем-то, кроме этого же элемента, начинаем двигаться по таблице далее
            # в поисках свободной ячейки.
            actual_hash = (calculated_hash + 1) % self._table_size
            while self._table[actual_hash] is not None:
                actual_hash = (actual_hash + 1) % self._table_size
                # Если вернулись туда, откуда шли, значит таблица полна.
                if actual_hash == calculated_hash:
                    return None
            self._table[actual_hash] = inserted_value
            return actual_hash
        # Будет выполнено, если данный объект уже добавлен и находится на calculated_hash:
        return calculated_hash

    def get_index(self, key: object,
                  compare_func: Callable[[object, object], bool] = default_compare
                  ) -> Optional[int]:
        """
        Возвращает индекс объекта в хеш-таблице, если он был найден по ключу key.
        В сложном случае: проверка на совпадение объекта осуществляется с использованием функции compare_func.
        :param key: Ключ для поиска.
        :param compare_func: (Необязательно) Функция, с помощью которой проверяется соответствие хранимых объектов в
         хеш-таблице с key.
        :return: Индекс объекта в хеш-таблице или None, если он не был найден.
        """
        calculated_hash = self._hash_function.hash(key)
        # Если элемента точно нет:
        if self._table[calculated_hash] is None:
            return None
        # Если на месте элемента он сам:
        if compare_func(self._table[calculated_hash], key):
            return calculated_hash
        # Если на его месте что-то другое, ищем его дальше по таблице, пока не найдём его самого, или None,
        # или вернёмся в начальный индекс.
        actual_hash = (calculated_hash + 1) % self._table_size
        while not compare_func(self._table[actual_hash], key):
            actual_hash = (actual_hash + 1) % self._table_size
            if self._table[actual_hash] is None or actual_hash == calculated_hash:
                return None
        return actual_hash

    def get_value(self, key: object,
                  compare_func: Callable[[object, object], bool] = default_compare
                  ) -> Optional[object]:
        """
        Возвращает объект в хеш-таблице, если он был найден по ключу key.
        В сложном случае: проверка на совпадение объекта осуществляется с использованием функции compare_func.
        :param key: Ключ для поиска.
        :param compare_func: (Необязательно) Функция, с помощью которой проверяется соответствие хранимых объектов в
         хеш-таблице с key.
        :return: Найденный объект или None, если он не был найден.
        """
        object_index = self.get_index(key, compare_func)
        return self._table[object_index] if object_index is not None else None

    def get_table(self):
        """
        Возвращает саму хеш-таблицу. НЕ ДЛЯ РЕДАКТИРОВАНИЯ ИЛИ ПРЯМОГО ДОСТУПА!
        :return: Массив внутреннего представления хеш-таблицы.
        """
        return self._table
