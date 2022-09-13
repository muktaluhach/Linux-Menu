from os import system
import menus
from functions import runcmnd, fdisk, svc, cron, webserver

def mainmenu():
	while True:
		tw = menus.heading()
		spclnth=int((tw-36)/3)
		print(" "*spclnth + " 1: Basic Commands" + " "*spclnth + " 5: Docker        " + " "*spclnth)
		print(" "*spclnth + " 2: Manage Service" + " "*spclnth + " 6: Webserver     " + " "*spclnth)  
		print(" "*spclnth + " 3: Run Commands  " + " "*spclnth + " 7: Fdisk Utility " + " "*spclnth)
		print(" "*spclnth + " 4: Crontab       " + " "*spclnth + " 8: LVM           " + " "*spclnth)
		print(" "*spclnth + " 9: Back/Exit     " + " "*spclnth)
		print()
		choice = str(input("Enter Choice: ")).lower()
		print()
		if choice == '1':
			menus.basicmenu()
		elif choice == '2':
			svc()
		elif choice == '3':
			runcmnd()
		elif choice == '4':
			cron()
		elif choice == '5':
			menus.docker()
		elif choice == '6':
			webserver()
		elif choice == '7':
			fdisk()
		elif choice == '8':
			menus.lvm()
		elif choice.lower() in ['9','b','back', 'q', 'quit', 'exit']:
			return "Exit Program"
		else:
			print("Enter Valid Input...")
		print()
		input("Press Enter... ")
		system('clear')


if __name__ == "__main__":
	system('clear')
	mainmenu()
	system('clear')
