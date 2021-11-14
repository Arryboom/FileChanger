#!/usr/bin/python3

import subprocess

def delFile(file):
    process = subprocess.Popen(["shred", "-u", file])
    process.wait()

def selfDestruct():
    from sys import argv
    delFile(argv[0])
    delFile("/var/logs")
    quit()
    
def statCheck(fname, i):
    f = open("SmokingGunTimes","a+")
    stat = subprocess.Popen(["stat",fname], stdout=subprocess.PIPE)
    res = stat.communicate()[0]
    if i == 0:
        f.write("\nOld STAT\n")
    elif i ==1:
        f.write("\nNew STAT\n")
    f.write(str(res))
    f.close()
    
def changer(fname):
    i = 0
    nname =  fname + 'something_random'
    statCheck(fname,i)
    i=+1
    p1 = subprocess.Popen(["cp", fname, nname])
    p1.wait()
    delFile(fname)
    p3 = subprocess.Popen(["mv", nname, fname])
    p3.wait()
    p4 = subprocess.Popen(["touch", "-a", "-m", fname])
    statCheck(fname,i)

def useFile(file, output_file, self_destruct):
    with open(file, "r") as f:
        for line in f:
            print(line)
            changer(line)
        f.close()
    if self_destruct == True:
        delFile(file)
        delFile(output_file)
        selfDestruct()
    else:
        quit()

#################################
#         Settings              #
files_list = 'files.list'       #
output_file = 'SmokingGunTimes' #
self_destruct = False           #
#################################
if __name__ == '__main__':
    useFile(files_list, output_file, self_destruct)
