#!/usr/bin/python
import os
import subprocess

subprocess.check_output(["mkdir", "/mnt/ssd"])
subprocess.check_output(["mkdir", "/mnt/NFSisix"])
subprocess.check_output(["mkdir", "/mnt/NFSisiz"])
subprocess.check_output(["mkdir", "/mnt/NFScascades"])
subprocess.check_output(["mkdir", "/mnt/SMBremote"])
subprocess.check_output(["mkdir", "/mnt/isiSMBdata"])

#Object
# 
ECS_label = "[ecsaccess]"
ECS_access = "aws_access_key_id=mkv1"
ECS_pwd = "aws_secret_access_key=zfmqrEF/3VoQ6l7JBcdJ8ccswnjBvdjAb6yF7ZFZ"

os.chdir("/opt/dataiq/aws")

f = open("credentials", 'a')
f.write(ECS_label)
f.write(ECS_access)
f.write(ECS_pwd)
f.close()

os.chdir("/etc")


_isiX_mnt = "hop-isi-x.solarch.lab.emc.com:/ifs     /mnt/NFSisix     nfs     defaults 0  0"
_isiZ_mnt = "hop-isi-z.solarch.lab.emc.com:/ISOs    /mnt/NFSisiz     nfs     username=root,password=@llianc3  0  0"
_cascades_mnt = "10.246.26.230:/ifs/devteam         /mnt/NFScascades nfs     defaults 0  0"
#_SMBremote_mnt = "//10.246.156.183/Data"
#_isiSMB = 

#edit the fstab
fstb = open("fstab", 'a')l
fstb.write(_isiX_mnt)
fstb.write(_isiZ_mnt)
fstb.write(_cascades_mnt)
fstb.close()

subprocess.check_output(["mount", "-a"])










subprocess.check_output("mount", "-t cifs", _SMBremote_mnt, "-o username=Administrator,password=Dangerous", "/mnt/SMBremote")

