import time

reason = 'Please type the file you want to create. (Including extension)'
done = 'Done! have fun!'
after = 'This script will be closed automatically after 30 seconds.'
br = ''


print(reason)
print(br)
time.sleep(1)

input = input()
f = open(input, "w")
time.sleep(1)

print(br)
print(done)
print(br)
print(after)
time.sleep(30)
