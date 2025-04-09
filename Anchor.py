class Anchor:
    def __init__(self):
        self.is_dropped = False

    def drop_anchor(self):
        if self.is_dropped:
            print("Якорь уже сброшен")
        else:
            self.is_dropped = True
            print("Якорь сброшен в воду")

    def raise_anchor(self):
        if self.is_dropped:
            self.is_dropped = False
            print("Якорь поднят")
        else:
            print("Якорь уже поднят")