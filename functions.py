from os import system
from subprocess import getstatusoutput

def fdisk():
    print("\nFdisk Utility - \n")
    diskname = input("Enter Disk Name: ")
    print()
    system("fdisk {}".format(diskname))

def runcmnd():
    cmnd = str(input("Enter Command: "))
    print()
    system("{}".format(cmnd))

def svc():
    svc = input("\nEnter Service Name :- ")
    action = str(input("Supported Actions :- \n\t1. [Status]\n\t2. Start\n\t3. Stop\n\t4. Restart\n\t5. Enable\n\t6. Disable\n\nEnter Action :- ").lower() or "status")
    if action in ["1", "status", "check"]:
        system("systemctl status {}".format(svc))
    elif action in ["2", "start"]:
        system("systemctl start {}".format(svc))
    elif action in ["3", "stop"]:
        system("systemctl stop {}".format(svc))
    elif action in ["4", "restart"]:
        system("systemctl restart {}".format(svc))
    elif action in ["5", "enable"]:
        system("systemctl enable {}".format(svc))
    elif action in ["6", "disable"]:
        system("systemctl disable {}".format(svc))
    else:
        print("Enter Valid Action!")

def cron():
    action = str(input("Supported Actions :- \n\t1. [List]\n\t2. Edit\n\t3. Delete\n\nEnter Action :- ").lower() or "list")
    if action in ["1", "l", "list", "view"]:
        system("crontab -l")
    elif action in ["2", "e", "edit"]:
        system("crontab -e")
    elif action in ["3", "d", "delete"]:
        system("crontab -r")
    else:
        print("Enter Valid Action!")

def listdir():
    path = str(input("\nPath: "))
    system("ls {}".format(path))
    choice = str(input("\nWant to Detailed List with Hidden Files (Y/N): ")).lower()
    if choice in ['y', 'yes']:
        print()
        system("ls -al {}".format(path))

def makenewdir():
    path = str(input("\nEnter Dir Path: "))
    system("mkdir {}".format(path))

def delfile():
    while True:
        choice = str(input('\nWant to Remove Directory of File (D/F): ')).lower()
        if choice in ['f', 'file']:
            path = str(input('\nEnter File Path: '))
            system("rm -f {}".format(path))
            break
        elif choice in ['d', 'dir', 'directory']:
            path = str(input('\nEnter Directory Path: '))
            recrs = input('\nWant to br recursive if Directory not empty (Y/[N]): ').lower()
            if recrs in ['y', 'yes']:
                system("rm -drf {}".format(path))
            else:
                system("rm -df {}".format(path))
            print()
            break
        else: 
            print('Enter a Valid Choice!')

def readfile():
    path = str(input("\nEnter File Path: "))
    print()
    system("cat {}".format(path))
    print("\n\n")

def createfile():
    while True:
        choice = str(input('\nCreate a New File or Edit a File (C/E): ')).lower()
        if choice in ['e', 'edit']:
            path = str(input('\nEnter file Path: '))
            system("vim {}".format(path))
            break
        elif choice in ['c', 'create', 'new']:
            path = str(input('\nEnter file Path: '))
            system("vim {}".format(path))
            break
        else: 
            print('Enter a Valid Choice!')

