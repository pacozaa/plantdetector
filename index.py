import covEX
import time
import os
from os import listdir
from os.path import isfile, join

start_time = time.time()
pathname = 'Images/'
pathsave = 'Images-converted/'

filelist = [f for f in listdir(pathname) if isfile(join(pathname, f))]

for i, val in enumerate(filelist):
    print('processing file number '+str(i))
    filename = os.path.splitext(val)[0]
    fileextension = os.path.splitext(val)[1]
    covEX.convertTofile(pathname, filename, fileextension, pathsave)

print('Shite! I\'m done ;) ')
print("--- %s seconds ---" % (time.time() - start_time))
