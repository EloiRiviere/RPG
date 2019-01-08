import pygame
from pygame.locals import *
from Classes import *
import time
from random import randrange

pygame.init()
pygame.mixer.init()


########## FONCTIONS ##########


def ajouter_lettre(lettre): #ajoute une lettre à la chaine de caractère
    global nom
    nom += lettre
    Son.JouerLettre()
    maj()

def supprimer_lettre(): #Supprime la dernière lettre du nom
    global nom, texte
    if len(nom) == 0:
        Son.JouerErreur()
    else:
        nom = nom[:len(nom)-1]
        Son.JouerErreur()
        maj()

def maj(): #met à jour toute la page
    global nom, texte, fenetre
    fenetre.blit(Fond, (0,0)) #Colle l'image de fond sur la fenêtre
    ZoneNom.set_colorkey((255,255,255)) #Rend le blanc de l'image du nom transparent
    fenetre.blit(ZoneNom, (Fond.get_rect().centerx - ZoneNom.get_rect().centerx, Fond.get_rect().centery - 3*ZoneNom.get_rect().centery)) #Colle l'image du nom sur la fenêtre

    texte = police.render(nom,1,(0,0,0)) #Créer une image contenant le nom
    fenetre.blit(texte,(Fond.get_rect().centerx - ZoneNom.get_rect().centerx + 5, Fond.get_rect().centery - 3*ZoneNom.get_rect().centery + 35)) #Colle l'image sur la fenêtre

    pygame.display.flip() #Actualise l'affichage


def nomperso(nom_final, boucle):
    global nom, continuer
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
                        Son.JouerErreur()
                    else:
                        boucle = 0
                        Son.JouerAccepte()
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
                    Son.JouerErreur()
    nom_final = nom
    if nom_final=="LEMMY":
        Hero.NomSecret()


def GameOver():
    PerduTesNulBouh = pygame.image.load("Textures/texture_Game_over.png").convert()
    fenetre.blit(PerduTesNulBouh, (0,0))
    Son.JouerGameOver()


def afficher_potion():
    txt(str(potion_vie), 550, 0) #Affiche le nombre de potions
    txt(str(potion_mana), 550, 64)
    txt(str(elixir), 550, 128)
    fenetre.blit(elixir, (580, 100)) #Affiche la texture des potions
    fenetre.blit(potion_vie, (580, 0))
    fenetre.blit(potion_mana, (580, 50))

def txt(txt,x,y): #Affiche un texte en fonction du texte et des coordonées
    text = font.render(txt, 1, (10, 10, 10))
    textpos = text.get_rect()
    fenetre.blit(text, (x, y))
    pygame.display.flip()

