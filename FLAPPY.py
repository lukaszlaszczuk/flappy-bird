# -*- coding: utf-8 -*-
"""
Created on Wed May 23 01:24:57 2018

@author: Luck777
"""

import pygame
import time
import random
import numpy as np

SZEROKOSC=480
WYSOKOSC=600

CZARNY = (0,0,0)
CZERWONY = (255,0,0)
JCZERWONY = (239, 57, 57)
ZIELONY = (113, 244, 66)
NIEBIESKI = (66,134,244)
JNIEBIESKI= (142, 183, 249)
ptak_dol_wysokosc = 53
pygame.init()#inicjaizujemy moduł pygame
ekran = pygame.display.set_mode((SZEROKOSC,WYSOKOSC)) #włączamy ekran o zadanych wymiarach


pygame.display.set_caption('Flappy') #tytuł
clock = pygame.time.Clock()
#ladujemy obrazek ptaka(co nie ma go jeszcze na ekranie)
ptaszek = pygame.image.load('flappymoj.png')
ptaszek1 = pygame.image.load('flappymoj1.png')#4 ptaki, aby mogl "latac"
ptaszek2 = pygame.image.load('flappymoj2.png')
ptaszek3 = pygame.image.load('flappymoj3.png')
zycia_3 = pygame.image.load('3zycia.png')
zycia_2 = pygame.image.load('2zycia.png')
zycia_1 = pygame.image.load('1zycie.png')
#aby wrzucić naszego birda na ekran w dannym miejscu używam:
def ptak(x,y): 
    ekran.blit(ptaszek,(x,y))
def ptak1(x,y): #blit wrzuci obrazek w podane miejsce
    ekran.blit(ptaszek1,(x,y))
def ptak2(x,y):
    ekran.blit(ptaszek2,(x,y))
def ptak3(x,y):
    ekran.blit(ptaszek3,(x,y))
def zycia3(x,y):
    ekran.blit(zycia_3,(x,y))
def zycia2(x,y):
    ekran.blit(zycia_2,(x,y))
def zycia1(x,y):
    ekran.blit(zycia_1,(x,y))
def przeszkoda(x_startowy, y_startowy, pw, wysokosci, color):
    for i in range(len(x_startowy)):
        pygame.draw.rect(ekran, color, [x_startowy[i],y_startowy,pw,wysokosci[i]])#gorna rura 1
        pygame.draw.rect(ekran,color,[x_startowy[i],wysokosci[i]+115,pw,WYSOKOSC-(wysokosci[i]+115)])#dolna rura 1
    
def text_objects(text, font):
    textSurface = font.render(text, True,CZERWONY)#rysuj tekst
    return textSurface, textSurface.get_rect()
def text_objects1(text, font):
    textSurface = font.render(text, True,CZARNY)#rysuj tekst
    return textSurface, textSurface.get_rect()
def wypisz_koniec(text):
    largeText = pygame.font.Font('freesansbold.ttf',60)    
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center=((SZEROKOSC/2),(WYSOKOSC/2))
    ekran.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    gameloop()
def wypisz_utrata(text,liczba):
    largeText = pygame.font.Font('freesansbold.ttf',30)    
    TextSurf, TextRect = text_objects(text+str(liczba),largeText)
    TextRect.center=((SZEROKOSC/2),(WYSOKOSC*0.25))
    ekran.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
def wynik(liczba):
    font = pygame.font.SysFont(None,30)
    text  = font.render("SCORE:"+str(liczba),True,CZERWONY)
    ekran.blit(text,(0.05*SZEROKOSC,0.07*WYSOKOSC ))
    
    
def koniec_gry():
    wypisz_koniec('GAME OVER!!!')
def kraksa(liczba):
    wypisz_utrata('CRASH! LIFES: ', liczba)
def loadSound(name):
    
    sound = pygame.mixer.Sound(name)
    return sound
def punkt():
    a=loadSound('sfx_point.wav')
    a.play()
def hit():
    a=loadSound('sfx_hit.wav')
    a.play()
def lot():
    a=loadSound('sfx_wing.wav')
    a.play()
