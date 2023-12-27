import turtle
import time
import os # it allows us to determinate the location of this file

import sys # it allows us to acces another python file
from fonctions import *

sys.path.insert(0,os.getcwd()) #pwd
#sys.path.insert(0,r'C:\Users\acer\Desktop\Python Kodlarım\Adam_Asmaca')

def LoadingScreen():
    # Create a turtle screen
    screen = turtle.Screen()

    # Set up the screen properties
    screen.title("Hangman")
    screen.bgcolor("light blue")
    screen.setup(width=800, height=600)

    # Create a turtle for drawing
    load_drawT = turtle.Turtle()
    load_drawT.color("white")
    load_drawT.penup()
    load_drawT.hideturtle()

    # Set the initial state of the turtle
    load_drawT.goto(0, 180)

    # Write loading screen text
    load_drawT.write("Hangman", align="center", font=("Times", 60, "normal"))

    # Load image in loading screen
    screen.addshape("darkS.gif")
    load_image = turtle.Turtle()
    load_image.penup()
    load_image.goto(0, 0)
    load_image.shape("darkS.gif")

    # Perform any tasks here
    time.sleep(2)   #time Package

    load_drawT.clear()
    load_image.hideturtle()

    # Call the Menu function
    Menu(screen)

def Menu(screen):
    # Create turtle for drawing
    menu_drawT = turtle.Turtle()
    menu_drawT.color("black")
    menu_drawT.penup()

    menu_drawT.goto(50, 200)
    y = 200

    menu_options = ["1- Play",
                    "2- Let AI play",
                    "3- Options",
                    "4- Quit"]

    for option in menu_options:
        menu_drawT.write(option, align="left", font=("Arial", 24, "normal"))
        y -= 50
        menu_drawT.goto(50, y)


    # Function to handle the menu selection
    def option_1(): 
        print("Option 1 selected")

        menu_drawT.clear()

        # Unregister the key press event handlers for the previous page
        screen.onkeypress(None, "1")
        screen.onkeypress(None, "2")
        screen.onkeypress(None, "3")
        screen.onkeypress(None, "4")

        #menu_drawT = turtle.Turtle()
        
        if topic == "film":
            partie_humain_alea("motsCinema.txt",nb_err_max,menu_drawT,"-")   #SHOULD CHANGE THE FOLDER NAME
        elif topic == "music":
            partie_humain_alea("motsMusic.txt",nb_err_max,menu_drawT,'-')   #SHOULD CHANGE THE FOLDER NAME



        def BackMENU():
            menu_drawT.clear()     # main
            #AutoT.clear()   
            

            menu_drawT.hideturtle() 
            #AutoT.hideturtle()
        

            # Unregister the key press event handlers for the previous page
            screen.onkeypress(None, "q")
            
            Menu(screen)

        
        screen.onkeypress(BackMENU, "q")
        screen.listen()

     

    def option_2():
        print("Option 2 selected")
        
        menu_drawT.clear()

        # Unregister the key press event handlers for the previous page
        screen.onkeypress(None, "1")
        screen.onkeypress(None, "2")
        screen.onkeypress(None, "3")
        screen.onkeypress(None, "4")

        
        AutoT = turtle.Turtle()
        AutoT.penup()
        
        
        menu_drawT.goto(20,220)
        menu_drawT.write("Erreur:",align="right",font=("Arial",24,"normal"))

        AutoT.goto(30,220)
        #AutoT.write("0",align="right",font=("Arial",24,"normal"))
        
        mot_mystere = choisir_mot_alea(one_topic_liste)
        # partie_auto(mot_myst,liste_lettres,affichage=True,pause=False)
        partie_auto(mot_mystere,liste_lettres,AutoT,True,False)



        # Return to MENU
        menu_drawT.goto(120,-240)
        menu_drawT.write("Press Q for returning to MENU", align="left", font=("Arial", 12, "normal"))

        
        def BackMENU():
            menu_drawT.clear()     # main
            AutoT.clear()   
            

            menu_drawT.hideturtle() 
            AutoT.hideturtle()
        

            # Unregister the key press event handlers for the previous page
            screen.onkeypress(None, "q")
            
            Menu(screen)

        
        screen.onkeypress(BackMENU, "q")
        screen.listen()


        
    def option_3():
        print("Option 3 selected")
        
        liste_lettres = fabrique_liste_alphabet()
        menu_drawT.clear()

        

        # Unregister the key press event handlers for the previous page
        screen.onkeypress(None, "1")
        screen.onkeypress(None, "2")
        screen.onkeypress(None, "3")
        screen.onkeypress(None, "4")


        global difficulty  # Add this line to access the global variable
        global topic       # Add this line to access the global variable

        # Rest of the function code...

        # Fonctions
        
        def DiffHard():
            global difficulty  # Add this line to access the global variable
            global nb_err_max
            
            difficulty = "hard"
            nb_err_max = 5
            print("max error number is 5")
            
            DiffT.clear()
            DiffT.goto(160,200)
            
            DiffT.write("Hard", align="left", font=("Arial", 24, "normal"))
            DiffT.goto(120,190)

            DiffT.pendown()
            for i in range(2):
                DiffT.fd(150)
                DiffT.left(90)
                DiffT.fd(60)
                DiffT.left(90)
            DiffT.penup()

        def DiffEasy():
            global difficulty  # Add this line to access the global variable
            global nb_err_max 
            
            difficulty = "easy"
            nb_err_max = 10
            print("max error number is 10")
            
            DiffT.clear()
            DiffT.goto(160,200)
            DiffT.write("Easy", align="left", font=("Arial", 24, "normal"))

            
            DiffT.goto(120,190)
            DiffT.pendown()
            for i in range(2):
                DiffT.fd(150)
                DiffT.left(90)
                DiffT.fd(60)
                DiffT.left(90)
            DiffT.penup()

        def TopicFilm():
            global topic       # Add this line to access the global variable
            topic = "film"
            one_topic_liste = importer_mots("motsCinema.txt")
            print("The subject is Films")
            
            TopicT.clear()
            TopicT.goto(160,y)
            TopicT.write("Films",align="left", font=("Arial", 24, "normal"))

            TopicT.goto(120,y-10)
            TopicT.pendown()
            for i in range(2):
                TopicT.fd(150)
                TopicT.left(90)
                TopicT.fd(60)
                TopicT.left(90)
            TopicT.penup()

        def TopicMusic():
            global topic       # Add this line to access the global variable
            global one_topic_liste
            topic = "music"
            one_topic_liste = importer_mots("motsMusic.txt")
            print("The subject is Music")
            
            TopicT.clear()
            TopicT.goto(150,y)
            TopicT.write("Musics",align="left", font=("Arial", 24, "normal"))

            TopicT.goto(120,y-10)
            TopicT.pendown()
            for i in range(2):
                TopicT.fd(150)
                TopicT.left(90)
                TopicT.fd(60)
                TopicT.left(90)
            TopicT.penup()


        def BackMENU():
            menu_drawT.clear()     # main
            DiffT.clear()   # option turtle 1
            TopicT.clear()        # option turtle 2

            menu_drawT.hideturtle() 
            DiffT.hideturtle()
            TopicT.hideturtle()

            # Unregister the key press event handlers for the previous page
            screen.onkeypress(None,"d")
            screen.onkeypress(None,"f")

            screen.onkeypress(None,"1")
            screen.onkeypress(None,"2")

            screen.onkeypress(None, "q")
            
            Menu(screen)
        
        # Difficulty
        menu_drawT.goto(-300,200)
        y = 200
        menu_drawT.write("Difficulty", align="left", font=("Arial", 24, "normal"))
        menu_drawT.goto(-300,y-20)
        y = y-20
        menu_drawT.write("Press F for EASY or D for DIFFICULT", align="left", font=("Courier", 12, "normal"))

        # Topic
        menu_drawT.goto(-300,y-100)
        y = y - 100
        menu_drawT.write("Topic", align="left", font=("Arial", 24, "normal"))
        menu_drawT.goto(-300,y-20)
        
        menu_drawT.write("1- Films | 2- Musics", align="left", font=("Courier", 12, "normal"))

        # Easy/Dificult indicator
        DiffT = turtle.Turtle() 
        DiffT.speed(0)
        DiffT.penup()

        
        DiffT.goto(150,200)
        if difficulty == "easy":
            DiffT.write("Easy", align="left", font=("Arial", 24, "normal"))

            
            DiffT.goto(120,190)
            DiffT.pendown()
            for i in range(2):
                DiffT.fd(150)
                DiffT.left(90)
                DiffT.fd(60)
                DiffT.left(90)
            DiffT.penup()
        else:
            DiffT.goto(160,200)
            DiffT.write("Hard", align="left", font=("Arial", 24, "normal"))
            DiffT.goto(120,190)

            DiffT.pendown()
            for i in range(2):
                DiffT.fd(150)
                DiffT.left(90)
                DiffT.fd(60)
                DiffT.left(90)
            DiffT.penup()

        
        # Topic indicator
        TopicT = turtle.Turtle()    
        TopicT.speed(0)
        TopicT.penup()

        if topic == "film":
            TopicT.goto(160,y)
            TopicT.write("Films",align="left", font=("Arial", 24, "normal"))

            TopicT.goto(120,y-10)
            TopicT.pendown()
            for i in range(2):
                TopicT.fd(150)
                TopicT.left(90)
                TopicT.fd(60)
                TopicT.left(90)
            TopicT.penup()

        elif topic == "music":
            TopicT.goto(150,y)
            TopicT.write("Musics",align="left", font=("Arial", 24, "normal"))

            TopicT.goto(120,y-10)
            TopicT.pendown()
            for i in range(2):
                TopicT.fd(150)
                TopicT.left(90)
                TopicT.fd(60)
                TopicT.left(90)
            TopicT.penup()


        # Return to MENU
        menu_drawT.goto(120,-240)
        menu_drawT.write("Press Q for returning to MENU", align="left", font=("Arial", 12, "normal"))


        # Register the key press event handlers
        screen.onkeypress(DiffHard,"d")
        screen.onkeypress(DiffEasy,"f")

        screen.onkeypress(TopicFilm,"1")
        screen.onkeypress(TopicMusic,"2")
            
        screen.onkeypress(BackMENU, "q")
        screen.listen()

        
        
    def option_4(): # Quit
        print("Option 4 selected")
        turtle.bye()


    
    # Register the key press event handlers
    screen.onkeypress(option_1, "1")
    screen.onkeypress(option_2, "2")
    screen.onkeypress(option_3, "3")
    screen.onkeypress(option_4, "4")

    # Keep the turtle window open
    screen.listen()


# The variants
difficulty = "normal" #10 chances
nb_err_max = 10

topic = "film"
one_topic_liste = importer_mots("motsCinema.txt")


liste_lettres = fabrique_liste_alphabet()

# Call the LoadingScreen function
LoadingScreen()
