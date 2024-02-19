from typing import Tuple, List
from carte import CarteDepart, CarteFin, Vide,URDL,UR,URD,URL,UD,UL,RL
from joueur import Joueur
from pioche import Pioche
# en fonction de nombre de joueur elle permet de savoir le nombre de chercheurs et le nombre de saboteurs dans la partie.
#Tuple[nombre de saboteurs, nombre de chercheurs]
#Tuple: est une liste qu'on ne peut pas modifier par la suite.
def config_joueur(nb_joueur: int) -> Tuple[int,int]:  
    match nb_joueur : 
        case 3: return (1,3)
        case 4: return (1,4)
        case 5: return (2,4)
        case 6: return (2,5)
        case 7: return (3,5)
        case 8: return (3,6)
        case 9: return (3,7)
        case 10: return (4,7)
        case _: 
            return (None,None)

    
def definir_joueur(nb_joueur: int,nb_saboteurs,nb_chercheurs) -> List[Joueur]:  
    joueurs = [] # création d'une liste de joueurs.
    pioche = Pioche(nb_joueur,nb_saboteurs,nb_chercheurs) # configuration du paquet primaire pour la partie.
    for i in range(1,nb_joueur+1):
        list_input = []
        while (len(list_input) != 2):
            list_input = str(input(f"Veuillez entrer le nom du joueur {i} et le status (IA: 0, Humain: 1):")).split(',') #saisir le nom de joueur ainsi que son statut.
            if len(list_input)==2 and list_input[1] in ["0","1"," 0 "," 1 ", " 0"," 1","0 ","1 "] : 
                nom = list_input[0]
                status = "IA" if list_input[1].find("0") != -1  else "humain"
                joueurs.append(Joueur(nom,status,pioche)) # création d'objet de type joueur et les ajouter dans la liste joueurs.
            else: 
                print("Erreur: Entree invalide: format d'entree: 'nom, status(0 ou 1)' ") 
                list_input = []
    return joueurs 

def afficher_joueur_en_cours(joueurs: list): # affichage des joueurs et leurs status présents dans la partie    print(f"-----------------------------------------------\nles {len(joueurs)} joueurs sont:",end=' ')
    for i, joueur in enumerate(joueurs) : 
        if i+1 == len(joueurs) : 
            print(f"{joueur.nom} ({joueur.statut})")
        else:
            print(f"{joueur.nom} ({joueur.statut})", end=", ")

def creer_plateau(): # méthode de création du plateau pour la partie.
    plateau = [] # déclaltion du plateau vide.
    for i in range(5): 
        plateau.append([])
        for j in range(9): 
            if i == 2 and j == 0:
                plateau[i].append(CarteDepart())  # Emplacement de la carte de depart 
            # positionnement des cartes de Fin dans le plateau 
            elif i == 0 and j == 8: 
                 plateau[i].append(CarteFin())  
            elif i == 2 and j == 8:
                 plateau[i].append(CarteFin()) 
            elif i == 4 and j == 8:
                 plateau[i].append(CarteFin()) 
            else :
                plateau[i].append(Vide()) # remplir le reste du plateau avec une carte <Vide>
    return plateau

