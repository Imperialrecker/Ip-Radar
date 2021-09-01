# Code written by Imperial Recker

from ip2geotools.databases.noncommercial import DbIpCity
import os

print("\n")

os.system("neofetch")

print("\n")

f = open("ascii.txt", "r")

ascii = "".join(f.readlines())

print(ascii)

print("\u001b[7mCoded and Designed by Nybble\u001b[0m")

print("\n")

ip = input("\u001b[44;1mEnter your IPv4 address : \u001b[0m")

response = DbIpCity.get(ip, api_key="free")

print("\u001b[0m\n")

print("\u001b[35;1mTarget IPv4 Entered is : \u001b[33;1m{0}".format(response.ip_address))

print("\u001b[35;1mTarget IP City is : \u001b[33;1m{0}".format(response.city))

print("\u001b[35;1mTarget IP Region is : \u001b[33;1m{0}".format(response.region))

print("\u001b[35;1mTarget IP Country is : \u001b[33;1m{0}".format(response.country))

print("\u001b[35;1mTarget IP Latitude is : \u001b[33;1m{0}".format(response.latitude))

print("\u001b[35;1mTarget IP Longitude is : \u001b[33;1m{0}".format(response.longitude))

print("\n")

print("\u001b[37;1mGoogle maps link is : \u001b[36;1mhttps://www.google.com/maps/place/" +
      "{0}".format(response.latitude)+","+"{0}".format(response.longitude))

print("\u001b[0m\n")
input("\u001b[7m\u001b[42;1mPress ENTER to exit\u001b[0m")
print("\u001b[0m\n")
