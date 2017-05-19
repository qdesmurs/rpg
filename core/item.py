#!/usr/bin/env python
#-- coding: UTF-8 --

from character import *

class Item(object):
    def __init__(self, weight):
        self.weight = weight

    def use(arg):
        pass


class Weapon(Item):
    def __init__(self, weight, damage):
        Item.__init__(self, weight)
        self.damage = damage

    def use(self):
        return self.damage


class Rock(Weapon):
    def __init__(self, weight):
        Weapon.__init__(self, weight, 10)


class Armor(Item):
    def __init__(self, weight, defence):
        Item.__init__(self, weight)
        self.defence = defence


class Shield(Item):
    def __init__(self, arg):
        self.arg = arg


class Helmet(Armor):
    def __init__(self, arg):
        Item.__init__(self, weight)
        self.arg = arg


class Food(Item):
    def __init__(self, weight, gain):
        self.weight = weight
        self.gain = gain


class Inventory(object):
    def __init__(self, size):
        self.items = []
        self.size = size

    def get_item(self, item):
        if item in self.items:
            return item

    def set_item(self, item):
        weight = 0
        for i in self.items:
            weight += i.weight
        if weight + item.weight <= self.size:
            self.items.append(item)
            return True
        return False

    def del_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False
