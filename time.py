from datetime import datetime
import os

#!/usr/bin/python
 
import time
 
now = time.strftime("%c")
## date and time representation
print "Current date & time " + time.strftime("%c")
 
## Only date representation
print "Current date "  + time.strftime("%x")
 
## Only time representation
print "Current time " + time.strftime("%X")
 
## Display current date and time from now variable 
print ("Current time %s"  % now )
print "############################################################"
import tweepy
import datetime
import time
endDate =   datetime.datetime(2015, 1, 1, 0, 0, 0)
yes = "yessssssssssssssssss"
hello = "helloooooooooooo"
f = open('myfile.txt','w')
f.write(str(5) +'\t'+ str(endDate)+'\t' +str(yes) +'\t' +str(hello)) # python will convert \n to os.linesep
f.close()