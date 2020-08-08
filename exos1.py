# author: Dabs
from math import* 

print("resolution d'une equation du second degre")
print("donner les 3 valeurs")
print("entrer valeur de a")
a = float(input("la valeur de a"))
print("entrer la valeur de b")
b = float(input("la valeur de b")) 
print("entrer la valeur de c")
c = float(input("la valeur de c"))

print("calculons et affichons les solutions")
if a == 0 :
  print("equation du premier degre b.x + C = 0")
  if b == 0 :
      print("constante")
      if c == 0 :
         print("tout les reels est solution")
      else :
          print("pas de solution")
  else :
       print("une solution unique:", c / b )
else :
   print("calculer le discriminant")
   delta = b*b - 4*a*c
   print("delta =", delta)
   if delta == 0 :
     print("l'equation admet deux solutions " , b/2*a)
   else :
    if delta > 0 :
     print("l'equation admet deux solutions ", (-b+sqrt(delta))/2*a, " et ",(-b-sqrt(delta))/2*a)  
    else :
      print("pas de reel")
print("fin de l'exercice1")         