# dévision du plateau sous forme d'une matrice 9 * 5 = 45 , selon la régle mentionée dans le jeu il faut qu'il soit 7 cartes entre la carte de départ et la carte Fin.
def afficher_plateau(plateau):
    c00l0, c00l1, c00l2 = plateau[0][0].affichage() 
    c01l0, c01l1, c01l2 = plateau[0][1].affichage()
    c02l0, c02l1, c02l2 = plateau[0][2].affichage()
    c03l0, c03l1, c03l2 = plateau[0][3].affichage()
    c04l0, c04l1, c04l2 = plateau[0][4].affichage()
    c05l0, c05l1, c05l2 = plateau[0][5].affichage()
    c06l0, c06l1, c06l2 = plateau[0][6].affichage()
    c07l0, c07l1, c07l2 = plateau[0][7].affichage()
    c08l0, c08l1, c08l2 = plateau[0][8].affichage()
    
    c10l0, c10l1, c10l2 = plateau[1][0].affichage()
    c11l0, c11l1, c11l2 = plateau[1][1].affichage()
    c12l0, c12l1, c12l2 = plateau[1][2].affichage()
    c13l0, c13l1, c13l2 = plateau[1][3].affichage()
    c14l0, c14l1, c14l2 = plateau[1][4].affichage()
    c15l0, c15l1, c15l2 = plateau[1][5].affichage()
    c16l0, c16l1, c16l2 = plateau[1][6].affichage()
    c17l0, c17l1, c17l2 = plateau[1][7].affichage()
    c18l0, c18l1, c18l2 = plateau[1][8].affichage()
    
    c20l0, c20l1, c20l2 = plateau[2][0].affichage()
    c21l0, c21l1, c21l2 = plateau[2][1].affichage()
    c22l0, c22l1, c22l2 = plateau[2][2].affichage()
    c23l0, c23l1, c23l2 = plateau[2][3].affichage()
    c24l0, c24l1, c24l2 = plateau[2][4].affichage()
    c25l0, c25l1, c25l2 = plateau[2][5].affichage()
    c26l0, c26l1, c26l2 = plateau[2][6].affichage()
    c27l0, c27l1, c27l2 = plateau[2][7].affichage()
    c28l0, c28l1, c28l2 = plateau[2][8].affichage()
    
    c30l0, c30l1, c30l2 = plateau[3][0].affichage()
    c31l0, c31l1, c31l2 = plateau[3][1].affichage()
    c32l0, c32l1, c32l2 = plateau[3][2].affichage()
    c33l0, c33l1, c33l2 = plateau[3][3].affichage()
    c34l0, c34l1, c34l2 = plateau[3][4].affichage()
    c35l0, c35l1, c35l2 = plateau[3][5].affichage()
    c36l0, c36l1, c36l2 = plateau[3][6].affichage()
    c37l0, c37l1, c37l2 = plateau[3][7].affichage()
    c38l0, c38l1, c38l2 = plateau[3][8].affichage()
    
    c40l0, c40l1, c40l2 = plateau[4][0].affichage()
    c41l0, c41l1, c41l2 = plateau[4][1].affichage()
    c42l0, c42l1, c42l2 = plateau[4][2].affichage()
    c43l0, c43l1, c43l2 = plateau[4][3].affichage()
    c44l0, c44l1, c44l2 = plateau[4][4].affichage()
    c45l0, c45l1, c45l2 = plateau[4][5].affichage()
    c46l0, c46l1, c46l2 = plateau[4][6].affichage()
    c47l0, c47l1, c47l2 = plateau[4][7].affichage()
    c48l0, c48l1, c48l2 = plateau[4][8].affichage()
    print(f"""Current mine state: 
 |  0    1    2    3    4    5    6    7    8   
-+---------------------------------------------
 |{c00l0}{c01l0}{c02l0}{c03l0}{c04l0}{c05l0}{c06l0}{c07l0}{c08l0}
0|{c00l1}{c01l1}{c02l1}{c03l1}{c04l1}{c05l1}{c06l1}{c07l1}{c08l1}       
 |{c00l2}{c01l2}{c02l2}{c03l2}{c04l2}{c05l2}{c06l2}{c07l2}{c08l2}
 |{c10l0}{c11l0}{c12l0}{c13l0}{c14l0}{c15l0}{c16l0}{c17l0}{c18l0}
1|{c10l1}{c11l1}{c12l1}{c13l1}{c14l1}{c15l1}{c16l1}{c17l1}{c18l1}       
 |{c10l2}{c11l2}{c12l2}{c13l2}{c14l2}{c15l2}{c16l2}{c17l2}{c18l2}
 |{c20l0}{c21l0}{c22l0}{c23l0}{c24l0}{c25l0}{c26l0}{c27l0}{c28l0}
2|{c20l1}{c21l1}{c22l1}{c23l1}{c24l1}{c25l1}{c26l1}{c27l1}{c28l1}       
 |{c20l2}{c21l2}{c22l2}{c23l2}{c24l2}{c25l2}{c26l2}{c27l2}{c28l2}
 |{c30l0}{c31l0}{c32l0}{c33l0}{c34l0}{c35l0}{c36l0}{c37l0}{c38l0}
3|{c30l1}{c31l1}{c32l1}{c33l1}{c34l1}{c35l1}{c36l1}{c37l1}{c38l1}       
 |{c30l2}{c31l2}{c32l2}{c33l2}{c34l2}{c35l2}{c36l2}{c37l2}{c38l2}
 |{c40l0}{c41l0}{c42l0}{c43l0}{c44l0}{c45l0}{c46l0}{c47l0}{c48l0}
4|{c40l1}{c41l1}{c42l1}{c43l1}{c44l1}{c45l1}{c46l1}{c47l1}{c48l1}       
 |{c40l2}{c41l2}{c42l2}{c43l2}{c44l2}{c45l2}{c46l2}{c47l2}{c48l2}
 """)
    
if __name__ == '__main__':
    nb_saboteurs, nb_chercheurs = None, None
    while (nb_saboteurs== None and nb_chercheurs == None):
        try:
            nb_joueur = int(input("Entrer le nombre de joueur:"))  #saisir le nombre de joueur pour la partie.
            nb_saboteurs, nb_chercheurs = config_joueur(nb_joueur) 
        except ValueError : 
           pass
    joueurs = definir_joueur(nb_joueur,nb_saboteurs,nb_chercheurs)
    afficher_joueur_en_cours(joueurs)
    plateau = creer_plateau() # création objet plateau.
    afficher_plateau(plateau) # affichage plateau.
    
    # afficher la main de chaque joueur.     
    manche = 0 ; 
    while manche < 3: 
        for joueur in joueurs: 
            joueur.affichage_main() # affichage main la main de joueur.
            num_carte = int(input("Quelle carte voulez vous jouer?")) # choix de la carte à jouer.
            coordonner = str(input("Ou souhaitez vous placer votre carte?")).split(',') # saisir la position ou placer la carte choisie.
            plateau[int(coordonner[0])][int(coordonner[1])] = joueur.main[num_carte-1] # déposer la carte choisie dans la pleateau et passer au joueur suivant.
            joueur.main.remove(joueur.main[num_carte-1])# mis à jour de la main du joueur aprés chaque carte jouée.
            joueur.affichage_main() # affichage de la main du joueur courante pour vérifier que la carte jouée à été bien retirée.
            afficher_plateau(plateau)
            pass
    
        

    

