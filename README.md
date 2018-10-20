# Ash Nazg - Recon Tool for Kali

Ash Nazg - Basic goal is to create a Penetratoin testing / Recon Framework so that the vulnerability scanning on a target is better and more effiecent.  This will be for single domain querying.  Also I'm tired of running the same commands over and over again.  And at the same time missing the low hanging fruit.

Depending on code complexity this project may get ported to python.  At this point the game plan is to make a list of tools and see what works and go from there.

Order of Ops: **Passive Recon** --> **Site Mapping** --> **Active Recon**  --> **Manual**--> **Exploitation**

### Legal Disclaimer
**Usage of Recon-Tool / Ash Nazg for attacking targets without prior mutal consent is illegal.  It is the end user's responsibility to obey all applicable local, state, and federal laws. Deveopers assume no liability and are not responsible for any misue or damage caused by this program.**

### Tool Usage:
./Recon.sh Domain CodeName

### Profile:
* Domain: Example.com
* IP Address: 192.168.11.1 (NSLookup Info)
* Operating System: Windows / Linux
* Server Host Software: IIS / Apache / Tomcat
* Server Software: IBM WebSphere, Adobe, ASP, WordPress, etc (nmap -sV hostname?)
* Port List:
* Target Website Map (crawler):

### Site Check
* Curl Check - HTTP/1.1 200 OK?

### Passive Recon
* Whois
* NSlookup
* **Wayback Enum** - Needs Work - Probably needs its own Terminal
* **Google Dorking:** - atscan - Probably needs its own terminal

### Site Mapping
* msfcrawler (need to add this)
* maltego
* skipfish - Probably needs its own Terminal

### Active Recon
* Nikto - Probably needs its own Terminal
* nmap (http-enum, etc)
* dirb (brute force) - Probably needs its own Terminal
* WhatWeb - ID software

#### Software Specific
* wpscan - Scans for Wordpress vulnerabilities

### Manual Recon (Research)
* ViewDNS.info (website)
* Netcraft (website)
* Sn1per (all-in-one)
* Google Analytics ID (Just to find what other sites are using the same ID)
* WAppalyzer
* pentest-tools.com (website)

### Exploitation
* sploitus.com (based on webservice)
* Burpsuite

### Social Engineering
* TheHarvester
* Pipl (website)
* Social Engineering Toolkit (SET)
