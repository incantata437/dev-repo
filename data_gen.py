#!/usr/bin/python3

import os
from faker import Faker

#Prompt for target directory for deployed data
#Prompt for number of directory depth
#Prompt for output file size
#Prompt for number of output files

fake = Faker()
Faker.seed(22)
_para = int(input("Number of sentences in paragraph of text:  "))
_numFiles = int(input("Number of files needed: "))
_begin_dir = input("Full path to start writing files: ")

os.chdir(_begin_dir)

for x in range(_numFiles):
    _filename = fake.ein() + '.txt'
    f = open(_filename, "w")
    f.writelines(fake.paragraphs(_para))
    f.close()
    
