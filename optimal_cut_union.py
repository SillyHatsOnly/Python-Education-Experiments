# (66, 91), (152, 230), (21, 81), (323, 342), (158, 211), (286, 332), (294, 330), (18, 58), (183, 236)

val = sorted(eval(input()))

def segments_union(sorted_list):
    start, end = None, None
    sum = 0
    for tuples in sorted_list:
        x,y = tuples
        if start == None and end == None:
            start, end = x, y
        if x < end < y :
            end = y
        if x > end:
            sum += end - start
            start, end = x, y
    sum += end - start
    print('Full sum = ', sum)

segments_union(val)

#(18, 91) = 73

#(152, 236) = 84

#(286, 342) = 56
