from pioche import Pioche

class Joueur(): # Classe joueur elle va contenir les informations nécessaires de chaque joueur 

    def __init__(self,nom:str,statut:str,pioche:Pioche):
        self.nom=nom
        self.statut=statut
        self.main=pioche.main_joueur()
        self.role=pioche.pioche_role_joueur() # récupere le role du joueur 

                
    def __str__(self) -> str:
        return f"{self.nom} ({self.role}) contient {len(self.main)} cartes dans la main"
    
    def affichage_main(self):  # elle va afficher les cartes de la main de chaque joueurn, le nombre de carte en fonction du nombre de joueur.
        i=1
        line1 =  "      "
        line2 = f"{i}:    "
        line3 =  "      "
        for carte in self.main: 
            i+=1 
            c48l0, c48l1, c48l2 = carte.affichage()
            line1 = line1 + c48l0 +  "     "
            line2 = line2 + c48l1 + f", {i}: " 
            line3 = line3 + c48l2 +  "     "
        line1+=""
        line2= line2[:-3] + f"{i}) jetez une carte"
        line3+=""
        print(f""" 
C'est le tour de {self.nom}:
{line1}
{line2}
{line3}
""")



#fonction test de nombre de carte pour chaque joueur avec le role.


if __name__ == '__main__':
    pioche = Pioche(4,1,2)    
        
    j1 = Joueur("toto","ia",pioche)
    j2 = Joueur("titi","ia",pioche)
    j3 = Joueur("tata","ia",pioche)

    print(j1)
    print(j2)
    print(j3)
    

