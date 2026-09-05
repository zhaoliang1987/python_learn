# 列表的学习

"""
列表由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0～9或所有
家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。列表
通常包含多个元素，因此给列表指定一个表示复数的名称（如letters、digits或names）是个
不错的主意
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'redline']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())

# Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让Python返回最后一个列表元素
print(bicycles[-1].title())

# modify list element
bicycles[1] = 'broccoli'
print(bicycles)
bicycles.append('chicken')
print(bicycles)

# 计算个数
print("bicycles.count() : " + str(len(bicycles)))

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

""" list element delete"""

# 删除特定的元素
motorcycles.remove('suzuki')
print(motorcycles)

# 根据索引删除元素
del motorcycles[0]
print(motorcycles)

del motorcycles[-1]
print(motorcycles)

# 另一种删除元素的方法 pop() 方法 Remove and return item at index (default last).
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# 排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

# 使用函数sorted()对列表临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)