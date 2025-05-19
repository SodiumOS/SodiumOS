import os
print("Welcome to the Sodium OS Installer!")
disk = ""
lock = True

while lock:
    disk = input("Enter disk (/dev/XXX): ")
    if os.path.exists(disk):
        print("Sanity Check Passed!")
        lock = False
    else:
        print("Disk does not exist, enter a new one!")
lock = True
swap = 4
while lock:
    swap = input("Enter swap size (in gigs): ")
    if swap.isdigit():
        if float(swap).is_integer():
            swap = int(swap) * 1024
            lock = False
        else:
            print("Is not an integer!")
    else:
        print("Is not a number!")

os.system("./parting.sh " + disk)
os.system("./mounting.sh " + disk)
os.system("./swapmake.sh " + str(swap))
