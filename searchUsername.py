import sqlite3
from colorama import Fore, Style
######### PESQUISAR NOME NO DB ######################
def searchUsername():
    user_search = input("Procure o usuário desejado: " + Style.RESET_ALL)
    print("")
    user_search = user_search.lower()
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );       
    ''')
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