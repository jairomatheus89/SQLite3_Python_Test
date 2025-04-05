from colorama import init, Fore, Style, Back

######### MY MODULES IMPORTS #########
from userInput import inputUser
from nameRegistry import nameRegistry
from searchUsername import searchUsername
from utils import exitApp, rangeOptions

#### CALL VARIABLE CHOICE FROM inputUser Function of userInput custom MODULE
def inputUserChoice():
    global choice
    choice = inputUser()
    print(choice)

###### CONVERT COLORAMA PARA CMD, POWERSHELL, BASH ETC....
init(convert=True)

######## PROGRAMA BASE ##########
def mainApp():
    print(Back.BLUE + Fore.WHITE + "Olá, Seja bem vindo ao JairoDB" + Style.RESET_ALL)
    print("")
    while True:
        inputUserChoice()
        if choice == 1:
            nameRegistry()
        elif choice == 2:
            searchUsername()
        elif choice > 3 or choice < 1:
            rangeOptions()
        else:
            exitApp()
            break

mainApp()