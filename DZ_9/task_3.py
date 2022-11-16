class Parallelogram:

    def get_area(self, width, length):
        return width * length

class Square(Parallelogram):

    def get_area(self, length):
        return length ** 2


fig1 = Parallelogram()
fig2 = Square()
print(fig1.get_area(20, 10))
print(fig2.get_area(10))
