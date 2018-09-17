# Recon-Tool - Ash Nazg

Recon-Tool - Basic goal is to create a Penetratoin testing / Recon Framework so that the vulnerability scanning on a target is better and more effiecent.  This will be for single domain querying.  Also I'm tired of running the same commands over and over again.  And at the same time missing the low hanging fruit.

Depending on code complexity this project may get ported to python.  At this point the game plan is to make a list of tools and see what works and go from there.

Order of Ops: **Passive Recon** --> **Site Mapping** --> **Active Recon**  --> **Manual**--> **Exploitation**

### Legal Disclaimer
**Usage of Recon-Tool / Ash Nazg for attacking targets without prior mutal consent is illegal.  It is the end user's responsibility to obey all applicable local, state, and federal laws. Deveopers assume no liability and are no responsible for any misue or damage caused by this program.**

### Profile:
* Domain: Example.com
* IP Address: 192.168.11.1 (NSLookup Info)
* Operating System: Windows / Linux
* Server Host Software: IIS / Apache / Tomcat
* Server Software: IBM WebSphere, Adobe, ASP, etc (nmap -sV hostname?)
* Port List:
* Target Website Map (crawler):

### Passive Recon
* **Website (ie google.com) says HTTP/1.1 200 OK** - PreCondition
* Whois
* NSlookup
* Wayback Enum
* Google Dorking: Recon-ng (recon/domains-hosts/google_site_web)

### Site Mapping
* msfcrawler
* maltego
* skipfish

### Active Recon
* Nikto
* nmap (http-enum, etc)
* Robots.txt: Recon-ng (discovery/info_disclosure/interesting_files) 443 / HTTPS & 80 / HTTP
* dirb (brute force)
* Need a way to identify the Web Server Software (ie Adobe, iis, oracle, etc): Wappalyzer / WhatWeb

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
