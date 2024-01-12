# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Ferry:
    def __init__(self, name: str, capacity: int, passengers: int):
        """
        Создание и подготовка к работе класса "Паром"

        :param name: Название парома
        :param capacity: Пассажировместимость парома
        :param passengers: Количество пассажиров

        Примеры:
        >>> ferry = Ferry('Alfa', 250, 0)#Иницмализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError('Название парома должно быть словом')
        self.name = name


        if not isinstance(capacity, int):
            raise TypeError('Пассажировместимость парома должна быть целым числом')
        if capacity <= 0:
            raise ValueError('Пассажировместимость парома должна быть положительным числом')
        self.capacity = capacity


        if not isinstance(passengers, int):
            raise TypeError('Количество пассажиров должно быть целым числом')
        if passengers < 0:
            raise ValueError('Количество пассажиров не может быть отрицательным числом')
        if passengers > capacity:
            raise ValueError('Перегрузка парома не допустима! ')
        self.passengers = passengers

    def is_vacant_seats(self, capacity: int, passengers: int) -> int:
        """
        Функция определяет количество свободных мест

        :return: Количество свободных мест

        Примеры:

        >>> ferry = Ferry('Beta', 250, 100)
        >>> ferry.is_vacant_seats(300, 210)
        90
        """
        vacant_seats = capacity - passengers
        if vacant_seats > 0:
            return vacant_seats
        else:
            raise ValueError('Свободных мест нет')

    def take_on_board(self, capacity: int, passengers: int, plus_passengers: int) -> int:

        """
        Принять новых пассажиров на борт

        :param plus_passengers: Количество новых пассажиров
        raise ValueError: Если количество новых пассажиров больше числа свободных мест

        Примеры:

        >>> ferry = Ferry('Beta', 250, 100)
        >>> ferry.take_on_board(250,50,100)
        (100, 150)
        """
        vacant_seats = capacity - passengers
        if vacant_seats >= plus_passengers:
            vacant_seats -= plus_passengers
            passengers += plus_passengers
            return vacant_seats, passengers
        else:
            raise ValueError('Количество новых пассажиров больше числа свободных мест')

    def disembark(self, capacity: int, passengers: int, minus_passengers: int) -> int:
        """
        Высадить пассажиров

        :param minus_passengers: Количество высаживающихся пассажиров

        Raise ValueError:Если количество высаживающихся пассажиров больше чем
        пассажиров на борту, то вызываем ошибку

        Примеры:

        >>> ferry = Ferry('Beta', 250, 100)
        >>> ferry.disembark(250,100, 50)
        (200, 50)
        """
        vacant_seats = capacity - passengers
        if minus_passengers <= passengers:
            vacant_seats += minus_passengers
            passengers -= minus_passengers
            return vacant_seats, passengers
        else:
            raise ValueError('На борту нет такого количества пассажиров!')



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
