"""最简单的函数"""
def greeting():
    print('hello world')

'''带参数的函数'''
def greet_user(username):
    print('hello, ' + username)


"带多个参数的函数"
def describe_pet(animal_type, pet_name):
    print(animal_type + ' ' + pet_name)

"函数的参数值带默认参数"
def describe_pet_v2(animal_type, pet_name='weston'):
    print(animal_type + ' ' + pet_name)

"返回参数"
def get_formatted_name(frist_name, last_name):
    full_name_temp = frist_name + ' ' + last_name
    return full_name_temp.title()

def get_formatted_name_v2(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name_2 = first_name + ' ' + middle_name + '' + last_name
    else:
        full_name_2 = first_name + ' ' + last_name
    return full_name_2.title()

"输入不确定个数的参数"
def make_pizza(*toppings):
    for topping in toppings:
        print(" - " + topping)

make_pizza('pepper', 'mushroom')

"输入一个确定参数，和一个不确定个数的参数"
def make_pizza_v2(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

"输入多个确定参数，和一个不确定个数的参数"
def build_profile(first_name, last_name, **user_info):
    profile_temp = {'first_name': first_name, 'last_name': last_name}
    for key, value in user_info.items():
        profile_temp[key] = value
    return profile_temp