# Clark Otte
# Lab01 Disk imaging
# CSC 5347
# February 4, 2022
# Depending on file permissions, this program may need to be run with sudo in order to access the drive
import subprocess
import os
import shutil

if __name__ == "__main__":
    # get the list of drives on the machine excluding main drive sda
    pathList = []
    output = subprocess.check_output(["lsblk", "-d", "-n", "-o", "KNAME,TYPE,PATH"], text=True)
    for line in output.splitlines():
        name, dtype, path = line.split()
        if dtype == "disk" and name != "sda":
            pathList.append(path)

    # Print out the list of drives
    for i in range(len(pathList)):
        print('Drive[{}]: {}'.format(i, pathList[i]))

    # Get the choice of drive to copy, the destination path/filename of the copy, and the block size
    driveNo = int(input("Please enter the number of the drive you wish to copy\n"))
    srcPath = pathList[driveNo]
    destPath = input("Please enter destination path of copied file (including file name and ext) \n")
    blockSize = int(input("Please enter the read/write block size"))

    # Open the drive, and open/create the copy file, then read the bits and write them to copy
    with open(srcPath, 'rb') as rf:
        with open(destPath, 'wb') as wf:
            while True:
                if wf.write(rf.read(blockSize))==0:
                    break
    # Copy is finished
    print("Success!")
