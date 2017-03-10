import covEXG
import os
from os import listdir
from os.path import isfile, join

pathname = 'Images/'
pathsave = 'Images-converted/'

filelist = [f for f in listdir(pathname) if isfile(join(pathname, f))]

for i, val in enumerate(filelist):
    print('processing file number '+str(i))
    filename = os.path.splitext(val)[0]
    fileextension = os.path.splitext(val)[1]
    covEXG.convert(pathname, filename, fileextension, pathsave)

print('Shite! I\'m done ;) ')    
