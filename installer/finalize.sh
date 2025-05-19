cp assets/sudoers /mnt/etc/sudoers
cp assets/os-release /mnt/etc/os-release
arch-chroot /mnt grub-install --removable
arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg
