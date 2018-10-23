#!/usr/bin/python3

# Add the necessary libs
import argparse
from subprocess import check_output
from urllib.parse import urlparse

# Escape Character Cleaning Function
def String_Clean(multi_string):
	import re
	ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
	clean = ansi_escape.sub('', out.decode('unicode_escape'))
	return clean

# =============================
# === PASSIVE RECON SECTION ===
# =============================

# Whois - Domain - Replace with Nmap?
def WhoIs(site, code):
	FileName = code + "_WhoIs.txt"
	out = check_output(["whois", site])
	result = String_Clean(out)
	return result

# NSLookup - Domain
def NSLookup(site, code):
	FileName = code + "_NSLookup"
	out = check_output(["nslookup", site])
	result = String_Clean(out)
	return result

# GoogleDork - Domain
def GoogleDork(site, code):
	FileName = code + "_GoogleDork.txt"
	out = check_output(["atscan","--dork", site, "--level 10", "-m 2"])
	result = String_Clean(out)
	return result
	
# Wayback Enumeration - Domain
# Soon
	
# =============================
# ==== ACTIVE RECON SECTION ===
# =============================

# SoftwareID - WhatWeb
def SoftwareID(site, code):
	FileName = code + "_WhatWeb.txt"
	out = check_output(["whatweb", "-a 3", "www.wired.com"])
	result = String_Clean(out)
	return result

# ===============================
# === WEBSITE MAPPING SECTION ===
# ===============================

# ==================================
# === SOCIAL ENGINEERING SECTION ===
# ==================================

# ==================================
# ===== MAIN FUNCTION SECTION ======
# ==================================

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("website", action="store", type=str, help="website domain goes here")
ap.add_argument("codeName", action="store", type=str, help="codeName goes here")
args = ap.parse_args()

# Raw Input
website = args.website # https://www.wired.com/raw
codeName = args.codeName # Test

# Parsed Input
parse_object = urlparse(website)
sub_site = parse_object.netloc

# Declare Vars
path = 'root/Desktop/' + codeName

# Main Function
def main():

	# Set / Make Directory
	import os
	if not os.path.exists(path):
		os.makedirs(path)
	
	# Get URL Library
	import urllib3
	http = urllib3.PoolManager()
	status = http.request('GET', website).status
	
	# Test Site
	if status == 200:
	
		# Passive Recon
		print('Ready for Testing')
		#WhoIs(website, codeName) # wired.com
		#NSLookup(website, codeName) # www.wired.com
		#GoogleDork(website, codeName)
		#Wayback(website, codeName)
		
		# Active Recon
		#whatweb(website, codeName)
		
	else:
		print('Website is not Online!')
	

# Call Main
if __name__ == '__main__':
    main()
