# Purpose: Control class
# Control class is used to control the flow of the program

import os 
from .program_control import ProgramControl
from .driver_scanner import DriverScanner
from .rename_computer import RenameComputer
from os import getlogin

class Control:
    def __init__(self):
        self._options = ("1. Driver installer", "2. Uninstall/install", "3. Rename the computer", "4. Everything", "5. Edit text file", "6. Exit", "")
        self._file_path = "Edit folder\Edit.txt"
        self._program_control = ProgramControl()
        self._computer_name = getlogin()

    # This method is used to write the menu
    def write_option(self):
        for option in self._options:
            print(option)

    # This method is used to select an option from the menu
    def select_option(self):
        while True:
            try:
                option = int(input(f"{self._computer_name}>"))
                if option == 1:
                    self._driver_scanner = DriverScanner()
                    path = self._driver_scanner.main() # "C:\\Users\\tomsn\\Documents\\GitHub\\driver-scanner\\nvidia.exe"
                    self._program_control.install_driver(self.read_file(), path)
                elif option == 2:
                    self._program_control.main(self.read_file())
                elif option == 3:
                    self._rename_computer = RenameComputer()
                    self._rename_computer.rename()
                elif option == 4:
                    # Rename the computer
                    self._rename_computer = RenameComputer()
                    self._rename_computer.rename()
                    
                    # Install the program
                    self._program_control.main(self.read_file())
                    
                    # Install drivers
                    self._driver_scanner = DriverScanner()
                    path = self._driver_scanner.main()
                    self._program_control.install_driver(self.read_file(), path)
                    
                elif option == 5:
                    self.edit_file()
                    self.read_file()
                elif option == 6:
                    exit()
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid option. Please try again.")

    def edit_file(self):
        # Open the file      
        if os.path.exists(self._file_path):
            os.startfile(self._file_path)

    def read_file(self):
        # Read the file
        if os.path.exists(self._file_path):
            lines = []
            with open(self._file_path, 'r') as file:
                for line in file.readlines():
                   lines.append(line.strip())
            return lines
        return None
    
    # This method is used to control the flow of the program
    def main(self):
        while True:
            self.write_option()
            self.select_option()

    def __str__(self):
        return 'Control class'
