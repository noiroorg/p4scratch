import os
import time
def Main(path):
    for file in os.listdir(path):
        print("Created: %s" % time.ctime(os.path.getctime(file)))

Main("/home/malibu/Documents")
