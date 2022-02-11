from contextlib import nullcontext


class Game():

    def __init__(self):
        print("bonjour ! ceci est un essai")
    
    def config(self):
        self.__nom = input("Entrer le nom du joueur : ")
    
    def start(self):
        self.__context = "mouvement"
        self.__butin = 40
        self.__team = []
        
    def status(self):
        if(self.__butin == 0):
            print("GAME OVER")
        else:
            print(self.__nom)
            print(self.__butin)
            print("nombre de guerriers : ...")
            print("nombre de chasseurs : ...")
            print("nombre de magiciens : ...\n")
            
            if(self.__context=="mouvement"):
                print("Vous pouvez acheter ou vous deplacer\n")
            else :
                print("Vous pouvez vous battre ou vous enfuire\n")
                
    def buy(self):
        if(self.__context!="mouvement"):
            res = input("Vous voulez acheter quelque chose ? [oui / non]")
            if(res=="oui"):
                self.__butin = self.__butin-1
            else :
                print("tant pis !!!\n")
            
if __name__ == '__main__':
    g = Game()
    g.config()
    g.start()
    
    temp = "null"
    while(temp!="fin"):
        temp = input("Que voulez vous faire ?\n- Voir le status [status]\n- Acheter [buy]\n...\n- Arreter la partie [fin]")
    
        if(temp=="status"):
            g.status()
            
        if(temp=="buy"):
            g.buy()
