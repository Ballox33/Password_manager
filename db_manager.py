import sqlite3
import os

def initialize_db():                                 #funzione per attivare il db
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "password_manager_db.sqlite")
    conn = sqlite3.connect(db_path)      #definisco una variabile che stabilisce la connessione col db
    cursor = conn.cursor()                           #crea il CURSORE per interagire col db   
    cursor.execute("""                               
        CREATE TABLE IF NOT EXISTS passwords (
            id_sito TEXT,
            password TEXT NOT NULL,
            user TEXT NOT NULL,
            Description TEXT
        );                                           
    """)                                             #execute esegue il comando SQL dal cursore, in realtà le ; sono opzionali qui
    conn.commit()                                    #per essere eseguita la transaction va committata
    conn.close()                                     #chiude il cursore e la connessione al db

def add_password(id_sito, password, user, Description =""):   #funz per aggiungere una psw
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "password_manager_db.sqlite")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO passwords (id_sito, password, user, Description)
        VALUES (?, ?, ?, ?);   
    """, (id_sito, password, user, Description))  #Sempre usa i segnaposto per passare valori alle query SQL. È più sicuro, affidabile e compatibile con tutti i database. 
    conn.commit()
    conn.close()

def get_passwords():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "password_manager_db.sqlite")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords;")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_passwords(sito_search, password_search, user_search):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "password_manager_db.sqlite")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM passwords WHERE id_sito LIKE '%{sito_search}%' AND password LIKE '%{password_search}%' 
                    AND user LIKE '%{user_search}%';""")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_password():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "password_manager_db.sqlite")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Digitare la ")
    cursor.execute()
#Da aggiungere la funzione per recuperare una psw alla volta per sito o utente
