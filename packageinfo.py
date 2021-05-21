import os
from os.path import join

def clean_count(directory):
# Calculate # of files in a barcode folder

    def topDir(barcode):
        total_size = 0 # individual sizes
        count = 0

        for files in os.listdir(barcode): # 1st level of barcodes
            filePath = join(barcode, files)
            #total_size = 0 # individual sizes

            if os.path.isdir(filePath):
                ## if dir, recursively count files in dir
                count +=topDir(filePath)

            else:  ## if file, increment
                if os.path.isfile(filePath):
                    count += 1
                    barcodefolder.append(filePath)
                    total_size += os.path.getsize(filePath)

        sizes.append(total_size)
        return count


    for paths in os.listdir(directory):
        barcode = join(directory, paths) #Barcode folder paths
        barcodefolder = [] # List of files
        sizes = [] # List of file sizes in Bytes
        add = 0

        """ No new vars above here ^ """

        topDir(barcode)
        add = sum(sizes)
        gigab = 1073741824 # 1 GB in Bytes
        megab = 1048576 # 1 MB in Bytes

        """ Calculate & Print Below """

        if add >= gigab: # Greater than or equal to 1 MB
            gb = (add / gigab)
            roundedgb = round(gb, 2)
            print("{0}: {1} Files & {2} GB".format(barcode,len(barcodefolder),roundedgb))

        elif add < gigab: # Less than 1 GB, but...
            if add >= megab: # Greater than or equal to 1 MB
                mb = (add / megab)
                roundedmb = round(mb, 2)
                print("{0}: {1} Files & {2} MB".format(barcode,len(barcodefolder),roundedmb))

        else: #Less than 1 MB
            if add < megab:
                print("{0}: {1} Files & {2} BYTES".format(barcode,len(barcodefolder),add))

    return paths

path = input("Enter the Top Directory Path: ")
clean_count(path)
