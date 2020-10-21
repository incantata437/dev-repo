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
ECS_label = "[ecsaccess]\n"
ECS_access = "aws_access_key_id=mkv1\n"
ECS_pwd = "aws_secret_access_key=zfmqrEF/3VoQ6l7JBcdJ8ccswnjBvdjAb6yF7ZFZ\n"
GCP_label = "[gcpaccess]\n"
GCP_access = "aws_access_key_id=GOOGL3BI66SSXDDBCSVKZJ6S\n"
GCP_pwd = "aws_secret_access_key=rzFk2kz/crHk1AKtwinL0FYJeUoq5VyJNoMb2d8T\n"
OneFSS3_label = "[onefsS3access]\n"
OneFSS3_access = "aws_access_key_id=objectuser\n"
OneFSS3_pwd = "aws_secret_access_key=2G4PA2Ziy_FUgeOxAdhFpFWihHkj\n"


os.chdir("/opt/dataiq/maunkea/aws")

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

os.chdir("/etc")


_isiX_mnt = "hop-isi-x.solarch.lab.emc.com:/ifs     /mnt/NFSisix     nfs     defaults 0  0\n"
_isiZ_mnt = "hop-isi-z.solarch.lab.emc.com:/ISOs    /mnt/NFSisiz     nfs     username=root,password=@llianc3  0  0\n"
_cascades_mnt = "10.246.26.230:/ifs/devteam         /mnt/NFScascades nfs     defaults 0  0\n"
_SMBremote_mnt = "//10.246.156.183/Data"            /mnt/SMBremote   user=Administrator,password=Dangerous    defautls 0  0\n"
#_isiSMB = 

#edit the fstab
fstb = open("fstab", 'a')
fstb.write(_isiX_mnt)
fstb.write(_isiZ_mnt)
fstb.write(_cascades_mnt)
fstb.write(_SMBremote_mnt)
fstb.close()

subprocess.check_output(["mount", "-a"])










#subprocess.check_output("mount", "-t cifs", _SMBremote_mnt, "-o username=Administrator,password=Dangerous", "/mnt/SMBremote")

