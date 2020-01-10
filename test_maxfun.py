from math import *

def maxfun(S, *F):
    return F[max(enumerate(sum(f(x) for x in S) for f in F), key=lambda x: x[1])[0]]
