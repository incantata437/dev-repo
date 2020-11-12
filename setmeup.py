#!/usr/bin/python3
import os
import subprocess
#optional line to create /mnt/ssd if not using a separate parition already established
#subprocess.check_output(["mkdir", "/mnt/ssd"])
subprocess.check_output(["mkdir", "/mnt/NFSisix"])
subprocess.check_output(["mkdir", "/mnt/NFSisiy"])
subprocess.check_output(["mkdir", "/mnt/NFScascades"])
subprocess.check_output(["mkdir", "/mnt/SMBremote"])
subprocess.check_output(["mkdir", "/mnt/isiSMBdata"])

#Object
# 
ECS_label = "[ecsaccess]\n"
ECS_access = "aws_access_key_id={your bucket}\n"
ECS_pwd = "aws_secret_access_key={your access password}\n"

GCP_label = "[gcpaccess]\n"
GCP_access = "aws_access_key_id={google access id}\n"
GCP_pwd = "aws_secret_access_key={google password key}\n"

OneFSS3_label = "[onefsS3access]\n"
OneFSS3_access = "aws_access_key_id={your cluster account user\n"
OneFSS3_pwd = "aws_secret_access_key={cluster object password}\n"


os.chdir("/opt/dataiq/maunakea/aws")

f = open("credentials", 'a')
f.write("\n")
f.write(ECS_label)
f.write(ECS_access)
f.write(ECS_pwd)
f.write("\n")
f.write(GCP_label)
f.write(GCP_access)
f.write(GCP_pwd)
f.write("\n")
f.write(OneFSS3_label)
f.write(OneFSS3_access)
f.write(OneFSS3_pwd)

f.close()
os.chdir("/root")
fc = open(".credentials", 'w')
fc.write("username=administrator\n")
fc.write("password={your password}\n")
fc.close()


os.chdir("/etc")

#define mount statements
_isiX_mnt = "hop-isi-x.solarch.lab.emc.com:/ifs     /mnt/NFSisix     nfs     defaults 0  0\n"
_cascades_mnt = "10.246.26.230:/ifs/devteam         /mnt/NFScascades nfs     defaults 0  0\n"
_SMBremote_mnt = "//10.246.156.183/Data            /mnt/SMBremote   cifs    credentials=/root/.credentials 0  0\n"

#edit the fstab
fstb = open("fstab", 'a')
fstb.write(_isiX_mnt)
fstb.write(_cascades_mnt)
fstb.write(_SMBremote_mnt)
fstb.close()

subprocess.check_output(["mount", "-a"])
#oddball mount command because of security
subprocess.check_output("mount", "-t nfs", "-O username=root,password=@llianc3", "hop-isi-y.solarch.lab.emc.com:/ifs/data/ISOs", "/mnt/NFSisiy")

