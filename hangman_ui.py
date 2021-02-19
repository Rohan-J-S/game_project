import pygame
import timer
import main_module_1
from threading import Thread
import encryption_after_termination
import decrypter_test
import tts
from sys import exit

pygame.init()   #initialising pygame

win = pygame.display.set_mode((300,300))
pygame.display.set_caption("HANGMAN")   #window is called hangman

class text():
    def __init__(self,font_style=None,x=100,y=100,size=24):
        self.x = x
        self.y = y
        self.font_style = font_style
        self.size = size
        self.text_font = pygame.font.Font(self.font_style,self.size)
        self.text = ''
        self.box = pygame.Rect(self.x-5,self.y-5,140,24)
        self.color = (255,0,0)
    def draw_box(self):
        pygame.draw.rect(win,self.color,self.box,2)

hang_draw = [] #image loading
for i in range(1,7):    #getting images of hangman
    img = pygame.image.load("C:\hangman_comp_project\hang" + str(i) + '.png')
    hang_draw.append(img)
mic_im = pygame.image.load("C:\hangman_comp_project\mic.png") #mic for voice input

#classes and variablea
user_text = text()
word = text(x=95,y=70)
info = text(x=0,y=250,font_style='C:\Windows\Fonts\HARNGTON.TTF',size=19)
info.text = None
word.text = main_module_1.word()
run = [True,10,set(),0,word.text[0],'Click button for voice input']
run[1],run[2] = len(word.text[0]) - word.text[1].count(' ') - main_module_1.vow_ct(word.text[1],run[2]),set()
time_left = text(font_style = 'C:\Windows\Fonts\ELEPHNTI.TTF',size = 18)
th_func = Thread(target = timer.func)
th_func.start()
mic_on = False
fps = pygame.time.Clock()

while run[0]:  #main loop
    fps.tick(10)
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
        elif event.type == pygame.MOUSEBUTTONDOWN and mic_on == False:
            mic_on = True
    if timer.ctdn == 0:
        run[0] = False
    if mic_on:
        try :
            user_text.text += tts.audio_input()
        except:
            pass
        finally:
            mic_on = False

    #rendering shit
    surface = user_text.text_font.render(user_text.text,True,(255,255,255))
    ctdn_surface = time_left.text_font.render(time_left.text,True,(255,0,0)) #countdown
    word_surface = word.text_font.render(run[4],True,(255,255,255)) #the word
    info_surface = info.text_font.render(run[5],True,(255,255,255)) #errors or mistakes
    user_text.box.w = max(50,surface.get_width() + 10) #text box
    if run[3]== 6:
        run[0] = False
    else:
        win.blit(hang_draw[run[3]],(0,0))   #hangman
    pygame.draw.rect(win,(0,0,0),(150,125,30,30))
    win.blit(mic_im,(150,125))
    win.blit(surface,(user_text.x,user_text.y))     #text input
    win.blit(word_surface,(word.x,word.y))
    win.blit(ctdn_surface,(0,0))
    win.blit(info_surface,(info.x,info.y))
    user_text.draw_box()
    pygame.display.update()

pygame.quit()
decrypter_test.decrypt_file(main_module_1.dec_2)
encryption_after_termination.encrypt()
exit()
