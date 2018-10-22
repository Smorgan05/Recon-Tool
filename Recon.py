#!/usr/bin/python3

# Escape Character Cleaning Function
def String_Clean(multi_string):
	import re
	ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
	clean = ansi_escape.sub('', out.decode('unicode_escape'))
	return clean

# =============================
# === PASSIVE RECON SECTION ===
# =============================

# =============================
# ==== ACTIVE RECON SECTION ===
# =============================

# ===============================
# === WEBSITE MAPPING SECTION ===
# ===============================

# ==================================
# === SOCIAL ENGINEERING SECTION ===
# ==================================

# ==================================
# ===== MAIN FUNCTION SECTION ======
# ==================================

# Add the necessary libs
import argparse

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('website', action="store", type=string, required=True)
ap.add_argument('codeName', action="store", type=string, required=True)
args = parser.parse_args()

# Declare Vars
path = 'root/Desktop/' + codeName

# Main Function
def main():

	# Set / Make Directory
	import os
	if not os.path.exists(path):
		os.makedirs(path)

# Call Main
 if __name__ == '__main__':
    main()
