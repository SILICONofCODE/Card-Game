from random import shuffle
class card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2","A","5","6","8","9","10","Jack","Queen","King","Ace"]
    def __init__(self, v, s):
        self.value = v
        self.suit = s