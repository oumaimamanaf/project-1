p=input("donner la pression")
d=input("donner le diamètre")
try:
    p=float(p)
    d=float(d)
    A=3.14*(d/2)**2
    F=p*10**6*A
    print("la force est :",F,"N")
except:
    print("la valeur de pression et/ou rayon que vous avez donné pas correcte")