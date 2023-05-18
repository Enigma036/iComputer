# Purpose: Control class
# Control class is used to control the flow of the program

import os 
from program_control import ProgramControl
from driver_scanner import DriverScanner
from rename_computer import RenameComputer

class Control:
    def __init__(self):
        self._options = ("1. Driver scanner (+ Dowload)", "2. Uninstall/install", "3. Rename the computer", "4. Everything", "5. Edit text file", "6. Exit", "")
        self._file_path = "edit_folder\edit.txt"
        self._program_control = ProgramControl()

    # This method is used to write the menu
    def write_option(self):
        for option in self._options:
            print(option)

    # This method is used to select an option from the menu
    def select_option(self):
        while True:
            try:
                option = int(input("Keywords>"))
                if option == 1:
                    self._driver_scanner = DriverScanner()
                    self._driver_scanner.main()
                elif option == 2:
                    self._program_control.main(self.read_file())
                elif option == 3:
                    self._rename_computer = RenameComputer()
                    self._rename_computer.rename()
                elif option == 4:
                    pass
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
