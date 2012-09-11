#!/usr/bin/python

import sys
sys.path.append("..")	#Add parent directoy to Include Paths

from simpleSNMP import SNMP
from time import sleep

oid = (1,3,6,1,2,1,2,2,1,16,2)


while True:

	print (SNMP.request(oid, sys.argv[1]))
	sleep(2)