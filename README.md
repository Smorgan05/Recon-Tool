# Recon-Tool

Depending on code complexity this project may get ported to python.  At this point the game plan is to make a list of tools and see what works and go from there.

### File List
* Recon.sh
* URLChecker.sh - Checks for valid URLs when given text file with list of URLs (this will get merged into Recon)
* Recon Logic.vsdx - Planning diagram to keep track of logic

### PreCondition
* Website (ie google.com) says HTTP/1.1 200 OK

### Passive Recon
* Whois
* NSlookup
* Wayback Enum
* TheHarvester

### Active Recon
* Nikto
* nmap enum
* Robots.txt
* Need a way to identify the Web Server Software (ie Adobe, iis, oracle, etc)

### Manual Recon
* ViewDNS.info (website)
* Pipl (website)
* Netcraft (website)
* Maltego (all-in-one)
* Sn1per (all-in-one)
* Google Analytics ID (Just to find what other sites are using the same ID)

### Change Log
* Add Arguments such as:
* Recon.sh -Passive
* Recon.sh -Active
* Recon.sh -All
