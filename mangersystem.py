from student import *

class StudentManager(object):

    def __init__(self):
        #存储学员的列表
        self.student_list=[]

    def run(self):
        # 1. 加载文件里面的学员数据
        while 1:
            self.show_menu()
                # 2. 显示功能菜单
                # 3. 用户输入目标功能序号
            menu_num=int(input("请输入你需要的功能序号："))
                # 4. 根据用户输入的序号执行不同的功能
            if menu_num == 1:

                #添加学员
                self.add_num()
            elif menu_num == 2:

                #删除学员
                self.del_num()
            elif menu_num == 3:

                #修改学员信息
                pass
            elif menu_num == 4:

                #查询学员信息
                pass
            elif menu_num == 5:

                #显示所有的学员信息
                pass
            elif menu_num == 6:

                #保存学员信息
                pass
            elif menu_num == 7:
                #退出系统
                exit()
            else:
                print("输入错误！请重试！")
    # 二. 系统功能函数：

    #显示功能菜单
    @staticmethod
    def show_menu():
        print("请输入如下功能：")
        print("1.添加学员")
        print("2.删除学员")
        print("3.修改学员信息")
        print("4.查询学员信息")
        print("5.显示所有的学员信息")
        print("6.保存学员信息")

    #添加学员
    def add_num(self):
        name=input("请输入学员姓名：")
        age=int(input("请输入学员年龄："))
        gender=input("请输入学员性别：")

        student_dict={}
        student_dict["name"]=name
        student_dict["age"] = age
        student_dict["gender"] = gender
        self.student_list.append(student_dict)
        print(self.student_list)
        print(student_dict)

    #删除学员
    def del_num(self):

        del_name=input("输入您要删除的名字：")
        for i in self.student_list:
            if del_name == i["name"]:
                self.student_list.remove(i)
                print(self.student_list)
            else:
                print("查无此人！")


    #修改学员信息

    #查询学员信息

    #显示所有的学员信息

    #保存学员信息
    #退出系统

















