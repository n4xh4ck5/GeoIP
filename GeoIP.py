##### Geolicating the IP's ####
#!/usr/bin/python
# Written by Ignacio Brihuega Rodriguez 
import argparse
from argparse import RawTextHelpFormatter
from urllib2 import urlopen
from contextlib import closing
import json
dataIP=[]
def whoismyIP(IP):
	# Automatically geolocate the connecting IP
	url = 'http://freegeoip.net/json/'+IP
	try:
	    with closing(urlopen(url)) as response:
	        location = json.loads(response.read())
	        print(location)
	        location_city = location['city']
	        location_state = location['region_name']
	        location_country = location['country_name']
	        location_zip = location['zipcode']
	except:
		pass
	    #print("Location could not be determined automatically")
#MAIN
parser = argparse.ArgumentParser(description='This script obtains information about IPs: geolocation, ASN,...', formatter_class=RawTextHelpFormatter)
parser.add_argument('-o','--option', help="Indicate the option of input\n\t1 -Enter a IP or hostname.\n\t2 -Enter a file in format txt which contains IP's.",required=True)
args = parser.parse_args()
option = int (args.option)
if (option == 1):
	print ("\t1.Enter IP:")
	IP=raw_input()
	whoismyIP(IP)
if (option == 2):
	#Open the file
	print ("\t1.Enter the file or path where it finds:")
	path=raw_input()
	fd = open (path,'r')
	IP=fd.readline()
	while IP:
		print "\nIP",IP
		whoismyIP(IP)
		#Read the next line
		IP=fd.readline()
	#Close the file
	fd.close()