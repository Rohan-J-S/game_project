import pygame
import timer
import main_module_1
from threading import Thread
pygame.init()   #initialising pygame

win = pygame.display.set_mode((300,300))
pygame.display.set_caption("HANGMAN")   #window is called hangman

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
    img = pygame.image.load("C:\hangman_comp_project\hang" + str(i) + '.png')
    hang_draw.append(img)

#classes
user_text = text()
word = text()
info = text()
info.y,info.x,info.text = 250,0,None
word.text = main_module_1.word()
word.y,word.x = word.y-30,word.x-5
run = [True,10,set(),0,word.text[0],None]
run[1],run[2] = len(word.text[0]) - word.text[1].count(' ') - main_module_1.vow_ct(word.text[1],run[2]),set()
time_left = text()
time_left.text_font = pygame.font.Font('C:\Windows\Fonts\ELEPHNTI.TTF',18)
info.text_font = pygame.font.Font('C:\Windows\Fonts\HARNGTON.TTF',19)
th_func = Thread(target = timer.func)
th_func.start()

while run[0]:  #main loop
    pygame.time.delay(75)
    time_left.text = str(timer.ctdn)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #when you press big red cross at corner
            run[0] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text.text = user_text.text[:-1]
            elif event.key == pygame.K_RETURN:
                run = main_module_1.game(word.text[1],user_text.text,run[1],run[2],run[3],run[4])
            else:
                user_text.text += event.unicode     #which key is pressed
    if timer.ctdn == 0:
        run[0] = False

    #rendering shit
    surface = user_text.text_font.render(user_text.text,True,(255,255,255))
    ctdn_surface = time_left.text_font.render(time_left.text,True,(255,0,0))
    word_surface = word.text_font.render(run[4],True,(255,255,255))
    info_surface = info.text_font.render(run[5],True,(255,255,255))
    user_text.box.w = max(50,surface.get_width() + 10)
    if run[3]== 6:
        run[0] = False
    else:
        win.blit(hang_draw[run[3]],(0,0))   #hangman
    win.blit(surface,(user_text.x,user_text.y))     #text input
    win.blit(word_surface,(word.x,word.y))
    win.blit(ctdn_surface,(0,0))
    win.blit(info_surface,(info.x,info.y))
    user_text.draw_box()
    pygame.display.update()
    
pygame.quit()
