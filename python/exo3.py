from random import *

r = randint(0,9)

a = input ("veuillez entrez un nombre entre 0 et 9 : ")

if r == a:
   print ("bravo,vous avez gagné")
else:
   print ("perdu! retry!")
