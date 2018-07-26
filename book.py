import textwrap
import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
#coach = ' '
class Template(object):
    #def __init__(self,img,text,opt,bckground,state):
    def __init__(self,img,text,bckground,inp=False, title=False):
        self.img = pygame.image.load(img)
        self.book = pygame.image.load(bckground) 
        self.text = None
        self.extract_response(textwrap.wrap(text, width = 50))
        self.font = pygame.font.SysFont('Arial', 20,1)
        self.input = inp
        self.title = title

    def extract_response(self, lines):
        for line in range(len(lines)):
            if "A)" in lines[line]:
                start= lines[line].find("A)")
                response_lines=textwrap.wrap(lines[line][start:]+''.join(lines[line+1:]), width=50)
                lines[line]= lines[line][:start]
                self.text = lines[:line+1] + response_lines
                break
        else:
            self.text = lines


    def call_tmp(self, window):
        
        window.fill(white)
        self.draw(window)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if pygame.KEYDOWN == event.type:
                    check = self.choose(event.key)
                    if self.input == False:
                        if check == ' ':
                            return
                        else:
                            continue
                    else:
                        if check == '@' or check == ' ':
                            continue
                        else:
                            return check
                if event.type == pygame.QUIT:
                    pygame.quit()

    
    def draw(self,window):
        x = (window.get_width() * 0.05)
        y = (window.get_height() * 0.1)

        # draw book
        window.blit(self.book, (x,y))

        book_width = self.book.get_width()
        book_height = self.book.get_height()

        self.draw_text(window)

        self.img = pygame.transform.scale(self.img, (book_width//5,book_height//4))
        window.blit(self.img,(book_width//10,book_height//5))

    def choose(self, press):
        if press == pygame.K_a:
            return 'A'
        elif press == pygame.K_b:
            return 'B'
        elif press == pygame.K_c:
            return 'C'
        elif press == pygame.K_d:
            return 'D'
        elif press == pygame.K_SPACE:
            return ' '
        else:
            return '@'

    def draw_text(self,window):
        book_width = self.book.get_width()
        book_height = self.book.get_height()

        if self.title:
            height = book_height//5
            for line in self.text:
                text_surf = self.font.render(line, False, black)
                window.blit(text_surf,(book_width//2.6,height))
                height += 30
        else:
            height = book_height//5
            for line in self.text:
                text_surf = self.font.render(line, False, black)
                window.blit(text_surf,(book_width//2.8,height))
                height += 30




# display_width = 1920
# display_height = 1080

# gameDisplay = pygame.display.set_mode((display_width,display_height))


# bkImg = pygame.image.load('book.png')

# tmp = Template('door.jpg','this is the prompt text',bkImg, True)
# print(tmp.call_tmp(gameDisplay))

# accompanying picture on book
# picLyst = ['blue.jpeg',  'choose.jpg', 'cs-class.jpeg', 'emoji.png', 'fam.jpg', 'fridge.jpg',  'knit.jpg',  'money.jpg', 'robot.jpg', 'time.jpg',
#  'clock.jpg', 'door.jpg', 'fairy-wings.png',  'F-emoji.png',  'hide.jpg', 'light.jpg',  'red-green.jpg',  'tomorrow.jpg']

# next button
    
   
