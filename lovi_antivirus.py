#!/usr/bin/python
import libraries
import sys

configlocal = "/home/onetechlabs/Public/Programming-Projects/Desktop_Software/Python/Projects/lovi_antivirus/db/config.cfg"

while True:
	select = raw_input("Lovi Antivirus 1.0\n[1] Start Scanning\n[2] View History Scan\n[x] Quit\nInput Answer: ")
	
	if select == "1":
		filename = ""
		while filename == "":
			filename = raw_input( "Input Location Filename or Directory to Scan Viruses: " )
		libraries.scan_viruses(filename, configlocal)
		
		libraries.save_report_after_scan('write', configlocal)
		
		continue
	elif select == "2":
		libraries.save_report_after_scan('get', configlocal)
		
		continue
	elif select == "x":
		sys.exit(0)
	else:
		print "Wrong Input Answer"
		
		continue
