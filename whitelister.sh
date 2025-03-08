#!/bin/bash

# reset all ufw rules and enable it
#sudo ufw --force reset
#sudo ufw enable


# json_file="db.json"

# # my dictionary (associative array whatever) with everyone's ips
# declare -A ip_db
# declare -A whitelisted
# declare -A blacklisted

# # loops through each key-value pair in the JSON and populate the associative array
# # used CHATGPT for some syntax help with formatting the json content.
# while IFS="=" read -r key value; do
#     ip_db["$key"]="$value"
# done < <(jq -r 'to_entries[] | "\(.key)=\(.value)"' "$json_file")


# # for loop silly syntax
# for person in "${!ip_db[@]}"; do
#     # also this sudo line allows each i term to connect to port 25565 with ufw    
#     #sudo ufw allow from "$ip" to any port 25565 proto tcp

#     # 
#     echo "$person has been whitelisted with ip: ${ip_db[$person]}"
#     whitelisted["$ip"]="${ip_db[$person]}"
    
# done


main() {
    read -p "Enter CMD:  |  LIST (a)  |  SHOWLIST (l)  |  SEARCH (s)  |  REMOVE (r)  |: " cmd

    if [[ "$cmd" == "a" ]]; then
        read -p "Enter player name: " name
        read -p "Enter player IP: " ip
        read -p "Whitelist or Blacklist (w/b): " w_b 
        list "$name" "$ip" "$w_b"
    fi

}

list() {
    # Used chatgpt for the json syntax !!!
    local player="$1"
    local ip="$2"
    local whiteblack="$3"

    if [[ "$3" == "w"]]
        
        # sudo ufw allow from "$ip" to any port 25565 proto tcp
        
        # adds to whitelisted database
        jq --arg player "$player" --arg ip "$ip" '.whitelisted[$player] = $ip' db.json > temp.json && mv temp.json db.json
        
        # success message
        echo "Successfully whitelisted $player with IP: $ip"
    
    if [[ "$3" == "b"]]
    
        # sudo ufw deny from "$ip" to any port 25565 proto tcp
        
        # adds to blacklisted database
        jq --arg player "$player" --arg ip "$ip" '.blacklisted[$player] = $ip' db.json > temp.json && mv temp.json db.json
        
        # success message
        echo "Successfully whitelisted $player with IP: $ip"
    
    elif [[ "$3" != "w" || "$3" != "b" ]]
        echo "Try again!"
        main
}

main


# once all ips are added it'll then deny all other ips attempting to connect
#sudo ufw deny 25565/tcp

# hackers can still see open port --> but denied by firewall
#    - still leaves it open to possible exploits if someone really tries -_-

# reloads all settings into effect
#sudo ufw reload