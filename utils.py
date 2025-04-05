from colorama import Fore, Style
from time import sleep
######## RANGE DE OPÇÕES DE 1 À 3 ################
def rangeOptions():
    print(Fore.RED + "Por Favor insira um numero dentre um dos mensionados no MENU(1 à 3)" + Style.RESET_ALL)
    print("")

###### SAIR DO APP #########
def exitApp():
    print(Fore.MAGENTA + "saindo da aplicação em:")
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1..." + Style.RESET_ALL)
    sleep(1)