import pygame
from pygame.locals import *
from Fonctions import *
from Classes import *
import time
from random import randrange

pygame.init()
pygame.mixer.init()


#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 512))


########## FONCTIONS ##########


def ajouter_lettre(lettre): #ajoute une lettre à la chaine de caractère
    global nom
    nom += lettre
    Son.JouerLettre
    maj()

def supprimer_lettre(): #Supprime la dernière lettre du nom
    global nom, texte
    if len(nom) == 0:
        Son.JouerErreur(Son)
    else:
        nom = nom[:len(nom)-1]
        Son.JouerEffacer(Son)
        maj()

def maj(): #met à jour toute la page
    global nom, texte
    Fenetre.blit(Fond, (0,0)) #Colle l'image de fond sur la fenêtre
    ZoneNom.set_colorkey((255,255,255)) #Rend le blanc de l'image du nom transparent
    Fenetre.blit(ZoneNom, (Fond.get_rect().centerx - ZoneNom.get_rect().centerx, Fond.get_rect().centery - 3*ZoneNom.get_rect().centery)) #Colle l'image du nom sur la fenêtre

    texte = police.render(nom,1,(0,0,0)) #Créer une image contenant le nom
    Fenetre.blit(texte,(Fond.get_rect().centerx - ZoneNom.get_rect().centerx + 5, Fond.get_rect().centery - 3*ZoneNom.get_rect().centery + 35)) #Colle l'image sur la fenêtre

    pygame.display.flip() #Actualise l'affichage


def nomperso(nom_final, boucle):
    global nom
    while boucle:
        for event in pygame.event.get():
            if event.type == QUIT: #Sort de la boucle
                continuer = 0
                boucle = 0
            if event.type == KEYDOWN:
                 ZoneNom = pygame.image.load("Textures/nom.png").convert()
                 print(nom)
                 if event.key == K_RETURN: #Valide le nom et passe au programme suivant
                    if len(nom) == 0:
                        son_erreur.play()
                    else:
                        boucle = 0
                        Son.JouerAccepter(Son)
                 if event.key == K_BACKSPACE: #permet d'effacer la dernière lettre
                    supprimer_lettre()
                 if len(nom)<11:
                    if event.key == K_q:  #lettres, attention l'aquisition ce fait en qwerty donc certains touches comme le q doivent afficher le a
                        ajouter_lettre("A")
                    if event.key == K_b:
                        ajouter_lettre("B")
                    if event.key == K_c:
                        ajouter_lettre("C")
                    if event.key == K_d:
                        ajouter_lettre("D")
                    if event.key == K_e:
                        ajouter_lettre("E")
                    if event.key == K_f:
                        ajouter_lettre("F")
                    if event.key == K_g:
                        ajouter_lettre("G")
                    if event.key == K_h:
                        ajouter_lettre("H")
                    if event.key == K_i:
                        ajouter_lettre("I")
                    if event.key == K_j:
                        ajouter_lettre("J")
                    if event.key == K_k:
                        ajouter_lettre("K")
                    if event.key == K_l:
                        ajouter_lettre("L")
                    if event.key == K_SEMICOLON:
                        ajouter_lettre("M")
                    if event.key == K_n:
                        ajouter_lettre("N")
                    if event.key == K_o:
                        ajouter_lettre("O")
                    if event.key == K_p:
                        ajouter_lettre("P")
                    if event.key == K_a:
                        ajouter_lettre("Q")
                    if event.key == K_r:
                        ajouter_lettre("R")
                    if event.key == K_s:
                        ajouter_lettre("S")
                    if event.key == K_t:
                        ajouter_lettre("T")
                    if event.key == K_u:
                        ajouter_lettre("U")
                    if event.key == K_v:
                        ajouter_lettre("V")
                    if event.key == K_z:
                        ajouter_lettre("W")
                    if event.key == K_x:
                        ajouter_lettre("X")
                    if event.key == K_y:
                        ajouter_lettre("Y")
                    if event.key == K_w:
                        ajouter_lettre("Z")
                 if len(nom)>=11:
                    Son.JouerErreur(Son)
    nom_final = nom


def GameOver(continuer):
    PerduTesNulBouh = pygame.image.load("Textures/game_over.png").convert()
    fenetre.blit(PerduTesNulBouh, (0,0))
    Son.CoupeLeSonJackie(Son)
    Son.JouerGameOver(Son)
    pygame.display.flip()
    while continuer == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                continuer=0
                pygame.quit()


def txt(txt,x,y): #Affiche un texte en fonction du texte et des coordonées
    text = police.render(txt, 1, (10, 10, 10))
    textpos = text.get_rect()
    fenetre.blit(text, (x, y))
    pygame.display.flip()

