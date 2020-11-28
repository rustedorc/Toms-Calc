class Convert:
    def __init__(self,x) :
        self.x = x

class Length(Convert) :
    def in_cm(self) :
        return self.x * 2.54

class Area(Convert):
    pass

class Volume(Convert) :
    pass

class Mass(Convert) :
    pass

class Velocity(Convert):
    pass

class Temp(Convert) :
    pass

q = Length(10)
print(q.in_cm())
