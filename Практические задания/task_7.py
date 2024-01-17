class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
                    )
    @staticmethod
    def is_leap_year(year: int) -> bool:

        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)


        """Проверяет, является ли год високосным"""
        # TODO реализовать метод

    def get_max_day(self, month: int, year: int)-> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""

        DAY_OF_MONTH = Date.DAY_OF_MONTH
        if self.is_leap_year(year):
            return DAY_OF_MONTH[1][month - 1]
        else:
            return DAY_OF_MONTH[0][month - 1]

    def is_valid_date(self, day: int, month: int, year: int)-> None:
        """Проверяет, является ли дата корректной"""
        ...  # TODO проверить валидность даты

        max_day = self.get_max_day(month, year)
        if day <= max_day:
            return "Эта дата правильная"
        else:
            return "Такой даты в этом месяце нет!"

if __name__ == '__main__':
    print(Date.is_leap_year(1920))
    print(Date.is_leap_year(1921))
    date = Date(29,2,1921)
    print(date.__dict__)
    print(date.is_valid_date(29, 2, 1921))


