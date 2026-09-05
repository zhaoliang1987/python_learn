from chaphter_07.car import Car
from chaphter_07.dog import Dog

my_dog = Dog("wang", 18)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

dog2 = Dog("cai", 18)

car = Car("tank", "300", 2024)
print(dog2.name)
print(dog2.age)
