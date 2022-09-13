from os import system, popen
import functions as fn

def heading():
	rows, columns = popen('stty size', 'r').read().split()
	terminalwidth = int(columns)
	system('clear')
	print("-"*terminalwidth)
	print(" "*int((terminalwidth - 10)/2) + "Linux Menu" + " "*int((terminalwidth - 10)/2))
	print("-"*terminalwidth)
	print()
	return terminalwidth

def basicmenu():
	while True:
		tw = heading()
		spclnth=int((tw-36)/3)
		print(" "*spclnth + " 1: Date          " + " "*spclnth + " 5: Make New Dir  " + " "*spclnth)
		print(" "*spclnth + " 2: Calendar      " + " "*spclnth + " 6: Del File/Dir  " + " "*spclnth)  
		print(" "*spclnth + " 3: Network Cards " + " "*spclnth + " 7: Read File     " + " "*spclnth)
		print(" "*spclnth + " 4: List Directory" + " "*spclnth + " 8: New/Edit File " + " "*spclnth)
		print(" "*spclnth + " 9: Back          " + " "*spclnth)
		print()
		choice = str(input("Enter Choice: ")).lower()
		print()
		if choice == '1':
			system('date') 
			print()
		elif choice == '2':
			system("cal") 
			print()
		elif choice == '3':
			system("ifconfig")
			print()
		elif choice == '4':
			fn.listdir()
		elif choice == '5':
			fn.makenewdir()
		elif choice == '6':
			fn.delfile()
		elif choice == '7':
			fn.readfile()
		elif choice == '8':
			fn.createfile()
		elif choice.lower() in ['9','b','back', 'q', 'quit', 'exit']:
			return "To Main Menu"
		else:
			print("Enter Valid Input...")
		print()
		input("Press Enter... ")
		system('clear')

def lvm():
	while True:
		tw = heading()
		spclnth=int((tw-36)/3)
		print(" "*spclnth + " 1: List PVs      " + " "*spclnth + " 9: Move PV       " + " "*spclnth)
		print(" "*spclnth + " 2: List VGs      " + " "*spclnth + "10: Remove PV     " + " "*spclnth)  
		print(" "*spclnth + " 3: List LVs      " + " "*spclnth + "11: Extend VG     " + " "*spclnth)
		print(" "*spclnth + " 4: Create PV     " + " "*spclnth + "12: Reduce VG     " + " "*spclnth)
		print(" "*spclnth + " 5: Create VG     " + " "*spclnth + "13: Remove VG     " + " "*spclnth)
		print(" "*spclnth + " 6: Create LV     " + " "*spclnth + "14: Extend LV     " + " "*spclnth)
		print(" "*spclnth + " 7: Format Disk   " + " "*spclnth + "15: Reduce LV     " + " "*spclnth)
		print(" "*spclnth + " 8: Mount/Unmount " + " "*spclnth + "16: Remove LV     " + " "*spclnth)
		print(" "*spclnth + "                  " + " "*spclnth + "17: Back          " + " "*spclnth)
		print()
		choice = str(input("Enter Choice: ")).lower()
		print()
		if choice == '1':
			system("pvdisplay")
		elif choice=='2':
			system("vgdisplay")
		elif choice=='3':
			system("lvdisplay")
		elif choice=='4':
			fn.createPV()
		elif choice=='5':
			fn.createVG()
		elif choice=='6':
			fn.createLV()
		elif choice=='7':
			fn.formatDisk()
		elif choice=='8':
			fn.mountUmountDisk()
		elif choice=='9':
			fn.movePV()
		elif choice=='10':
			fn.removePV()
		elif choice=='11':
			fn.extendVG()
		elif choice=='12':
			fn.reduceVG()
		elif choice=='13':
			fn.removeVG()
		elif choice=='14':
			fn.extendLV()
		elif choice=='15':
			fn.reduceLV()
		elif choice=='16':
			fn.removeLV()
		elif choice in ['17','b', 'back']:
			return "To Main Menu"
		else:
			print("Enter Valid Input...")
		print()
		input("Press Enter... ")
		system('clear')

def dockercontainer():
	while True:
		tw = heading()
		spclnth=int((tw-36)/3)
		print(" "*spclnth + " 1: List Container" + " "*spclnth + " 6: Exec Container" + " "*spclnth)
		print(" "*spclnth + " 2: Run Container " + " "*spclnth + " 7: Attach        " + " "*spclnth)  
		print(" "*spclnth + " 3: Re/Start/Stop " + " "*spclnth + " 8: Exchange Files" + " "*spclnth)
		print(" "*spclnth + " 4: Inspect/Logs  " + " "*spclnth + " 9: Commit        " + " "*spclnth)
		print(" "*spclnth + " 5: Remove        " + " "*spclnth + "10: Back          " + " "*spclnth)
		print()
		choice = str(input("Enter Choice: ")).lower()
		print()
		if choice == '1':
			fn.dkrlistcont()
		elif choice == '2':
			fn.dkrruncont()
		elif choice == '3':
			fn.dkrrestartopcont()
		elif choice == '4':
			fn.dkrinspectlogs()
		elif choice == '5':
			fn.dkrrmcont()
		elif choice == '6':
			fn.dkrexeccont()
		elif choice == '7':
			fn.dkrattachcont()
		elif choice == '8':
			fn.dkrcopycont()
		elif choice == '9':
			fn.dkrcommitcont()
		elif choice.lower() in ['10','b','back', 'q', 'quit', 'exit']:
			return "To Docker Menu"
		else:
			print("Enter Valid Input...")
		print()
		input("Press Enter... ")
		system('clear')

def docker():
	while True:
		tw = heading()
		spclnth=int((tw-36)/3)
		print(" "*spclnth + " 1: Container     " + " "*spclnth + " 4: Network       " + " "*spclnth)
		print(" "*spclnth + " 2: Images        " + " "*spclnth + " 5: Volume        " + " "*spclnth)  
		print(" "*spclnth + " 3: System Prune  " + " "*spclnth + " 6: Back          " + " "*spclnth)
		print()
		choice = str(input("Enter Choice: ")).lower()
		print()
		if choice == '1':
			dockercontainer()
		elif choice == '2':
			fn.dockerimages()
		elif choice == '3':
			fn.dockerprune()
		elif choice == '4':
			fn.dockernetwork()
		elif choice == '5':
			fn.dockervolumes()
		elif choice.lower() in ['6','b','back', 'q', 'quit', 'exit']:
			return "To Main Menu"
		else:
			print("Enter Valid Input...")
		print()
		input("Press Enter... ")
		system('clear')