def webserver():
    action = str(input("Supported Actions :- \n\t1. [Check]\n\t2. Install\n\t3. Change Port\n\nEnter Action :- ").lower() or "check")
    if action in ["1", "check"]:
        chkpkg = getstatusoutput("rpm -q httpd")
        if chkpkg[0] == 0:
            print("Package httpd is Installed\nPackage Full Name - {}".format(chkpkg[1]))
            chkpkg = getstatusoutput("systemctl status httpd")
            if chkpkg[0] == 0:
                print("Webserver Service is Running!".format(chkpkg[1]))
                print("Listening on Address:Port - {}".format(getstatusoutput("netstat -tnlp | grep httpd | awk '{ print $4 }'")[1]))
            else:
                print("\nWebserver Service Not Running!")
        else:
            print("Package httpd is Not Installed")
    elif action in ["2", "install"]:
        chkpkg = getstatusoutput("rpm -q httpd")
        if chkpkg[0] == 0:
            print("Package httpd is already installed, {}".format(chkpkg[1]))
        else:
            choice = str(input("\nInstall with Root Privilege i.e. sudo (Y/[N]): ").lower())
            if choice == "y":
                cmnd = "sudo yum install httpd -y >> /dev/null"
            else:
                cmnd = "yum install httpd -y >> /dev/null"
            system("{}".format(cmnd))
    elif action in ["3", "change", "port", "change port", "changeport"]:
        configfile = str(input("\nServer Config File Path [/etc/httpd/conf/httpd.conf]: ") or "/etc/httpd/conf/httpd.conf")
        newport = int(input("Enter New Port Number [80]: ") or "80")
        cmnd = "sed -i s/'^Listen.*'/'Listen {}'/g {}".format(newport, configfile)
        system("{}".format(cmnd))
        system("systemctl restart httpd")
    else:
        print("Enter Valid Action!")

def formatDisk():
    ft = input("Full or Resized Format (Enter F or R): ")
    if ft.lower() == 'f':
        print("\nDISK LIST - \n")
        system("lsblk -a")
        print("\nFORMAT FULL DISK - \n")
        diskname = input("Enter Disk Name: ")
        frmtType = input("Fromat Type: ")
        print()
        system("mkfs -t {} {}".format(frmtType, diskname))
    elif ft.lower() == 'r':
        print("\nDISK LIST - \n")
        system("lsblk -a")
        print("\nFORMAT RESIZED DISK - \n")
        diskname = input("Enter Disk Name: ")
        print()
        system("resize2fs {}".format(diskname))
    else:
        print("Enter F or R")
        formatDisk()

def mountUmountDisk():
    ft = input("Mount or Unmount Disk (Enter M or U): ")
    if ft.lower() == 'm':
        print("DISK LIST - \n")
        system("lsblk -a")
        print("\nMOUNT DISK - \n")
        diskname = input("Enter Disk Name: ")
        mntPath = input("Enter Mount Path: ")
        print()
        system("mount {} {}".format(diskname, mntPath))
    elif ft.lower() == 'u':
        print("DISK LIST - \n")
        system("{} lsblk -a")
        print("\nUNMOUNT DISK - \n")
        path = input("Enter Disk or Path to unmount: ")
        print()
        system("{} umount {}".format(path))
    else:
        print("Enter M or U")
        mountUmountDisk()    
    
def createPV():
    print("DISK LIST - \n")
    system("'fdisk -l | grep {}'".format("Disk /"))
    print("\nCREATE PV - \n")
    disknames = input("Enter Disk Names (Seperate by Space if multiple): ")
    print()
    system("pvcreate {}".format(disknames))
    
def createVG():
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nCREATE VG - \n")
    vgname = input("Enter VG Name: ")
    pvnames = input("Enter PV Names (Seperate by Space if multiple): ")
    print()
    system("vgcreate {} {}".format(vgname, pvnames))

def createLV():
    print("VG LIST - \n")
    system("vgdisplay -C")
    print("\nCREATE LV - \n")
    lvname = input("Enter LV Name: ")
    vgnames = input("Enter VG Name (Seperate by Space if multiple): ")
    lvsize = input("Enter LV Size: ")
    print()
    system("lvcreate --size {} --name {} {}".format(lvsize, lvname, vgnames))

def extendVG():
    print("VG LIST - \n")
    system("vgdisplay -C")
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nREDUCE VG - \n")
    vgname = input("Name of VG to Extend: ")
    pvname = input("Enter PV Name to Add: ")
    print()
    system("vgextend {} {}".format(vgname, pvname))

