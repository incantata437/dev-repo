#!/usr/bin/python3
import os
import sys
import subprocess 
import time

#user1 = hwick@demo.local : Helen Wick
#user2 = jwick@demo.local : John Wick
#user3 = byaga@demo.local : Baba Yaga
#user4 = patreides@demo.local : Paul Atreides
#local ip = 192.168.1.15
#SMB test variables  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Missing the SMB server IP!!!!!!!!!!!!!!!!!!!!!
data_dir = "/usr/local/testdata3/"
mountcmd = ["mount", 
            "-t cifs", 
            #add actual network cifs share here
            "-o username=byaga@demo.local,password=Password123!",
            "//192.168.1.22/ifs/home/DEMO/byaga/",
            "/mnt/byaga"]
targetdir = "/mnt/byaga"

##variables to mount the user1 share as hwick
hwick_data_dir = "/usr/local/testdata1/"
hwick_targetdir = "/mnt/hwick"
hwick_mountcmd = ["mount", "-t nfs", 
                "-O username=hwick,password=Password123!", 
                "192.168.1.22:/ifs/home/DEMO/hwick", 
                "/mnt/hwick"]

##variables to mount the user2 share as jwick
jwick_data_dir = "/usr/local/testdata2/"
jwick_targetdir = "/mnt/jwick"

jwick_mountcmd = ["mount", "-t nfs", 
                "-O username=jwick,password=Password123!", 
                "192.168.1.22:/ifs/home/DEMO/jwick", 
                "/mnt/jwick"]
#begin test loop
for x in range (20):   #  <<<<-------


##smb user
##Begin writing smb user test data group
##lots of small files ending with the extension .fle
#copy data folder from host to Isilon
    os.chdir(data_dir)
    subprocess.check_output(mountcmd)
    for filename in os.listdir(data_dir):
        subprocess.check_output("cp", filename, targetdir) 
        time.sleep(5)
    continue

##user1
# # large files should be placed on the Isilon home dir folder for hwick for this test
#copy data folder from host to Isilon
    os.chdir(hwick_data_dir)
    subprocess.check_output(hwick_mountcmd)
    for filename in os.listdir(hwick_targetdir):
        subprocess.check_output("cp", hwick_targetdir + "/" + filename, hwick_data_dir) 
#        time.sleep(20)
    continue


##user2
# # many small files should be placed on the local folder for hwick for this test
#copy data folder from host to Isilon
    os.chdir(jwick_data_dir)
    subprocess.check_output(jwick_mountcmd)
    for filename in os.listdir(jwick_targetdir):
        subprocess.check_output("cp", jwick_targetdir + "/" + filename, hwick_data_dir) 
        time.sleep(2)
    continue



#remove SMB data to start over
#close SMB share
    os.chdir(targetdir)
    subprocess.check_output(["rm", "*.fle"])
    subprocess.check_output(["umount", "/mnt/byaga"])

##user1 
##Delete target data on Isilon
    os.chdir(hwick_data_dir)
    subprocess.check_output(["rm", "*.fle"])
    subprocess.check_output(["umount", "/mnt/hwick"])

    
##user2 
#remove locale large file
    os.chdir(jwick_data_dir)
    subprocess.check_output(["rm", "*.fle"])
    subprocess.check_output(["umount", "/mnt/jwick"])

exit(0)
