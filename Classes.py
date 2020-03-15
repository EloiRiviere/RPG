import pygame
from pygame.locals import *
from random import randrange

pygame.init()
pygame.mixer.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 512))

class Textures:
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
    pave = pygame.image.load("Textures/texture_pierre_pavee.png").convert_alpha()
    caillou_mur = pygame.image.load("Textures/texture_rochers_pointus.png").convert_alpha()
    terre = pygame.image.load("Textures/texture_terre.png").convert_alpha()

    ### Potions ###
    potion_vie = pygame.image.load("Textures/potionvie.png").convert_alpha()
    potion_mana = pygame.image.load("Textures/potionmana.png").convert_alpha()
    elixir = pygame.image.load("Textures/potionelixir.png").convert_alpha()

    ### Autre ###
    fireball = pygame.image.load("Textures/fireball.png").convert_alpha()
    apparition_coming = pygame.image.load("Textures/texture_hd_apparition.png").convert_alpha()
    faucheur_coming = pygame.image.load("Textures/texture_hd_spectre.png").convert_alpha()
    fond = pygame.image.load("Textures/background.jpg").convert()



class Son: #Classe stockant les sons et musiques

    ### Musiques du jeu ###
    combatFinal = "Sounds/donjon1.ogg" #Musique du dernier combat
    donjon = "Sounds/donjon2.ogg" #Musiques de donjon
    donjonBadass = "Sounds/donjonbadass.ogg"
    combat1 = "Sounds/fight1.ogg" #Musiques de combat
    combat2 = "Sounds/fight2.ogg"
    combatMetal = "Sounds/fightMetal.ogg"
    gameover = "Sounds/gameover.ogg" #Musique de game over

    ### Sons menu nom ###
    son_effacer = pygame.mixer.Sound("Sounds/cancel1.ogg") #Son joué lorsqu'une lettre est effacée
    son_accepte = pygame.mixer.Sound("Sounds/chime2.ogg") #Son joué lorsqu'on finalise le nom
    son_lettre = pygame.mixer.Sound("Sounds/cursor1.ogg") #Son joué lorsqu'une lettre est ajoutée

    ### Sons menu combat ###
    son_epee = pygame.mixer.Sound("Sounds/Attack1.ogg") #Son joué lors d'une attaque
    son_sort = pygame.mixer.Sound("Sounds/Fire1.ogg") #Son joué lors d'une Boule de feu
    son_boom = pygame.mixer.Sound("Sounds/Blow10.ogg") #Son joué lorsque la BdF explose
    son_victory1 = pygame.mixer.Sound("Sounds/Victory1.ogg") #Sons de victoire
    son_victory2 = pygame.mixer.Sound("Sounds/Victory2.ogg")
    son_victory3 = pygame.mixer.Sound("Sounds/Victory3.ogg")
    son_victory4 = pygame.mixer.Sound("Sounds/Victory4.ogg")
    son_victory5 = pygame.mixer.Sound("Sounds/Victory5.ogg")
    son_victory6 = pygame.mixer.Sound("Sounds/Victory6.ogg")
    son_victoryFinal = pygame.mixer.Sound("Sounds/VictoryFinal.ogg")

    ### Autres sons
    son_erreur = pygame.mixer.Sound("Sounds/buzzer1.ogg") #Son joué lors d'une erreur

        ##### Musiques #####
    def JouerCombatFinal(self): #Lance la musique de combat final
        pygame.mixer.music.load(self.combatFinal)
        pygame.mixer.music.play()

    def JouerDonjon(self): #Lance la musique de donjon
        pygame.mixer.music.load(self.donjon)
        pygame.mixer.music.play()

    def JouerCombat1(self): #Lance la musique de combat
        pygame.mixer.music.load(self.combat1)
        pygame.mixer.music.play()

    def JouerCombat2(self): #lance la musique de combat
        pygame.mixer.music.load(self.combat2)
        pygame.mixer.music.play()

    def JouerCombatMetal(self): #Lance la musique de combat
        pygame.mixer.music.load(self.combatMetal)
        pygame.mixer.music.play()

    def JouerGameOver(self): #Lance la musique de game over
        pygame.mixer.music.load(self.gameover)
        pygame.mixer.music.play()

    def JouerDonjonBadass(self): #Lance la musique de donjon
        pygame.mixer.music.load(self.donjonBadass)
        pygame.mixer.music.play()

    def CoupeLeSonJackie(self): #Coupe toutes les musiques lancées
        pygame.mixer.music.stop()

        ##### Sons #####
    def JouerEffacer(self): #Joue le son d'effacage
        self.son_effacer.play()

    def JouerAccepter(self): #Joue le son pour accepter le nom
        self.son_accepte.play()

    def JouerLettre(self): #Joue le son lorsqu'on entre une lettre
        self.son_lettre.play()

    def JouerAttaque(self): #Joue le son d'attaque
        self.son_epee.play()

    def JouerSort(self): #Joue le son de sort
        self.son_sort.play()

    def JouerBoom(self): #Joue le son d'explosion du sort
        self.son_boom.play()

    def JouerVictoire(self, son): #Joue un son de victoire de combat
        son = randrange(1,7)
        if son == 1:
            self.son_victory1.play()
        if son == 2:
            self.son_victory2.play()
        if son == 3:
            self.son_victory3.play()
        if son == 4:
            self.son_victory4.play()
        if son == 5:
            self.son_victory5.play()
        if son == 6:
            self.son_victory6.play()

    def JouerVictoireFinale(self): #Joue le son de victoire
        self.son_victoryFinal.play()

    def JouerErreur(self):
        self.son_erreur.play()



