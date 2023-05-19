# Purpose: To control the installation of the program and uninstallation of the program

# Import statements
import os
import subprocess
from time import sleep
import pyautogui
import re


class ProgramControl:
    def __init__(self):
        self._default_value = 60
    
    def divide(self, text):
    
        match_hashtag = re.search(r"#(.*?)#", text)
        hashtag_text = match_hashtag.group(1) if match_hashtag else ""
        
        match_brackets = re.search(r"\[(.*?)\]", text)
        brackets_text = match_brackets.group(1) if match_brackets else ""
        
        rest_text = re.sub(r"#.*?#|\[.*?\]", "", text)

        return hashtag_text, brackets_text, rest_text
    
    def install_with_guide(self, path, time_limit, image_path):
        os.startfile(path)
        for i in range(len(image_path)):
            check = True
            
            try:
                time = len(time_limit[i])
            except:
                time = self._default_value
                
            for y in range(time):
                sleep(1)
                button_location = pyautogui.locateCenterOnScreen(image_path[i], confidence=0.75)   
                if button_location != None:
                    button1_x, button1_y = button_location
                    pyautogui.moveTo(button1_x, button1_y)
                    pyautogui.click()
                    check = False
                    break
            if check:
                break
            
        if check:
            print("Cannot install " + path + ".") 
        else:
            print("Installed " + path + " successfully.")   
            
    def images_path(self, file_path):
        paths = []

        files = os.listdir("photos/" + file_path)

        for file in files:
            cesta = os.path.abspath(os.path.join("photos", file_path, file))
            if file.lower().endswith((".png", ".jpg")):
                paths.append(cesta)

        return paths

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
                    elif line.count("#") == 2:
                        hashtag_text, brackets_text, rest_text = self.divide(line)
                        image_paths = self.images_path(hashtag_text)
                        try:
                            time_limit = brackets_text.split(";")
                        except:
                            time_limit = None
                        file_path = rest_text
                        self.install_with_guide(file_path, time_limit, image_paths)
                    else:
                        self.install(line[1:])
            except:
                print("Invalid line: " + line)
    
    def __str__(self):
        return "Program Control"    
        
        
        