def rules():
    intro = True #przycisk(msg,x,y,w,h,i,a)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        ekran.fill(ZIELONY)
        largeText = pygame.font.Font('freesansbold.ttf',25)
        TextSurf, TextRect = text_objects('Press space to fly.',largeText)
        TextRect.center=((SZEROKOSC/2),(WYSOKOSC*0.15))
        TextSurf1, TextRect1 = text_objects('Avoid crashing into black pipes.',largeText)
        TextSurf2, TextRect2 = text_objects("Don't fall on the ground!",largeText)
        TextSurf3, TextRect3 = text_objects("You have 3 lifes.",largeText)
        TextRect1.center=((SZEROKOSC/2),(WYSOKOSC*0.25))
        TextRect2.center=((SZEROKOSC/2),(WYSOKOSC*0.35))
        TextRect3.center=((SZEROKOSC/2),(WYSOKOSC*0.45))
        ekran.blit(TextSurf, TextRect)
        ekran.blit(TextSurf1, TextRect1)
        ekran.blit(TextSurf2, TextRect2)
        ekran.blit(TextSurf3, TextRect3)
        przycisk('Menu',SZEROKOSC*0.7,WYSOKOSC*0.85,100,50,NIEBIESKI,JNIEBIESKI,'menu')
        przycisk('FLY!',SZEROKOSC*0.1,WYSOKOSC*0.85,100,50,NIEBIESKI,JNIEBIESKI,'play')
        pygame.display.update()
        clock.tick(15)
def update():
    intro = True #przycisk(msg,x,y,w,h,i,a)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        ekran.fill(ZIELONY)
        largeText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects('Nothing to update.',largeText)
        TextRect.center=((SZEROKOSC/2),(WYSOKOSC*0.15))
        
        ekran.blit(TextSurf, TextRect)
        
        przycisk('Menu',SZEROKOSC*0.7,WYSOKOSC*0.85,100,50,NIEBIESKI,JNIEBIESKI,'menu')
        przycisk('FLY!',SZEROKOSC*0.1,WYSOKOSC*0.85,100,50,NIEBIESKI,JNIEBIESKI,'play')
        pygame.display.update()
        clock.tick(15)
def about():
    intro = True #przycisk(msg,x,y,w,h,i,a)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        ekran.fill(ZIELONY)
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects('AUTOR: ŁUKASZ ŁASZCZUK',largeText)
        TextSurf1, TextRect1 = text_objects('INDEKS: 243024',largeText)
        TextRect.center=((SZEROKOSC/2),(WYSOKOSC*0.15))
        TextRect1.center=((SZEROKOSC/2),(WYSOKOSC*0.25))
        
        ekran.blit(TextSurf, TextRect)
        ekran.blit(TextSurf1, TextRect1)
        przycisk('Menu',SZEROKOSC*0.7,WYSOKOSC*0.85,100,50,NIEBIESKI,JNIEBIESKI,'menu')
        przycisk('FLY!',SZEROKOSC*0.1,WYSOKOSC*0.85,100,50,NIEBIESKI,JNIEBIESKI,'play')
        pygame.display.update()
        clock.tick(15)
def records():
    intro = True #przycisk(msg,x,y,w,h,i,a)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        ekran.fill(ZIELONY)
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects('FLY TO THE SKY!',largeText)
        TextRect.center=((SZEROKOSC/2),(WYSOKOSC*0.15))
        ekran.blit(TextSurf, TextRect)
        przycisk('Menu',SZEROKOSC*0.7,WYSOKOSC*0.85,100,50,NIEBIESKI,JNIEBIESKI,'menu')
        przycisk('FLY!',SZEROKOSC*0.1,WYSOKOSC*0.85,100,50,NIEBIESKI,JNIEBIESKI,'play')
        pygame.display.update()
        clock.tick(15)
    
def przycisk(msg,x,y,w,h,i,a,action=None):
    click = pygame.mouse.get_pressed()#3elementowy tuple(0,0,0) jesli nie wcisniete
    mouse = pygame.mouse.get_pos()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(ekran,a,(x, y,w,h))
        if click[0]==1 and action!= None:
            if action == "play":
                gameloop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "rules":
                rules()
            elif action == "menu":
                menu()
            elif action == "update":
                update()
            elif action == "about":
                about()
            elif action == 'records':
                records()
    else:
        pygame.draw.rect(ekran,i,(x, y,w,h))
        
    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf, textRect = text_objects1(msg,smallText)
    textRect.center=((x+x+w)/2,(y+y+h)/2)
    ekran.blit(textSurf, textRect)
    
