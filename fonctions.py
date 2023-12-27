import copy
import random
import turtle
from turtle import *
import time

#from faker import Faker




# partie: initialisation du jeu et affichage

def importer_mots(nom_fichier):
     ###choisir les mot d'au moins trois lettres###
     f=open(nom_fichier)
     liste=[]
     for ligne in f :
         x=ligne.strip()
         if len(x)>= 3 : 
             liste.append(x.upper())
     f.close()
     return liste


def choisir_mot_alea(liste): 
    ### It chouses a random name from the list. ###
    a = len(liste)-1    
    b = random.randint(0,a)     
    return liste[b]

def initialiser_mot_part_decouv(mot_myst,car_subst="-"):
    l=[car_subst for i in range (1,len(mot_myst)-1)]
    l.append(mot_myst[-1])
    l.insert(0,mot_myst[0])
    return l   
    
def afficher_potence_texte(nb_err,nb_err_max):
    ### affichage le numero des erreurs grace a "!" and les lettres de "PERDU" ###
    liste = ["P","E","R","D","U"]  #liste=P.E.R.D.U
    n=0   #compteur des etapes
    val=0    #valeur pour les lettres
    
    if (nb_err <= 5):
        val = nb_err
    else :
        val = 5

    
    for i in range(val):
        print (liste[i],end="")
        n+= 1
     
    if (nb_err > 5):
        for i in range(5,nb_err):   
            print("!",end="")
            n+= 1
    if (n < nb_err_max):
        for i in range (n,nb_err_max):
            print("-",end="")
            n+=1
    
    print("!")
    return

#Partie pour un joueur humain

def demander_proposition(deja_dit):
    deja_dit_majuscule=[let.upper() for let in deja_dit ]
    lettre= input("entrer une lettre ")
    lettremaj= lettre.upper()
    if not( lettremaj in deja_dit_majuscule ) and lettremaj>="A" and lettremaj<="Z" :
         return lettremaj
    else:
         while lettremaj in deja_dit_majuscule or lettremaj<"A" or lettremaj>'Z':
              lettre= input("entrer une lettre ")
              lettremaj=lettre.upper()
         return lettremaj
     
def decouvrir_lettre(lettre,mot_myst,lmot_decouv):
    s=0
    for i in range (len(mot_myst)):
        for i in range (len(lmot_decouv)):
            if mot_myst[i] == lettre and lmot_decouv[i] != lettre:
                lmot_decouv[i]=lettre
                s=1
    if s==1:
        return True
    else:
        return False


    
def potencedifficile(faute,mot_myst,mottrouve,t):
  #turtle.TurtleScreen._RUNNING=True
  #turtle.setup(480,640,-100,50)
  #turtle.title("Le Jeu Du Pendu")
  #turtle.bgcolor("#27BAFF") #bleu
  #t = turtle.Turtle()
  t.pensize(4)
  t.speed(0)
  t.ht()
  if mot_myst == mottrouve:
     t.penup()
     y = 100
     t.goto(0,y)
     return
  else:
    t.penup()
    y = y + 50
    t.goto(0,y)
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.seth(90)
    t.forward(300)
    t.seth(180)
    t.forward(50)
    if faute == 0 :
         return
    t.left(90)
    t.forward(25)
    if faute == 1:
         return

    t.seth(180)
    t.circle(25)
    t.seth(270)
    if faute == 2 :
       return

    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(25)
    t.left(30)
    t.forward(40)
    t.backward(40)
    t.right(60)
    t.forward(40)
    t.backward(40)
    if faute == 3 :
         return


    t.seth(270)
    t.forward(75)
    t.left(30)
    t.forward(40)
    t.backward(40)
    t.right(60)
    t.forward(40)
    t.backward(40)
    if faute == 4:
         return
    t.seth(90)
    t.penup()
    t.forward(120)
    t.seth(0)
    t.write('Mort',False,align="center",font=("Times",10))
    if faute == 5 :
         t.goto(0,-100)
         return
    

