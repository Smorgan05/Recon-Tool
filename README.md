# Recon-Tool - Ash Nazg

Recon-Tool - Basic goal is to create a Penetratoin testing / Recon Framework so that the vulnerability scanning on a target is better and more effiecent.  Also I'm tired of running the same commands over and over again.

Depending on code complexity this project may get ported to python.  At this point the game plan is to make a list of tools and see what works and go from there.

Order of Ops: **Passive Recon** --> **Site Mapping** --> **Active Recon** --> **Exploitation**

### Profile:
* Domain: Example.com
* IP Address: 192.168.11.1 (NSLookup Info)
* Operating System: Windows / Linux
* Server Host Software: IIS / Apache / Tomcat
* Server Software: IBM WebSphere, Adobe, ASP, etc (nmap -sV hostname?)
* Port List:
* Target Website Map (crawler):
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

### Website Crawler
* msfcrawler
* maltego
* skipfish

### Site Mapping
* Nikto
* nmap (http-enum, etc)
* Robots.txt
* dirb
* Need a way to identify the Web Server Software (ie Adobe, iis, oracle, etc): Wappalyzer

### Exploitation
* sploitus.com (based on webservice)
* Burpsuite

### Manual Recon
* ViewDNS.info (website)
* Pipl (website)
* Netcraft (website)
* Sn1per (all-in-one)
* Google Analytics ID (Just to find what other sites are using the same ID)
* WAppalyzer
* pentest-tools.com (website)

### Change Log
* Add Arguments such as:
* Recon.sh -Passive
* Recon.sh -Active
* Recon.sh -All
