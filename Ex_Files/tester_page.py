# def fun (n):
#   for i in range(n):
#     yield(i)

# for v in fun(5):
#  print(v)

# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
# the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

# for v in the_list:
#   print(v, end=" ")

# print(the_list)

# for v in the_generator:
#   print(v, end=" ")
# print(the_generator)

# print(type(the_list))
# print(type(the_generator))
# print(len(the_list))
# print(len(the_generator))

# print(ord("r"))
# print(chr(3219123))

# def print_function(args, fun):
#   for x in args:
#     print('f(', x, ')=', fun(x), sep='')

# print_function([x for x in range(-2,3)], lambda x: 2 * x**2 - 4 * x + 2)

# print(-3**3)

# from random import seed, randint

# seed()
# data = [randint(-10,10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

# print(data)
# print(filtered)
# print(randint(-30, 4))

# def make_closure(par):
#   loc = par
#   def power(p):
#     return p ** loc
#   return power

# fsqr = make_closure(2)
# fcub = make_closure(3)

# print(fsqr(9))

# for i in range(5):
#   print(i, fsqr(i), fcub(i))

# import os

# try:
#     s = open("doesnt_exist.txt", "r")
#     read = s.readlines
#     print(read)
#     s.close()
# except IOError as exc:
#     print("file could not be opened coz: ", os.strerror(exc.errno))
#     print(exc.errno)

# import time
# import datetime

# # timestamp = 1601823300.0
# # print(time.ctime(timestamp))

# # var = time.asctime()
# # print(var)

# # t = datetime.time(14,53)
# # print(t.strftime("%H:%M:%S"))

# # dt = datetime.datetime(2023,1,21,10,4,30)
# # print(dt.strftime("%y %b %d %D %H:%M:%S"))
# # print(dt.strptime("23 Jan 05 10:04:30", "%y %b %d %H:%M:%S"))

# # timestamp = time.time()
# # d = datetime.date.fromtimestamp(timestamp)
# # print(d)
# # print(timestamp)

# import calendar

# # c = calendar.Calendar()

# # for iter in c.itermonthdays4(2019,11):
# #   print(iter, end=" ")

# calendar.setfirstweekday(3)
# calendar.weekheader(3)
# print(calendar.month(2023, 1))

# multiline = '''line
# that'''
# newline = '\n'
# print(len(multiline))
# print(ord(newline))

# tr = sorted(multiline)

# print(' '.join(tr))
# print("cisco.com yep           ".center("  "))

# assert float(4) == int(4)

# try:
#   x = int(input("Enter number: "))
#   y = 1/x
#   print(y)
# except ValueError:
#   print("must enter integer")
# except TypeError:
#   print("no lists")
# except:
#   print("something else")

# from time import sleep

# seconds = 0

# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("Don't do that!")
#         break

# class Example:
#     attr = 1
#     def __init__(self):
#         num = 1

# myEx = Example()
# myEx1 = Example()

# myEx.attr = 3
# print(myEx.attr)
# Example.attr = 3
# print(myEx1.__module__)
# print(type(myEx).__name__)

# print(hasattr(Example, 'attr'))
# print(hasattr(Example, 'num'))
# print(hasattr(myEx, 'attr'))
# print(hasattr(myEx, 'num'))

# class Top:
#     def m_top(self):
#         print("top")


# class Middle(Top):
#     def m_middle(self):
#         print("middle")


# class Bottom(Middle, Top):
#     def m_bottom(self):
#         print("bottom")


# boject = Bottom()
# boject.m_bottom()
# boject.m_middle()
# boject.m_top()
# print(Middle.__getattribute__)
# print(Middle.__dict__)
# print(Middle.__dir__)

import math
print(dir(math))

from datetime import datetime
print(dir(datetime))