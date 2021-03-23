import os

while True:
	print('Hello! Welcome to the LVM AUTOMATION')
	print('What would you like to do?')
	print('1.Create PV')
	print('2.Create VG')
	print('3.Create LV')
	print('4.Add PV to VG')
	print('5.Resize the LV')
	print('6.Mount LV to the folder')
	print('7.EXIT')
	print("Enter your choice")
	ch=input()
	ch=int(ch)
	if ch==1:
		os.system('fdisk -l')
		print('Enter the disk name')
		disk=input()
		os.system("pvcreate {0}".format(disk))
		os.system("pvdisplay {0}".format(disk))
	if ch==2:
		os.system("pvdisplay")
		print("Enter the PV that you want to add to VG")
		PVs=input()
		VG_name=input("Enter name of VG") 
		os.system("vgcreate {0} {1}".format(VG_name,PVs))
		os.system("vgdisplay {0}".format(VG_name))
	if ch==3:
		LV_name=input("Enter the LV name:")
		os.system('vgdisplay')
		VG_name=input("Enter the VG name:")
		size=input("How much size do you want:")
		os.system("lvcreate --size {0} --name {1} {2}".format(size,LV_name,VG_name))
		os.system("mkfs.ext4 /dev/{0}/{1}".format(VG_name,LV_name))
	if ch==4:
		PV_name=input("Enter the PV name")
		VG_name=input("Enter the VG name")
		os.system("vgextend {0} {1}".format(VG_name,PV_name))
	if ch==5:
		LV_name=input("Enter the LV name")
		VG_name=input("Enter the VG name")
		size=input("Enter the size")
		os.system("lvextend --size {0} /dev/{1}/{2}".format(size,VG_name,LV_name))
	if ch==6:
		folder=input("Enter the folder name with path")
		LV_name=input("Enter the LV_name")
		os.system("mount {0} {1}".format(LV_name,folder))
	if ch==7:
		break	
	o=input("Do you want to continue(y/n):")
	#if o=="y": ch=0
	if o=="n":
		print("======GOOD BYE========")
		break
