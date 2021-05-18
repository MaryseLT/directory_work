# List all of the folders & their sizes in a directory
import os
from os.path import join

def folderSize(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        factor=1073741824 # 1 GB in Bytes
        add = 0
        total_size = 0
        for f in filenames:
            files = []
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
                files.append(total_size)
            add = sum(files)
        if add < factor:
            continue
        else:
            gb = (add / factor)
            rounded = round(gb, 1)
            print("{0}:{1}".format(dirpath, rounded))
    return total_size


path = r'C:\Path\On\Windows'
coll_input = input("Enter the Directory Name: ")
coll = str(coll_input)
#rcoll = "<PREFIX>"+coll #Add a directory prefix if necessary
#directory = join(path,rcoll) #If you added a directory prefix
directory = join(path,coll)

folderSize(directory)
