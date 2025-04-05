import sqlite3
from colorama import Fore, Style
####### FUNÇÃO DE CADASTRO DE NOME ###########
def nameRegistry():
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
