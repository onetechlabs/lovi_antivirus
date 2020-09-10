#!/usr/bin/python
import re
import os
import hashlib

def scan_viruses(filename, configlocal):
	config = open(configlocal, "r").read().split('\n')
	virsigdes = config[0].split('=')
	if os.path.isdir(filename) == True:
		safedir = 0
		os.chdir(filename)
		for fileline in os.listdir(os.getcwd()):
			if os.path.isdir(fileline) == True:
				print '\033[94m' + "[Invalid Input Directories]" + '\033[0m' + " %s" % fileline
			elif os.path.exists(fileline) == True: 
				filecontent = open(fileline).read()
				for line in open(virsigdes[1]):
					virname, virsigs = line.split('=')
					virusFinalSign = virsigs.replace('\n','')
					fileCheckSumMD5 = hashlib.md5(filecontent).hexdigest()
					print(virusFinalSign)
					print(hashlib.md5(filecontent).hexdigest())
					if fileCheckSumMD5==virusFinalSign:
						print '\033[91m' + "[Infected by %s]" % virname + '\033[0m' + " %s" % fileline
						infectedsel = raw_input("What will you do with the infected file?\n[1] Remove file\n[2] Nothing\nInput Answer: ")
						if infectedsel == "1":
							os.remove(fileline)
							print "File successfully Destroyed!"
						elif infectedsel == "2":
							print "It's Save for Me"
					elif fileCheckSumMD5!=virusFinalSign:
						safedir += 1
						if safedir == 1781:
							print '\033[92m' + "[No Virus]" + '\033[0m' + " %s" % fileline 
							safedir = 0
	elif os.path.isdir(filename) == False:
		safefile = 0
		path_of_filename, filename_ext = os.path.split(filename)
		for line in open(virsigdes[1]):
			virname, virsigs = line.split('=')
			virusFinalSign = virsigs.replace('\n','')
			fileCheckSumMD5 = hashlib.md5(open(filename).read()).hexdigest()
			print(fileCheckSumMD5)
			print(virusFinalSign)
			if fileCheckSumMD5 == virusFinalSign:
				print '\033[91m' + "[Infected by "+virname+"]" + '\033[0m' + filename_ext +" "
				infectedsel = raw_input("What will you do with the infected file?\n[1] Remove file\n[2] Nothing\nInput Answer: ")
				if infectedsel == "1":
					os.remove(filename)
					print "File successfully Destroyed!"
				elif infectedsel == "2":
					print "It's Save for Me"
			elif fileCheckSumMD5 != virusFinalSign:
				safefile += 1
				if safefile == 1781:
					print '\033[92m' + "[No Virus]" + '\033[0m' + " %s" % filename_ext
			
	else:
		print '\033[94m' + "[Invalid File]" + '\033[0m' + " %s" % filename
