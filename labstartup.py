#!/usr/bin/python
import os
import sys
import subprocess 
import time

#user1 = hwick@demo.local : Helen Wick
#user2 = jwick@demo.local : John Wick
#user3 = byaga@demo.local : Baba Yaga
#user4 = patreides@demo.local : Paul Atreides
#local ip = 192.168.1.15
#SMB test variables
data_dir = "/usr/local/testdata3/"
mountcmd = ["mount", 
            "-t cifs", 
            "-o username=byaga@demo.local,password=Password123!",
            "/mnt/byaga"]
targetdir = "/mnt/byaga"

##variables to mount the user1 share as hwick
hwick_data_dir = "/usr/local/testdata1/"
hwick_targetdir = "/mnt/hwick"
hwick_mntcmd = ["mount", "-t nfs", 
                "-O user=hwick,pass=Password123!", 
                "//192.168.1.22/ifs/home/DEMO/hwick", 
                "/mnt/hwick"]

##variables to mount the user2 share as jwick
jwick_data_dir = "/usr/local/testdata2/"
jwick_targetdir = "/mnt/jwick"

jwick_mntcmd = ["mount", "-t nfs", 
                "-O user=jwick,pass=Password123!", 
                "//192.168.1.22/ifs/home/DEMO/jwick", 
                "/mnt/jwick"]
#begin test loop

while loopcount < 20:


##user1
##Begin writing user1 test data group
##lots of small files
#copy data folder from host to Isilon
    os.chdir = (data_dir)
    subprocess.check_output(mountcmd)
    for filename in os.listdir(data_dir):
        subprocess.check_output("cp", filename, targetdir) 
        time.sleep(20)
    continue

##user2
##Count/wait 10  Begin reading large file back

##user1
## Begin reading back user1 2nd batch with pauses

##user3
#mount SMB share for user3
#mountcifs = "mount -t cifs -o username=byaga@demo.local,password=Password123! //192.168.1.21/ifs/home/DEMO/byaga /mnt/byaga"

os.chdir = (data_dir)
subprocess.check_output(mountcmd)



#copy data folder from host to Isilon
for filename in os.listdir(data_dir):
    subprocess.check_output("cp", filename, targetdir) 
    time.sleep(20)
    continue

#close SMB share

subprocess.check_output(["umount", "/mnt/byaga"])

##user1 
##Delete target data on Isilon

##user2 
#remove locale large file

##user3 
#remove data folder on Isilon

##repeat loop count of 10