def potencefacile(faute,mot_myst,mottrouve,t):
  #turtle.TurtleScreen._RUNNING=True
  #turtle.setup(480,640,-100,50)
  #turtle.title("Le Jeu Du Pendu")
  #turtle.bgcolor("#27BAFF") #bleu
  t = turtle.Turtle()
  t.speed(0)
  t.ht()
  if mot_myst == mottrouve :
     t.penup()
     return
     
     return
  else :
    t.penup()
    y = 50
    t.goto(0,y)
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.seth(90)
    if faute == 0:
         return
    t.forward(300)
    t.seth(180)
    t.forward(50)
    if faute == 1:
         return
    
    t.left(90)
    t.forward(25)
    if faute == 2 :
         return
    t.seth(180)
    t.circle(25)
    t.seth(270)
    if faute == 3 :
       return
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(25)
    if faute == 4 :
         return
    t.left(30)
    t.forward(40)
    t.backward(40)
    if faute == 5:
         return
    t.right(60)
    t.forward(40)
    t.backward(40)
    if faute == 6 :
         return
    t.seth(270)
    t.forward(75)
    if faute == 7 :
         return
    t.left(30)
    t.forward(40)
    t.backward(40)
    if faute == 8:
         return
    t.right(60)
    t.forward(40)
    t.backward(40)
    if faute == 9:
         return
    t.seth(90)
    t.penup()
    t.forward(120)
    t.seth(0)
    t.write('MORT',False,align="center",font=("Times",10))
    if faute==10 :
         t.goto(0,-100)
         return

    
def partie_humain(mot_myst, nb_err_max, t, car_subst='-', mode_graphique=False):
    lis_mot_myst = initialiser_mot_part_decouv(mot_myst, car_subst)
    deja_dit = []
    i = 0
    mottrouve = ''.join(lis_mot_myst)

    

    if mode_graphique:
        if nb_err_max == 10:
            potencefacile(0, mottrouve, mot_myst, t)
        else:
            potencedifficile(0, mottrouve, mot_myst, t)

    while i < nb_err_max and mottrouve != mot_myst:
        print("===", mottrouve, "===")
        t.goto(0, 0)
        t.write(mottrouve, align="center", font=("Times", 30, "normal"))

        if deja_dit:
            print("Les lettres utilisées", deja_dit)
            y = 280
            t.goto(-100, y)
            for letter in deja_dit:
                t.write(letter, align="center", font=("Times", 18, "normal"))
                y -= 10

        mot = input('Entrer une lettre:')

        a = mot.upper()
        b = decouvrir_lettre(a, mot_myst, lis_mot_myst)
        deja_dit.append(a)
        mottrouve = ''.join(lis_mot_myst)

        if b:
            
            print("Lettre présente")
        else:
            i += 1
            print("le nombre d'erreurs déjà commises :", str(i))  # Convert i to string

            if mode_graphique:
                if nb_err_max == 10:
                    potencefacile(i, mottrouve, mot_myst, t)
                else:
                    potencedifficile(i, mottrouve, mot_myst, t)

        if i >= 1:
            afficher_potence_texte(i, nb_err_max)
            print("")

    if mottrouve == mot_myst:
        t.goto(0,-150)
        t.write("You win",align="center", font=("Arial", 24, "normal"))
        print("vous avez gagné")
        if mode_graphique:
            if nb_err_max == 10:
                potencefacile(i, mot_myst, mottrouve, t)
            else:
                potencedifficile(i, mot_myst, mottrouve, t)
        return True
    else:
        t.goto(0,-150)
        t.write("You have lost",align="center", font=("Arial", 24, "normal"))
        print("vous avez perdu")
        print("le mot à trouver est", mot_myst)
        return False