def reduceVG():
    print("VG LIST - \n")
    system("vgdisplay -C")
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nREDUCE VG - \n")
    vgname = input("Name of VG to Reduce: ")
    pvname = input("Enter PV Name to Remove: ")
    print()
    system("vgreduce {} {}".format(vgname, pvname))
    
def extendLV():
    print("LV LIST - \n")
    system("lvdisplay -C")
    print("\nEXTEND LV - \n")
    lvname = input("Enter LV Name: ")
    size = input("Enter Size to Extend (nM = nMB): ")
    print()
    system("lvextend -L+{} {}".format(size,lvname))

def reduceLV():
    print("LV LIST - \n")
    system("lvdisplay -C")
    print("\nEXTEND LV - \n")
    lvname = input("Enter LV Name: ")
    size = input("Enter Size to Reduce (nM = nMB): ")
    print()
    system("lvreduce -L-{} {}".format(size, lvname))

def movePV():
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nMOVE PV - \n")
    ldpv = input("Enter Old PV Name: ")
    newpv = input("Enter New PV Name: ")
    print()
    system("pvmove {} {}".format(ldpv,newpv))
    
def removePV():
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nREMOVE PV - \n")
    pvname = input("Enter PV Name: ")
    print()
    system("pvremove {}".format(pvname))

def removeVG():
    print("VG LIST - \n")
    system("vgdisplay -C")
    print("\nREMOVE VG - \n")
    vgname = input("Enter VG Name: ")
    print()
    system("vgremove {}".format(vgname))

def removeLV():
    print("LV LIST - \n")
    system("lvdisplay -C")
    print("\nREMOVE LV - \n")
    lvname = input("Enter LV Name: ")
    print()
    system("lvremove {}".format(lvname))

def dockerimages():
    action = str(input("Supported Actions :- \n\t1. [List]\n\t2. Inspect\n\t3. Pull\n\t4. Tag\n\t5. Remove\n\nEnter Action :- ").lower() or "list")
    if action in ["1", "l", "list", "view"]:
        system("docker image ls")
        print()
    elif action in ["2", "i", "inspect"]:
        names = str(input("Enter Image Name: "))
        print()
        system("docker image inspect {}".format(names))
    elif action in ["3", "p", "pull"]:
        name = str(input("Enter Image name: "))
        system("docker image pull {}".format(name))
    elif action in ["4", "t", "tag"]:
        src = str(input("Enter Source Image name: "))
        target = str(input("Enter Target Image name: "))
        system("docker image tag {} {}".format(src, target))
    elif action in ["5", "r", "rm", "remove"]:
        names = str(input("Enter Image Name to Remove: "))
        print()
        system("docker image rm {}".format(names))
    else:
        print("Enter Valid Action!")

def dockernetwork():
    action = str(input("Supported Actions :- \n\t1. [List]\n\t2. Inspect\n\t3. Create\n\t4. Remove\n\nEnter Action :- ").lower() or "list")
    if action in ["1", "l", "list", "view"]:
        system("docker network ls")
    elif action in ["2", "i", "inspect"]:
        names = str(input("Enter Network Name: "))
        print()
        system("docker network inspect {}".format(names))
    elif action in ["3", "c", "create"]:
        netname = str(input("Enter Network Name: "))
        driver = str(input("Driver for the network [default bridge]: ") or "")
        if driver != "": driver = "--driver {}".format(driver)
        internal = str(input("Restrict external access to the network (Y/[N]): ").lower())
        internal = "--internal" if internal in ["y", "yes"] else ""
        system("docker network create {} {} {}".format(driver, internal, netname))
    elif action in ["4", "r", "rm", "remove"]:
        names = str(input("Enter Network Name to Remove: "))
        print()
        system("docker network rm {}".format(names))
    else:
        print("Enter Valid Action!")

