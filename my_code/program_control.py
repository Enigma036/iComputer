# Purpose: To control the installation of the program and uninstallation of the program

# Import statements
import os
import subprocess
from time import sleep
import pyautogui
import re
from colorama import Fore, init

init() # Initialize colorama


class ProgramControl:
    def __init__(self):
        self._default_value = 60
    
    def divide(self, text, char="#"):
    
        match_hashtag = re.search(rf"{char}(.*?){char}", text)
        hashtag_text = match_hashtag.group(1) if match_hashtag else ""
        
        match_brackets = re.search(r"\[(.*?)\]", text)
        brackets_text = match_brackets.group(1) if match_brackets else ""
        
        rest_text = re.sub(r"#.*?#|\[.*?\]", "", text)

        return hashtag_text, brackets_text, rest_text
    
    def install_with_guide(self, path, time_limit, image_path):
        os.startfile(path)
        check = True
        for i in range(len(image_path)):
            check = True
            
            try:
                time = int(time_limit[i])
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
            
        if check and len(image_path) == 0:
            print("Cannot find the images.")    
            print(f"[{Fore.RED}Installation of driver was not successful{Fore.RESET}]")
        elif check:
            print("Cannot install " + path + ".") 
            print(f"[{Fore.RED}Installation of driver was not successful{Fore.RESET}]")
        else:
            print(f"[{Fore.GREEN}The installation was successful{Fore.RESET}]")
            
    def images_path(self, file_path):
        paths = []

        files = os.listdir("Photos/" + file_path)

        for file in files:
            cesta = os.path.abspath(os.path.join("Photos", file_path, file))
            if file.lower().endswith((".png", ".jpg")):
                paths.append(cesta)

        return paths

    def install(self, path):
        print(f"\n[{Fore.YELLOW}Installing program{Fore.RESET}]")
        try:
            if os.path.exists(path):
                os.startfile(path)
            else:
                print("Path does not exist. Cannot install.")
                print(f"[{Fore.RED}Installation of program was not successful{Fore.RESET}]")
        except Exception as e:
            print(f"Error: {e}")
            print(f"[{Fore.RED}Installation of program was not successful{Fore.RESET}]")
        print(f"[{Fore.GREEN}Installation of program was successful{Fore.RESET}]")
            
    def uninstall(self, program):
        try:
            print(f"\n[{Fore.YELLOW}Uninstalling program{Fore.RESET}]")
            print("Uninstalling " + program + "...")
            program_name = program
            command = f'wmic product where name="{program_name}" call uninstall /nointeractive'

            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
                    
            if "ReturnValue = 0;" in output.decode("utf-8"):
                print(f"[{Fore.GREEN}Uninstalled program successfully{Fore.RESET}]")
            elif "ReturnValue = 1603;" in output.decode("utf-8"):
                print("Error code: 1603")
                print(f"[{Fore.RED}Cannot uninstall program{Fore.RESET}]")
            elif "No Instance(s) Available." in output.decode("utf-8"):
                print("Error code: No Instance(s) Available.")
                print(f"[{Fore.RED}Cannot uninstall program{Fore.RESET}]")
        except:
            print("Name does not exist.")
            print(f"[{Fore.RED}Cannot uninstall program{Fore.RESET}]")
    
    def main(self, lines):
        for line in lines:
            try:
                if not line:
                    continue
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
                        print(f"\n[{Fore.YELLOW}Installing program{Fore.RESET}]") # Its here because of sharing the same code with install_driver
                        self.install_with_guide(file_path, time_limit, image_paths)
                    else:
                        self.install(line[1:])
            except:
                print("Invalid line: " + line)
                print(f"[{Fore.RED}Installation of program was not successful{Fore.RESET}]")
                
    def install_driver(self, lines, driver_path):
        check_file = True
        for line in lines:
            try:
                if not line:
                    continue
                if line[0] == "@":
                    check_file = False
                    hashtag_text, brackets_text, rest_text = self.divide(line, "@")
                    try:
                        if not hashtag_text or hashtag_text == "":
                            hashtag_text = "DRIVER"
                        image_paths = self.images_path(hashtag_text)
                    except:
                        print("Cannot find Photos/DRIVER folder.")
                    try:
                        time_limit = brackets_text.split(";")
                    except:
                        time_limit = None
                    self.install_with_guide(driver_path, time_limit, image_paths)
            except Exception as e:
                print("Invalid line: " + line)
                print(e)
                print(f"[{Fore.RED}Installation of driver was not successful{Fore.RESET}]")
        if check_file:
            print("Cannot find DRIVER(@) in the file.")
            print(f"[{Fore.RED}Installation of driver was not successful{Fore.RESET}]")
            
                
    def __str__(self):
        return "Program Control"    
        
        
        