x = [5,4,3,2]
#n = 0

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            x[i],x[j]=x[j],x[i]
    print(x)


print(x)
    
