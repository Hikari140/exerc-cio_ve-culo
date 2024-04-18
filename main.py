from modelos.carro import Carro
from modelos.moto import Moto

c1 = Carro('Toyota', 'Corolla', 4)
c2 = Carro('Honda', 'Civic', 2)
c3 = Carro('Ford', 'Fusion', 4)

m1 = Moto('Haley-Davidson', 'Street 750', 'Esportiva')
m2 = Moto('Honda', 'CB 500', 'Casual')
m3 = Moto('Yamaha', 'NT-09', 'Esportiva')

def main():
    print(c1)
    print(c2)
    print(c3)
    print(m1)
    print(m2)
    print(m3)

if __name__ == '__main__':
    main()