import subprocess
from shlex import quote
from colorama import Fore, init

init() # Initialize colorama

class RenameComputer:
    def __init__(self):
        print(f"\n[{Fore.YELLOW}Renaming computer{Fore.RESET}]")
        print(f"Your current computer name: {Fore.YELLOW}{subprocess.check_output(['hostname']).decode('utf-8').strip()}{Fore.RESET}")
        while True:
            self._computer_name = input("Enter new computer name: ")
            if self._computer_name == "" or self._computer_name.isspace() == True:
                print("Computer name cannot be empty!")
            else:
                break
            
    def rename(self):
        try:
            if self._computer_name == "" or self._computer_name.isspace() == True:
                print("Computer name cannot be empty!")
            else:
                new_name = quote(self._computer_name)
                command = ['powershell.exe', 'Rename-Computer', '-NewName', new_name, '-Force']
                subprocess.call(command) 
            
            # Change computer name in Windows registry
            print(f"New name: {self._computer_name}")
            print(f"[{Fore.GREEN}Computer renamed successfully{Fore.RESET}]")
        except subprocess.CalledProcessError as e:
            print(f"Cannot rename computer. Error: {e}")
            print(f"[{Fore.RED}Cannot rename computer{Fore.RESET}]")

    def __str__(self):
        print("Renaming computer...")