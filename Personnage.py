from random import *
import abc

class Personnage(abc.ABC):

    #constructeur abstrait
    @abc.abstractmethod
    def display_info(self):
        pass
    
    #getters abstrait
    @abc.abstractmethod
    def getDegat(self):
        pass
    def getChance(self):
        pass
    def getFuite(self):
        pass
    def getPrix(self):
        pass


#----------------------------------------------------------------------------------------------------------------------------------------------
#classe Chasseur
class Chasseur(Personnage):
    def __init__(self):
        self.__degat = randint(1,2)
        self.__chance = 10
        self.__fuite = 20
        self.__prix = 25

    #Constructeur de Chasseur
    def display_info(self):
        print("Chasseur - ","Degat :", self.__degat, "|", "Chance :", self.__chance, "|", "Fuite :", self.__fuite, "|", "Prix :", self.__prix, "|")
    
    #Getters de Chasseur
    #-----------------------------------------------------------------------
    def getDegat(self):
        return self.__degat
    def getChance(self):
        return self.__chance
    def getFuite(self):
        return self.__fuite
    def getPrix(self):
        return self.__prix
    #-----------------------------------------------------------------------
    #fin de classe Chasseur
#----------------------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------------------
#classe Guerrier
class Guerrier(Personnage):
    #Constructeur Guerrier
    def __init__(self):
        self.__degat = randint(3,5)
        self.__chance = 5
        self.__fuite = 3
        self.__prix = 10
    
    #Constructeur de Guerrier
    def display_info(self):
        print("Guerrier - ","Degat :", self.__degat, "|", "Chance :", self.__chance, "|", "Fuite :", self.__fuite, "|", "Prix :", self.__prix, "|")
    
    #Getters de Guerrier
    #-----------------------------------------------------------------------
    def getDegat(self):
        return self.__degat
    def getChance(self):
        return self.__chance
    def getFuite(self):
        return self.__fuite
    def getPrix(self):
        return self.__prix
    #-----------------------------------------------------------------------
    #fin de classe Guerrier
#----------------------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------------------
#classe Magicien
class Magicien(Personnage):
    def __init__(self):
        self.__degat = randint(2,4) 
        self.__chance = 20
        self.__fuite = 10
        self.__prix = 15
    
    #Constructeur de Magicien
    def display_info(self):
        print("Magicien - ","Degat :", self.__degat, "|", "Chance :", self.__chance, "|", "Fuite :", self.__fuite, "|", "Prix :", self.__prix, "|")
    
    #Getters de Magicien
    #-----------------------------------------------------------------------
    def getDegat(self):
        return self.__degat
    def getChance(self):
        return self.__chance
    def getFuite(self):
        return self.__fuite
    def getPrix(self):
        return self.__prix
    #-----------------------------------------------------------------------
    #fin de classe Magicien
#----------------------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    #test d'initialisation et du print des infos
    chasseur1 = Chasseur()
    chasseur1.display_info()
    
    guerrier1 = Guerrier()
    guerrier1.display_info()
    
    magicien1 = Magicien()
    magicien1.display_info()


    #11/02/2022 - 16h09 - les getters viennent d'être testé et ils fonctionnent tous.
  
