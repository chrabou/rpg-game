class Game:

    def __init__(self, nom, context, butin, team):
        self.__nom = nom
        self.__context = context
        self.__butin = butin
        self.__team = team
    
    def config(self):
        self.__nom = input("Entrer le nom du joueur : ")
    
    def start(self):
        self.__context = "mouvement"
        self.__butin = 40
        self.__team = []
        
    def status(self):
        