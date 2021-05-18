import os
from os.path import join

# Messy counting files in directory
# def messy_file_count(directory):
#     for dirpath, dirs, files in os.walk(directory):
#         filelist = []
#         for f in files:
#             filelist.append(f)
#         if len(filelist) == 0:
#             continue
#         else:
#             print("{0}: {1} Files".format(dirpath,len(filelist)))
#     return directory

#
def clean_file_count(directory):
    # iterate through all files and dir names in path
    def topDir(topFolder):
        count = 0
        #exts = ['.BAK', '.SAM', '.DOC', '.GAR', '.NTS','.LEA']
        ext = "."
        for files in os.listdir(topFolder):
            filePath = join(barcodes, files)
            if os.path.isdir(filePath):
                # if dir, recursively count files in dir
                    continue
            elif os.path.isfile(filePath):
                # if file, increment
                count += 1
            else:
                if ext in filePath:
                    print(filePath)
                    count +=1
        if count > 1:
            print("{0}: {1} Files".format(topFolder,count))
        return count

    path = 0
    for paths in os.listdir(directory):
        path +=1
        topFolder = join(directory, paths)
        topDir(topFolder)
    return path

path = r'C:\Path\On\Windows'
coll_input = input("Enter the Directory Name: ")
coll = str(coll_input)
#rcoll = "<PREFIX>"+coll #Add a directory prefix if necessary
#directory = join(path,rcoll) #If you added a directory prefix
directory = join(path,coll)
#messy_file_count(directory)
clean_file_count(directory)
