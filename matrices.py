# create a class to represent a 2 X 2 matrix
# it should have methods that allow the following
# addition, subtraction, multiplication by a scalar and determinant of a matrix

# matrix1 = (
# [a1, a2],
# [b1, b2]
# )

class Matrices:
    def __init__(self, a1, a2, b1, b2, i1, i2, j1, j2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        self.i1 = i1
        self.i2 = i2
        self.j1 = j1
        self.j2 = j2


    def matrix(self):
        mat_1 = (
            [self.a1, self.a2],
            [self.b1, self.b2]
        )
        return mat_1
    
    def mat2(self):
        mat_2 = (
            [self.i1, self.i2],
            [self.j1, self.j2]
        )
        return mat_2

    def addition(self):
        add = (
            [self.a1 + self.i1, self.a2 + self.i2],
            [self.b1 + self.j1, self.b2 + self.j2]
        )
        return add
    
    def subtraction(self):
        minus = (
            [self.a1 - self.i1, self.a2 - self.i2],
            [self.b1 - self.j1, self.b2 - self.j2]
        )
        return minus
    
    def multiplication(self, n):
        matx = (
            [n * self.a1, n * self.a2],
            [n * self.b1, n * self.b2]
        )
        return matx
    
    def determinant(self):
        matx = self.a1 * self.b2 - self.a2 * self.b1
        return matx

num = Matrices(3, -2, 7, 4, -3, 0, 7, -4)
print(num.matrix())
print(num.addition())
print(num.subtraction())
print(num.multiplication(4))
print(num.determinant())



        