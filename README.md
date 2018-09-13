# Recon-Tool

Depending on code complexity this project may get ported to python.  At this point the game plan is to make a list of tools and see what works and go from there.

### Profile:
* Domain: Example.com
* IP Address: 192.168.11.1 (NSLookup Info)
* Operating System: Windows / Linux
* Server Host Software: IIS / Apache / Tomcat
* Server Software: IBM WebSphere, Adobe, ASP, etc (nmap -sV hostname?)
* Port List:
* Wayback Enum:

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
* Google Dorking

### Active Recon
* Nikto
* nmap enum
* Robots.txt
* dirb
* Need a way to identify the Web Server Software (ie Adobe, iis, oracle, etc)

### Exploitation
* sploitus.com
* Burpsuite

### Manual Recon
* ViewDNS.info (website)
* Pipl (website)
* Netcraft (website)
* Maltego (all-in-one)
* Sn1per (all-in-one)
* Google Analytics ID (Just to find what other sites are using the same ID)
* WAppalyzer
* pentest-tools.com (website)

### Change Log
* Add Arguments such as:
* Recon.sh -Passive
* Recon.sh -Active
* Recon.sh -All
