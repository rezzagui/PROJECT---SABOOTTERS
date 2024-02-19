from carte import URDL,UR,URD,URL,UD,UL,RL,U,R,Li,P,W,LiP,LiW,PW,MAP,RoF,G1,G2,G3
import random

class Pioche(): # la classe pioche va contenir toute les cartes de la partie à la base et ensuite quand la partie commence 
    def __init__(self,nb_joueur:int,nb_saboteurs:int,nb_chercheurs:int):
        self.list_cartes=[] # 1er paquet c'est les cartes actions et les cartes chemins
        self.list_cartes_or = [] # 2eme paquet les 3 type de carte or 
        self.cartes_role = [] # 3eme paquet c'est les cartes role en fonction du nombre de joueur 3 --> 1 saboteur et 3 chercheur 
       
        # définir le nombre de carte qu'aura chaque joueur en fonction du nombre de joueurs.
        if 3 <= nb_joueur <= 5 :  
            self.nb_carte_main = 6 
        elif 6 <= nb_joueur <= 7: 
            self.nb_carte_main = 5
        elif 8 <= nb_joueur <= 10: 
            self.nb_carte_main = 4
        # création du paquet carteRole en fonction du nombre de saboteurs et nombre de chercheurs. 
        for _ in range(nb_saboteurs) : 
            self.cartes_role.append("saboteur")
        for _ in range(nb_chercheurs) : 
            self.cartes_role.append("chercheur")
            
        # 5 cartes positives  + une carte négative 
        for _ in range(5): 
            self.list_cartes.append(URDL("+")) 
        self.list_cartes.append(URDL("X"))
        for _ in range(5): 
            self.list_cartes.append(URD("+"))
        self.list_cartes.append(URD("X"))
        
        for _ in range(5): 
            self.list_cartes.append(URL("+"))
        self.list_cartes.append(URL("X"))
        
        for _ in range(5): 
            self.list_cartes.append(UR("+"))
        self.list_cartes.append(UR("X"))
        
        for _ in range(4): 
            self.list_cartes.append(UL("+"))
        self.list_cartes.append(UL("X"))
        
        for _ in range(4): 
            self.list_cartes.append(UD("+"))
        self.list_cartes.append(UD("X"))
        
        
        
        for _ in range(3): 
            self.list_cartes.append(RL("+")) 
        self.list_cartes.append(RL("X"))
        self.list_cartes.append(U())
        self.list_cartes.append(R())
        
        for _ in range(2): # 2 cartes positives
            self.list_cartes.append(Li("ATT")) 
        for _ in range(3): # 3 cartes négatives  
            self.list_cartes.append(Li("DEF"))
            
        for _ in range(2): 
            self.list_cartes.append(P("ATT"))
        for _ in range(3): 
            self.list_cartes.append(P("DEF"))
        
        for _ in range(2): 
            self.list_cartes.append(W("ATT"))
        for _ in range(3): 
            self.list_cartes.append(W("DEF"))
                
        self.list_cartes.append(LiP())
        self.list_cartes.append(LiW())
        self.list_cartes.append(PW())
        
        for _ in range(6):
            self.list_cartes.append(MAP())
            
        for _ in range(3):
            self.list_cartes.append(RoF())
        for _ in range(16):
            self.list_cartes_or.append(G1())
        for _ in range(8):
            self.list_cartes_or.append(G2())
        for _ in range(4):
            self.list_cartes_or.append(G3())
        
        
    # méthode qui va déterminer les cartes de chaque joueur.   
    def main_joueur(self): 
        main = random.sample(self.list_cartes,self.nb_carte_main) 
        for carte in main:
            self.list_cartes.remove(carte)
        return main
    # méthode qui va retirer de la list_cartes une carte piochée.
    def pioche_carte(self):
        carte = random.choice(self.list_cartes)
        self.list_cartes.remove(carte)
        return carte
    # defénition de carte role de chaque joueur à partir du paquet cartes role.
    def pioche_role_joueur(self):
        carte_role_joueur = random.choice(self.cartes_role)
        self.cartes_role.remove(carte_role_joueur)
        return carte_role_joueur
        
