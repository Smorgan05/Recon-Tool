#!/usr/bin/env sh

# Declare Functions

HttpEnum (){
	FileName = "$2 HttpEnum.txt"
	nmap –script http-enum $1 > $FileName
}


Wayback () {
	$FileName = "$2 Wayback.txt"
	$Command = "use auxiliary/scanner/http/enum_wayback;\
	set domain $1;\
	set outfile root\Desktop\'FileName';\
	run"
	msfconsole -x $Command > $FileName
}
	
NiktoFind () {
	$FileName = "$2 Nikto.txt"
	nikto -h $1 > $FileName
}

# Test URL
URLTest () {
	$result = curl -Is $1 | head -n 1
	if [$result -eq "HTTP/1.1 200 OK"]
	then
		HttpEnum $1 $2
		Wayback $1 $2
		NiktoFind $1 $2
		func4 $1 $2 # Robots / Sitemap
	else
		echo "$1 - Website is not responding!"
	fi
}

# URLTest $1 $2
# URLTest Website CodeName
