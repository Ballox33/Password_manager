import os
import sqlite3


def get_db_path():
    try:
        # Check if the environment variable is set
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, "password_manager_db.sqlite")
    except Exception as e:
        print(f"Error getting database path: {e}")
        return None
    
def id_sito_input():
    while True:
        id_sito = input("Sito: ")
        if id_sito.lower() == "master":
            print("Non puoi usare 'master' come nome del sito. Scegli un altro nome.")
        else:
            break  
    return id_sito

def id_sito_input_search():   
    while True:
        sito_search = input("Di che sito è la password che stai cercando: \n")
        if sito_search.lower() == "master":
            print("Non puoi usare 'master' come nome del sito per la ricerca. Scegli un altro nome.")
        else:
            break
    return sito_search