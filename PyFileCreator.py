import time
import os
import sys

# Variables 
reason = 'Please type the file you want to create. (Including extension)'
done = 'Done! have fun!'
after = 'This script will be closed automatically after 30 seconds.'
blankracket = ''


def naarconsole(zin):
  print("--------------------------------")
  print(zin)
  print("--------------------------------")

    

naarconsole(reason)
naarconsole(blankracket)
time.sleep(1)

input = input()
f = open(input, "w")
time.sleep(1)

naarconsole(blankracket)
naarconsole(done)
naarconsole(blankracket)
naarconsole(after)
time.sleep(30)
sys.exit()
