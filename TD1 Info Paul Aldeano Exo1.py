def somme(x):
    nombre=2**x
    liste=str(nombre)
    compteur=0
    for i in range(len(liste)):
        compteur+=int(liste[i])
    return compteur

d=somme(1000)
print(d)

