from abc import ABC, abstractmethod
import random
class Carte(ABC):# Déclaration d'une classe mère abstraite qui contient deux méthodes abstraites.
    @abstractmethod  
    def jouer(self):pass
    @abstractmethod  
    def affichage(self):pass # méthode qui va afficher la carte.
    
class CarteChemin(Carte):#Cette classe va hérité de la classe " Carte " précédement déclaré et elle va contenir toutes les cartes chemins.
    pass

class CarteAction(Carte):#Cette classe va hérité de la classe " Carte " précédement déclaré et elle va contenir toutes les cartes actions.
    pass
class CarteOr(Carte):#Cette classe va hérité de la classe " Carte " précédement déclaré et elle va contenir toutes les trois cartes Or.
    pass
class Vide(Carte): # cette carte elle va servir dans la création du plateau.
    def jouer(self): pass
    
    def __str__(self) -> str:
        return "     \n     \n     "
    def affichage(self): 
        return ("     ","     ","     ")
    
class CarteDepart(CarteChemin): #carte départ du jeu
    
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( | )","(-S-)","( | )")
      
class CarteFin(CarteOr): # carte de fin " END " c'est une classe fille de carteor.
    cp_carte_fin = 0
    est_carte_or = False
    def __init__(self) -> None:
        self.est_or = False
        CarteFin.cp_carte_fin+=1 
        if CarteFin.cp_carte_fin < 3 and CarteFin.est_carte_or == False : 
            self.est_or = random.choice([True, False])
        if self.est_or: 
            CarteFin.est_carte_or = True 
        elif CarteFin.cp_carte_fin == 3 and not CarteFin.est_carte_or: 
            self.est_or = True
            CarteFin.cp_carte_fin = 0 
        # print(CarteFin.est_carte_or, CarteFin.cp_carte_fin)
        
    def jouer(self):
        pass
    def devoiller(self): # Cette méthode va dévoiler parmi les 3 cartes de fin la carte qui contient de l'or.
        if self.est_or : 
            return "est or"
        return "not or"
    def affichage(self):
        return ("(   )","(END)","(   )")
      
class URDL(CarteChemin): # carte chemin ==> Up+Right+Down+Left
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( | )",f"(-{self.types}-)","( | )") 


class URD(CarteChemin): # carte chemin ==> Up+Right+Left 
    def __init__(self,types: str) -> None:
        self.types = types # type de la carte ==> positif ou négatif 
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( | )",f"( {self.types}-)","( | )")
    
class URL(CarteChemin):# carte chemin ==> Up+Right+Left 
    
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( | )",f"(-{self.types}-)","(   )") 
     
class UR(CarteChemin):# carte chemin ==> Up+Right 
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( | )",f"( {self.types}-)","(   )") 
 
class UL(CarteChemin):# carte chemin ==> Up+Left 
    
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( | )",f"(-{self.types} )","(   )") 

class UD(CarteChemin):# carte chemin ==> Up+Down 
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( | )",f"( {self.types} )","( | )")   

class RL(CarteChemin):# carte chemin ==> Right+Left
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("(   )",f"(-{self.types}-)","(   )")    
    
class U(CarteChemin): # carte chemin ==> Up
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( | )","( X )","(   )")    
    
class R(CarteChemin): # carte chemin ==> Right  
    def jouer(self):
        pass
    
    def affichage(self): 
        return ("(   )","( X-)","(   )")    
    

class Li(CarteAction): # carte action ==> Light
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return (f"({self.types})","(LI )","(   )")    
    
class P(CarteAction):# carte action ==> Pike 
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return (f"({self.types})","( P )","(   )")    
    
class W(CarteAction):# carte action ==> Wagon 
    def __init__(self,types: str) -> None:
        self.types = types
        
    def jouer(self):
        pass
    
    def affichage(self): 
        return (f"({self.types})","( W )","(   )") 
    
class LiP(CarteAction):# carte action ==> LightPike 

    def jouer(self):
        pass
    
    def affichage(self): 
        return ("(ATT)","(LiP)","(   )") 
           
class LiW(CarteAction):# carte action ==> LightWagon

    def jouer(self):
        pass
    
    def affichage(self): 
        return ("(ATT)","(LiW)","(   )") 

class PW(CarteAction):# carte action ==> PikeWagon 

    def jouer(self):
        pass
    
    def affichage(self): 
        return ("(ATT)","(PW )","(   )") 
    
class MAP(CarteAction):# catre action ==> map permet de voir une des cartes 

    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( M )","(MAP)","( P )") 
    
class RoF(CarteAction):# carte action ==> Rock Fall qui permet de retirer une carte du plateau 

    def jouer(self):
        pass
    
    def affichage(self): 
        return ("( R )","(RoF)","( F )") 
    
class G1(CarteOr): # carte Or ==> carte or 1 pépite
    def jouer(self):
        return 1
            
    
    def affichage(self): 
        return ("(   )","(G1 )","(   )") 
class G2(CarteOr):# carte Or ==> carte  or  2 pépite
    def jouer(self):
        return 2
            
    
    def affichage(self): 
        return ("(   )","(G2 )","(   )") 
class G3(CarteOr):# carte Or ==> carte  or  3 pépite
    def jouer(self):
        return 3
            
    
    def affichage(self): 
        return ("(   )","(G3 )","(   )") 
    


if __name__ == '__main__':
    carte_depart = CarteDepart()
    carte_fin1 = CarteFin()
    carte_fin2 = CarteFin()
    carte_fin3 = CarteFin()
    
    
    print(carte_fin1.devoiller()) # or
    print(carte_fin2.devoiller()) # not or
    print(carte_fin3.devoiller()) # not or 