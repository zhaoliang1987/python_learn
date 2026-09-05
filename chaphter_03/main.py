cars = ['bmw', 'yamahu', 'suzuki']
for car in cars:
    if car == 'suzuki':
        print(car.upper())
    else:
        print(car.lower())

age = 22
if age >= 18:
    print('You are old enough to desert it.')



age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
