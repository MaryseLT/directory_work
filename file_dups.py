# A Python script for idenitifying duplicate file names from 2 different directories.

import os
    # A module used to explore the operating system this code is executed on.

root1 = input("Please enter the first directory: ")
    # User inputs the directory they want to check
root2 = input("Please enter the second directory: ")
    # User inputs the directory they want to check

d1 = [] # A list that will contain file names from directory 1
d2 = [] # A list that will contain file names from directory 2

for r, d, f in os.walk(root1):
    # Walk through the root, directories, & files of directory 1
    for file in f: # Loop through the files in each subdirectory
        files1 = file  # With each loop, collect the file names & extensions
        d1.append(files1)  # Add the file name & extension to the list

for r, d, f in os.walk(root2):
    for file in f:
        files2 = file
        d2.append(files2)

diff = [a for a, b in zip(d1, d2) if a == b]
    # Combine the 2 lists of file names and check for matches

if diff is True:  # If there is a match
    print(diff)  # Print the matches

else:  # If there isn't a match
    print("There are no matching file names between '{}' & '{}'.".format(root1,root2))

# from os.path import join
# import csv
# dup_paths = 'Path/To/CSV.csv'
# with open(dup_paths, 'w') as csv_writer:
#     writer = csv.writer(csv_writer)
#     writer.writerow([])
#     for row in d1:
#         writer.writerow([row])
#     for row in d2:
#         writer.writerow([row])

# dup_finder(feeds)
