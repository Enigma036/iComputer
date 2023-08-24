
# iComputer
## Brief Description

*iComputer* is an application designed for easy driver discovery and installation (exclusive to NVIDIA drivers), program installation and uninstallation, and computer renaming. Users have the ability to customize their own sequences for program installation/uninstallation. This program was employed by **Keywords Studios (Dublin)** to automate the installation of drivers and programs.

## Usage

After launching the program, you will be presented with six options:
<br>
**(NOTE: ALWAYS RUN THE PROGRAM WITH ADMINISTRATIVE PRIVILEGES)**
- Driver installer
- Uninstall/install
- Rename the computer
- Everything
- Edit text file
- Exit

### Automatic Installation Workflow

Automatic installation works by setting up a sequence of steps with images, which are then searched for on the desktop and clicked on when automatic installation starts. The Photos folder is used for this purpose, where you first create a folder and name it arbitrarily (Note: the "DRIVER" folder serves as the default folder for driver installation). Then you can add pictures with the steps that the program will perform during the installation (Recommendation: Name the pictures according to the steps - 1.png, 2.png, etc.). In the text file Edit.txt you can then assign the folders with the installation steps to the commands.

### Driver Installer

The driver installation process is straightforward. Begin by opening the "Edit.txt" text document (accessible through option 5 in the main program menu). To configure driver installation, use the following command structure:
<br>
<code>@*folder name*@[*seconds to attempt finding and clicking on the designated image on-screen*]</code>
<br>
Practical command example:
<br>
<code>@DRIVER1_NEW@[500;300;500;100]</code>
<br>
Then select option 1 in the menu.
  
### Uninstall/Install 

For  program  uninstallation,  input  the  command  into  "Edit.txt":
<br>
<code>!*program name*</code>
<br>
Practical command example:
<br>
<code>!Discord</code>
<br>
If you wish the program to  not automatically proceed to the next command (e.g., subsequent uninstallation), use the command:
<br>
<code>!!Discord</code>
<br>
Program installation follows a similar process to driver installation. The command format  is  as follows:
<br>
<code>@*folder name*@[*step durations*]*path to the file you wish to install*</code>
<br>
Practical command: 
<br>
<code>#Connect#[60;60;60;60;60]C:\TomasHanak\ScreenConnect_23.2.9.8466_Release.exe
##C:\TomasHanak\ScreenConnect_23.2.9.8466_Release.exe</code>
<br>
Double # - They mean that the program will not automatically continue to the next command.

Then select option 2 in the menu.

### Rename the Computer

Select option 3 in the menu.<br>
When changing the computer's name, simply input the new name. 

### Everything

Select option 4 in the menu.<br>
The sequence begins with renaming the computer, followed by program installation and uninstallation, and concludes with driver installation. 

### Edit Text File

Select option 5 in the menu.
 You have the freedom to modify the "Edit.txt" file. 

### Exit

Select option 6 in the menu.
 Selecting this option will close the program.