class Hero: #Classe du personnage jouable
    nom = "Jean-Jacques" #Nom du hero
    vie = 42  #Points de vie, le joueur perd si ils arrivent a 0
    mana = 59 #Mana permettant de lancer des sorts

    texture_droite = pygame.image.load("Textures/persolife_d.png").convert_alpha()
    texture_droite_attaque = pygame.image.load("Textures/persolife_d_atk.png").convert_alpha()
    texture_droite_attaque2 = pygame.image.load("Textures/persolife_d_atk2.png").convert_alpha()
    texture_droite_mouvement = pygame.image.load("Textures/persolife_d_moving.png").convert_alpha()
    texture_gauche = pygame.image.load("Textures/persolife_g.png").convert_alpha()
    texture_gauche_attaque = pygame.image.load("Textures/persolife_g_atk.png").convert_alpha()
    texture_gauche_attaque2 = pygame.image.load("Textures/persolife_g_atk2.png").convert_alpha()
    texture_gauche_mouvement = pygame.image.load("Textures/persolife_g_moving.png").convert_alpha()

    def BoirePotionVie(self, son):
        if self.potion_vie > 0:
            if self.vie <= 22:
                self.vie += 20
            else:
                self.vie += 42 - self.vie

        if self.potion_vie == 0:
            son.JouerErreur()

    def BoirePotionMana(self, son):
        if self.potion_mana > 0:
            if self.mana <= 39:
                self.mana += 20
            else:
                self.mana += 59 - self.mana
        if self.potion_mana == 0:
            son.JouerErreur()

    def BoireElixir(self, son):
        if self.elixir > 0:
            if self.vie <= 22 and self.mana <= 39:
                self.vie += 20
                self.mana += 20
            elif self.vie <= 22 and self.mana > 39:
                self.vie += 20
                self.mana += 59 - self.mana
            elif self.vie > 22 and self.mana <= 39:
                self.vie += 42 - self.vie
                self.mana += 20

        if self.elixir == 0:
            son.JouerErreur()

    def RecupererPotionVie(self):
        self.potion_vie += 1

    def RecupererPotionMana(self):
        self.potion_mana += 1

    def RecupererElixir(self):
        self.elixir += 1

    def LancerSort(self,son,cible,proba=None):
        if self.mana >= 20:
            if proba == 16:
                cible.SubitDegats(20)
            else:
                cible.SubitDegats(10)
        else:
            son.JouerErreur()

    def Attaque(self,cible,proba=None):
        proba = randrange(1,16)
        if proba == 16:
            cible.SubitDegats(10)
        else:
            cible.SubitDegats(5)

    def SubitDegats(self,degats):
        if self.vie < degats:
            self.vie = 0
        else:
            self.vie -= degats

    def Mort(self,son):
        son.JouerGameOver()



class Poulpe:
    def __init__(self):
        self.nom = "Poulpe"
        self.vie = 30

        self.texture_droite = pygame.image.load("Textures/cuttlefish_d.png").convert_alpha()
        self.texture_droite_attaque1 = pygame.image.load("Textures/cuttlefish_d_atk1.png").convert_alpha()
        self.texture_droite_attaque2 = pygame.image.load("Textures/cuttlefish_d_atk2.png").convert_alpha()
        self.texture_gauche = pygame.image.load("Textures/cuttlefish_g.png").convert_alpha()
        self.texture_gauche_attaque1 = pygame.image.load("Textures/cuttlefish_g_atk1.png").convert_alpha()
        self.texture_gauche_attaque2 = pygame.image.load("Textures/cuttlefish_g_atk2.png").convert_alpha()

    def AttaquePrincipale(self,hero,proba=None):
        proba = randrange(1,16)
        if proba == 16:
            hero.SubitDegats(6)
        else:
            hero.SubitDegats(3)

    def AttaqueSecondaire(self,hero,proba=None):
        proba = randrange(1,16)
        if proba == 16:
            hero.SubitDegats(10)
        else:
            hero.SubitDegats(5)

    def SubitDegats(self,degats):
        if self.vie < degats:
            self.vie = 0
        else:
            self.vie -= degats

    def Mort(self,son):
        son.JouerGameOver()



