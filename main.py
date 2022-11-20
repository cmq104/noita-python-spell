import math
import string
import fileinput
#number（int）
# a = 1
# a = 2
# print (a)


#string（字符）
# string1 = "一一一五五五五"
# string2 = "二二二"
# print(string1+string2)
# print(string1[0:4])

#define（函数）
# def get_sum(sum1,sum2):
#     result = sum1+sum2
#     return result

#
# a = 1
# b = 2
# c = get_sum(a,b)
# print(c)

# class Person:
#     def __init__(self,name,height,weight):
#         self.height = height
#         self.mame= name
#         self.weight = weight
#         self.sanwei = weight
#
#     def say_name(self):
#         print("我的名字叫"+self.mame)
#         print(self.sanwei)
#
#
# person1 = Person("cmq",178,60)
# person2 = Person("nima",160,50)
#
# person1.say_name()
# person2.say_name()
#
# class asdad:
#     def init(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

# number
#    int,float,complex
# a = 1
# b = 2
# print(float(a))
#
# print(a//b)
#
# print(int(a))
# abs(a) #绝对值
# round(a)#四舍六入五凑偶
# pow(a,2)#取幂,a方
# math.ceil(a)#大于a的最小整数
# c = "实打实的是"
# print(len(c))
# print(c.capitalize())
# print(c.upper())
# print(c.lower())
# print(c.replace("实打实的","你妈死了"))
# print(c.find("实"))#找首项

# list1 = [1,2,3,4,5]
# list1.append(2)#往顶端插入2
# print(list1)
# list1.sort()#排序
# print(list1)
# list1.pop()#弹出最高位
# print(list1)
# list1.reverse()#逆序
# print(list1)
# tuple1 = (1,2,3)#元组，无法修改的列表

# dict1 = {"name":"asd","height":177,"weight":60}
# print(dict1.keys())
# print(dict1.items())
#
#
# set1 = {1,3,2,4,5}#没有顺序，只允许一个元素的集合
# set1.discard(3)#删除
# set1.add(7)
# set2 = {3,4,5,6,7,8}
#
# print(set1)
# print(set1.difference(set2))#找不同元素
# print(set1.intersection(set2))#找相同元素
# print(set2.issubset(set1))#2是否是1的子集，是则返回true

#字符串拼接
# a=1
# b="sadasd"
# c=a
# print(b+str(a))

# list1 = [1,2,3]
# list2 = list1
# list2[2] = 4
# print("list1:"+str(list1))#list存储是用指针存储，list2=list1是将指针传递了，修改list2就是修改指针指向的数字，同时list1也会被修改
# list2 = [2,3,4]
# print("list1:"+str(list1))
# print("list2:"+str(list2))

# homework_finished = True
# if(homework_finished):
#     print("完成了")
# else:
#     print("写")
# #对比符号:> < <= >= ==
# prize = 700
# expensive = (prize>800)
# print(expensive)
# if(prize>=800):
#     print("a")
# elif(prize>=600):#只要完成一个条件立刻跳出elif
#     print("b")
# elif(prize>=650):
#     print("c")
# i=0
# while(i<5):
#     print(i)
#     i=i+1


# string1="asdasdasdasd"
# for char in string1:#for是遍历,和java等不同
#     print(char)
# list1 = ["好的","收到","妈的"]
# # for person in list1:
# #     print(person)
# for i in range(0,len(list1),1):#也可以用range(len(list1)),默认步距1,从0开始
#     print(list1[i])
#     if(i==1):
#         break
#continue直接进行下一个循环,break跳出循环
# patients = [False,True,False,True]
# for i in range(len(patients)):
#     if patients[i]==True:
#         continue
#     print("已经治愈")

# print(list(range(0,10,2)))#从0到10间隔2


# a = float(input())
# print(a)
# # print(format(a,'.2f'))#format就是规定以某种格式输出
#
# with open("cmq.txt","r") as f:#f用于接受文件流，用于打开文件
#     f.read()
#     f.close()



