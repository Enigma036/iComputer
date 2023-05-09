# Purpose: To control the installation of the program and uninstallation of the program

# Import statements
import os
import subprocess

class ProgramControl:
    def __init__(self):
        pass
    
    def install(self, path):
        if os.path.exists(path):
            os.startfile(path)
        else:
            print("Path does not exist. Cannot install.")
            
    def uninstall(self, program):
        try:
            os.system("wmic product where name=\"" + program + "\" call uninstall")
        except:
            print("Cannot uninstall " + program + ". Name does not exist.")
    
    def main(self, lines):
        for line in lines:
            try:
                if line[0] == "!":
                    if line[1] == "!":
                        self.uninstall(line[2:])
                        print("Press enter to continue...")
                    else:
                        self.uninstall(line[1:])
                elif line[0] == "#":
                    if line[1] == "#":
                        self.install(line[2:])
                        print("Press enter to continue...")
                    else:
                        self.install(line[1:])
            except:
                print("Invalid line: " + line)
    
    def __str__(self):
        return "Program Control"    
        
        
        