def map(Niveau): #Affiche la map en fonction du fichier txt
    i=0
    global x_perso
    global y_perso
    x=0
    y=0
    while i<len(Niveau):
        if x==10:
            x=0
            y=y+1

        if Niveau[i] == "0": #Si le fichier annonce "0", le jeu affichera un bloc de Terre
            fenetre.blit(Textures.terre, (64*x,64*y))
            pygame.display.flip()
        if Niveau[i] == "1": #Si le fichier annonce "1", le jeu affichera un bloc de Cristal
            fenetre.blit(Textures.sol_cristal, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "2": #Si le fichier annonce "2", le jeu affichera un mur de Cristal
            fenetre.blit(Textures.mur_cristal, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "3": #Si le fichier annonce "3", le jeu affichera un bloc de Cailloux
            fenetre.blit(Textures.caillou_sol, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "4": #Si le fichier annonce "4", le jeu affichera un bloc de Glace
            fenetre.blit(Textures.glace1, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "5": #Si le fichier annonce "5", le jeu affichera un autre bloc de Glace
            fenetre.blit(Textures.glace2, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "6": #Si le fichier annonce "6", le jeu affichera un mur de Glace
            fenetre.blit(Textures.glace_mur, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "7": #Si le fichier annonce "7", le jeu affichera un bloc de Pavé
            fenetre.blit(Textures.pave, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "8": #Si le fichier annonce "8", le jeu affichera un Mur
            fenetre.blit(Textures.mur, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "9": #Si le fichier annonce "9", le jeu affichera un bloc Volcanique
            fenetre.blit(Textures.volcan, (64*(x),64*y))
            pygame.display.flip()
        if Niveau[i] == "à": #Si le fichier annonce "à", le jeu affichera un mur de Caillou
            fenetre.blit(Textures.caillou_mur, (64*(x),64*y))
            pygame.display.flip()
        i=i+1
        x=x+1
    i=0
    if x_perso==448 and y_perso==192:
        i=randrange(1,4)
        print(i)
        if i==1:
            combat1("Drake")
        if i==2:
            combat1("Poulpe")
        if i==3:
            combat1("Liche")
        x_perso=0
        y_perso=0

def ennemi_attaque(ID_ennemi): #Lancé quand c'est le tour de l'ennem
    if ID_ennemi=="Drake" or ID_ennemi=="Poulpe":
        Hero.vie=Hero.vie-7
        txt("-7 PV", 20, 200)
        pygame.display.flip()
        time.sleep(0.2)
    if ID_ennemi=="Liche":
        Hero.vie=Hero.vie-14
        txt("-14 PV", 20, 200)
        pygame.display.flip()
        time.sleep(0.2)
    fond_combat1(ID_ennemi)

def introbadass(ID_ennemi): #Sers d'image d'introduction pour les Boss
    if ID_ennemi=="Liche":
        Liche = pygame.image.load("Textures/texture_hd_spectre.png").convert_alpha()
        fenetre.blit(Liche, (128, 128))
        pygame.display.flip()
        time.sleep(2)
    fond_combat1(ID_ennemi)



def fond_combat1(ID_ennemi): #Affiche le fond, le perso et l'ennemi
    global x_perso
    global y_perso

    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()
    Liche = pygame.image.load("Textures/lich_g.png").convert_alpha()
    Drake = pygame.image.load("Textures/Drake.png").convert_alpha()
    Poulpe = pygame.image.load("Textures/cuttlefish_g.png").convert_alpha()
    Fireball = pygame.image.load("Textures/Fireball.png").convert_alpha()

    fenetre.blit(fond, (0, 0))
    x_perso=10
    y_perso=240
    fenetre.blit(Perso, (x_perso, y_perso))

    if ID_ennemi=="Drake":
        fenetre.blit(Drake, (500, 240))
    if ID_ennemi=="Poulpe":
        fenetre.blit(Poulpe, (500, 240))
    if ID_ennemi=="Liche":
        fenetre.blit(Liche, (500, 240))

    txt("Attaque (F1)", 5, 15)
    txt("Magie (F2)", 20, 40)
    txt("Sac (F3)", 35, 65)
    pygame.display.flip()


def combat1(ID_ennemi):
    Son.JouerCombat1(Son)
    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha() #Charge les textures
    Liche = pygame.image.load("Textures/lich_g.png").convert_alpha()
    Poulpe = pygame.image.load("Textures/cuttlefish_g.png").convert_alpha()
    Drake = pygame.image.load("Textures/Drake.png").convert_alpha()
    Fireball = pygame.image.load("Textures/Fireball.png").convert_alpha()
    x_fire = 15


    fenetre.blit(fond, (0,0)) #Introduction oùle personnage aance de 2 pas
    pygame.display.flip()
    time.sleep(0.5)
    x_perso=10
    y_perso=240
    fenetre.blit(Perso, (10,200))
    x_perso=x_perso+5
    Perso = pygame.image.load("Textures/persolife_d_moving.png").convert_alpha()
    fenetre.blit(fond, (0,0))
    fenetre.blit(Perso, (x_perso,y_perso))
    pygame.display.flip()
    x_perso=x_perso+5
    time.sleep(0.2)
    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()
    fenetre.blit(fond, (0,0))
    fenetre.blit(Perso, (x_perso,y_perso))
    pygame.display.flip()
    coté=1
    time.sleep(0.2)


    if ID_ennemi=="Drake": #Affiche l'ennemi
        fenetre.blit(Drake, (500, 240))
        PV_Ennemi=50
    if ID_ennemi=="Poulpe":
        fenetre.blit(Poulpe, (500, 240))
        PV_Ennemi = 50
    if ID_ennemi=="Liche":
        fenetre.blit(Liche, (500, 240))
        PV_Ennemi = 100

    Intro=ID_ennemi
    introbadass(Intro)

    time.sleep(0.2)
    txt("Attaque (F1)", 5, 15) #Affiche les choix
    time.sleep(0.2)
    txt("Magie (F2)", 20, 40)
    time.sleep(0.2)
    txt("Sac (F3)", 35, 65)
    pygame.display.flip()

    while Hero.vie > 0 and PV_Ennemi > 0:
        for event in pygame.event.get():
            fenetre.blit(Perso, (x_perso, y_perso))
            if event.type == KEYDOWN:
                if event.key == K_F1: #Choix de l'attaque
                    Perso = pygame.image.load("Textures/persolife_d_atk.png").convert_alpha()
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    Perso = pygame.image.load("Textures/persolife_d_atk2.png").convert_alpha()
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    Son.JouerAttaque(Son)
                    time.sleep(0.2)
                    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    PV_Ennemi=PV_Ennemi-25
                    txt("-25 PV", 500, 200)
                    fenetre.blit(Perso, (x_perso, y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso, y_perso))
                    ennemi_attaque(ID_ennemi)
                    x_perso=10
                    y_perso=240

                if event.key == K_F2:#Choix de la Boule de Feu
                    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    Perso = pygame.image.load("Textures/persolife_g.png").convert_alpha()
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()

                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    Son.JouerSort(Son)
                    time.sleep(0.2)
                    while x_fire < 480:
                        x_fire=x_fire+64
                        txt("Attaque (F1)", 5, 15)
                        txt("Magie (F2)", 20, 40)
                        txt("Sac (F3)", 35, 65)
                        fenetre.blit(Fireball, (x_fire, 230))
                        fenetre.blit(Perso, (x_perso, y_perso))
                        pygame.display.flip()
                        time.sleep(1)
                        fond_combat1(ID_ennemi)
                    Son.JouerBoom(Son)


                    fond_combat1(ID_ennemi)
                    PV_Ennemi=PV_Ennemi-60
                    txt("-60 PV", 500, 200)
                    txt("-20 Mana", 128, 128)
                    pygame.display.flip()
                    time.sleep(0.2)
                    ennemi_attaque(ID_ennemi)

                if event.key == K_F3: #Choix du Sac
                    txt("Vie : F1", 320, 100)
                    txt("Mana : F2", 320, 80)
                    txt("Elixir : F3", 320, 60)
                    time.sleep(2)
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_F1:
                                Hero.BoirePotionVie()
                            if event.type == K_F2:
                                Hero.BoirePotionMana()
                            if event.type == K_F3:
                                Hero.BoirePotionElixir()
                            time.sleep(1)
                    ennemi_attaque(ID_ennemi)
    x_perso=0
    y_perso=0
    Son.CoupeLeSonJackie(Son)
    if Hero.vie==0:
        GameOver(continuer)

    else :
        print("ts")
        if ID_ennemi!="Liche":
            Son.JouerVictoire(Son, ID_ennemi)
        else:
            Son.JouerVictoireFinale(Son)
        time.sleep(1)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                Son.CoupeLeSonJackie(Son)
                map(Lvl)





########## VARIABLES ##########

nom = "JEANJACQUES" #Chaine de caractère ou est stocké le nom saisi
boucle = 1 #Permet de créer une boucle
Lvl = "00000000000000000000000000030000000033300000000300000000000000000000000000000009" #Variable qui sert de modèle à la map

Fenetre = pygame.display.set_mode((640, 512)) #Crée la fenêtre
Fond = pygame.image.load("Textures/parchemin.jpg").convert() #Crée l'image qui servira de fond
fond = pygame.image.load("Textures/background.jpg").convert()
ZoneNom = pygame.image.load("Textures/nom.png").convert() #Crée l'image entourant le nom
TesNul = pygame.image.load("Textures/game_over.png").convert()

police = pygame.font.Font("Verdana.ttf", 36) #Choisi la police d'écriture
texte = police.render(nom,1,(0,0,0)) #Créer une image contenant le nom
textpos = texte.get_rect() #Position du texte
Perso=Hero.texture_droite
x_perso=0
y_perso=0
cooldown=0

random = 0


Hero.vie=42
Hero.mana=59



########## CORPS DU PROGRAMME ##########


#BOUCLE INFINIE

continuer = 1
maj()
nomperso(Hero.nom,boucle)
map(Lvl)


while continuer == 1:
    fenetre.blit(Perso, (x_perso,y_perso))
    pygame.display.flip()
    position_perso = Perso.get_rect()

    if x_perso<0: #Système de monde Infini
        x_perso=640
    if x_perso>640:
        x_perso=0
    if y_perso<0:
        y_perso=512
    if y_perso>512:
        y_perso=0

    for event in pygame.event.get():
        if cooldown==0:
            if event.type == KEYDOWN:
                cooldown = 1
                map(Lvl)

                if event.key == K_RIGHT:
                    x_perso=x_perso+32
                    Perso = pygame.image.load("Textures/persolife_d_moving.png").convert_alpha()
                    map(Lvl)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    x_perso=x_perso+32
                    time.sleep(0.2)
                    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()
                    map(Lvl)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    coté=1
                    time.sleep(0.2)

                if event.key == K_LEFT:
                    x_perso=x_perso-32
                    Perso = pygame.image.load("Textures/persolife_g_moving.png").convert_alpha()
                    map(Lvl)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    x_perso=x_perso-32
                    time.sleep(0.2)
                    Perso = pygame.image.load("Textures/persolife_g.png").convert_alpha()
                    map(Lvl)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    coté=2
                    time.sleep(0.2)

                if event.key == K_UP:
                    y_perso=y_perso-32
                    Perso = pygame.image.load("Textures/persolife_d_moving.png").convert_alpha()
                    map(Lvl)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    y_perso=y_perso-32
                    time.sleep(0.2)
                    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()
                    map(Lvl)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    coté=1
                    time.sleep(0.2)

                if event.key == K_DOWN:
                    y_perso=y_perso+32
                    Perso = pygame.image.load("Textures/persolife_d_moving.png").convert_alpha()
                    map(Lvl)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    y_perso=y_perso+32
                    time.sleep(0.2)
                    Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()
                    map(Lvl)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    coté=1
                    time.sleep(0.2)

                if event.key == K_SPACE:
                    if coté == 1:
                        x_perso=x_perso+32
                        Perso = pygame.image.load("Textures/persolife_d_moving.png").convert_alpha()
                        map(Lvl)
                        fenetre.blit(Perso, (x_perso,y_perso))
                        pygame.display.flip()
                        time.sleep(0.2)
                        x_perso=x_perso+32
                        Perso = pygame.image.load("Textures/persolife_d_atk.png").convert_alpha()
                        map(Lvl)
                        fenetre.blit(Perso, (x_perso,y_perso))
                        pygame.display.flip()
                        x_perso=x_perso+32
                        Son.JouerAttaque(Son)
                        time.sleep(0.2)
                        Perso = pygame.image.load("Textures/persolife_d.png").convert_alpha()
                        map(Lvl)
                        fenetre.blit(Perso, (x_perso,y_perso))
                        x_perso=x_perso+32
                        pygame.display.flip()
                        time.sleep(0.2)
                        coté=1
                    if coté == 2:
                        x_perso=x_perso-32
                        Perso = pygame.image.load("Textures/persolife_g_moving.png").convert_alpha()
                        map(Lvl)
                        fenetre.blit(Perso, (x_perso,y_perso))
                        pygame.display.flip()
                        time.sleep(0.2)
                        x_perso=x_perso-32
                        Perso = pygame.image.load("Textures/persolife_g_atk.png").convert_alpha()
                        map(Lvl)
                        fenetre.blit(Perso, (x_perso,y_perso))
                        pygame.display.flip()
                        x_perso=x_perso-32
                        Son.JouerAttaque(Son)
                        time.sleep(0.2)
                        Perso = pygame.image.load("Textures/persolife_g.png").convert_alpha()
                        map(Lvl)
                        fenetre.blit(Perso, (x_perso,y_perso))
                        x_perso=x_perso-32
                        pygame.display.flip()
                        time.sleep(0.2)
                        coté=2
                cooldown = 0
                map(Lvl)
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = 0

pygame.quit()