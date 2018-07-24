import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
coach = ' '
class Template(object):
    #def __init__(self,img,text,opt,bckground,state):
    def __init__(self,img,text,bckground):
        self.img = pygame.image.load(img)
        self.book = bckground
        self.text = text
        self.font = pygame.font.SysFont('Arial', 35)
        #self.state = state

        # self.opt = {}
        # key = 'a'
        # for o in opt:
        #     self.opt[key] = o
        #     key = chr(ord(key) + 1)
    
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
            pass
        elif press == pygame.K_b:
            pass
        elif press == pygame.K_c:
            pass

    def draw_text(self,window):
        book_width = self.book.get_width()
        book_height = self.book.get_height()

        text_surf = self.font.render(self.text, False, black)
        window.blit(text_surf,(book_width//2.6,book_height//4))




display_width = 1920
display_height = 1080

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Open Book')


clock = pygame.time.Clock()
crashed = False
bkImg = pygame.image.load('book.png')


   
# while not crashed:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True
#


 
# def newPic(file, ):
#     for i in picLyst = []:

# title text    
#title_font = pygame.font.SysFont('Arial', 115)
#title = 'This Is The Title'
#title_surf = title_font.render(title, False, black)
    
# accompanying picture on book
# picLyst = ['blue.jpeg',  'choose.jpg', 'cs-class.jpeg', 'emoji.png', 'fam.jpg', 'fridge.jpg',  'knit.jpg',  'money.jpg', 'robot.jpg', 'time.jpg',
#  'clock.jpg', 'door.jpg', 'fairy-wings.png',  'F-emoji.png',  'hide.jpg', 'light.jpg',  'red-green.jpg',  'tomorrow.jpg']

# next button
rect = pygame.Rect(1500, 450, 100, 100)

tmp = Template('door.jpg','this is the prompt text',bkImg)

while True:
    for event in pygame.event.get():
        if pygame.KEYDOWN == event.type:
            tmp.choose(event.key)
        if event.type == pygame.QUIT:
            pygame.quit()

    gameDisplay.fill(white)
    tmp.draw(gameDisplay)
    pygame.draw.rect(gameDisplay,pygame.Color(0,0,0),rect)
        
    pygame.display.update()
    clock.tick(60)
