#!/usr/bin/env/python3
#Alec Loehr & Monet Salazar
#Dias 1121
#Lab8 hash.py python script

#sources:
#https://www.tutorialspoint.com/python/os_walk.htm
#https://www.tutorialspoint.com/python/os_listdir.htm
#https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
#https://nitratine.net/blog/post/how-to-hash-files-in-python/
#https://docs.python.org/3/library/datetime.htmldoc
#https://wwww.geeksforgeeks.org/writing-csv-files-in-python/
#https://www.guru99.com/python-check-if-file-exists.html#1
#https://www.realpython.com/python-csv/
#Example provided by Prof Dias-> https://github.com/BeagleD/SY402-Lab8/blob/main/hash%20(1).py


import os
import sys 
import hashlib
import datetime  
import csv

BUFFSIZE = 4096

def main():
    if os.path.exists("/tmp/hashBaseline.csv"):
        print("COMMENCING HASH AND COMPARE\n\n")
        hashCompare()
    else:
        print("COMMENCING BASELINE HASH\n\n")
        hashBaseline()

def hashBaseline():
    badDirList = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run", "/usr/share", "/usr/src", "/lib/modules"]
    with open("/tmp/hashBaseline.csv", "w") as file1:
        writer = csv.writer(file1)
        fields = ["FILENAME (FULL PATH)", "HASH", "DATE-TIME"]
        writer.writerow(fields)
        for root, dirs, files in os.walk("/", topdown = True):
            if root in badDirList:
                dirs[:] = []
                files[:] = []
            for f in files:
                filepath = os.path.join(root,f)
                sha = hashlib.sha256()
                try:
                    with open(filepath, "rb") as file2:
                        fbytes = file2.read(BUFFSIZE)
                        while len(fbytes) > 0:
                            sha.update(fbytes)
                            fbytes= file2.read(BUFFSIZE)
                except:
                    continue
                dt = datetime.datetime.now().isoformat()
                fHash = sha.hexdigest()
                row = [filepath, fHash, dt]
                writer.writerow(row)

def hashCompare():
    with open("/tmp/hashBaseline.csv", "r+") as file0:
        hashList = []
        reader = csv.reader(file0)
        for row in reader:
            hashList.append(row[1])
    badDirList = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run", "/usr/share", "/usr/src", "/lib/modules"]
    with open("/tmp/hashBaseline.csv", "w") as file1:
        updateList = []
        writer = csv.writer(file1)
        fields = ["FILENAME (FULL PATH)", "HASH", "DATE-TIME"]
        writer.writerow(fields)
        for root, dirs, files in os.walk("/", topdown = True):
            if root in badDirList:
                dirs[:] = []
                files[:] = []
            for f in files:
                filepath = os.path.join(root,f)
                sha = hashlib.sha256()
                try:
                    with open(filepath, "rb") as file2:
                        fbytes = file2.read(BUFFSIZE)
                        while len(fbytes) > 0:
                            sha.update(fbytes)
                            fbytes= file2.read(BUFFSIZE)
                except:
                    continue
                dt = datetime.datetime.now().isoformat()
                fHash = sha.hexdigest()
                row = [filepath, fHash, dt]
                if fHash not in hashList:
                    updateList.append(row)
                writer.writerow(row)
        print("To see modifactions please open /tmp/modifications.txt")
        with open("/tmp/modifcations.txt", "w+") as modFile:
            modFile.write("MODIFICATIONS WERE DETECTED WERE FOR THE FOLLIWING FILES:\n\n")
            for update in updateList:
                modFile.write("{}".format("FILNAME (FULL PATH)"))
                modFile.write("\n")
                modFile.write("{}".format("-------------------"))
                modFile.write("\n")
                modFile.write("{}".format(update[0]))
                modFile.write("\n")
                modFile.write("{:<70} {}".format("SHA256 HASH", "DATE-TIME"))
                modFile.write("\n")
                modFile.write("{:<70} {}".format("-----------", "---------"))
                modFile.write("\n")
                modFile.write("{:<70} {}".format(update[1], update[2]))
                modFile.write("\n\n\n")

if __name__ == "__main__":
    main()        