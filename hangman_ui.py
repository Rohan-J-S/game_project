import pygame
import timer
import threading
pygame.init()   #initialising pygame

win = pygame.display.set_mode((300,300))
pygame.display.set_caption("hangman")   #window is called hangman
run,ct = True,0
PATH = "C:\hangman_comp_project"    #path of folder

class text():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.text_font = pygame.font.Font(None,24)
        self.text = ''
        self.box = pygame.Rect(self.x-5,self.y-5,140,24)
        self.color = (255,0,0)
    def draw_box(self):
        pygame.draw.rect(win,self.color,self.box,2)

hang_draw = []
for i in range(1,7):    #getting images of hangman
    img = pygame.image.load(PATH +"\hang" + str(i) + '.png')
    hang_draw.append(img)

#classes
user_text = text()
word = text()
word.y,word.text,word.x = word.y-30,'WORD',word.x-5
time_left = text()
th_func = threading.Thread(target = timer.func)
th_func.start()
time_left.text = str(timer.ctdn)
while run:  #main loop
    pygame.time.delay(75)
    time_left.text = str(timer.ctdn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #when you press big red cross at corner
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text.text = user_text.text[:-1]
            elif event.key == pygame.K_RETURN:
                ct+=1
            else:
                user_text.text += event.unicode     #which key is pressed
    if timer.ctdn == 0:
        run = False
    win.fill((0,0,0))
    surface = user_text.text_font.render(user_text.text,True,(255,255,255))
    ctdn_surface = time_left.text_font.render(time_left.text,True,(255,0,0))
    word_surface = word.text_font.render(word.text,True,(255,255,255))
    user_text.box.w = max(50,surface.get_width() + 10)
    win.blit(hang_draw[ct],(0,0))   #hangman
    win.blit(surface,(user_text.x,user_text.y))     #text input
    win.blit(word_surface,(word.x,word.y))
    win.blit(ctdn_surface,(0,0))
    user_text.draw_box()
    pygame.display.update()

pygame.quit()
