class AreaRect:

    def __int__(self, b, a):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b


area1 = AreaRect(6, 6)
area1.calculate_area()