def partie_humain_alea(nom_fichier,nb_err_max,t,car_subst='-'):
    liste=importer_mots(nom_fichier)
    mot=choisir_mot_alea(liste)
    partie=partie_humain(mot,nb_err_max,t,car_subst,True)
    return partie
        

     
#Partie en mode automatique
     
def fabrique_liste_alphabet():
    ### cree une liste de alphabet(seulement MAJUSCULE)###
    liste=[]
    for i in range(65,91):
    	liste.append(chr(i)) #ASCII -> les lettres -> le liste
    return liste
    
def fabrique_liste_alea():
    ### il melange le liste ###
    liste = fabrique_liste_alphabet()
    random.shuffle(liste)	#shuffle
    return liste


    ##fabrique_liste_frequence(dans 3 fonction)
    
def dico_frequence(nom_fichier):	#1. fonction de (fabrique_liste_frequence)
    ### il stocke les lettres(MAJUSCULE) dans un dictionner ###
    f=open(nom_fichier)
    texte = f.read()
    texte = texte.upper()
    dic = {}
    alpha = fabrique_liste_alphabet()	
    for i in range(0,len(texte)):
    	if texte[i] not in dic:
    		if texte[i] in alpha:	#alpha = alphabet
    			dic[texte[i]]=1
    	else:
    		dic[texte[i]]+=1
    f.close()
    return dic	

def lettre_la_plus_frequente(dico):		#2. fonction de (fabrique_liste_frequence)
    ### il nous donne le lettre le plus utilise dans un dictionnaire ###
    CLES = list(dico.keys()) 	#".keys()" nous permet d'acceder aux cles d'un dictionnaire
    PlusGrandV  = -1
    for cle in CLES:
    	if PlusGrandV < dico[cle]:
    		PlusGrandV = dico[cle]
    		GrandCle = cle
    return GrandCle

def fabrique_liste_freq(nom_fichier):		#3. fonction de (fabrique_liste_frequence)
    ### Il cree une liste qui renvoie les MAJUSCULE, de la plus fréquente dans le fichier ###
    dictL = dict(dico_frequence(nom_fichier))		#dictionnaire de lettre en majuscule dans le fichier
    lenthDictL = len(dictL)
    listeFreq = [] 		#une liste pour frequence de lettre
    for i in range(lenthDictL):
    	X = lettre_la_plus_frequente(dictL)
    	listeFreq.append(X)
    	del dictL[X]
    return listeFreq


## Les fonctions de parite auto
def Fpause(n):
    if n==True:
    	input("Appuyez sur n'importe quelle touche pour continuer:")
    return

def Faffiche(n,liste,erreur,AutoT):
    ### il affiche le liste ###
    if n == True:
          AutoT.clear()
          AutoT.goto(0,0)
          
          mot = " ".join(liste)
          
          AutoT.write(mot,align="center",font=("Arial",24,"normal"))
          

          AutoT.goto(30,220)
          AutoT.write(erreur,align="left",font=("align",24,"normal"))
          time.sleep(0.5)

          
          print(liste,end="")
          print("")
          print("Numero d'erreur:",erreur)
        
          return


def partie_auto(mot_myst,liste_lettres,AutoT,affichage=True,pause=False):
     mot_myst = mot_myst.upper() #si mot mystere a un lettre minuscule?
     secret = initialiser_mot_part_decouv(mot_myst) #fonction cache le mot mysto
     
     
     erreur = 0
     Faffiche(True,secret,erreur,AutoT)
     Fpause(pause) 
    	
     for i  in range(0,len(liste_lettres)):
          a = decouvrir_lettre(liste_lettres[i],mot_myst,secret) #modifie le secret 
          if a:	# "a" peut etre TRUE ou FALSE
               Faffiche(affichage,secret,erreur,AutoT)
               Fpause(pause)
          else:
               erreur += 1
          
        
          if "".join(secret) == mot_myst: # <"-".join> nous permet de recolle(colle ici est "-") tous les parties d' un liste
               print("Vous avez gagné avec",erreur,"erreurs.")
               AutoT.goto(0,-100)
               AutoT.write("You have won with " + str(erreur) + " errors",align="center",font=("Arial",18,"normal"))
               return erreur
     return erreur
  

