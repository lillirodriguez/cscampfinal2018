# Vassar CS Camp
# Name: Maimuna Touray
# Filename: fiction.py

""" 
Title for your adventure:   The Coach.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.

"""

import time

""" this function runs one session of interactive fiction
    Well, it's "fiction," depending on the pill color chosen...
    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
"""
delay = 0.0          # change to 0.0 for testing or speed runs,
                     # ..larger for dramatic effect!

username = input("What what should we call you? ")

print()
print("Welcome.", username, " You are freshman in CMPU101")
print()
print("You are struggling to understand Lists and Splicing.")
print()
#2
print("After class, you ask the Coach for help. You say hi...")
print()
coach = input("What is the name of the Coach?: Liam, Hazelle, Arya, Emery.")
print()
if coach == "Liam ":
        print("Liam is into horseback riding and has a secret passion for knitting.")
elif coach == "Hazelle":
        print("Hazelle loves dogs! Enjoys midnight walks to the fridge.")
elif coach == "Arya":
        print("Arya wants to design AI that does your laundry, and has a massive stamp collection.")   
elif coach == "Emery":
        print("Emery like to paint nude self portraits, and east blueberries.")
print()

print("Ya'll sit down to look at your code.Your hand is on the mouse.")
print(coach,"slowly puts their hand on top of yours. Your heart begins to race... ")
print("The palms of your hands sweat and you begin to think there are vibes between you.")
time.sleep(delay)
print()

choice1 = input("Do you move your hand or keep it under " + coach + "s'? [move/stay] ")
print()
#3
if choice1 == "stay":
    print("you catch "+ coach +"s' eye and they smile at you...")
    time.sleep(delay)
    print("You imagine yourself 10 years in the future, married, coparenting, and happily ever after.")
    print("...But then "+ coach +" asks you to explain line 37.")
    print()
    print("You realize you've been staring and drooling just a little bit." )
    print("You wipe the spit out of the corner of your mouth and smile the biggest full tooth grin.")
    print("You know that this is just the beginning of something great between you two! ")
    print ()
else:  
    print("You move your hand,"+ coach + " says, 'oh Im sorry' ")
    print("You shoot them side-eye, and say 'im not into holding hands'. ")
    print()
    print("You slowly move your hand to their thigh. You both lock eyes. The vibes are definitely there")
    print()
    print("You know that this is just the beginning of something great between you two! ")
time.sleep(delay)
print()
print("Three months later...")
print()
print("It's a regular Saturday morning. You lie in bed alone wondering what to get " + coach + " for your three month anniversary")
print("You have never been more in love in your life but, " + coach + " has been acting strange recently . . .") 
print()
print("They've been coming home at odd hours of the night.") 
print("One day you saw them in bloody clothes but they wouldn't tell you whose blood it was.")
print()
print( coach + " says, 'Hey Bae, I have something I need to tell you. But, I'm afraid you wont believe me' ")
print()
print("Your mind goes blank with panic, you stare at them daring them to continue . . .")
print()
print (coach + " says, 'I am a...")
time.sleep(delay)
print()

choice2 = input("What is " + coach + "? [Demigod/Capitalist/Fairy] ")
print()
#4
if choice2 == "Demigod":
    print(coach + " says, I am a Demigod.")
    print()
    print("My father goes by many names, Thor, Zeus, but I call him Abassi,creator of humanity, and lord of the sky. Abassi is trying to kill me." )
    print("I broke my sacred oath as the child of Abassi.")
    print("I was never supposed to fall in love with you, and now because of our love, I have to die. ")
elif choice2 == "Capitalist":
    print(coach + " says, I am a Capitalist.")
    print()
    print("I have been exchanging in the stock market for a year now.")
    print("I have a hookup on the inside that tells me where to put my money. But now hes not responding to any of my calls, I think he got, got")
    print("The italian mafia is after me, they left me a note in my car threatening us.")
elif choice2 == "Fairy": 
    print(coach + " says, I am a Fairy.")
    print()
    print("You're probably more familiar with my cousins, the pixie fairies. But I little something a little more domestic" )
    print("You can think of me as a Tooth Fairy, except instead of giving you money we actually grant wishes") 
    print("Someone wished for me to intiate the apocalypse. I have to refuse but if dont grant a tooth bearers wishes I will die a slow and painful death")
print()
print("You cant even find the words. You turn away from " + coach + " to catch your breath.")
print()
print("They are waiting for your response." )
print()

#1
print("one = I dont want you to die. How can I help you?")
print("two = I need some time to process this foolishness.")
print("three = This is crazy!! Im out.")
print()

choice3 = input("How do you respond? [one/two/three] ")
print()

if choice3 == "one":
    print(coach + " says, 'you mean everything to me, if I die and it protects you its worth it!!!' ")
    print()
elif choice3 == "two":
    print(coach + " says, Of course, take all the time you need. Just stay inside the house where its safe. ")
    print()
else:
    print(coach + "  responds,  noooo I need you to believe me!!")
    print()
    print("You get heated, and say ' " + coach + " I know you're lying to me!! You're cheating and this is the best you can come up with?!?!' ")
    print("I'm done. Pack your bags and be out by Monday!! ")
print()

print("You're heartbroken, the weight of this news knocks you off your feet. You slump into a ball on the floor and cry until...")
print()
print()
time.sleep(delay)
print("You wake up!!! Its dark outside your window. You realize it was all a dream")
print()
print("THE END!")