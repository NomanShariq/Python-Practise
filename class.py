


class Vehicle():
    def __init__(self,make,model):
    
        self.make = make
        self.model = model
    
    def moves(self):
        print("Moves fast....")
        
    def describe_car(self):
        print(f'I am {self.make} {self.model}.. ')

my_car = Vehicle("Toyota","Corolla")

# print(my_car.make)
# print(my_car.model)

my_car.describe_car()
my_car.moves()

make_another_car = Vehicle('Toyota','Supra')
make_another_car.describe_car()
make_another_car.moves()

class Airplane(Vehicle):
    def __init__(self,make,model,Airplane_id):
        
        super().__init__(make,model)
        self.Airplane_id = Airplane_id
        
    def moves(self):
        print('Flying Along')

class Truck(Vehicle):
    def moves(self):
        print('Drive Along')
        
class Bike(Vehicle):
    pass


Emirates = Airplane('Emirates','AA-2332','EA-78652')
Emirates.describe_car()
Emirates.moves()

Peterbilt = Truck('Peterbilt','Model 352')
Peterbilt.describe_car()
Peterbilt.moves()

Kawasaki = Bike('Kawasaki','Ninja H2')
Kawasaki.describe_car()
Kawasaki.moves()


print('\n\n\n')


for v in (my_car,make_another_car,Emirates,Peterbilt,Kawasaki):

        v.describe_car()
        v.moves()