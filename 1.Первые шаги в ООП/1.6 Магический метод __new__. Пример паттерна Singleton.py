"""
__new__ вызывается пред созданием обьекта класса
"""


# class Point:
#     def __new__(cls, *args, **kwargs):
#         print('Вызов __new__ для ' + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print('Вызов __init__ для ' + str(self))
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)

# '''
# Патерн синглетон
# '''
#
#
# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __del__(self):
#         DataBase.__instance = None
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def connect(self):
#         print(f'соединение с бд: {self.user}, {self.psw}, {self.port}')
#
#     def close(self):
#         print('Закрытие соединение с бд')
#
#     def read(self):
#         return 'Данные из бд'
#
#     def write(self, data):
#         print(f'запись в бд {data}')
#
#
# db = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '01234', 8080)
#
# print(id(db), id(db2))
# db.connect()
# db2.connect()
#
#


# class  AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"
#
# obj = AbstractClass()


# class SingletonFive:
#     __isinstance = None
#     __n = 1
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__n <= 5:
#             cls.__isinstance = super().__new__(cls)
#             cls.__n += 1
#         return cls.__isinstance
#
#     def __init__(self, name):
#         self.name = name
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# # for el in objs:
# #     print(el.name, end='')


