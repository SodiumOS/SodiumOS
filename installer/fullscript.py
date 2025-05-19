import os
print("Welcome to the Sodium OS Installer!")
disk = ""
lock = True
os.system("clear")
while lock:
    print("INSTALLATION CONFIG (1/4)")
    print("Here, you must specify what disk you are actually installing the OS onto. This is a very important step as if you were to pick the incorrect option, you could cause damage to the system.")
    disk = input("Enter disk (/dev/XXX): ")
    if os.path.exists(disk):
        print("Sanity Check Passed!")
        confirmation = input("Are you sure you want to use this disk? (Y/N)")
        if confirmation == "Y":
            lock = False
    else:
        os.system("clear")
        print("Disk does not exist, enter a new one!")
lock = True
swap = 4
os.system("clear")
while lock:
    print("SWAPFILE CONFIGURATION (2/4)")
    print("To those unfamiliar, swap is virtual memory that the kernel can fall back on in cases where it is needed.")
    print("SodiumOS reccomends having at least 1 gigabyte of swap, just in case.")
    swap = input("Enter swap size (in gigs): ")
    if swap.isdigit():
        if float(swap).is_integer():
            swap = int(swap) * 1024
            lock = False
        else:
            os.system("clear")
            print("Is not an integer!")
    else:
        os.system("clear")
        print("Is not a number!")
lock = True
username = ""
password = ""
while lock:
    print("USER CONFIGURATION")
    print("This will take you through the process of making your Administrator user (i.e. a user that can run sudo.)")
    username = input("Create username: ")
    password = input("Create password: ")
    confirm = input("Confirm password: ")
    if password == confirm:
        lock = False

os.system("clear")
os.system("./parting.sh " + disk)
os.system("clear")
os.system("./mounting.sh " + disk)
os.system("clear")
os.system("./swapmake.sh " + str(swap))
os.system("clear")
os.system("./arch-install.sh")
os.system("clear")
os.system("./userconf.sh " + username + " " + password)
os.system("clear")
os.system("./finalize.sh")
print("Your installation has completed! Press Enter to continue!")
input()
