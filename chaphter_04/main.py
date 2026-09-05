"""
字典可存储的信息量几乎不受限制，因此我们会演示如何遍历字典中的数据。另
外，你还将学习存储字典的列表、存储列表的字典和存储字典的字典。理解字典后，
就能够更准确地为各种真实物体建模。你可以创建一个表示人的字典，然后想在其中存
储多少信息就存储多少信息：姓名、年龄、地址、职业，以及能描述他的任何方面。你
还能够存储任意两种相关的信息，如一系列单词及其含义，一系列人名及其喜欢的数，
以及一系列山脉及其海拔，等等。
"""

alien_0 = {'color': 'green', 'points': 5}

'''访问'''
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}

'''添加'''
alien_0['x_position'] = 0
alien_0['y_position'] = 20

print(alien_0)

"""修改"""
alien_0['color'] = 'yellow'
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position:" + str(alien_0['x_position']))

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

user_0 = {'username': 'sarah', 'email': 'sarah@142.com', 'password': '332x'}


'''同时遍历key和value'''
for key, value in user_0.items():
    print(key + ":" + value)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("  Hi " + name.title() +
              ",I see your favorite language is " +
              favorite_languages[name].title() + "!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll.")

for language in set(favorite_languages.values()):
    print(f"language.title() = {language.title()}")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name:" + full_name.title())
    print("\tLocation:" + location.title())

user_mcu = users['mcurie']
while user_mcu:
    print(user_mcu.popitem())
