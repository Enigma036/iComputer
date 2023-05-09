# Purpose: Control class
# Control class is used to control the flow of the program

import os 


class Control:
    def __init__(self):
        self._options = ("1. Driver scanner (+ Dowload)", "2. Uninstall/install", "3. Everything", "4. Edit text file", "5. Exit", "")
        self._file_path = '/edit/edit.txt'

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
                    return 1
                elif option == 2:
                    return 2
                elif option == 3:
                    self.read_file()
                elif option == 4:
                    self.edit_file()
                    self.read_file()
                elif option == 5:
                    exit()
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Invalid option. Please try again.")

    def edit_file(self):
        if os.path.exists(self._file_path):
            os.startfile(self._file_path)

    def read_file(self):
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file:
                for line in file.strip():
                    print(line)

    # This method is used to control the flow of the program
    def main(self):
        while True:
            self.write_option()
            self.select_option()

    def __str__(self):
        return 'Control class'
