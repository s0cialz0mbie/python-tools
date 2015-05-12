#!/usr/bin/python

# Originally from Pierre Lamy (FIS)
# Purpose: to scan internal network from Internet via Microsoft Direct Access
#          IPv6 to IPv4 gateway without authentication using ping6 utility

import os
import sys
import time

os.system("clear")
scan_network = "2002:c7c8:1898:8001::10.132.201."
mine = []

for i in range(1, 254):
	z =  scan_network + str(i)
	result = os.system("ping6 -c 1 "+ str(z))
	os.system("clear")
	if result == 0:
		mine.append(z)

for j in mine:
	print "host ", j ," is up"
