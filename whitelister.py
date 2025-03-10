import os
import subprocess
import json

def main():
    start=input("ENTER CMD #:\n1) MANAGE Players (Add/Remove/Switch)\n2) SHOW Whitelist/Blacklist\n3) SEARCH for a player\n4) EXIT\n\n")
    if start == '1':
        manager()
    if start == '2':
        show_db()
    if start == '3':
        search()
    if start == '4':
        exit()
        

def manager():
    # takes player name, ip, white/black list, does the sudo ufw allow ip, then returns confirm message, asks if more players to add
    name=input("Player Name? ")
    ip=input("Player IP? ")
    w_b=input("Whitelist or Blacklist? (w/b) ")
    
    if w_b not in ["w", "b"]:
        print("\nPlease specify white/black list!")
        manager()

    # Load the database file if it exists, otherwise create a new database
    db_file = 'db.json'

    # if file exists in path then open as read, if not create local db
    if os.path.exists(db_file):
        with open(db_file, 'r') as file:
            db = json.load(file)
    else:
        db = {"whitelist": {}, "blacklist": {}}

    # Check if the player is already in the whitelist or blacklist
    if name in db["whitelist"] and db["whitelist"][name] == ip:
        if w_b == 'w':
            print(f"\n{name} is already in the whitelist.\n")
        else:
            # Ask if the user wants to switch the player to the blacklist
            switch = input(f"{name} is in the whitelist. Do you want to switch to blacklist? (y/n) ")
            if switch == 'y':
                db["whitelist"].pop(name)
                db["blacklist"][name] = ip
                print(f"\n{name} has been moved to the blacklist.\n")
                
    elif name in db["blacklist"] and db["blacklist"][name] == ip:
        if w_b == 'b':
            print(f"\n{name} is already in the blacklist.\n")
        else:
            # Ask if the user wants to switch the player to the whitelist
            switch = input(f"{name} is in the blacklist. Do you want to switch to whitelist? (y/n) ")
            if switch == 'y':
                db["blacklist"].pop(name)
                db["whitelist"][name] = ip
                print(f"\n{name} has been moved to the whitelist.\n")
    else:
        # Add the player to the specified list
        if w_b == 'w':
            db["whitelist"][name] = ip
            print(f"\n{name} has been added to the whitelist.\n")
        else:
            db["blacklist"][name] = ip
            print(f"\n{name} has been added to the blacklist.\n")

    # Save the updated database back to the file
    with open(db_file, 'w') as file:
        json.dump(db, file, indent=2)

    # Ask if the user wants to add more players
    more = input("Do you want to add more players? (y/n) ")
    if more == 'y':
        manager()
    else:
        print("\nReturning to menu!\n")
        main()

def show_db():
    pass

def search():
    pass

main()