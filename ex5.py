p=input("donner la pression")
S=input("donner la surface")
try:
    p=float(p)
    S=float(S)
    F=p*S
    print("la force est :",F,"N")
except:
    print("la valeur de pression et/ou surface que vous avez donné pas correcte")