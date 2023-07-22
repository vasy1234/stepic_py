'''
Инициализация и финализатор
__имя магического метода__
__init__(self) - инициализатор
__del__(self) - финализатор класса
'''

# class Point:
#     color = 'red'
#     circle = 2
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
# pt = Point(1, 2)
# print(pt.__dict__)


# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu, *mems):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mems[:self.total_mem_slots]
#
#     def get_config(self):
#         return [f'Материнская плата: {self.name}',
#                 f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
#                 f'Слотов памяти: {self.total_mem_slots}',
#                 'Память: ' + "; ".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))]
#
#
# mb = MotherBoard('Asus', CPU('Intel', 2000), Memory('Kingston', 1000), Memory('Kingston', 1300))
# print(mb.get_config())


# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         return [f'{i.name}: {i.price}' for i in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
# cart.add(TV("Samsung", 20000))
# cart.add(TV("Sony", 30000))
# cart.add(Table("Ёж", 1200))
# cart.add(Notebook("LG", 37000))
# cart.add(Notebook("HP", 70000))
# print(cart.get_list())


'''Односвязный список'''
# import sys
#
# class ListObject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj  = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# head_obj = ListObject(lst_in[0])
# obj = head_obj
#
# for i in range(1, len(lst_in)):
#     obj_new  = ListObject(lst_in[i])
#     obj.link(obj_new)
#     obj = obj_new

from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
        self.init()

    def init(self):
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x + i][y + j].mine for i, j in indx if
                                 0 <= x + i < self._n and 0 <= y + j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.show()
