from transitions import Machine
import time

delay = 0.0

class myClass(object):
    def __init__(self):
        self.coach = ''

    def chapterone(self):
        username = input("What should we call you? ")
        time.sleep(delay)
        print()
        print("Welcome,", username, "!")
        print("You are a freshman in CMPU101")

    def chaptertwo(self):
        print("After class, you ask the coach for help. You say hi...")
        time.sleep(delay)
        print()
        self.coach = input("What is the name of the coach? A) Liam, B) Hazelle, C) Arya, D) Emery? ")
        time.sleep(delay)
        if self.coach == "A":
            print("Liam is into horseback riding and has a secret passion for knitting.")
            self.coach = "Liam"
        elif self.coach == "B":
            print("Hazelle loves dogs! Enjoys midnight walks to the fridge.")
            self.coach = "Hazelle"
        elif self.coach == "C":
            print("Arya wants to design AI that does your laundry and has a massive stamp collection.")
            self.coach = "Arya"  
        elif self.coach == "D":
            print("Emery like to paint nude self portraits, and eat blueberries.")
            self.coach = "Emery"
        time.sleep(delay)

    def chapterthree(self):
        print()
        print("Y'all sit down to look at your code. Your hand is on the mouse.")
        time.sleep(delay)
        print(self.coach + " slowly puts their hand on top of yours. Your heart begins to race... ")
        time.sleep(delay)
        print("The palms of your hands sweat and you begin to think there are vibes between you.")
        time.sleep(delay)
        print()

        choice1 = input("Do you move your hand or keep it under " + self.coach + "'s? A) Move or B) Stay ")
        time.sleep(delay)
        print()
        #3
        if choice1 == "A":
            time.sleep(delay)
            print("you catch "+ self.coach +"'s eye and they smile at you...")
            time.sleep(delay)
            print("You imagine yourself 10 years in the future, married, coparenting, and happily ever after.")
            time.sleep(delay)
            print("...But then "+ self.coach +" asks you to explain line 37.")
            time.sleep(delay)
            print()
            print("You realize you've been staring and drooling just a little bit." )
            time.sleep(delay)
            print("You wipe the spit out of the corner of your mouth and smile the biggest full tooth grin.")
            time.sleep(delay)
            print("You know that this is just the beginning of something great between you two!")
            time.sleep(delay)
            print ()
        else:
            time.sleep(delay)
            print("You move your hand, "+ self.coach + " says, 'oh Im sorry' ")
            time.sleep(delay)
            print("You shoot them side-eye, and say 'I'm not into holding hands.' ")
            time.sleep(delay)
            print()
            print("You slowly move your hand to their thigh. You both lock eyes. The vibes are definitely there...")
            print()
            time.sleep(delay)
            print("You know that this is just the beginning of something great between you two! ")

    def chapterfour(self):
        time.sleep(delay)
        print()
        print("Three months later...")
        print()
        time.sleep(delay)
        print("It's a regular Saturday morning. You lie in bed alone wondering what to get " + self.coach + " for your three month anniversary")
        time.sleep(delay)
        print("You have never been more in love in your life but, " + self.coach + " has been acting strange recently . . .") 
        print()
        time.sleep(delay)
        print("They've been coming home at odd hours of the night.") 
        time.sleep(delay)
        print("One day you saw them in bloody clothes but they wouldn't tell you whose blood it was.")
        print()
        time.sleep(delay)
        print(self.coach + " says, 'Hey Bae, I have something I need to tell you. But, I'm afraid you wont believe me' ")
        print()
        time.sleep(delay)
        print("Your mind goes blank with panic, you stare at them daring them to continue . . .")
        print()
        time.sleep(delay)
        print (self.coach + " says, 'I am a...")
        time.sleep(delay)
        print()

        choice2 = input("What is " + self.coach + "? A) Demigod, B) Capitalist, C) Fairy ")
        print()
        #4
        if choice2 == "A":
            print(self.coach + " says, I am a Demigod.")
            time.sleep(delay)
            print()
            print("My father goes by many names, Thor, Zeus, but I call him Abassi,creator of humanity, and lord of the sky. Abassi is trying to kill me." )
            time.sleep(delay)
            print("I broke my sacred oath as the child of Abassi.")
            time.sleep(delay)
            print("I was never supposed to fall in love with you, and now because of our love, I have to die. ")
        elif choice2 == "B":
            print(self.coach + " says, I am a Capitalist.")
            time.sleep(delay)
            print()
            print("I have been exchanging in the stock market for a year now.")
            time.sleep(delay)
            print("I have a hookup on the inside that tells me where to put my money. But now hes not responding to any of my calls, I think he got, got")
            time.sleep(delay)
            print("The italian mafia is after me, they left me a note in my car threatening us.")
        elif choice2 == "C": 
            print(self.coach + " says, I am a Fairy.")
            time.sleep(delay)
            print()
            print("You're probably more familiar with my cousins, the pixie fairies. But I little something a little more domestic" )
            time.sleep(delay)
            print("You can think of me as a Tooth Fairy, except instead of giving you money we actually grant wishes") 
            time.sleep(delay)
            print("Someone wished for me to intiate the apocalypse. I have to refuse but if dont grant a tooth bearers wishes I will die a slow and painful death")
        time.sleep(delay)
        print()
        print("You cant even find the words. You turn away from " + self.coach + " to catch your breath.")
        print()
        time.sleep(delay)
        print("They are waiting for your response." )
        print()
        time.sleep(delay)

    def chapterfive(self):
        print("A) I dont want you to die. How can I help you?")
        print("B) I need some time to process this foolishness.")
        print("C) This is crazy!! Im out.")
        print()
        time.sleep(delay)

        choice3 = input("How do you respond? A, B, or C? ")
        print()

        if choice3 == "A":
            print(self.coach + " says, 'you mean everything to me, if I die and it protects you its worth it!!!' ")
            print()
        elif choice3 == "B":
            print(self.coach + " says, Of course, take all the time you need. Just stay inside the house where its safe. ")
            print()
        else:
            print(self.coach + "  responds,  noooo I need you to believe me!!")
            print()
            time.sleep(delay)
            print("You get heated, and say ' " + self.coach + ", I know you're lying to me!! You're cheating and this is the best you can come up with?!?!' ")
            time.sleep(delay)
            print("I'm done. Pack your bags and be out by Monday!!")
            print()

    def chaptersix(self):
        time.sleep(delay)
        print("You're heartbroken, the weight of this news knocks you off your feet. You slump into a ball on the floor and cry until...")
        print()
        print()
        time.sleep(delay)

    def chapterseven(self):
        print("You wake up!!! Its dark outside your window. You realize it was all a dream")
        time.sleep(delay)
        print()
        print("THE END!")


