i = int(input())
lst = []

for x in range (i) :
    y = input()
    if y.__len__() > 10 :
      lst.append( y[0] + str(y.__len__()-2) + y[-1] )
    else : 
        lst.append(y)  
        
        
# print(lst)

for s in lst :
    print(s)