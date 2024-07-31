count=0
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
for clents in client:
    nom=clents["name"]
    Age=clents["age"]
    membre=clents["membre"]
    moyenne=clents["moyenne"]
    moy=sum(moyenne)/len(moyenne)
    if membre:
        count +=1
        print(f"{nom} est membre de la famille avec le numero: {count}")
        print(f"voici ses notes: {moyenne} et sa moyenne est: {moy}")
        print(f"il a {Age} ans ")
    else:
        print(f"{nom} n est pas membre")
