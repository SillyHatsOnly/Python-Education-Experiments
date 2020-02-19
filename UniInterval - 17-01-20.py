#a = eval(input())
#for i in range(len(b)-1):
#    if b[i+1][0] > b[i][1] or b[i+1][1] < b[i][1]:
#        c.append((b[i][0], b[i][1]))
#        print(">")
#        print(c)
#    elif b[i+1][0] < b[i][1]:
#        if b[i+1][1] > b[i][1]:
#            c.append((b[i][0], b[i+1][1]))
#            print(">>")
#            print(c)
#        else:
#            c.append((b[i][0], b[i][1]))
#            print(">>>")
#            print(c)


#a = eval(input())
#for i in range(len(b)-1):
#    if b[i+1][0] < b[i][1]:
#        if b[i+1][1] > b[i][1]:
#            b[:(i+2)] = [(b[i][0], b[i+1][1]),]
#            print(">")
#            print(b)
#        else:
#            b[:(i+2)] = [(b[i][0], b[i][1])]
#            print(">>")
#            print(b)
#print(b)


#a = eval(input())
#i = 0
#print(b)
#def recur_func(b):
#    for i in range(len(b)):
#        if b[i+1][0] < b[i][1]:
#            if b[i+1][1] > b[i][1]:
#                b[i:i+2] = [(b[i][0], b[i+1][1])]
#                print(">")
#                print("i = ", i)
#                print("b = ", b)
#                recur_func(b)
#            else:
#                b[i:i+2] = [(b[i][0], b[i][1])]
#                print(">>")
#                print("i = ", i)
#                print("b = ", b)
#                recur_func(b)
#        else:
#            print(">>>")
#            print("i = ", i)
#            print("b = ", b) 
#
#recur_func(b)


#if i == (len(b)-1):
#    return b

a = eval(input())
b = sorted(a)
print(b)
def recur_func(b):
    for i in range(len(b)-1):
        print("----------------")
        print("----------------")
        print(range(len(b)-1))
        print("----------------")
        print(">>>>>>>>>>", i)
        print("----------------")
        if b[i+1][0] < b[i][1]:
            if b[i+1][1] > b[i][1]:
                print("new tuple with old X and new Y")
                print("make new recursion")
                print("i = ", i)
                print("b = ", b)
                b[i:i+2] = [(b[i][0], b[i+1][1])]
                recur_func(b)
            else:
                print("new tuple with old X and old Y")
                print("make new recursion")
                print("i = ", i)
                print("b = ", b)
                b[i:i+2] = [(b[i][0], b[i][1])]
                recur_func(b)
        else:
            print(">>>")
            print("nothing change")
            print("i = ", i)
            print("b = ", b) 

recur_func(b)
