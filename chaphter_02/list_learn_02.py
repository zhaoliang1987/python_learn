magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")

# rang() 的使用
for value in range(1, 11):
    print(value)

print(list(range(1, 11)))

squares = []
for value in range(1, 20):
    # 求平方是value ** 2
    # 求立方是value ** 3
    print(value ** 2)
    squares.append(value ** 2)

print(squares)
print("min(squares) = " + str(min(squares)))
print(f"max(squares) = {str(max(squares))}")

# 简约创建数组的表达式
squares = [value ** 2 for value in range(1, 11)]

my_foods = ['pizza', 'falafel', 'carrot cake']

# 这种方式只是多一个引用
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 需要复制，需要这么做
friend_foods_duplicate = friend_foods[:]

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
