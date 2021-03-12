



import spc_spectra as spc
import os


def listFiles(path, extension):
    return [f for f in os.listdir(path) if f.endswith(extension)]

inputpath='/home/adrianl/Documents/Semester 10/Tesis Data/IFTR'
ext = '.spc'
files = listFiles(inputpath, ext)
outputpath='/Filestxt/'

for f in files:
	d_name,d_ext=os.path.splitext(f)
	d = spc.File(str(f))
	d.data_txt()
	d.write_file(path+outputpath+d_name+'.txt')