# fabrique_liste_alphabet --> 17 erreur sur 'BONJOUR'
# fabrique_liste_alea ------> ??(change pour chaque tour)erreur sur 'BONJOUR'
# fabrique_liste_freq ------> 19 erreur sur 'BONJOUR'

#Partie extention :

#				      !======MENU======!

def affichepropo():
    ###la fonction affiche les opositions du jeu ###
    print("Bonjour! Vous etes pret pour jouer ")
    print(" 1.Partie manuelle pour un humain \n",
          "2.Partie automatique par l'ordinateur \n",
          "3.Quitter le jeu \n")


"""
reponse="-1"

while reponse != "3":	
     affichepropo()
     reponse=input("Choisir 1 ou 2  ou 3 pour faire votre choix:")
     
     while reponse!="1" and reponse!="2"and reponse!="3":
          reponse=input("Veuillez choisir 1 ou 2 ou 3 comme chiffre:")
       
     # ===PARTIE HUMAIN===
     if reponse == "1":
               # ==SUJET==      
               nb_sujet=input("\nChoissir un sujet ou tape 'q' pour retourner a la Menu \n 1.Cinema \n 2.Music \n 3.Sport \n 4.Animaux \nVotre reponce:")
               while nb_sujet != "1" and nb_sujet != "2" and nb_sujet != "3" and nb_sujet != "4" and nb_sujet != "q":
                     nb_sujet=input("Choissir un sujet")

               if nb_sujet == "q":
                    print("\n")
                    continue
               elif nb_sujet == "1":
                    mot_mystere_liste = importer_mots("motsCinema.txt")	#doit changer le fichier Cinema
               elif nb_sujet == "2" :
                    mot_mystere_liste = importer_mots("motsMusic.txt")	#doit changer le fichier music
               elif nb_sujet == "3" :
                    mot_mystere_liste = importer_mots("motsSport.txt")	#doit changer le fichier sport
               elif nb_sujet == "4" :
                    mot_mystere_liste = importer_mots("motsAnimaux.txt")#doit changer le fichier animaux
               mot_mystere = choisir_mot_alea(mot_mystere_liste)
               print("")
       	
               # ==DIFFICULTE==
               nb_difficulte = input("Choisir un difficulte 'f/d'(facile|difficile) ou tape 'q' pour retourner a la menu:")
       	
               while nb_difficulte != "f" and nb_difficulte != "d" and nb_difficulte != 'q' :
                    nb_difficulte = input("Choisir un difficulte (facile|difficile) ou tape 'q' pour retourner a la menu:")
       	
               if nb_difficulte == "q":
                    print("\n")
                    continue
               elif nb_difficulte == "f":
                    nb_err_max = 10
               else:
                    nb_err_max = 5
       	       #====affichage======
               mode = input("voulez-vous une interface graphique (affichage de la potence) ? repondez par 'vrai' ou 'faux': ")
               #==PARTIE JEU==
               if mode =='vrai':
                    mode_graphique=True
               else :
                    mode_graphique=False
               partie_humain(mot_mystere,nb_err_max,'-',mode_graphique)
               print("")
               #==REJOUER==
               rejouer = 'e'
               while rejouer == "e":
                    rejouer=input("Vous voulez rejouez si oui tape 'e' sinon tape 'q':")
                    while rejouer !="e" and rejouer !="q":
                         rejouer=input("Vous voulez rejouez si oui tape 'e' sinon tape 'q':")
                    if rejouer == "e":
                         mot_mystere = choisir_mot_alea(mot_mystere_liste) #il change le mot mystere
                         partie_humain(mot_mystere,nb_err_max,'-',mode_graphique)
                    print("\n")
       		
     # ===PARTIE AUTOMATIQUE===	
     elif reponse == "2":
          
          #==Fichier==
          fake = Faker("Fr-FR")
          
          
          f = open("mots.txt",'w')
          
          for i in range(15):
          	f.write(fake.word())
          	f.write("\n")
          f.close()


          #==STRATEGIE==
          nb_strategie = input("\nChoisir la stratégie \n 1. Stratégie alphabétique \n 2. Stratégie aléatoire \n 3. Stratégie complexe \n Ou tape 'q' pour retourner a la menu \n \n Votre choix:")
          while nb_strategie != "1" and nb_strategie != "2" and nb_strategie != "3" and nb_strategie != 'q':
               nb_strategie = input("Choisir la stratégie \n 1. Stratégie alphabétique \n 2. Stratégie aléatoire \n 3. Stratégie complexe \n Ou tape 'q' pour retourner a la menu \n \nVotre choix:")
       	
          if nb_strategie == 'q':
               print("\n")
               continue
          elif nb_strategie == "1":
               liste_lettres = fabrique_liste_alphabet()
          elif nb_strategie == "2":
               liste_lettres = fabrique_liste_alea()
          elif nb_strategie == "3":
               liste_lettres = fabrique_liste_freq("mots.txt")  
       	
          #==SUJET==
          mot_mystere_liste = importer_mots("mots.txt") 
          mot_mystere = choisir_mot_alea(mot_mystere_liste)

         
          #==AFFICHAGE ET PAUSE==
          affichage_i = input("Vous voulez afficher votre Progresse et vos erreurs \n Si oui tapez 'o' \n Sinon tapez 'n' \n Si vous voulez quitter taper 'q' \n \n Votre choix:")
          if affichage_i == 'q':	#affichage_i = affichage indicateur
               print("\n")
               continue
          pause_i = input("\nVous voulez afficher examiner chaque etape \n Si oui tapez 'o' \n Sinon tapez 'n' \n Si vous voulez quitter taper 'q' \n \n Votre choix:")
          if pause_i == 'q':	#pause_i = pause indicateur
               print("\n")
               continue
       		
          while affichage_i != 'o' and affichage_i != 'n' and affichage_i != 'q':
               affichage_i = input("Vous voulez afficher votre Progresse et vos erreurs \n Si oui tapez 'o' \n  Sinon tapez 'n' \n Si vous voulez quitter taper 'q'\n \n Votre choix:")
       		
          if affichage_i == 'q':
               print("\n")
               continue
          elif affichage_i == 'o':
               affichage = True
          elif affichage_i == 'n':
               affichage = False
       	

          while pause_i != 'o' and pause_i != 'n' and pause_i != 'q':
               pause_i = input("Vous voulez afficher examiner chaque etape \n Si oui tapez 'o' \n Sinon tapez 'n' \n Si vous voulez quitter taper 'q' \n \n Votre choix:")
       	
          if pause_i == 'q':
               print("\n")
               continue
          elif pause_i == 'o':
               pause = True
          elif pause_i == 'n':
               pause = False
       	
          #==PARTIE JEU==
          partie_auto(mot_mystere,liste_lettres,affichage,pause) #arg3 : affichage=True,arg4 : pause=False
          print("")
          
          #==REJOUER==
          rejouer = 'e'
          while rejouer == "e":
               rejouer=input("Vous voulez rejouez si oui tape 'e' sinon tape 'q':")
               while rejouer !="e" and rejouer !="q":
                    rejouer=input("Vous voulez rejouez si oui tape 'e' sinon tape 'q':")
               if rejouer == "e":
                    mot_mystere = choisir_mot_alea(mot_mystere_liste)
                    partie_auto(mot_mystere,liste_lettres,affichage,pause) #arg3 : affichage=True,arg4 : pause=False
               print("\n")
       	
     # elif reponse =="3": quitter le jeu
print("Au revoir")
"""

     
     
     


     
    



