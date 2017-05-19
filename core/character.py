#!/usr/bin/env python
#-- coding: UTF-8 --

from core.item import *

class Character(object):

    def __init__(self, health, xp):
        self.health = health
        self.xp = xp

    def move():
        pass

    def eat(self, food):
        self.health += food.use()

    def die():
        pass

    def receive_attack(self, damage):
        self.health -= damage


class Player(Character):
    def __init__(self, health, xp):
        # self.name = ?
        # self.inventory = ?
        Character.__init__(self, 50, 5)
        self.inventory = Inventory(20)

    def pick(self, item):
        self.inventory.set_item(item)

    def drop(self, item):
        self.inventory.del_item(item)

    def fight(self, enemy):
        damage = 10
        enemy.receive_attack(damage)

    # def receive_attack(self, damage):
    #     Character.receive_attack(self, damage)


class Chicken(Character):
    def __init__(self):
        Character.__init__(20, 1)

    # def die():
    #     pass
    #
    # def move():
    #     pass
    #
    # def attack():
    #     pass
    #
    # def reveive_attack():
    #     pass
