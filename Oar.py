class Oar:
    def __init__(self):
        self.is_attached = False

    def attach(self):
        if self.is_attached:
            print("Вёсла уже закреплены")
        else:
            self.is_attached = True
            print("Вёсла закреплены")

    def row(self):
        if not self.is_attached:
            raise RuntimeError('Сначала закрепите вёсла!')