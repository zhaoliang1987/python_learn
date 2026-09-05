with open('pi_digits.txt') as f:
    content = f.read()
    print(content)
    print('---------')
    print(content.strip())

'''
    逐行读取文件的每一行
'''
file_name = 'pi_digits.txt'
with open(file_name) as f:
    for line in f:
        print(line.strip())

'''
    追加文件内容
'''
file_program = 'programming.txt'
with open(file_program, 'a+') as f:
    f.write('I love programming\n')
    f.write('I love creating new games')

print("please input your birthday:\n")
birthday = input()
pi_file = 'pi_million_digits.txt'
with open(pi_file) as f:
    lines = f.readlines()

for line in lines:
    if birthday in line:
        print(line.strip())
