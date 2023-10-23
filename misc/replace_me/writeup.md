abootimg -x dist

gunzip initrd.gz

mkdir cpio
mv ./initrd ./cpio/
cd cpio

cpio -id < initrd

cpio/res/images/charger/battery_fail.png:
	bctf{gr33n_r0b0t_ph0N3}
