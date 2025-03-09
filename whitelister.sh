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

    # Check if player is already on the whitelist or blacklist and switch accordingly
    if [[ "$whiteblack" == "w" ]]; then
        # If player is blacklisted, remove from blacklist and add to whitelist
        if [[ $(jq -r ".blacklisted[$player]" db.json) != "null" ]]; then
            jq --arg player "$player" 'del(.blacklisted[$player])' db.json > temp.json && mv temp.json db.json
            echo "$player was blacklisted. They have been switched to the whitelist."
        fi

        # Add to the whitelist
        jq --arg player "$player" --arg ip "$ip" '.whitelisted[$player] = $ip' db.json > temp.json && mv temp.json db.json
        echo "Successfully whitelisted $player with IP: $ip"

    elif [[ "$whiteblack" == "b" ]]; then
        # If player is whitelisted, remove from whitelist and add to blacklist
        if [[ $(jq -r ".whitelisted[$player]" db.json) != "null" ]]; then
            jq --arg player "$player" 'del(.whitelisted[$player])' db.json > temp.json && mv temp.json db.json
            echo "$player was whitelisted. They have been switched to the blacklist."
        fi

        # Add to the blacklist
        jq --arg player "$player" --arg ip "$ip" '.blacklisted[$player] = $ip' db.json > temp.json && mv temp.json db.json
        echo "Successfully blacklisted $player with IP: $ip"

    else
        echo "Invalid input. Please try again!"
        main
    fi
}

showlist() {
    local all={$1}
}

main