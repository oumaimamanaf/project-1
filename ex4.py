po=input("donner la masse volumique")
h=input("donner la hauteur")
g=input("donner la gravité")
L=input("donner la longeur")
l=input("donner la largeur")
try:
    po=float(po)
    h=float(h)
    g=float(g)
    L=float(L)
    l=float(l)
    s=L*l
    p=po*g*h
    print("la pression est:",p,"Pa")
    F=p*s
    print("la force est:",F,"N")
except:
    print("la valeur de certains paramètres que vous avez donné pas correcte")