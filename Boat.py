from Oar import Oar
from Passenger import Passenger
from Anchor import Anchor


class Boat:
    def __init__(self, maximum_capacity, current_capacity):
        self.maximum_capacity = maximum_capacity
        self.current_capacity = current_capacity
        self.passengers = []
        self.anchor = Anchor()
        self.left_oar = Oar()
        self.right_oar = Oar()

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


    def move(self, direction: str):
        match direction:
            case 'вперёд':
                self.right_oar.row()
                self.left_oar.row()
                print('Лодка движется вперёд')
            case 'назад':
                self.right_oar.row()
                self.left_oar.row()
                print('Лодка движется назад')
            case 'вправо':
                self.left_oar.row()
                print('Лодка поворачивает направо')
            case 'влево':
                self.right_oar.row()
                print('Лодка поворачивает налево')

    def drop_anchor(self):
        self.anchor.drop_anchor()

    def raise_anchor(self):
        self.anchor.raise_anchor()

    def get_status(self):
        return "Список пассажиров: {}".format(', '.join(*self.passengers))