class Drake:

    nom = "Drake"
    vie = 50

    texture = pygame.image.load("Textures/drake.png").convert_alpha()

    def Attaque(self):
        return 0

    def SubitDegats(self,degats):
        if self.vie < degats:
            self.vie = 0
        else:
            self.vie -= degats

    def Mort(self,son):
        son.JouerGameOver()



class Loup:
    def __init__(self):
        self.nom = "Jeune Loup"
        self.vie = 30

        self.texture_droite = pygame.image.load("Textures/texture_jeune_loup_d.png").convert_alpha()
        self.texture_droite_attaque = pygame.image.load("Textures/texture_jeune_loup_d_atk.png").convert_alpha()
        self.texture_gauche = pygame.image.load("Textures/texture_jeune_loup_g.png").convert_alpha()
        self.texture_gauche_attaque = pygame.image.load("Textures/texture_jeune_loup_g_atk.png").convert_alpha()

    def Attaque(self,hero,proba=None):
        proba = randrange(1,16)
        if proba == 16:
            hero.SubitDegats(10)
        else:
            hero.SubitDegats(5)

    def SubitDegats(self,degats):
         if self.vie < degats:
            self.vie = 0
         else:
            self.vie -= degats

    def Mort(self,son):
        son.JouerGameOver()



class Nain:
    def __init__(self):
        self.texture_droite = pygame.image.load("Textures/nain_d.png").convert_alpha()
        self.texture_droite_coupe = pygame.image.load("Textures/nain_d_cutting.png").convert_alpha()
        self.texture_gauche = pygame.image.load("Textures/nain_g.png").convert_alpha()



class Tentacule:
    def __init__(self):
        self.nom = "Tentacule des profondeurs abyssales du dragon"
        self.vie = 50

        self.texture_droite = pygame.image.load("Textures/deep_tentacule_d.png").convert_alpha()
        self.texture_droite_attaque = pygame.image.load("Textures/deep_tentacule_d_atk.png").convert_alpha()
        self.texture_gauche = pygame.image.load("Textures/deep_tentacule_g.png").convert_alpha()
        self.texture_gauche_attaque = pygame.image.load("Textures/deep_tentacule_g_atk.png").convert_alpha()

    def Attaque(self,hero,proba=None):
        proba = randrange(1,16)
        if proba == 16:
            hero.SubitDegats(14)
        else:
            hero.SubitDegats(7)

    def SubitDegats(self,degats):
         if self.vie < degats:
            self.vie = 0
         else:
            self.vie -= degats

    def Mort(self,son):
        son.JouerGameOver()

class Liche:
    def __init__(self):
        self.nom = "Liche"
        self.vie = 100

        self.texture_droite = pygame.image.load("Textures/lich_d.png").convert_alpha()
        self.texture_droite_attaque1 = pygame.image.load("Textures/lich_d_atk1.png").convert_alpha()
        self.texture_droite_attaque2 = pygame.image.load("Textures/lich_d_atk2.png").convert_alpha()
        self.texture_gauche = pygame.image.load("Textures/lich_g.png").convert_alpha()
        self.texture_gauche_attaque1 = pygame.image.load("Textures/lich_g_atk1.png").convert_alpha()
        self.texture_gauche_attaque2 = pygame.image.load("Textures/lich_g_atk2.png").convert_alpha()

    def Attaque(self,hero,proba=None):
        proba = randrange(1,16)
        if proba == 16:
            hero.SubitDegats(14)
        else:
            hero.SubitDegats(7)

    def SubitDegats(self,degats):
         if self.vie < degats:
            self.vie = 0
         else:
            self.vie -= degats

    def Mort(self,son):
        son.JouerGameOver()

class LoupAlpha:
    def __init__():
        self.nom = "Loup Alpha"
        self.vie = 40

        self.texture_droite = pygame.image.load("Textures/texture_loup_alpha_d.png").convert_alpha()
        self.texture_droite_attaque = pygame.image.load("Textures/texture_loup_alpha_d_atk.png").convert_alpha()
        self.texture_gauche = pygame.image.load("Textures/texture_loup_alpha_g.png").convert_alpha()
        self.texture_gauche_attaque = pygame.image.load("Textures/texture_loup_alpha_d_atk.png").convert_alpha()

    def Attaque(self,hero,proba=None):
        proba = randrange(1,16)
        if proba == 16:
            hero.SubitDegats(14)
        else:
            hero.SubitDegats(7)

    def SubitDegats(self,degats):
         if self.vie < degats:
            self.vie = 0
         else:
            self.vie -= degats

    def Mort(self,son):
        son.JouerGameOver()