import os
import json

def main():
    start = input("ENTER CMD #:\n1) MANAGE Users (Add/Remove/Switch)\n2) SHOW Whitelist/Blacklist\n3) EXIT\n\n")
    if start == '1':
        manager()
    if start == '2':
        show_db()
    if start == '3':
        exit()

def manager():
    name = input("\nUser Name? ")
    ip = input("User IP? ")
    w_b = input("Whitelist or Blacklist? (w/b) ")

    if w_b not in ["w", "b"]:
        print("\nPlease specify white/black list!")
        manager()

    db_file = 'db.json'

    if not os.path.exists(db_file):
        print(f"\nDatabase file '{db_file}' does not exist in the current directory.\n")
        return

    with open(db_file, 'r') as file:
        db = json.load(file)

    if name in db["whitelist"] and db["whitelist"][name] == ip:
        if w_b == 'w':
            print(f"\n{name} is already in the whitelist.\n")
        else:
            switch = input(f"{name} is in the whitelist. Do you want to switch to blacklist? (y/n) ")
            if switch == 'y':
                db["whitelist"].pop(name)
                db["blacklist"][name] = ip
                print(f"\n{name} has been moved to the blacklist.\n")
                
    elif name in db["blacklist"] and db["blacklist"][name] == ip:
        if w_b == 'b':
            print(f"\n{name} is already in the blacklist.\n")
        else:
            switch = input(f"{name} is in the blacklist. Do you want to switch to whitelist? (y/n) ")
            if switch == 'y':
                db["blacklist"].pop(name)
                db["whitelist"][name] = ip
                print(f"\n{name} has been moved to the whitelist.\n")
    else:
        if w_b == 'w':
            db["whitelist"][name] = ip
            print(f"\n{name} has been added to the whitelist.\n")
        else:
            db["blacklist"][name] = ip
            print(f"\n{name} has been added to the blacklist.\n")

    with open(db_file, 'w') as file:
        json.dump(db, file, indent=2)

    more = input("Do you want to add more users? (y/n) ")
    if more == 'y':
        manager()
    else:
        print("\nReturning to menu!\n")
        main()

def show_db():
    db_file = 'db.json'

    if not os.path.exists(db_file):
        print("\nReturning to menu!\n")
        main()

def show_db():

    # Load the database file if it exists, otherwise create a new database
    db_file = 'db.json'
    # if file exists in path then open as read, if not create local db
    if os.path.exists(db_file):
        with open(db_file, 'r') as file:
            db = json.load(file)

    which=input("\nWhich database would you like to see? Whitelist, Blacklist or All? (w/b/a) ")
    match which:
        case "w":
            print("\n===== WHITELIST =====")
            print(json.dumps(db.get("whitelist", {}), indent=4))
        case "b":
            print("\n===== BLACKLIST =====")
            print(json.dumps(db.get("blacklist", {}), indent=4))
        case "a":
            print("\n===== ALL LISTS =====")
            print(json.dumps(db, indent=4))

main()