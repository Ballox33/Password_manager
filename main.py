from db_manager import initialize_db,add_password, get_passwords, search_passwords \
,delete_password,update_password
from crypto_manager import encrypt_password, decrypt_password, check_master_password #potrei anche importare tutto con *
from utils import id_sito_input, id_sito_input_search

def show_menu():
    print("\nMenu:")
    print("1. Aggiungi una nuova password")
    print("2. Visualizza tutte le password")
    print("3. Cerca una password")
    print("4. Cerca e rimuovi/aggiorna una password")
    print("5. Esci")

def add_new_password(master):
    id_sito = id_sito_input()  # Uso una funzione per fare il check sul master
    password = input("Password: ")
    user = input("User: ")
    Description = input("Descrizione (opzionale): ")
    add_password(id_sito,encrypt_password(master, password), user, Description)
    print("Password aggiunta con successo!")

def display_passwords(master):
    passwords = get_passwords()
    if not passwords:
        print("Nessuna password trovata.")
        return
    for pwd in passwords:
        decrypted_password = decrypt_password(master, pwd[1])  # Decrypt the password
        print(f"Sito: {pwd[0]} | Password: {decrypted_password} | User: {pwd[2]} | Descrizione: {pwd[3]}")

def search_passwords_main(master):
    print("Per effettuare la ricerca delle tue password digita il nome o parte di esso di ciò che vuoi cercare per ogni campo richiesto!\n")
    print("Ricorda che se vuoi puoi lasciare un campo vuoto!\n")
    sito_search = id_sito_input_search()  # Uso una funzione per fare il check sul master
    description_search = input("Che descrizione ha la password che stai cercando: \n")
    user_search = input("Chi è l'utente al quale appartiene la password: \n")
    passwords = search_passwords(sito_search, description_search, user_search)
    if not passwords:
        print("Nessuna password trovata.")
        return
    else:
        print("Ecco le password trovate:\n")
        for pwd in passwords:
            decrypted_password = decrypt_password(master, pwd[1])
            print(f"Sito: {pwd[0]} | Password: {decrypted_password} | User: {pwd[2]} | Descrizione: {pwd[3]}")
        return passwords,sito_search,description_search,user_search   #sto ritornando una tupla!!

def delete_update_password_main(master):
    while True:
        print("Effettua la ricerca della password e successivamente eliminala/aggiornala!\n")
        result = search_passwords_main(master)
        if len(result[0]) != 1 :
            print("Puoi eliminare/aggiornare una sola password alla volta!")
        else:
            print("Vuoi eliminare o aggiornare la tua password? (delete/update) ")
            confirm = input()
            if confirm == 'delete':
                delete_password(result[1],result[2],result[3])
                print("La password è stata eliminata con successo!")
                break
            elif confirm == 'update':
                print("inserisci in sequenza i nuovi campi:")
                Sito = id_sito_input() 
                Password = input("Password: ")
                Username = input("Username: ")
                Descrizione = input("Descrizione: ")
                encrypted_password = encrypt_password(master, Password) 
                update_password(Sito,encrypted_password,Username,Descrizione,result[1],result[2],result[3])
                print("La password è stata aggiornata con successo!")
                break
            else:
                print("Opzione non valida!")
        print("Vuoi tornare al menu? (y/n)")
        confirm_1 = input()
        if confirm_1 == 'y':
            break
    return


def main():
    print("Benvenuto nel Password Manager!\n")
    print("Scegli una master password per cifrare le tue password.\n" \
    "Se hai già una master password, inseriscila per usare il password manager.\n")
    # Qui potresti implementare un controllo per verificare se la master password è corretta
    while True:
        master = input("Inserisci la tua master password: ")
        initialize_db(master)
        if check_master_password(master) == True :
            break
        else:
            print("La master password è errata!")  # Verifica la master password

    actions = {                               #è un type dictionary (ad ogni parola corrisponde una chiave)
        "1": add_new_password,
        "2": display_passwords,
        "3": search_passwords_main,
        "4": delete_update_password_main,
        "5": exit_program
    }

    while True:                                        #while true serve a tenere il ciclo del menu attivo finchè non si esce
        show_menu()
        choice = input("Scegli un'opzione: ")
        action = actions.get(choice)                   #salva in "action" l'azione desiderata
        if action:                                #in python valori vuoti o 0 sono considerati falsi
            action(master)
        else:
            print("Scelta non valida, riprova.")

def exit_program(master):
    print("Uscita...")
    exit(0)                                    #termina il programma correttamente (0) altrimenti per errori si usa exit(1)

if __name__ == "__main__":      #if __name__ == "__main__": è un'istruzione utile per distinguere tra quando un modulo 
   main()                       #viene eseguito come script principale e quando viene importato da un altro script. 
                                #Garantisce che il codice all'interno della condizione venga eseguito solo nel primo caso

#quando avrai espanso il progetto crea l'eseguibile!!!