def menu():
    intro = True #przycisk(msg,x,y,w,h,i,a)
    skrzydelka1=0
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        ekran.fill(ZIELONY)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects('Flappy',largeText)
        TextRect.center=((SZEROKOSC/2),(WYSOKOSC*0.15))
        ekran.blit(TextSurf, TextRect)
        if skrzydelka1%12 in range(6):
                    ptak(SZEROKOSC*0.45,WYSOKOSC*0.35)
                    skrzydelka1+=2
        elif skrzydelka1%12 in range(6,12):  
                    ptak2(SZEROKOSC*0.45,WYSOKOSC*0.35)
                    skrzydelka1+=2 
        przycisk('FLY!',SZEROKOSC*0.1,WYSOKOSC*0.6,100,50,NIEBIESKI,JNIEBIESKI,'play')
        przycisk('RULES',SZEROKOSC*0.4,WYSOKOSC*0.6,100,50,NIEBIESKI,JNIEBIESKI,'rules')
        przycisk('UPDATE',SZEROKOSC*0.7,WYSOKOSC*0.6,100,50,NIEBIESKI,JNIEBIESKI,'update')
        przycisk('RECORDS',SZEROKOSC*0.1,WYSOKOSC*0.75,100,50,NIEBIESKI,JNIEBIESKI,'records')
        przycisk('ABOUT ME',SZEROKOSC*0.4,WYSOKOSC*0.75,100,50,NIEBIESKI,JNIEBIESKI,'about')
        przycisk('EXIT',SZEROKOSC*0.7,WYSOKOSC*0.75,100,50,CZERWONY,JCZERWONY,"quit")
        pygame.display.update()
        clock.tick(15)
    
def gameloop():
    
    x = SZEROKOSC/4#miejsce gdzie ptaszek zaczyna lot
    y = WYSOKOSC/2
    x1 =[SZEROKOSC*0.75,SZEROKOSC*0.83,SZEROKOSC*0.91]
    y1 = WYSOKOSC*0.05
    y_change = 1.5#predkosc ptaszka
    dziob_dol = 0#zmienna pomocnicza uzywana przy okresleniu czy ptaszek spada
    
    przeszkoda_startx = np.linspace(480,24240,100)
    przeszkoda_starty = 0
    
    przeszkoda_szerokosc = 70
    przeszkoda_wysokosc=[]
    for a in range(100):
        przeszkoda_wysokosc.append(random.randint(100,400)) 
    przeszkoda_szybkosc = -1.5
    #przeszkoda_starty_dol=
    wynik_i=0
    skrzydelka = 0#zmienna pomocnicza przy imitacji lotu
    licznik_zyc = 3
    running = True
    crashed = False
    while running:#pętla logiczna event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  
                
                
                
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    y-= 35 #spacja- przesuniecie ptaka
                    dziob_dol=0
                    lot() 
                    
       
            
         
        y += y_change#przesuwamy ptaka w gore jesli spacja nacisnieta (jednorazowo)           
        ekran.fill(ZIELONY)#tlo
        
        
        przeszkoda(przeszkoda_startx,przeszkoda_starty,przeszkoda_szerokosc,przeszkoda_wysokosc,CZARNY)
        
        for i in range(len(przeszkoda_startx)):
            przeszkoda_startx[i] += przeszkoda_szybkosc
            if przeszkoda_startx[i]<x+ptak_dol_wysokosc and przeszkoda_startx[i]>x-przeszkoda_szerokosc:
                
                if y<przeszkoda_wysokosc[i]-5 or y>przeszkoda_wysokosc[i]+70:
                    hit()
                    y_change=20   
                    crashed=True
                    przeszkoda_startx[i]-=ptak_dol_wysokosc+200
            if przeszkoda_startx[i]==x-54: 
                punkt()
                wynik_i+=1
                      
        
                     
                 
                   
        if licznik_zyc == 3:
            zycia3(x1[0],y1)
        elif licznik_zyc == 2:
            zycia2(x1[1],y1)
        elif licznik_zyc == 1:
            zycia1(x1[2],y1)
        
        
                
        if y_change>0:#jesli ptak spada
            dziob_dol+=1#liczymy klatki do zmienienia obrazka na spadajacego ptaszka
            if dziob_dol>30:
                
                if skrzydelka%12 in range(6):
                    ptak1(x,y)
                    skrzydelka+=1
                    
                elif skrzydelka%12 in range(6,12):
                    ptak3(x,y)
                    skrzydelka+=1
                    
            else:#jesli jeszcze nie doliczylismy
                if skrzydelka%12 in range(6):
                    ptak(x,y)
                    skrzydelka+=1
                elif skrzydelka%12 in range(6,12):  
                    ptak2(x,y)
                    skrzydelka+=1 
        wynik(wynik_i) 
        if y<= 0:
            y = 0
        elif y>WYSOKOSC - ptak_dol_wysokosc+10 :
            hit()
            y=WYSOKOSC/2
            licznik_zyc-=1
            crashed=False
            y_change=2
            kraksa(licznik_zyc)
        if licznik_zyc==0:
            koniec_gry() 
        
        if not crashed:
            if dziob_dol>30:
                y_change=4
            else:
                y_change=2
            
                
            
            
         #jesli nie "molestujesz" spacji to spadasz w dol    
        
        pygame.display.update()
        
        clock.tick(60) 
menu()
gameloop()      
  