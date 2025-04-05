import sqlite3
from colorama import Fore, Style
def listAll():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    check_table_exist = cursor.execute('''
        SELECT EXISTS (
            SELECT 1 FROM sqlite_master WHERE type='table' AND name='users'                              
        );
    ''').fetchone()[0]
    if check_table_exist:
        conn = sqlite3.connect("example.db")
        cursor.execute('''
            SELECT * FROM users;
        ''')
        names_rows = cursor.fetchall()
        conn.close()

        print(Fore.BLUE + "TODOS OS USUÁRIOS:\n")
        for row in names_rows:
            print(row)
        print("")
    else:
        print(Fore.RED + "Não existe nenhuma tabela criada ainda, selecione a opção 1 no Menu principal para adicionar o primeiro usuário" + Style.RESET_ALL)
        print("")