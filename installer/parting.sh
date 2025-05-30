
DISK=$1

echo "$DISK is being partitioned now"
# Creates a GPT partition table on the disk!
echo -e "g\nw\n" | fdisk $DISK
# Creates a 100MB partition, makes it into an EFI system partition, creates a regular Linux filesystem partition on the rest of the disk
echo -e "n\n\n\n+100M\nt\n1\nn\n\n\n\nw\n" | fdisk $DISK
mkfs.fat -F 32 $(echo "$(echo $DISK)1")
mkfs.ext4 $(echo "$(echo $DISK)2")

