#!/bin/bash

# reset all ufw rules and enable it
sudo ufw --force reset
sudo ufw enable


# my dictionary (associative array whatever) with everyone's ips
declare -A ips
# --- insert associative array of ips
ips["person1"]="12.345.678.90"


# for loop silly syntax
for ip in "${ips[@]}"; do
    # also this sudo line allows each i term to connect to port 25565 with ufw    
    sudo ufw allow from "$ip" to any port 25565 proto tcp

done

# once all ips are added it'll then deny all other ips attempting to connect
sudo ufw deny 25565/tcp

# hackers can still see open port --> but denied by firewall
#    - still leaves it open to possible exploits if someone really tries -_-

# reloads all settings into effect
sudo ufw reload