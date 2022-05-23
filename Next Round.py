n,k = input().split()
x = int(k)
a = input()
lst = a.split()
if lst[x]==lst[x-1]:
    x+=1
if lst[0]=="0" :
    x=0    
print (x)    