
GIGS=$1
echo "Creating $SWAP" "megabytes of swap" 
echo "Generating swapfile (This will take some time)@"
dd if=/dev/zero of=/mnt/swapfile.img bs=1K count=$GIGS status=progress
mkswap /mnt/swapfile.img
swapon /mnt/swapfile.img

