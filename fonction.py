def  bonjour(prenom):
    print("Bonjour",prenom)
    
bonjour("ERIC")

def animal(nom1,nom2):
    print(f"vous avez deux animaux qui sont {nom1} et {nom2}")
animal("lion","elephant")

def jumeau(prenom="Jean MARC"):
    print(f"vous etes jumelle avec {prenom}")
jumeau("ALICE")

def moyenne(*note):
    return sum(note)/len(note)
print(moyenne(13,12,17,9,10))


client = [
    {
    "name":"GASPARD","membre": True,"age":27,"moyenne" :[12,13,11,10]
    },
    {
    "name":"NORBERT","membre": False,"age":23, "moyenne" :[12,13,11,10]
    },
     {
    "name":"OKA","membre": True,"age":28,"moyenne":[12,13,11,10]
    },
    {
    "name":"LANDRY","membre": False,"age":27,"moyenne" :[12,13,11,10]
    },
    {
    "name":"LAI","membre": True,"age":27,"moyenne" :[4,13,11,9]
    },
    {
    "name":"ARMAND","membre": False,"age":20,"moyenne" :[5,10,11,10]
    },
 ]

def affichage(**arg):
    for key,value in arg.items():
       print(f"{key}:{value}")
affichage (nom="GASPARD",membre=True,age=27,moyenne =[12,13,11,10]
    )
def info_utilisateur():
    donnees=[]
    print("saisissez vos informations nom,prenom,age et taille et saisissez fin lorsque vous avez finis")
    nom=input("tapez le nom : ")
    prenom=input("tapez le prenom : ")
    age=input("tapez le nom")
    taille=input("tapez le nom")
    arret=input("si vous avez fini tapez fin sinon tapez autre chose")
    while True:
        if arret.lower()=="fin":
            break
        else: 
            donnees.append(nom,prenom,age,taille)
    return donnees
identite=info_utilisateur()
print("merci pour votre cooperation ")
print(f"voici vos donnees : {identite}")



