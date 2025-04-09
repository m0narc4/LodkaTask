class Anchor:
    def __init__(self):
        self.is_dropped = False

    def drop_anchor(self):
        self.is_dropped = True

    def raise_anchor(self):
        self.is_dropped = False