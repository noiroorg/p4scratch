#THE FOLLWING SCRIPT IS A BUILD UP ON PREVIOUS SCRIPT MODULES
# + Threading class +
#Script function Display files and their time stamps
import argparse
import os
import time
from threading import Thread


# Function to display creation time of files in a directory
def user_path(u_path, process ,delay, repeat):
    for file in os.listdir(u_path):
        print(file + " created: %s" % time.ctime(os.path.getctime(file)))
# main function
def Main():

    
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Enter the path e.g /home/malibu")
    args = parser.parse_args()
    u_path =args.path
    os.chdir(u_path)
    #print(u_path)
    t1 = Thread(target=user_path, args=(u_path, "process_1", 1, 3))
    t2 = Thread(target=user_path, args=(u_path, "process_2", 1,3))
    t1.start()
    t2.start()
   

if __name__ == "__main__":
    Main()
