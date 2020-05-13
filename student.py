class Student(object):

    def __init__(self, name, age, gender):

        #名字
        self.name=name
        #年龄
        self.age=age
        #性别
        self.gender=gender

    def __str__(self):
        return f'{self.name}, {self.age}, {self.gender}'

