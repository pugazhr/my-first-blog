l = [3,1,2, 0, -1]

def min(l):
    x = l[0]

    for i in l:
        if x > i:
            x =i

    return x

print(min(l))
