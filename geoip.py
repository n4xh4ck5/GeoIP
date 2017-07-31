#!/usr/bin/python
import argparse
from argparse import RawTextHelpFormatter
from urllib2 import urlopen
from contextlib import closing
import json
import sys
def banner():
	print """
		                               .-'''-.                                
	                               '   _    \                              
	              __.....__      /   /` '.   \ .--._________   _...._      
	  .--./)  .-''         '.   .   |     \  ' |__|\        |.'      '-.   
	 /.''\\  /     .-''"'-.  `. |   '      |  '.--. \        .'```'.    '. 
	| |  | |/     /________\   \\    \     / / |  |  \      |       \     \
	 \`-' / |                  | `.   ` ..' /  |  |   |     |        |    |
	 /("'`  \    .-------------'    '-...-'`   |  |   |      \      /    . 
	 \ '---. \    '-.____...---.               |  |   |     |\`'-.-'   .'  
	  /'""'.\ `.             .'                |__|   |     | '-....-'`    
	 ||     ||  `''-...... -'                        .'     '.             
	 \'. __//                                      '-----------'           
	  `'---'                                                               
  	"""
	print "\n"
	print """** Tool to geolocate IP's
    ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
    ** DISCLAMER This tool was developed for educational goals. 
    ** The author is not responsible for using to others goals.
    ** A high power, carries a high responsibility!
    ** Version 1.1"""

def help():
	print  """ \nThis script obtains a piece of informacion about the geolocation about a IP's

	 			Example of usage: python geoip.py -i IP """

def whoismyIP(ip):
	# Automatically geolocate the connecting IP
	url = 'http://freegeoip.net/json/'+ip
	try:
	    with closing(urlopen(url)) as response:
	        location = json.loads(response.read())
        	print "\n\t-Direction IP:", location['ip']
        	print "\n\t-Country_code:",location['country_code']
        	print "\n\t-Country name:",location['country_name']
        	print "\n\t-Region code:",location['region_code']
        	print "\n\t-Region name:",location['region_name']
        	print "\n\t-City:",location['city']
        	print "\n\t-Zip code:",location['zip_code']
        	print "\n\t-Time zone:",location['time_zone']
        	print "\n\t-Latitude:",location['latitude']
        	print "\n\t-Longitude:",location['longitude']
	except Exception as e:
		print e
		print "Don't find any information about IP in Whois"
		pass
"""MAIN"""
def main (argv):
	parser = argparse.ArgumentParser(description='This script obtains information about IPs: geolocation, ASN,...', formatter_class=RawTextHelpFormatter)
	parser.add_argument('-i','--input', help="Enter a IP or hostname.", required=False)
	parser.add_argument('-f','--file', help="Enter a file in format txt which contains IP's",required=False)
	args = parser.parse_args()
	banner()
	help()
	ip = args.input
	ip_txt=args.file
	try:
		if ip is None and ip_txt is None:
			print "Both inputs are empty"
			exit (0)
		if ip is not None:
			whoismyIP(ip)
		else:
			try:
				fd = open (ip_txt,'r')
				ip_file=fd.readline()
				while ip_file:
					print "\nIP:",ip_file
					whoismyIP(ip_file)
					#Read the next line
					ip_file=fd.readline()
				#Close the file
				fd.close()
			except Exception as e:
				print e
				pass
	except Exception as e:
		print e
		pass
	
if __name__ == "__main__":
	main(sys.argv[1:])
