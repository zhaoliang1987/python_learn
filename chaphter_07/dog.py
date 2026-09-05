class Dog:
    """
    __init__()是一个特殊方法，每当你根据Dog类创建新实例时，Python都会自动运行它。
    为何必须在方法定义中包含形参self呢？因为Python调用这个方法来创建Dog实例时，将自动传
    入实参self。每个与实例相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，
    让实例能够访问类中的属性和方法
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is a dog")

    def roll_over(self):
        print(self.name.title() + " rolled over!")
