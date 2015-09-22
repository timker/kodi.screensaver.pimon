import os
import sys
import subprocess
import re
#import xml.sax


def ensurePath():
	 binPath = '/opt/vc/bin'
	 paths = os.environ["PATH"].split(os.pathsep)
	 if binPath not in paths:
		 os.environ["PATH"] += os.pathsep + binPath     

def ensurePath2():
	 binPath = '/opt/vc/bin'
	 #p = re.compile('[a-z]+')
	 #print p.match("")
	 #os.environ["PATH"] += os.pathsep + '/opt/vc/bin'
	 paths = os.environ["PATH"].split(os.pathsep)
	 print paths
	 if binPath not in paths:
		 print "should add"
		 os.environ["PATH"] += os.pathsep + binPath
	 #split
	 #contains
	 
	 print os.environ["PATH"]
#e = xml.etree.ElementTree.parse('kodi.screensaver.pimon\addon.xml').getroot()
print ("yahoo!" if 3 > 5 else 2) 
ensurePath()
print "ghgfhg"
ensurePath()