story = myClass()

states = ['yourName', 'theirName', 'moment', 'trouble', 'response', 'heartBreak', 'theEnd']

#def afterInputName():
#    print('Yay! You have entered your name!')
transitions = [
    {'trigger': 'inputName', 'source': 'yourName', 'dest': 'theirName'}, 
    {'trigger': 'decision', 'source': 'theirName', 'dest': 'moment'},
    {'trigger': 'toTrouble', 'source': 'moment', 'dest': 'trouble'},
    {'trigger': 'whatAreYou', 'source': 'trouble', 'dest': 'response'},
    {'trigger': 'trigger', 'source': 'response', 'dest': 'heartBreak'},
    {'trigger': 'gameOver', 'source': 'heartBreak', 'dest': 'theEnd'},
]

machine = Machine(model=story, states=states, transitions=transitions, initial='yourName', ignore_invalid_triggers=True)



machine.on_exit_yourName('chapterone')
machine.on_enter_theirName('chaptertwo')
machine.on_enter_moment('chapterthree')
machine.on_enter_trouble('chapterfour')
machine.on_enter_response('chapterfive')
machine.on_enter_heartBreak('chaptersix')
machine.on_enter_theEnd('chapterseven')
story.inputName()
story.decision()
story.toTrouble()
story.whatAreYou()
story.trigger()
story.gameOver()
    