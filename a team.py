i = int(input())
  
count = 0 

for x in range(i):
    a,b,c = input().split()

    if int(a) + int(b) + int(c) > 1 :
        count+=1

print(count)         