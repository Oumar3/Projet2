import random
n = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','l','m','n','o','p']
liste=[]
dic={}
j=1
m=int(input("entrez la taille du groupe ?"))

### Création d'une liste aleatoirement apartir de la liste n.
def créerUnListe():
     while len(liste)<m:
        val=random.choice(n)
        n.remove(val)
        liste.append(val)
for i in n:
    if len(n)>m:
        ### appelle de la fonction créer une liste
        créerUnListe()
        ### Création d'une copie de la liste precedement créer
        newliste=[]
        for k in liste:
            newliste.append(k)
        ### l'affectation de la liste à la j éme clé du dictionnaires
        dic[j]=newliste
        j=j+1
        ### suppression de la liste créer avec la fonction créerUnList 
        liste.clear()
        if n!=[]:
            dic[j]=n
    else:
        dic[j]=n

print(dic)