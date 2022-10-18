H=input("donner la hauteur")
masseV=input("donner la masse volumique")
g=input("donner la gravité")
L=input("donner la longeur")
l=input("donner la largeur")
try:
    H=float(H)
    masseV=float(masseV)
    g=float(g)
    L=float(L)
    l=float(l)
    P=masseV*g*H
    S=L*l
    F=P*S
    print("la force est :",F,"N")
except:
    print("la valeur de certains paramètres que vous avez donné pas correcte")