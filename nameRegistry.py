import sqlite3
from colorama import Fore, Style
import re

##### FUNÇÃO PARA CHECAR CARACTERES ESPECIAIS #######
def have_special_characteres(s):
    detect_pattern = re.compile(r'[^a-zA-Z0-9]')
    return bool(detect_pattern.search(s))

####### FUNÇÃO DE CADASTRO DE NOME ###########
def nameRegistry():
    username_registry = input("Digite seu nome para cadastro: ")
    if not " " in username_registry and len(username_registry) > 4 and not have_special_characteres(username_registry):
        valueregistry = username_registry
        valueregistry = valueregistry.lower()    
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );       
        ''')

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
        print("")
        print(Fore.RED + "NÃO pode conter espaços, DEVE conter mais que 4 caracteres e NÃO DEVE conter caracteres especiais" + Style.RESET_ALL)
        print("")
