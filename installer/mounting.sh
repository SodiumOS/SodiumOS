echo "Sodium OS Installer First-Mounting Module [by Alexander Scott]"
DISK=$1

mount $(echo $DISK)2 /mnt
mkdir /mnt/boot
mkdir /mnt/boot/efi
mount $(echo $DISK)1 /mnt/boot/efi
