#!/usr/bin/env bash

# Define Path
Path="/root/Desktop/"$2

# Make the Directory
if [ ! -d $Path ]
then
	mkdir $Path
fi

# Switch to that Directory
cd $Path

# =============================
# === PASSIVE RECON SECTION ===
# =============================

# Whois - Domain - (Passive Recon)
Whois (){
	FileName=$2"Whois.txt"
	whois $1 > $FileName
}

# NSLookup - Domain - (Passive Recon)
NSlookup (){
	FileName=$2"NSLookup.txt"
	nslookup $1 > $FileName
}

# Google Dorker - Domain - (Passive Recon)
GoogleDork (){
	FileName = $2"GoogleDork.txt"
	
}

# Wayback Enumeration - Domain - (Passive Recon)
WayBack (){

	# URL Checker Function
	# This needs to be switched over to a parallel execution
	# How many curls can we execute at once without choking the network?
	URLChecker (){
	while read -r LINE; do
		read -r REP < <(exec curl -IsS "$LINE" 2>&1)
		echo "$LINE: $REP" # Keep all items (may be useful)
	#done <<< "$list"
	done <<< "$1"
	}
	export -f URLChecker

	FileName=$2"WayBack.txt"
	printf -v Command 'use auxiliary/scanner/http/enum_wayback; \nset domain '$1'; \nrun; \nexit'
	Result=$(msfconsole -x "$Command")
	Filter=$(echo "$Result" | sed -n -e '/domain/,$p') # Cut everything after "domain"
	Test=$(echo "$Filter" | sed -n 3p) # Get the Located Portion line
	if [ $Test != *"Located 0"* ];
	then
		Store=$(echo "$Filter" | sed 1,3d | head -n -2) #Get the URL List
		
		# We could use mulitple servers to make this go faster
		Return=$(echo "$Store" | parallel -j10 -k URLChecker) # Need to test this (where j is number of parallel URL Checkers)
		Return=$(URLChecker $Store)#Parse List to get Active URLs (needs work)
		echo "$Return" > $FileName
	else
		echo "Archive is Empty." #List is Empty
	fi
}

# =============================
# ==== ACTIVE RECON SECTION ===
# =============================

# SoftwareID - WhatWeb - (Active Recon)
SoftwareID (){
	FileName=$2"WhatWeb.txt"
	whatweb -a 3 $1 > $FileName
}

# Robots Discovery - Nikto - (Active Recon)
Nikto (){
	FileName=$2"Nikto.txt"
	nikto -h $1 > $FileName
}

# Robots Discovery Alt - Recon-cli - (Active Recon)
RobotsAlt(){
	FileName=$2"RobotsAlt.txt"

}

# ===============================
# === WEBSITE MAPPING SECTION ===
# ===============================

# Webcrawler - Skipfish
Skipfish (){


}

# ==================================
# === SOCIAL ENGINEERING SECTION ===
# ==================================

# Harvest the Emails - Domain - (Social Engineering)
TheHarvester (){
	FileName=$2"Harvester"
	theharvester -d $1 -l 500 -b google > $FileName
}

# Main Function (Ash Nazg / The One Ring)
URLTest () {
	result=$(curl -Is $1 | head -n 1)
	if [ "$result"=="HTTP/1.1 200 OK" ];
	then
		echo "Website is working"
		Whois $1 $2
		NSlookup $1 $2
		WayBack $1 $2
		TheHarvester $1 $2
	else
		echo "Website is dead"
	fi
}

# URLTest Website CodeName
URLTest $1 $2

