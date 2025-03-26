class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(self,
                 message='Введено значение за границами игрового поля!'):
        super().__init__(message)


class CellOccupiedError(ValueError):

    def __init__(self,
                 message='Ячейка занята'):
        super().__init__(message)
