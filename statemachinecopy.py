from transitions import Machine
import time
import book
import text
import pygame

pygame.init()
display_width = 1920
display_height = 1080

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Open Book')

delay = 0.0
 

class myClass(object):
    def __init__(self):
        self.coach = ''

    def chapterone(self):
        result = text.prompts['titlepage'].call_tmp(gameDisplay)
        result == None

    def chaptertwo(self):
        result = text.prompts['inclass'].call_tmp(gameDisplay)
        if result == "A":
            result = text.prompts['liam'].call_tmp(gameDisplay)
            text.choose_coach('Liam')
        elif result == "B":
            result = text.prompts['hazelle'].call_tmp(gameDisplay)
            text.choose_coach('Hazelle')
        elif result == "C":
            result = text.prompts['arya'].call_tmp(gameDisplay)
            text.choose_coach('Arya') 
        elif result == "D":
            result = text.prompts['emery'].call_tmp(gameDisplay)
            text.choose_coach('Emery')

    def chapterthree(self):
        result = text.prompts['backinclass'].call_tmp(gameDisplay)

        result = text.prompts['moveorstay'].call_tmp(gameDisplay)
        if result == "A":
            result = text.prompts['move'].call_tmp(gameDisplay)
        else:
            result = text.prompts['stay'].call_tmp(gameDisplay)

    def chapterfour(self):
        result = text.prompts['threemonths'].call_tmp(gameDisplay)
        result = text.prompts['whatiscoach'].call_tmp(gameDisplay)

        if result == "A":
            result = text.prompts['demigod'].call_tmp(gameDisplay)
        elif result == "B":
            result = text.prompts['capitalist'].call_tmp(gameDisplay)
        elif result == "C": 
            result = text.prompts['fairy'].call_tmp(gameDisplay)

    def chapterfive(self):
        result = text.prompts['whatisresponse'].call_tmp(gameDisplay)

        if result == "A":
            result = text.prompts['fear'].call_tmp(gameDisplay)
        elif result == "B":
            result = text.prompts['clock'].call_tmp(gameDisplay)
        else:
            result = text.prompts['door'].call_tmp(gameDisplay)

    def chaptersix(self):
        result = text.prompts['hide'].call_tmp(gameDisplay)

    def chapterseven(self):
        result = text.prompts['nextday'].call_tmp(gameDisplay)


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
    