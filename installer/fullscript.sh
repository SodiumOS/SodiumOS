echo "What disk do you wish to install this operating system on. (/dev/XXX)"
read DISK
echo "How many gigabytes of swap do you want on this system? (1G default)"
read SWAP
./parting.sh $DISK
./mounting.sh $DISK
./swapmake.sh $SWAP
