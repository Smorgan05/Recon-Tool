#!/usr/bin/python3
# Add the necessary libs
import argparse
from subprocess import check_output

# Escape Character Cleaning Function
def String_Clean(multi_string):
	import re
	ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
	clean = ansi_escape.sub('', out.decode('unicode_escape'))
	return clean

# =============================
# === PASSIVE RECON SECTION ===
# =============================

# Whois - Domain
def WhoIs(site, code):
	FileName = code + "_WhoIs.txt"
	out = check_output(["whois", site])
	result = String_Clean(out)
	return

# NSLookup - Domain
def NSLookup(site, code):
	FileName = code + "_NSLookup"
	out = check_output(["nslookup", site])
	result = String_Clean(out)
	return

# GoogleDork - Domain
def GoogleDork(site, code):
	FileName = code + "_GoogleDork.txt
	out = check_output(["atscan","--dork", site, "--level 10", "-m 2"])
	result = String_Clean(out)
	return
	
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
	return

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

website = args.website
codeName = args.codeName

# Declare Vars
path = 'root/Desktop/' + codeName

# Main Function
def main():

	# Set / Make Directory
	import os
	if not os.path.exists(path):
		os.makedirs(path)
	
	# Get URL Library
	import urllib.request
	status = urllib.request.urlopen(website).getcode()
	
	# Test Site
	if status == 200:
	
		# Passive Recon
		WhoIs(website, codeName)
		#NSLookup(website, codeName)
		#GoogleDork(website, codeName)
		
		# Active Recon
		whatweb(website, codeName)
		
	else:
		print('Website is not Online!')
	

# Call Main
 if __name__ == '__main__':
    main()
