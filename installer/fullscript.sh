echo "What disk do you wish to install this operating system on. (/dev/XXX)"
read DISK
./parting.sh $DISK
./mounting.sh $DISK
