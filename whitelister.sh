#!/bin/bash

# reset all ufw rules and enable it
# sudo ufw --force reset
# sudo ufw enable

main() {
    read -p "Enter CMD:  |  LIST (a)  |  SHOWLIST (l)  |  SEARCH (s)  |  REMOVE (r)  |: " cmd

    if [[ "$cmd" == "a" ]]; then
        read -p "Enter player name: " name
        read -p "Enter player IP: " ip
        read -p "Whitelist or Blacklist (w/b): " w_b 
        list "$name" "$ip" "$w_b"

        # once all ips are added it'll then deny all other ips attempting to connect
        # sudo ufw deny 25565/tcp

        # hackers can still see open port --> but denied by firewall
        #    - still leaves it open to possible exploits if someone really tries -_-

        # reloads all settings into effect
        # sudo ufw reload

    elif [[ "$cmd" == "l" ]]; then
        read -p "Whitelist, Blacklist, or ALL? (a/w/b)" 

    fi



}

list() {
    # Used chatgpt for the json syntax !!!
    local player="$1"
    local ip="$2"
    local whiteblack="$3"

    if [[ "$3" == "w" ]] then
        
        # sudo ufw allow from "$ip" to any port 25565 proto tcp
        
        # adds to whitelisted database
        jq --arg player "$player" --arg ip "$ip" '.whitelisted[$player] = $ip' db.json > temp.json && mv temp.json db.json
        
        # success message
        echo "Successfully whitelisted $player with IP: $ip"
    
    elif [[ "$3" == "b" ]] then
    
        # sudo ufw deny from "$ip" to any port 25565 proto tcp
        
        # adds to blacklisted database
        jq --arg player "$player" --arg ip "$ip" '.blacklisted[$player] = $ip' db.json > temp.json && mv temp.json db.json
        
        # success message
        echo "Successfully blacklisted $player with IP: $ip"
    
    else
        echo "Try again!"
        main

    fi 
}

showlist() {
    local all={$1}
}

main