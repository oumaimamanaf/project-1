d=input("donner densité")
v=input("donner viscosité cinématique")
try:
    d=float(d)
    v=float(v)
    u=v*0.0001*1000*d
    print("la viscosité dynamique est:",u,"PI")
except:
    print("la valeur de densité et/ou viscosité que vous avez donné pas correcte")