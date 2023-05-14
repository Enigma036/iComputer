# Purpose: To control the installation of the program and uninstallation of the program

# Import statements
import os
import subprocess
import time
import pyautogui

class ProgramControl:
    def __init__(self):
        pass
    
    def install_crowdstrike(self):
        try:
            time.sleep(1)
            screen_width, screen_height = pyautogui.size()
            print(screen_width, screen_height)
            button1_x, button1_y = pyautogui.locateCenterOnScreen('discord.png')
            pyautogui.moveTo(button1_x, button1_y)
            pyautogui.click()
        except Exception as e:
            print(e)
            print("Cannot find discord")
        
    def install(self, path):
        if os.path.exists(path):
            os.startfile(path)
        else:
            print("Path does not exist. Cannot install.")
            
    def uninstall(self, program):
        try:
            print("Uninstalling " + program + "...")
            program_name = program
            command = 'wmic product where name="{}" call uninstall'.format(program_name)

            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            
            if "ReturnValue = 0;" in output.decode("utf-8"):
                print("Uninstalled " + program_name + " successfully.")
            elif "ReturnValue = 1603;" in output.decode("utf-8"):
                print("Error: Uninstalled " + program_name + " unsuccessfully. Error code: 1603")
        except:
            print("Cannot uninstall " + program + ". Name does not exist.")
    
    def main(self, lines):
        for line in lines:
            try:
                if line[0] == "!":
                    if line[1] == "!":
                        self.uninstall(line[2:])
                        input("Press enter to continue...")
                    else:
                        self.uninstall(line[1:])
                elif line[0] == "#":
                    if line[1] == "#":
                        self.install(line[2:])
                        input("Press enter to continue...")
                    elif line[1] == "C" and line[2] == "#":
                        #self.install(line[3:])
                        self.install_crowdstrike()
                    else:
                        self.install(line[1:])
            except:
                print("Invalid line: " + line)
    
    def __str__(self):
        return "Program Control"    
        
        
        