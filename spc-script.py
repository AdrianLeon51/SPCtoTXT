#Made by AdrianLeon51(github)

#This script runs with python 3.
#This script will check all *spc files in 'inputpath' and transform them to *txt in 'outputpath' inner folder.

#1) Create an empty folder into the 'inputpath' direction and place the name in 'outputpath'
#2) Run the script

import spc_spectra as spc
import os


def listFiles(path, extension):
    return [f for f in os.listdir(path) if f.endswith(extension)]

inputpath='/home/adrianl/Documents/Semester 10/Tesis Data/IFTR'
ext = '.spc'
files = listFiles(inputpath, ext)
outputpath='/Filestxt2/'


for f in files:
	d_name,d_ext=os.path.splitext(f)
	d = spc.File(str(f))
	d.data_txt()
	d.write_file(inputpath+outputpath+d_name+'.txt')
