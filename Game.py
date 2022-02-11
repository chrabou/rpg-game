class Game():

    def __init__(self):
        print("bonjour ! ceci est un essai")
    
    def config(self):
        self.__nom = input("Entrer le nom du joueur : ")
        print("ok config")
    
    def start(self):
        self.__context = "mouvement"
        self.__butin = 40
        self.__team = []
        print("ok start")
        
    def status(self):
        if(self.__butin == 0):
            print("GAME OVER")
        else:
            print(self.__nom)
            print(self.__butin)
            # i = 0
            # while i<=self.__team.__len__():
            #     print()
            
            print("ok status")
            
            
if __name__ == '__main__':
    g = Game()
    g.config()
    g.start()
    g.status()
        