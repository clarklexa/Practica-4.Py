
class Operaciones:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b 

 
#


x = int(input('Ingrese el primer número: '))
y = int(input('Ingrese el segundo número: '))


op = Operaciones(x,y)


print(f'La suma de los numeros es: {op.sumar()}')
print(f'La resta de los numeros es: {op.restar()}')
print(f'La multiplicación de los numeros es: {op.multi()}')
print(f'La división de los numeros es: {op.div()}')






