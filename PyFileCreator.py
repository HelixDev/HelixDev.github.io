# Os nodig miss later altidj gebruiken in een script! (maakt respond time sneller!)
import time
import os
import sys

# Variabels
reason = 'Please type the file you want to create. (Including extension)'
done = 'Done! have fun!'
after = 'This script will be closed automatically after 30 seconds.'
processing = 'Processing Script...'
editing = 'Editing Script...'
koel = 'Script Generated by FileGen by HelixDev'


# Integer Functie
def naarconsole(zin):
  print("--------------------------------")
  print(zin)
  print("--------------------------------")


    

naarconsole(reason)
time.sleep(1)

input = input()
file = open(input, "w+")
naarconsole(processing)
file.write(koel)
file.seek(0, os.SEEK_SET)
print(file.read())


time.sleep(1)
naarconsole(editing)
time.sleep(1)
naarconsole(done)
naarconsole(after)
time.sleep(30)
sys.exit()
