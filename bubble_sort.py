x = [5,4,3,2,1]

for i in range(len(x)):
    swapped = False
    for j in range(0, len(x)-i-1):

        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
            swapped = True
        if not swapped:
            break

        print(x)

print ("sorted list : ", x)
