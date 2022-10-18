m=float(input("donner la masse volumique de mercure"))
mp=float(input("donner la masse volumique de platine"))
mz=float(input("donner la masse volumique de zinc"))
Hmin=(mp-m)/(m-mz)
print("la valeur minimal de h2/h1 est:",Hmin,"m")
import numpy as np
coeff=[1,-2.4,-3.62]
sol=np.roots(coeff)
print(sol[0].real)
print("la valeur maximal de h2/h1 est:",sol,"m")