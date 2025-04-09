from Oar import Oar
from Passenger import Passenger
from Anchor import Anchor


class Boat:
    def __init__(self, maximum_capacity):
        self.maximum_capacity = maximum_capacity
        self.current_capacity = 0
        self.passengers = []
        self.anchor = Anchor()
        self.left_oar = Oar()
        self.right_oar = Oar()
        self.direction = None

    def add_passenger(self, passenger: Passenger):
        if passenger.weight + self.current_capacity <= self.maximum_capacity:
            self.current_capacity += passenger.weight
            self.passengers.append(passenger)
        else:
            print("Невозможно посадить человека")

    def remove_passenger(self, passenger: Passenger):
        if passenger in self.passengers:
            self.current_capacity -= passenger.weight
            self.passengers.remove(passenger)
        else:
            print("Такого пассажира нет на лодке")

    def attach_oars(self):
        self.right_oar.attach()
        self.left_oar.attach()


    def move(self, direction: str):
        match direction:
            case 'вперёд':
                self.right_oar.row()
                self.left_oar.row()
                self.direction = 'вперёд'
                print('Лодка движется вперёд')
            case 'назад':
                self.right_oar.row()
                self.left_oar.row()
                self.direction = 'назад'
                print('Лодка движется назад')
            case 'вправо':
                self.left_oar.row()
                self.direction = 'вправо'
                print('Лодка поворачивает направо')
            case 'влево':
                self.right_oar.row()
                self.direction = 'влево'
                print('Лодка поворачивает налево')

    def drop_anchor(self):
        self.direction = 'стоп'
        if self.anchor.is_dropped:
            return 'Якорь уже сброшен в воду'
        else:
            self.anchor.drop_anchor()
            return 'Якорь сброшен в воду'


    def raise_anchor(self):
        self.direction = None
        if self.anchor.is_dropped:
            self.anchor.raise_anchor()
            return 'Якорь поднят'
        else:
            return 'Якорь уже поднят'

    def get_passengers(self):
        return "Список пассажиров: {}".format(', '.join(*self.passengers))