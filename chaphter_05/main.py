"""用户输入"""
message = input('Enter your message: ')
print(message)

age = int(input('Enter your age: '))
print("You are " + str(age) + " years old.")
#
height = input("How tall are you,in inches?")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

"""while循环的使用"""
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

message = ""
while message != "quit":
    print(message)
    message = input()

prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(city)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
