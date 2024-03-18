class Vectors:

    vect = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Vectors.vect.append(self)

    def modulus(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __gt__(self, instance):
        return self.modulus > instance
    
    def __repr__(self):
        return f'{self.x}i, {self.y}j'
    
vector_1 = Vectors(3, 5)
vector_2 = Vectors(4, 8)
print(vector_1)
print(vector_2)
print(Vectors.vect)

print(vector_1.modulus())
print(vector_2.modulus())

# print(vector_1.modulus > vector_2.modulus)