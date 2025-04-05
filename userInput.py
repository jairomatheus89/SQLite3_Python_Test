from colorama import Fore, Style
# FUNÇÃO RECEBER O INPUT E CHECAR SE O VALOR É UM NUMERO VALIDO
def inputUser():
    while True:
        print("Oque voce gostaria de fazer: ")
        try:
            choice = int(input(Fore.YELLOW + "1 - Cadastrar-se no Banco de Dados\n2 - Procurar um usuário\n3 - Sair\n" + Style.RESET_ALL))
            print("")
            return choice
        except ValueError:
            print("")
            print(Fore.RED + "Digite um número válido!" + Style.RESET_ALL)
            print("")