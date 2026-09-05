print("Hello Python World")

message = "Hello Python World"
print(message)

''' 变量名只能包含字母、数字和下划线，变量名能以字母或下划线打头，但不能以数字打头。'''
message = "Hello Python Crash Course world"
print(message)


first_name = "adam"
last_name = "liang"

'''使用变量'''
full_name = f"{first_name} {last_name}"

'''使用变量的方法'''
full_name_title = f"{full_name.title()}"

print(full_name)
print(full_name_title)

'''使用空格符，制表符等'''
like_language = "Languages:\n\tPython\n\tC\n\tJavaScript"
print(like_language)