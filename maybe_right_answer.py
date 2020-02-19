# new input:
# (66, 91), (152, 230), (21, 81), (323, 342), (158, 211), (286, 332), (294, 330), (18, 58), (183, 236)

a = sorted(eval(input()))

def some_func(val):
    print(val)
    full_val = []
    temp_val = []
    lost_val = val[:]
    
    for i in val:
        if i not in lost_val:
            continue
        for j in val:
            if j not in lost_val:
                continue
            elif i == j:
                continue
            elif i > j:
                continue
            elif i[1] >= j[0]:
                temp_val.append(j)
        else:
            if temp_val == []:
                temp_val.append(i)
        if len(temp_val) > 0:
            for k in val:
                if k not in lost_val:
                    continue
                for l in temp_val:
                    if l not in lost_val:
                        continue
                    elif k in temp_val:
                        continue
                    elif k[0] < l[1]:
                        temp_val.append(k)
                    else:
                        continue
        else:
            temp_val.append(i)
        full_val.append((temp_val))
        for h in temp_val:
            lost_val.remove(h)
        temp_val = []
    print(full_val)
    sum_1 = 0
    for lists in full_val:
        print("lists = ", lists)
        start, end = None, None
        for my_tuple in lists:
            print("my_tuple = ", my_tuple)
            
            min_v, max_v = my_tuple
            print("min_v = ", min_v)
            print("max_v = ", max_v)
            if start == None or min_v < start:
                start = min_v
                print("start = ", start)
            if end == None or max_v > end:
                end = max_v
                print("end = ", end)
        sum_1 += (end - start)
    print(sum_1)

some_func(a)


