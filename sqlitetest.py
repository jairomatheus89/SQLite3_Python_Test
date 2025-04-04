import sqlite3
from time import sleep
from colorama import init, Fore, Style

init(convert=True)

print(Fore.CYAN + "Olá, Seja bem vindo ao JairoDB")
print("")
while True:
    while True:
        print("Oque voce gostaria de fazer: ")
        try:
            choice = int(input(Fore.YELLOW + "1 - Cadastrar-se no Banco de Dados\n2 - Procurar um usuário\n3 - Sair\n" + Style.RESET_ALL))
            print("")
            break
        except ValueError:
            print("")
            print(Fore.RED + "Digite um número válido!" + Style.RESET_ALL)
            print("")

    if choice == 1:
        username_registry = input("Digite seu nome para cadastro: ")

        if username_registry:
            valueregistry = username_registry
            valueregistry = valueregistry.lower()
           
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()

            checkQuery_name = f"SELECT EXISTS(SELECT 1 FROM users WHERE name = ? LIMIT 1)"

            cursor.execute(checkQuery_name,(valueregistry,))
            exist_name = cursor.fetchone()

            if exist_name[0]:
                print(Fore.RED + f"O nome {valueregistry} já existe, registre outro por favor!!!" + Style.RESET_ALL)
                conn.close()
                print("")
            else:
                cursor.execute('INSERT INTO users (name) VALUES (?)', (valueregistry.lower(),))

                conn.commit()
                conn.close()
                print("")
                print(Fore.BLUE +"Nome cadastrado com sucesso!" + Style.RESET_ALL)
                print("")
        else:
            valueregistry = "Por Favor tente novamente digitando um nome!"
    elif choice == 2:

        user_search = input("Procure o usuário desejado: " + Style.RESET_ALL)
        print("")
        user_search = user_search.lower()

        ######## SQL SECTION ########

        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        cursor.execute('SELECT name FROM users WHERE name = ?;',(user_search,))
        name_selected = cursor.fetchone()

        if name_selected:
            namezin = str(name_selected[0])
            value = Fore.GREEN + f"O usuário {namezin.upper()} esta na lista!" + Style.RESET_ALL
        else:
            value = Fore.RED + f"O usuário {user_search} não existe mermaum!" + Style.RESET_ALL

        conn.close()

        print(value)
        print("")
    elif choice > 3 or choice < 1:
        print("")
        print(Fore.RED + "Por Favor insira um numero dentre um dos mensionados no MENU(1 à 3)" + Style.RESET_ALL)
        print("")
    else:
        print("saindo da aplicação em:")
        print("3...")
        sleep(1)
        print("2...")
        sleep(1)
        print("1...")
        sleep(1)
        break