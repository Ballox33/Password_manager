from db_manager import initialize_db, add_password, get_passwords #potrei anche importare tutto con *

def show_menu():
    print("\nMenu:")
    print("1. Aggiungi una nuova password")
    print("2. Visualizza tutte le password")
    print("3. Esci")

def add_new_password():
    id_sito = input("Sito: ")               #input permette di inserire il valore
    password = input("Password: ")
    user = input("User: ")
    Description = input("Descrizione (opzionale): ")
    add_password(id_sito, password, user, Description)
    print("Password aggiunta con successo!")

def display_passwords():
    passwords = get_passwords()
    if not passwords:
        print("Nessuna password trovata.")
        return
    for pwd in passwords:
        print(f"Sito: {pwd[0]}, Username: {pwd[1]}, Password: {pwd[2]}, Descrizione: {pwd[3]}")

def main():
    print("Benvenuto nel Password Manager!")
    initialize_db()

    actions = {                               #è un type dictionary (ad ogni parola corrisponde una chiave)
        "1": add_new_password,
        "2": display_passwords,
        "3": exit_program
    }

    while True:                                        #while true serve a tenere il ciclo del menu attivo finchè non si esce
        show_menu()
        choice = input("Scegli un'opzione: ")
        action = actions.get(choice)                   #salva in "action" l'azione desiderata
        if action:                                #in python valori vuoti o 0 sono considerati falsi
            action()
        else:
            print("Scelta non valida, riprova.")

def exit_program():
    print("Uscita...")
    exit(0)                                    #termina il programma correttamente (0) altrimenti per errori si usa exit(1)

if __name__ == "__main__":      #if __name__ == "__main__": è un'istruzione utile per distinguere tra quando un modulo 
   main()                       #viene eseguito come script principale e quando viene importato da un altro script. 
                                #Garantisce che il codice all'interno della condizione venga eseguito solo nel primo caso

#quando avrai espanso il progetto crea l'eseguibile!!!