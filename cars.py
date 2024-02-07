"""Программа для взаимодействия с объектами класса Car."""


class Car:
    """Стандартный класс машин."""

    def __init__(self, firm, series, number,
                 price, year, month, color, engine_volume) -> None:
        """Конструктор класса."""
        self.firm: str = firm
        self.model: [str, int] = [series, int(number)]
        self.price: int = int(price)
        self.date: [int, int] = [int(year), int(month)]
        self.color: str = color
        self.engine_volume: int = int(engine_volume)

    def __str__(self) -> str:
        """Описание объекта."""
        return (f"Автомобиль марки {self.firm}, {self.color} цвета, "
                f"дата выпуска - {self.date[1]}.{self.date[0]}, "
                f"стоимость - {self.price}, объем двигателя - "
                f"{self.engine_volume}, серия/номер - "
                f"{self.model[0]}/{self.model[1]}"
                )


def car_input() -> [Car]:
    """Функция ввода объектов класса Car."""
    cars = []
    print('Откуда взять информацию о машинах?')
    ans = input('text/file: ')
    if ans == 'text':
        num_car = int(input('Введите количество машин: '))
        for i in range(num_car):
            print(f'Введите информацию о машине {i+1}:')
            cars.append(Car(
                input('    Марка: '),
                input('    Серия: '),
                int(input('    Номер: ')),
                int(input('    Цена: ')),
                int(input('    Год выпуска: ')),
                int(input('    Месяц выпуска: ')),
                input('    Цвет: '),
                int(input('    Объем двигателя: '))
            ))
    elif ans == 'file':
        file = open(input('Введите имя файла: '))
        for i in file:
            cars.append(Car(*i.strip().split(' ')))
    else:
        raise ValueError('Некорректное значение')
    return cars


def save_to_file(info):
    """Функция для записи информауии в файл."""
    with open(input('Введите название файла: '), 'w') as file:
        for i in info:
            file.write(i)


def one_color_firms(car_list):
    """Функция для нахождения фирм, производящих автомобили заданного цвета."""
    color = input('Введите цвет: ')
    result = []
    for car in car_list:
        flag = 0
        if car.color == color:
            flag = 1
            for car2 in car_list:
                if (car != car2 and car2.firm == car.firm
                        and car2.color != color):
                    flag = 0
                    break
        if flag == 1 and car.firm not in result:
            result.append(car.firm)
    res = f'Фирмы, производящие машины только цвета {color}:\n'
    for firm in result:
        res += f'{firm}\n'
    return res


def sort_by_date(cars):
    """Функция сортировки автомобилей по дате выпуска."""
    cars.sort(key=lambda x: x.date)
    res = '\nМашины, отсортированные по дате выпуска:\n'
    for car in cars:
        res += f'{car}\n'
    return res


def main():
    """Основная функция."""
    cars = car_input()
    info = [one_color_firms(cars), sort_by_date(cars)]
    save_to_file(info)


if __name__ == '__main__':
    main()
