import textwrap
import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
#coach = ' '
class Template(object):
    #def __init__(self,img,text,opt,bckground,state):
    def __init__(self,img,text,bckground,inp=False):
        self.img = pygame.image.load(img)
        self.book = pygame.image.load(bckground) 
        self.text = textwrap.wrap(text, width = 70)
        self.font = pygame.font.SysFont('Arial', 20)
        self.input = inp

       
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

        frac_height = 6
        for line in self.text:
            if frac_height < 1:
                break
            text_surf = self.font.render(line, False, black)
            window.blit(text_surf,(book_width//2.6,book_height//frac_height))
            frac_height -= 0.5




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
    
   
