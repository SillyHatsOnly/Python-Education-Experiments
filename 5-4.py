from math import *
def pigen():
    chisl = 4
    znam = 1
    sum_of = chisl/znam
    while True:
        yield sum_of
        znam += 2
        sum_of -= chisl/znam
        yield sum_of
        znam += 2
        sum_of += chisl/znam
