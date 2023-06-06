import subprocess
from shlex import quote

class RenameComputer:
    def __init__(self):
        while True:
            self._computer_name = input("Enter new computer name: ")
            if self._computer_name == "" and self._computer_name.isspace() == True:
                print("Computer name cannot be empty!")
            else:
                break
            
    def rename(self):
        try:
            if self._computer_name == "" and self._computer_name.isspace() == True:
                print("Computer name cannot be empty!")
            else:
                new_name = quote(self._computer_name)
                command = ['powershell.exe', 'Rename-Computer', '-NewName', new_name, '-Force']
                subprocess.call(command) 
            
            # Change computer name in Windows registry
            print(f"New name: {self._computer_name}")
        except subprocess.CalledProcessError as e:
            print(f"Cannot rename computer. Error: {e}")

    def __str__(self):
        print("Renaming computer...")