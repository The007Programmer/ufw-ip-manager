import os
import json
import subprocess

def run_bash_cmd(command):
    """
    Runs a Bash command and prints its output/errors.
    """
    try:
        # Running bash command via -c flag
        process = subprocess.run(['bash', '-c', command], capture_output=True, text=True, check=True)
        return process.stdout
    except subprocess.CalledProcessError as e:
        # Print error if command execution fails
        print(f"Error executing command: {e.stderr if e.stderr else e}")
    except FileNotFoundError:
        # Error if bash binary is not found
        print("Error: Bash not found.")

def main():
    """
    DESC: Main program run. Checks UFW status and enables it if inactive.
    ARGS: NONE
    RTNS: NONE
    """
    # Check if UFW is active using match-case
    match run_bash_cmd("sudo ufw status"):
        # If UFW is inactive, enable it and warn about default IP blocking
        case "Status: inactive\n":
            print("\nUFW currently disabled... ENABLING UFW\n\nREMINDER: All IPs blocked by default, add to whitelist to allow users to connect.\n")
            run_bash_cmd("sudo ufw enable")
        case "Status: active\n":
            # If UFW is active, continue with the program
            print("\nUFW enabled... continuing.\n")
    
    # Call the main program loop
    prgm()

def prgm():
    # Prompt user for what they want to do next
    start = input("ENTER CMD #:\n1) MANAGE Users (Add/Remove/Switch)\n2) SHOW Whitelist/Blacklist\n3) EXIT\n\n")
    match start:
        case '1':
            # Call user management function
            manager()
        case '2':
            # Show the whitelist and/or blacklist
            show_db()
        case '3':
            # Exit the application
            exit()

def manager():
    # Ask user specific details for modifying the lists
    name = input("\nUser Name? ")
    ip = input("User IP? ")
    ports = input("Which ports to allow/block? (e.g. '80, 443' or 'all' for all ports) ")
    
    # Process ports input
    if ports.lower() != 'all':
        try:
            # Validate port numbers
            port_list = [int(p.strip()) for p in ports.split(',')]
            for port in port_list:
                if port < 1 or port > 65535:
                    print("\nInvalid port number! Ports must be between 1-65535")
                    manager()
                    return
            ports = port_list
        except ValueError:
            print("\nInvalid port format! Use comma-separated numbers or 'all'")
            manager()
            return

    w_b = input("Whitelist or Blacklist? (w/b) ")
    match w_b:
        case "w" | "b":
            pass
        case _:
            print("\nPlease specify white/black list!")
            manager()
            return

    db_file = 'db.json'
    if not os.path.exists(db_file):
        print(f"\nDatabase file '{db_file}' does not exist in the current directory.\n")
        return

    with open(db_file, 'r') as file:
        db = json.load(file)

    # Modified data structure to include ports
    user_data = {
        "ip": ip,
        "ports": ports
    }

    match w_b:
        case 'w':
            match True:
                case _ if name in db.get("whitelist", {}) and db["whitelist"][name]["ip"] == ip:
                    print(f"\n{name} is already in the whitelist.\n")
                case _ if name in db.get("blacklist", {}) and db["blacklist"][name]["ip"] == ip:
                    switch = input(f"{name} is in the blacklist. Do you want to switch to whitelist? (y/n) ")
                    if switch == 'y':
                        db["blacklist"].pop(name)
                        db.setdefault("whitelist", {})[name] = user_data
                        print(f"\n{name} has been moved to the whitelist.\n")
                case _:
                    db.setdefault("whitelist", {})[name] = user_data
                    print(f"\n{name} has been added to the whitelist.\n")
        case 'b':
            match True:
                case _ if name in db.get("blacklist", {}) and db["blacklist"][name]["ip"] == ip:
                    print(f"\n{name} is already in the blacklist.\n")
                case _ if name in db.get("whitelist", {}) and db["whitelist"][name]["ip"] == ip:
                    switch = input(f"{name} is in the whitelist. Do you want to switch to blacklist? (y/n) ")
                    if switch == 'y':
                        db["whitelist"].pop(name)
                        db.setdefault("blacklist", {})[name] = user_data
                        print(f"\n{name} has been moved to the blacklist.\n")
                case _:
                    db.setdefault("blacklist", {})[name] = user_data
                    print(f"\n{name} has been added to the blacklist.\n")

    with open(db_file, 'w') as file:
        json.dump(db, file, indent=2)

    more = input("Do you want to add more users? (y/n) ")
    if more == 'y':
        manager()
    else:
        print("\nReturning to menu!\n")
        prgm()

def show_db():
    # Load database file if it exists, otherwise exit function
    db_file = 'db.json'
    if os.path.exists(db_file):
        with open(db_file, 'r') as file:
            db = json.load(file)
    else:
        print(f"\nDatabase file '{db_file}' not found.\n")
        return
    # Ask user which list to view: whitelist, blacklist or all
    which = input("\nWhich database would you like to see? Whitelist, Blacklist or All? (w/b/a)\n")
    # Selecting proper list to display using match-case
    match which:
        case "w":
            print("\n===== WHITELIST =====\n\n" + f"{json.dumps(db.get('whitelist', {}), indent=4)}\n")
        case "b":
            print("\n===== BLACKLIST =====\n\n" + f"{json.dumps(db.get('blacklist', {}), indent=4)}\n")
        case "a":
            print("\n===== ALL LISTS =====\n\n" + f"{json.dumps(db, indent=4)}\n")

# Starting the program
main()

# ------------------------------------------------------------------------------
# main structure:
# --- checking if UFW enabled ---
# If UFW is not enabled, it will be enabled automatically.
# Also displays a reminder that by default all IPs are blocked until added.
# Then moves into the main program loop: managing users, showing lists or exit.
#
# note:
# Feature ideas: SYNC current UFW rules, check whitelist against active rules,
# prompt for user names if mismatch occurs, and sync lists accordingly.
# ------------------------------------------------------------------------------