USER=$1
PASSWORD=$2
arch-chroot /mnt useradd -m -G wheel $USER
arch-chroot /mnt usermod --password $(echo $PASSWORD | openssl passwd -1 -stdin) $USER
