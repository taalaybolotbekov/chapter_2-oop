class House:
    ploshad = 'default'
    mebel = 'default'
    def __init__ (self,s,t):
        self.t = input('Enter type:')
        self.s = int(input('Enter the area:'))

class Furniture(House):
    name = '2'
    plosad_ = 'default'
    bed = 'default'
    def furn(self,name,plosad_,bed):
        self.name = 2
        self.plosad_ = 1.5
        self.bed = 4
a = Furniture(1,2)
a.furn(1,2,3)
print('тип дома',a.t,'площадь дома',a.s,'\nсписок мебели внутри дома: кровать, шкаф,стол')
d =(a.s -(a.name+a.plosad_+a.bed))
if d > 0:
    print('Осталось',d, 'кв.м свободных мест')
else:
    print('Нет места для мебели')