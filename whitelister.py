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
    w_b=input("Whitelist or Blacklist? (w/b)")
    
    if w_b not in ["w", "b"]:
        print("\nPlease specify white/black list!")
        manager()



def show_db():
    pass

def search():
    pass

main()