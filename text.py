import book

titlepage = ('What should we call you?')

inclass = ("Welcome! You are a freshman in CMPU101. \
After class, you ask the coach for help. You say hi. . . \
What is the name of the coach? A) Liam, B) Hazelle, C) Arya, D) Emery?")

liam = ("Liam is into horseback riding and has a secret passion for knitting.")

hazelle = ("Hazelle loves dogs! Enjoys midnight walks to the fridge.")

arya = ("Arya wants to design AI that does your laundry and has a massive stamp collection.")

emery = ("Emery like to paint nude self portraits, and eat blueberries.")

backinclass = ("Y'all sit down to look at your code. Your hand is on the mouse. \
{0} slowly puts their hand on top of yours. Your heart begins to race. . . \
The palms of your hands sweat and you begin to think there are vibes between you.")

moveorstay = ("Do you move your hand or keep it under {0}'s? A) Move or B) Stay")

move = ("You move your hand, {0} says, 'Oh, I'm sorry.' You shoot them side-eye, and say 'I'm not into holding hands.' You slowly move your hand to their thigh. You both lock eyes. The vibes are definitely there. . . You know that this is just the beginning of something great between you two!")

stay = ("You catch {0}'s eye and they smile at you... \
You imagine yourself 10 years in the future, married, coparenting, and happily ever after \
. . . But then {0} asks you to explain line 37. \
You realize you've been staring and drooling just a little bit. \
You wipe the spit out of the corner of your mouth and smile the biggest full tooth grin. \
You know that this is just the beginning of something great between you two!")

threemonths = ("Three months later. . . \
It's a regular Saturday morning. You lie in bed alone wondering what to get {0} for your three month anniversary. \
You have never been more in love in your life, but {0} has been acting strange recently . . . \
They've been coming home at odd hours of the night. \
One day you saw them in bloody clothes but they wouldn't tell you whose blood it was.")

whatiscoach = ("{0} says, 'Hey Bae, I have something I need to tell you, but I'm afraid you wont believe me' \
Your mind goes blank with panic, you stare at them daring them to continue . . . \
                     {0} says, 'I am a. . . \
What is {0}? A) Demigod, B) Capitalist, C) Fairy")

demigod = ("{0} says, 'I am a Demigod. \
My father goes by many names, Thor, Zeus, but I call him Abassi, creator of humanity, and lord of the sky. Abassi is trying to kill me. \
I broke my sacred oath as the child of Abassi. \
I was never supposed to fall in love with you, and now because of our love, I have to die.' \
You can't even find the words. You turn away from {0} to catch your breath.")

capitalist = ("{0} says, 'I am a Capitalist. \
I have been exchanging in the stock market for a year now. \
I have a hookup on the inside that tells me where to put my money. But now he's not responding to any of my calls. I think he got, got. . . \
The italian mafia is after me, they left me a note in my car threatening us.' \
You can't even find the words. You turn away from {0} to catch your breath.")

fairy = ("{0} says, 'I am a Fairy.\
You're probably more familiar with my cousins, the pixie fairies. But I'm something a little more domestic.\
You can think of me as a Tooth Fairy, except instead of giving you money for teeth we actually grant wishes. \
Someone wished for me to intiate the apocalypse. I have to refuse, but if dont grant a tooth bearer's wishes I will die a slow and painful death.' \
You can't even find the words. You turn away from {0} to catch your breath.")

whatisresponse = ("They are waiting for your response. \
A) I don't want you to die. How can I help you?    \
B) I need some time to process this foolishness.      \
C) This is crazy!! Im out. \
How do you respond?")

fear = ("{0} says, 'You mean everything to me, if I die and it protects you it' s worth it!!!'")

clock = ("{0} says, 'Of course, take all the time you need. Just stay inside the house where it's safe.'")

door = ("{0} responds,'Noooo I need you to believe me!!'")

hide = ("You're heartbroken, the weight of this news knocks you off your feet. You slump into a ball on the floor and cry until...")

nextday = ("You wake up!!! It's dark outside your window. You realize it was all a dream. \
THE END!")

bkImg = 'book.png'
prompts = {
    'titlepage': book.Template('choose.jpg', titlepage, bkImg, title=True),
    'inclass': book.Template('cs-class.jpeg', inclass, bkImg, inp=True),
    'liam': book.Template('knit.jpg', liam, bkImg),
    'hazelle': book.Template('fridge.jpg', hazelle, bkImg),
    'arya': book.Template('robot.jpg', arya, bkImg),
    'emery': book.Template('blue.jpeg', emery, bkImg),
    'backinclass': book.Template('cs-class.jpeg', backinclass, bkImg),
    'moveorstay': book.Template('red-green.jpg', moveorstay, bkImg, inp=True),
    'move': book.Template('emoji.png', move, bkImg), 
    'stay': book.Template('fam.jpg', stay, bkImg),
    'move': book.Template('emoji.png', move, bkImg),
    'threemonths': book.Template('time.jpg', threemonths, bkImg),
    'whatiscoach': book.Template('threepic.png', whatiscoach, bkImg, inp=True),
    'demigod': book.Template('threepic.png', demigod, bkImg),
    'capitalist': book.Template('threepic.png', capitalist, bkImg),
    'fairy': book.Template('threepic.png', fairy, bkImg),
    'whatisresponse': book.Template('threepic.png', whatisresponse, bkImg, inp=True),
    'fear': book.Template('F-emoji.png', fear, bkImg),
    'clock': book.Template('clock.jpg', clock, bkImg),
    'door': book.Template('door.jpg', door, bkImg), 
    'hide': book.Template('hide.jpg', hide, bkImg),
    'nextday': book.Template('tomorrow.jpg', nextday, bkImg),
}

def choose_coach(name):
    global prompts

    for tmp in prompts.values():
        for line in range(len(tmp.text)):
            tmp.text[line] = tmp.text[line].format(name)
