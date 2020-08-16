from abc import ABC, abstractmethod
class shape (ABC) : # THIS CLASS WILL NOT ALLOW US TO MAKE OBJECT OF IT.
    @abstractmethod # THIS WILL ALLOW TO USE THIS FUNCTION MIDENTRY
    def printarea(self):
        return 0
class squre (shape) :
    def __init__(self):
        self.length = 3
        self.breadh = 4
    def printarea(self):                # IF WE REMOVE THESE TWO LINES THEN THERE WILL BE AN ERROR
        return self.length * self.breadh
an = squre()