class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self._day, self._month, self._year)

    @staticmethod
    # TODO какой декоратор следует применить?
    def is_leap_year(_year: int) -> bool:
        """Проверяет, является ли год високосным"""
        return (_year % 4 == 0 and _year % 100 != 0) or _year % 400 == 0

    @classmethod
    def get_max_day(cls, _month: int, _year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        ...  # TODO вернуть количество дней указанного месяца
        if cls.is_leap_year(_year):
            max_day = cls.DAY_OF_MONTH[1][_month - 1]
        else:
            max_day = cls.DAY_OF_MONTH[0][_month - 1]
        return max_day

    def is_valid_date(self, _day: int, _month: int, _year: int) -> None:
        """Проверяет, является ли дата корректной"""
        ...  # TODO если указанный набор день, месяц и год неверны, то вызвать ошибку ValueError
        max_day = self.get_max_day(self._month, self._year)
        if _day <= max_day:
            print('Эта дата правильная.')
        else:
            raise ValueError('Дата неправильная!')

    # TODO записать getter и setter для дня
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, new_day: int) -> None:
        if not isinstance(new_day, int):
            raise TypeError('День должен быть типа "int" - целочисленным.')
        if new_day <= 0:
            raise ValueError('День должен быть положительным числом..')
        if new_day > 31:
            raise ValueError('День не может быть больше 31.')
        self._day = new_day

    # TODO записать getter и setter для месяца
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, new_month: int) -> None:
        if not isinstance(new_month, int):
            raise TypeError('Месяц должен быть типа "int" - целочисленным.')
        if new_month < 1 or new_month > 12:
            raise ValueError('Месяц не может быть меньше 1 или больше 12.')
        self._month = new_month

    # TODO записать getter и setter для года
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year: int) -> None:
        if not isinstance(new_year, int):
            raise TypeError('Год должен быть типа "int" - целочисленным.')
        if new_year <= 0:
            raise ValueError('Год должен быть положительным числом..')
        self._year = new_year


data = Date(29, 2, 1920.4)
print(data.__dict__)

