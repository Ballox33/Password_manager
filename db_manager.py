import sqlite3
import os

def get_db_path():
    try:
        # Check if the environment variable is set
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, "password_manager_db.sqlite")
    except Exception as e:
        print(f"Error getting database path: {e}")
        return None

def initialize_db():                                 #funzione per attivare il db
    conn = sqlite3.connect(get_db_path())      #definisco una variabile che stabilisce la connessione col db
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
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO passwords (id_sito, password, user, Description)
        VALUES (?, ?, ?, ?);   
    """, (id_sito, password, user, Description))  #Sempre usa i segnaposto per passare valori alle query SQL. È più sicuro, affidabile e compatibile con tutti i database. 
    conn.commit()
    conn.close()

def get_passwords():
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM passwords;")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_passwords(sito_search, password_search, user_search):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM passwords WHERE id_sito LIKE ? AND password LIKE ? AND user LIKE ?;
""", (f"%{sito_search}%", f"%{password_search}%", f"%{user_search}%"))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_password(sito_search, password_search, user_search):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    cursor.execute(f"""DELETE FROM passwords WHERE id_sito LIKE ? AND password LIKE ? 
                    AND user LIKE ?;""",(f"%{sito_search}%", f"%{password_search}%", f"%{user_search}%"))
    conn.commit()
    conn.close()

def update_password(Sito, Password, Username, Descrizione, sito_search, password_search, user_search):
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()
    query = """
    UPDATE passwords
    SET id_sito = ?, 
        password = ?, 
        user = ?, 
        Description = ?
    WHERE id_sito LIKE ? AND password LIKE ? AND user LIKE ?;
    """
    params = (Sito, Password, Username, Descrizione, f"%{sito_search}%", f"%{password_search}%", f"%{user_search}%")
    cursor.execute(query, params)
    conn.commit()
    conn.close()


#Da aggiungere la funzione per recuperare una psw alla volta per sito o utente
