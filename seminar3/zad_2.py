# Задайте список. Напишите программу, 
# которая определит, присутствует ли в 
# заданном списке строк некое число.
# [''ffff'.'3rfhg','4'] -> YES

from random import randint
import itertools

n = 4
    
mylist = ['jh',  'kjahsd', 'dpo', '7']

def find_number(n, lst):
    return str(n) in lst

print(find_number(n, mylist))
    



