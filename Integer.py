class Integer:
    _int: int = None

    def __init__(self, _int: int = None):
        if _int is not None:
            self._int = _int

    def __int__(self):
        assert self._int is not None
        return self._int

    def add(self, other: int):
        self._int += other
