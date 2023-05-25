# Purpose: To scan the driver

# Import libraries
import os
import urllib.request
import wmi
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from fuzzywuzzy import fuzz
from re import findall

class DriverScanner:
    def __init__(self, url="https://www.nvidia.com/Download/index.aspx?lang=en-us"):
        self._url = url
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument('--log-level=3')
        self._driver = webdriver.Chrome(options=chrome_options)
        print("Opening browser...")
        print("Please wait...")
        self._driver.get(self._url)
    
    def get_gpu_info(self):
        
        gpu_info = []
        try:
            # Connect to the WMI service
            c = wmi.WMI()

            # Query for GPU information
            gpu_devices = c.Win32_VideoController()

            for i, gpu in enumerate(gpu_devices, 1):
                gpu_name = gpu.Name

                gpu_info.append(gpu_name)
                
        except Exception as e:
            print(f"Process has failed: {str(e)}")
        
        if len(gpu_info) == 0:
            gpu_info.append("No GPU detected")
        elif len(gpu_info) > 1:
            print("Multiple GPUs detected")
            print("Please select the GPU you want to use:")
            for i, gpu in enumerate(gpu_info, 1):
                print(f"{i}: {gpu}")
            gpu_index = int(input("Enter the number of the GPU you want to use: "))
            try:
                gpu_info = [gpu_info[gpu_index - 1]]
            except Exception as e:
                print(f"Process has failed: {str(e)}")
                gpu_info = ["No GPU detected"]
                
        return gpu_info[0]

    def get_os_info(self):
        
        os_name = platform.system()
        os_version = platform.release()
        bit_version = platform.architecture()[0]
        machine_type = platform.machine()

        # Get machine type
        machine_type = platform.machine()
        # Get the node name (computer name)
        node_name = platform.node()
        # Check if the machine type or node name indicates a notebook (laptop)
        is_notebook = machine_type.lower().startswith('arm') or 'notebook' in node_name.lower() or 'laptop' in node_name.lower()
        
        return f"{os_name} {os_version} {bit_version}", is_notebook
        
    def find_matching_series(self, card_name, series_list):
        best_match = None
        best_ratio = -1
        
        for series_name in series_list:
            ratio = fuzz.ratio(card_name, series_name)

            if ratio > best_ratio:
                best_ratio = ratio
                best_match = series_name
                
        return best_match
        
    def change_combobox_value(self, combobox_id, target_text):
        combobox = Select(self._driver.find_element(By.ID, combobox_id))
        options = list(option.text for option in combobox.options)
        try:
            target_text = self.find_matching_series(target_text, options)
            combobox.select_by_visible_text(target_text)
            return target_text
        except Exception:
            return None
        
    def get_driver_info(self, source, gtype, info_success, info_error):
        info = self.change_combobox_value(gtype, source)
        if info:
            print(f"{info_success} {info}")
        else:
            print(f"{info_error}")
        
    def download_driver(self, path):
        file_url = path 
        file_path = os.path.join("C:\\", "Users", os.getlogin(), "Downloads")
        print(file_path)
        
        print(f"Downloading driver ...")
        try:
            urllib.request.urlretrieve(file_url, file_path)
        except Exception as e:
            try:
                file_path = "nvidia.exe"
                urllib.request.urlretrieve(file_url, file_path)
            except Exception as e:
                print(f"Process has failed: {str(e)}")
                return None
        
        absolute_path = os.path.abspath(file_path)

        print(f"Driver downloaded to {absolute_path}")
        
        return absolute_path
    
    def change_number(self, number):
        if len(number) == 4:
            changed_number = number[:2]
        elif len(number) == 3:
            changed_number = number[:1] + '00'
        else:
            changed_number = number
        return changed_number
    
    def get_gpu_series(self, gpu, is_notebook):
        gpu_series = gpu.replace(" (Notebooks)","")
        gpu_series = gpu_series.replace("Ti","")
        gpu_series = gpu_series.replace("SUPER","")
        
        # Find numbers in string
        numbers = findall(r'\d+', gpu_series)
        for number in numbers:
            changed_number = self.change_number(number)
            gpu_series = gpu_series.replace(number, changed_number, 1)
            
        gpu_series += "Series" 
        
        if is_notebook:
            gpu_series += " (Notebooks)"
        
        gpu_series = gpu_series.replace("GTX","")
        
        return gpu_series
                 
            
    def main(self):
        gpu = self.get_gpu_info()
        os_info, is_notebook = self.get_os_info()
        
        gpu = gpu.replace("NVIDIA","")
        print(f"\n\nGPU: {gpu}")
        
        gpuSeries = self.get_gpu_series(gpu, is_notebook)
        
        self.get_driver_info(gpu, "selProductSeriesType", "Product series type:", "Product series tyoe was not found.")
        self.get_driver_info(gpuSeries, "selProductSeries", "Product series:", "Product series was not found.")
        self.get_driver_info(gpu, "selProductFamily", "Product family:", "Product family was not found.")
        self.get_driver_info(os_info, "selOperatingSystem", "Operating system:", "Operating system was not found.")    

        for i in range(5):
            try:
                # Click on button
                button = self._driver.find_element(By.CLASS_NAME, 'btn_drvr_lnk_txt')
                button.click()
            except:
                break
            
            
        # Find element by xpath
        xpath_expression = '//a[contains(@onclick, "nvEventTracker")]'
        element = self._driver.find_element(By.XPATH, xpath_expression)

        # Get the value of the href attribute of the element
        href_value = element.get_attribute('href')

        # Download driver
        value = self.download_driver(href_value)
        
        # Close browser
        self._driver.quit()
        
        print(value)
        return value

    def __str__(self):
        return "Driver Scan"