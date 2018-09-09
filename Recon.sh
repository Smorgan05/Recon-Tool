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

# Whois Domain lookup
Whois (){
	FileName=$2"Whois.txt"
	whois $1 > $FileName
}

# NSLookup of Domain
NSlookup (){
	FileName=$2"NSLookup.txt"
	nslookup $1 > $FileName
}

# Wayback of Domain
WayBack (){
	FileName=$2"WayBack.txt"
	printf -v Command 'use auxiliary/scanner/http/enum_wayback; \nset domain '$1'; \nrun; \nexit'
	$Result=$(msfconsole -x "$Command")
	Filter=$(echo "$Test" | sed 1,28d)
	echo "$Filter" > $FileName

	#Test=$(echo "${Filter:112:19}") # Get the Located Portion
	# if [ "$Test"!="Located 0 addresses" ];	
}

# Harvest the Emails
TheHarvester (){
	FileName=$2"Harvester"
	theharvester -d $1 -l 500 -b google > $FileName
}

# Main Function
URLTest () {
	result=$(curl -Is $1 | head -n 1)
	if [ "$result"=="HTTP/1.1 200 OK" ];
	then
		echo "Website is working"
		#Whois $1 $2
		#NSlookup $1 $2
		WayBack $1 $2
		#TheHarvester $1 $2
	else
		echo "Website is dead"
	fi
}

# URLTest Website CodeName
URLTest $1 $2

