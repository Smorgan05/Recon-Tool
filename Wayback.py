#!/usr/bin/python3

# Declare necessary Libs
import sys

# Wayback Function
def Wayback_Enum(website, codeName):
	fileName = codeName + "Wayback.txt"

	# URL Checker Function
	def URLChecker():

		# Get URL Library
		import urllib.request

		# Get Status code (Hopefully 200)
		status = urllib.request.urlopen("http://www.stackoverflow.com").getcode()

		return status

	# Writing to File
	#f = open(fileName, "w+")
	#f.write()
	#f.close()

	


