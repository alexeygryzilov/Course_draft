class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date()

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        # TODO реализовать метод
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году

        if cls.is_leap_year(year):
            max_day = cls.DAY_OF_MONTH[1][month - 1]
        else:
            max_day = cls.DAY_OF_MONTH[0][month - 1]
        return max_day

    def is_valid_date(self):
        """Проверяет, является ли дата корректной"""

        # TODO проверить валидность даты
        max_day = self.get_max_day(self.month, self.year)
        if self.day <= max_day:
            return "Эта дата правильная"
        else:
            return "Такой даты не существует!"


print(Date.is_leap_year(1920))  # True
print(Date.is_leap_year(1921))  # False
print(Date.get_max_day(2, 1920))  # 29
print(Date.get_max_day(2, 1921))  # 28
date1 = Date(29, 2, 1920)
date2 = Date(29, 2, 1921)
print(date1.is_valid_date())  # Эта дата правильная
print(date2.is_valid_date())  # Такой даты не существует