def dockervolumes():
    action = str(input("Supported Actions :- \n\t1. [List]\n\t2. Inspect\n\t3. Create\n\t4. Remove\n\nEnter Action :- ").lower() or "list")
    if action in ["1", "l", "list", "view"]:
        system("docker volume ls")
    elif action in ["2", "i", "inspect"]:
        names = str(input("Enter Volume Name: "))
        print()
        system("docker volume inspect {}".format(names))
    elif action in ["3", "c", "create"]:
        name = str(input("Enter Volume Name to Create: "))
        driver = str(input("Volume Driver (Press Enter for default): ") or "")
        if driver != "": driver = "--driver {}".format(driver)
        print()
        system("docker volume create {} {}".format(driver, name))
    elif action in ["4", "r", "rm", "remove"]:
        names = str(input("Enter Volume Name to Remove: "))
        force = str(input("Remove Forcefully (Y/[N]): ").lower())
        force = "--force" if force in ["y", "yes"] else ""
        print()
        system("docker volume rm {} {}".format(force, names))
    else:
        print("Enter Valid Action!")

def dockerprune():
    allprune = str(input("Remove all unused images (Y/[N]): ").lower())
    allprune = "--all" if allprune in ["y", "yes"] else ""
    volumes = str(input("Prune Volumes (Y/[N]): ").lower())
    volumes = "--volumes" if volumes in ["y", "yes"] else ""
    print()
    system("docker system prune {} {}".format(allprune, volumes))

def dkrlistcont():
    system("docker container ls")
    showall = str(input("\nShow all Containers (Y/[N]): ").lower())
    print()
    if showall in ["y", "yes"]:
        system("docker container ls -a")

def dkrruncont():
    image = str(input("Enter Image Name: ") or "")
    extraopts = str(input("Specify Options if needed (Type --help for help): ") or "")
    if extraopts in ["-h", "--help"]: 
        system("docker container run --help | sed -n '5,$p'")
        print() 
        extraopts = str(input("Specify Options if needed: ") or "")
    print()
    cmd = str(input("Command to run container with (leave empty for default): ") or "")
    system("docker container run {} {} {}".format(extraopts, image, cmd))

def dkrrestartopcont():
    choice = str(input("Want to Start/Restart/Stop container: ").lower())
    while True:
        if choice == "start":
            names = str(input("\nEnter Container Name to Start: "))
            system("docker container start {}".format(names))
            break
        elif choice in ["stop"]:
            names = str(input("\nEnter Container Name to Stop: "))
            system("docker container stop {}".format(names))
            break
        elif choice in ["restart"]:
            names = str(input("\nEnter Container Name to Restart: "))
            system("docker container restart {}".format(names))
            break
        elif choice == "":
            break
        else:
            choice = str(input("Enter valid choice (start/restart/stop): ").lower())
            print()

def dkrinspectlogs():
    choice = str(input("Want to see Logs or Inspect container: ").lower())
    while True:
        if choice in ["logs", "log", "l"]:
            name = str(input("Enter Container Name: "))
            print()
            system("docker container logs {}".format(name))
            break
        elif choice in ["inspect", "inspec", "insp", "ins", "i"]:
            names = str(input("Enter Container Name: "))
            system("docker container inspect {}".format(names))
            break
        elif choice == "":
            break
        else:
            choice = str(input("Enter valid choice (Logs/Inspect): ").lower())
            print()

def dkrrmcont():
    names = str(input("Enter Container Name to Remove: "))
    print()
    system("docker container rm {}".format(names))

def dkrexeccont():
    name = str(input("Enter Container Name: "))
    cmd = str(input("Enter Command with args: "))
    print()
    system("docker container exec {} {}".format(name, cmd))

def dkrattachcont():
    name = str(input("Enter Container Name to Attach: "))
    print()
    system("docker container attach {}".format(name))

def dkrcopycont():
    src = str(input("Enter Source: "))
    target = str(input("Enter Target: "))
    system("docker container cp {} {}".format(src, target))

def dkrcommitcont():
    contname = str(input("Enter Container Name: "))
    targetimg = str(input("Enter Target Image Name: "))
    print()
    system("docker container commit {} {}".format(contname, targetimg))
