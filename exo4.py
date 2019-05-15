from random import randint
random_joueur = randint(0, 9)
joueur_answer = 3
while joueur_answer > 0:

     joueur = int(input("Veuillez entrer un nombre compris entre 0 et 9: "))
     if joueur == random_joueur:
           print ("Bravo!tu as choisi le bon numéro")
           break
     elif joueur != random_joueur:
           print ("Attention! mauvais numéro reéssayer")
     joueur_answer -= 1
else:
    print ("Désolé, vous avez échoué 3 fois!")  
 
