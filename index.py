import random
count = 0
pivot= random.randint(1,9)
while True:
    num=input("ENTREZ UN NOMBRE ENTRE 0 ET 10 vous avez droit a trois essaie ")
    count +=1
    reste=3-count
    if pivot==num:
        print("bravo vous avez remportez lz grand prix")
        break
    elif count==3:
        print("terminez")
        break
    
    else:
        print("votre numero gagant est incorret ils vous reste",reste,"chances")
    
            
print("vous avez terminez votre partie a biento")

for i in range(4,100,4):
    print(i)