def map(Niveau): #Affiche la map en fonction du fichier txt
    i=0
    x=0
    y=16
    while i<len(Niveau):
        if x==0:
            y=y+50
            x=x-64
        if Niveau[i] == "0": #Si le fichier annonce "0", le jeu affichera un bloc de Terre
            fenetre.blit(terre, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "1": #Si le fichier annonce "1", le jeu affichera un bloc de Cristal
            fenetre.blit(sol_cristal, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "2": #Si le fichier annonce "2", le jeu affichera un mur de Cristal
            fenetre.blit(mur_cristal, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "3": #Si le fichier annonce "3", le jeu affichera un bloc de Cailloux
            fenetre.blit(caillou_sol, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "4": #Si le fichier annonce "4", le jeu affichera un bloc de Glace
            fenetre.blit(glace1, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "5": #Si le fichier annonce "5", le jeu affichera un autre bloc de Glace
            fenetre.blit(glace2, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "6": #Si le fichier annonce "6", le jeu affichera un mur de Glace
            fenetre.blit(glace_mur, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "7": #Si le fichier annonce "7", le jeu affichera un bloc de Pavé
            fenetre.blit(pave, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "8": #Si le fichier annonce "8", le jeu affichera un Mur
            fenetre.blit(mur, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "9": #Si le fichier annonce "9", le jeu affichera un bloc Volcanique
            fenetre.blit(volcan, (64*(x),y))
            pygame.display.flip()
        if Niveau[i] == "à": #Si le fichier annonce "à", le jeu affichera un mur de Caillou
            fenetre.blit(caillou_mur, (64*(x),y))
            pygame.display.flip()
        i=i+1
        x=x+1
    i=0
    afficher_potion()
    random = randrange(1,20)
    if random == 1:
        combat("Loup")

def fond_combat1(ID_ennemi):

    fenetre.blit(fond, (0, 0))
    x_perso=10
    y_perso=240
    Perso = Hero.texture_droite
    fenetre.blit(Perso, (x_perso, y_perso))

    if ID_ennemi=="Drake":
        fenetre.blit(Drake, (500, 240))

    txt("Attaque (F1)", 5, 15)
    txt("Magie (F2)", 20, 40)
    txt("Sac (F3)", 35, 65)
    pygame.display.flip()


def combat(ID_ennemi):
    Loup = Classes.Loup()
    Drake = Classes.Drake()




    Son.JouerCombat1()

    x_fire = 15


    fenetre.blit(fond, (0,0))
    pygame.display.flip()
    time.sleep(0.5)
    x_perso=10
    y_perso=240
    Perso = Hero.texture_droite
    fenetre.blit(Perso, (10,200))
    x_perso=x_perso+5
    Perso = Hero.texture_droite_mouvement
    fenetre.blit(fond, (0,0))
    fenetre.blit(Perso, (x_perso,y_perso))
    pygame.display.flip()
    x_perso=x_perso+5
    time.sleep(0.2)
    Perso = Hero.texture_droite
    fenetre.blit(fond, (0,0))
    fenetre.blit(Perso, (x_perso,y_perso))
    pygame.display.flip()
    coté=1
    time.sleep(0.2)



    if ID_ennemi=="Drake":
        fenetre.blit(Drake, (500, 240))

    time.sleep(0.2)
    txt("Attaque (F1)", 5, 15)
    time.sleep(0.2)
    txt("Magie (F2)", 20, 40)
    time.sleep(0.2)
    txt("Sac (F3)", 35, 65)
    pygame.display.flip()

    while Hero.vie > 0 and ID_ennemi.vie > 0:
        for event in pygame.event.get():
            fenetre.blit(Perso, (x_perso, y_perso))
            if event.type == KEYDOWN:
                if event.key == K_F1:  #Choix de l'attaque
                    Perso = Hero.texture_droite_attaque
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    Perso = Hero.texture_droite_attaque2
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    Hero.Attaque(Son, ID_ennemi)
                    time.sleep(0.2)
                    Perso = Hero.texture_droite
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    PV_Ennemi=PV_Ennemi-20
                    txt("-20 PV", 500, 200)
                    fenetre.blit(Perso, (x_perso, y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso, y_perso))

                if event.key == K_F2:#Choix de la Boule de Feu
                    Perso = Hero.texture_droite
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    Perso = Hero.texture_gauche
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    time.sleep(0.2)
                    Perso = Hero.texture_droite
                    fenetre.blit(fond, (0,0))
                    fond_combat1(ID_ennemi)
                    fenetre.blit(Perso, (x_perso,y_perso))
                    pygame.display.flip()
                    Hero.LancerSort(Son, ID_ennemi)
                    time.sleep(0.2)
                    while x_fire < 480:
                        x_fire += 1
                        if ID_ennemi == 0:
                            fenetre.blit(Drake, (500, 230))
                        txt("Attaque (F1)", 5, 15)
                        txt("Magie (F2)", 20, 40)
                        txt("Sac (F3)", 35, 65)
                        fenetre.blit(fireball, (x_fire, 230))
                        fenetre.blit(Perso, (x_perso, y_perso))
                        pygame.display.flip()
                        time.sleep(0.0001)
                        fond_combat1(ID_ennemi)
                    Son.JouerBoom()


                    fond_combat1(ID_ennemi)
                    txt("-50 PV", 500, 200)
                    txt("-20 Mana", x_perso, y_perso-30)
                    pygame.display.flip()
                    time.sleep(0.2)

                if event.key == K_F3:
                    txt("Vie : F1", )
    Son.CoupeLeSonJackie()
    if Hero.vie == 0:
        Hero.Mort()

    else :
        Son.JouerVictoire()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                Son.CoupeLeSonJackie()
                deplacer_sur_map()

def deplacer_sur_map():
        global x_perso, y_perso, coté
        if event.key == K_RIGHT:
            x_perso += 5
            Perso = Hero.texture_droite_mouvement
            fenetre.blit(fond, (0,0))
            map(Lvl_actuel)
            fenetre.blit(Perso, (x_perso,y_perso))
            pygame.display.flip()
            x_perso += 5
            time.sleep(0.2)
            Perso = Hero.texture_droite
            fenetre.blit(fond, (0,0))
            map(Lvl_actuel)
            fenetre.blit(Perso, (x_perso,y_perso))
            pygame.display.flip()
            coté=1
            time.sleep(0.2)

        if event.key == K_LEFT:
            x_perso -= 5
            Perso = Hero.texture_droite_mouvement
            fenetre.blit(fond, (0,0))
            map(Lvl_actuel)
            fenetre.blit(Perso, (x_perso,y_perso))
            pygame.display.flip()
            x_perso -= 5
            time.sleep(0.2)
            Perso = Hero.texture_gauche
            fenetre.blit(fond, (0,0))
            map(Lvl_actuel)
            fenetre.blit(Perso, (x_perso,y_perso))
            pygame.display.flip()
            coté = 2
            time.sleep(0.2)

        if event.key == K_UP:
            y_perso=y_perso-5
            Perso = Hero.texture_droite_mouvement
            fenetre.blit(fond, (0,0))
            map(Lvl_actuel)
            fenetre.blit(Perso, (x_perso,y_perso))
            pygame.display.flip()
            y_perso -= 5
            time.sleep(0.2)
            Perso = Hero.texture_droite
            fenetre.blit(fond, (0,0))
            map(Lvl_actuel)
            fenetre.blit(Perso, (x_perso,y_perso))
            pygame.display.flip()
            coté=1
            time.sleep(0.2)

        if event.key == K_DOWN:
            y_perso += 5
            Perso = Hero.texture_droite_mouvement
            fenetre.blit(fond, (0,0))
            map(Lvl_actuel)
            fenetre.blit(Perso, (x_perso,y_perso))
            pygame.display.flip()
            y_perso += 5
            time.sleep(0.2)
            Perso = Hero.texture_droite
            fenetre.blit(fond, (0,0))
            map(Lvl_actuel)
            fenetre.blit(Perso, (x_perso,y_perso))
            pygame.display.flip()
            coté = 1
            time.sleep(0.2)

        if event.key == K_SPACE:
            if coté == 1:
                x_perso += 10
                Perso = Hero.texture_droite_mouvement
                fenetre.blit(fond, (0,0))
                map(Lvl_actuel)
                fenetre.blit(Perso, (x_perso,y_perso))
                pygame.display.flip()
                time.sleep(0.2)
                x_perso += 10
                Perso = Hero.texture_droite_attaque
                fenetre.blit(fond, (0,0))
                map(Lvl_actuel)
                fenetre.blit(Perso, (x_perso,y_perso))
                pygame.display.flip()
                x_perso += 10
                Son.JouerAttaque()
                time.sleep(0.2)
                Perso = Hero.texture_droite
                fenetre.blit(fond, (0,0))
                map(Lvl_actuel)
                fenetre.blit(Perso, (x_perso,y_perso))
                x_perso += 10
                pygame.display.flip()
                time.sleep(0.2)
                coté=1
            if coté == 2:
                Perso = Hero.texture_gauche_mouvement
                fenetre.blit(fond, (0,0))
                map(Lvl_actuel)
                fenetre.blit(Perso, (x_perso,y_perso))
                pygame.display.flip()
                time.sleep(0.2)
                x_perso -= 10
                x_perso -= 10
                Perso = Hero.texture_gauche_attaque
                fenetre.blit(fond, (0,0))
                map(Lvl_actuel)
                fenetre.blit(Perso, (x_perso,y_perso))
                pygame.display.flip()
                x_perso -= 10
                Son?JouerAttaque()
                time.sleep(0.2)
                Perso = Hero.texture_gauche
                fenetre.blit(fond, (0,0))
                map(Lvl_actuel)
                fenetre.blit(Perso, (x_perso,y_perso))
                x_perso -= 10
                pygame.display.flip()
                time.sleep(0.2)
                coté=2
        cooldown = 0




########## VARIABLES ##########


    ### Textures de sol ###
plante = pygame.image.load("Textures/texture_cannabis.png").convert_alpha()
sol_cristal = pygame.image.load("Textures/texture_cristaux_brises.png").convert_alpha()
mur_cristal = pygame.image.load("Textures/texture_cristaux_pointus.png").convert_alpha()
caillou_sol = pygame.image.load("Textures/texture_galet.png").convert_alpha()
glace1 = pygame.image.load("Textures/texture_glace.png").convert_alpha()
glace2 = pygame.image.load("Textures/texture_glace_moche.png").convert_alpha()
glace_mur = pygame.image.load("Textures/texture_glace_pointue.png").convert_alpha()
pave = pygame.image.load("Textures/texture_pierre_pavee.png").convert_alpha()
mur = pygame.image.load("Textures/texture_pierre_taillee.png").convert_alpha()
volcan = pygame.image.load("Textures/texture_pierre_volcanique.png").convert_alpha()
caillou_mur = pygame.image.load("Textures/texture_rochers_pointus.png").convert_alpha()
terre = pygame.image.load("Textures/texture_terre.png").convert_alpha()

    ### Potions ###
potion_vie = pygame.image.load("Texture/potionvie.png").convert_alpha()
potion_mana = pygame.image.load("Texture/potionmana.png").convert_alpha()
elixir = pygame.image.load("Texture/potionelixir.png").convert_alpha()

     ### Autre ###
fireball = pygame.image.load("Textures/fireball.png").convert_alpha()
apparition_coming = pygame.image.load("Textures/texture_hd_apparition.png").convert_alpha()
faucheur_coming = pygame.image.load("Textures/texture_hd_faucheur.png").convert_alpha()
fond = pygame.image.load("Textures/background.jpg").convert()

#################
Fond = pygame.image.load("Textures/parchemin.jpg").convert() #Crée l'image qui servira de fond
ZoneNom = pygame.image.load("Textures/nom.png").convert() #Crée l'image entourant le nom

nom = "" #Chaine de caractère ou est stocké le nom saisi
boucle = 1 #Permet de créer une boucle

police = pygame.font.Font("Verdana.ttf", 36) #Choisi la police d'écriture
texte = police.render(nom,1,(0,0,0)) #Créer une image contenant le nom
textpos = texte.get_rect() #Position du texte


#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 512))


########## CORPS DU PROGRAMME ##########


#BOUCLE INFINIE

continuer = 1
maj()
nomperso(nom_perso,boucle)
map(Lvl1)
Son = Classes.Son()
Hero = Classes.Hero(nom)

while continuer == 1:

    map(Lvl_actuel)
    Perso = Hero.texture_droite
    fenetre.blit(Perso, (x_perso,y_perso))
    pygame.display.flip()
    position_perso = Perso.get_rect()

    if x_perso < 0:
        continuer = 0

    for event in pygame.event.get():
        if cooldown == 0:
            if event.type == KEYDOWN:
                cooldown = 1
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer = 0
                deplacer_sur_map()
