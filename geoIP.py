import argparse
from argparse import RawTextHelpFormatter
from urllib2 import urlopen
from contextlib import closing
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
print " _____           ___________  "
print "|  __ \         |_   _| ___ \ "
print "| |  \/ ___  ___  | | | |_/ / "
print "| | __ / _ \/ _ \ | | |  __/  "
print "| |_\ \  __/ (_) || |_| |     "
print " \____/\___|\___/\___/\_|     "  
print "\n"
print """** Tool to automate to geolocalize IP or domains
		 ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
		 ** DISCLAMER This tool was developed for educational goals. 
		 ** The author is not responsible for using to others goals.
		 **  A high power, carries a high responsibility!"""           
option = int (args.option)
if (option == 1):
	print ("\n\t1.Enter IP:")
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