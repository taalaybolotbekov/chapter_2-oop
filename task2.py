class Car:
    make = 'default'
    model = 'default'
    year = 1
    fuel = 70
    def __init__ (self, make, model, year, fuel):
        self.make = input('Country:')
        self.model = input('Model:')
        self.year = int(input('Date:'))
        self.fuel = int(input('Petrol:'))
car = Car(1,2,3,4)
# car.drive()
print('Страна:',car.make,'\nмарка:',car.model,'\nГод выпуска:',car.year ,'\nБензин в баке:',car.fuel)



class Add(Car):
    odometer = 0
    def __init__ (self, odometer):
        self.odometer = car.fuel*10
a = Add(1)
# a._Add__dictance()
print('на', a.odometer,' км хватает бензина')
class Subtrack(Car):
    fuel = 70
    def __init__(self,fuel):
        self.fuel = fuel


v = Subtrack(int(Car.fuel - int(input('dictance:'))*10))
# v._Subtrack__fuel()
print('осталось',v.fuel,'литр бензина')
if v.fuel > 0:
    print("Let's drive")
else:
    print("Need more fuel, please, fill more")
        
