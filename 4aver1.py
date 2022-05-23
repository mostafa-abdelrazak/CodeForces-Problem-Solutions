w = input()

lst = []

for i in range(1,101):
    lst.append(str(i))

while w not in lst :
    w = input()

if w not in lst :
    print ("no")

elif int(w) % 2 == 0 and int(w) != 2 : 
    print("yes")

else : 
    print("no") 
       
   