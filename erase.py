#!/usr/bin/env python2
import os, time, sys
"""change the folderpath and size/day to remove, put in crontab"""
if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

def get_size(start_path = '/var/ftp/pub'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return ("ALARM" if total_size >= 100000 else "OK")

def erase_oldest():
    path = ("/var/ftp/pub")
    now = time.time()
    for f in os.listdir(path):
        print "stat on file" + f
        file_ = os.path.join(path,f)
        if os.stat(file_).st_mtime < now - 7 * 86400:
               print "Removing file" + file_
               os.remove(file_)

if get_size() == "ALARM":
    print erase_oldest()
else:
    print ("OK")
print ("Enjoy the space")
