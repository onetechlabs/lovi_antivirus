#!/usr/bin/python
import time

def save_report_after_scan(which, configlocal):
                config = open(configlocal, 'r').read().split('\n')
                loglocal = config[1].split('=')
		
		if which == 'write':
			endtime = time.strftime("%b %d %Y/%H:%M:%S").split('/')
			curloglocal = open(loglocal[1], 'r').read()
			open(loglocal[1], 'w').write(curloglocal + "Last Scan at %s %s\n" % (endtime[0], endtime[1]))
		elif which == 'get':
			print open(loglocal[1], 'r').read() + "\n"
