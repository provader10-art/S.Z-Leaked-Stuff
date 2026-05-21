import tkinter as tk
import subprocess
import winreg   
from tkinter import messagebox
import os
import wmi
from tkinter import *
from threading import Thread
from PIL import Image
from send2trash import send2trash
import discord
import shutil
import concurrent.futures
from tqdm import tqdm
from discord.ext import commands
from customtkinter import CTkProgressBar
import re
import requests
from PIL import Image, ImageTk
import sys
import time
from time import sleep
import urllib.request
import ctypes
from tkinter import messagebox
from tkinter import messagebox
import customtkinter as ctk
import os
import threading
import winreg  
import ctypes
import customtkinter
import webbrowser
import platform
import socket
from pymongo import MongoClient
from tkinter import messagebox
import json

data = {
    "CTk": {
        "fg_color": ["gray95", "gray10"]
    },
    "CTkToplevel": {
        "fg_color": ["gray95", "gray10"]
    },
    "CTkFrame": {
        "corner_radius": 6,
        "border_width": 0,
        "fg_color": ["gray90", "gray13"],
        "top_fg_color": ["gray85", "gray16"],
        "border_color": ["gray65", "gray28"]
    },
    "CTkButton": {
        "corner_radius": 6,
        "border_width": 0,
        "fg_color": ["#3d1985", "#3d1985"],
        "hover_color": ["#31196a", "#31196a"],
        "border_color": ["#3E454A", "#949A9F"],
        "text_color": ["#DCE4EE", "#DCE4EE"],
        "text_color_disabled": ["gray74", "gray60"]
    },
    "CTkLabel": {
        "corner_radius": 0,
        "fg_color": "transparent",
        "text_color": ["gray14", "gray84"]
    },
    "CTkEntry": {
        "corner_radius": 6,
        "border_width": 2,
        "fg_color": ["#F9F9FA", "#343638"],
        "border_color": ["#979DA2", "#565B5E"],
        "text_color": ["gray14", "gray84"],
        "placeholder_text_color": ["gray52", "gray62"]
    },
    "CTkCheckBox": {
        "corner_radius": 6,
        "border_width": 3,
        "fg_color": ["#3d1985", "#3d1985"],
        "border_color": ["#3E454A", "#949A9F"],
        "hover_color": ["#31196a", "#31196a"],
        "checkmark_color": ["#DCE4EE", "gray90"],
        "text_color": ["gray14", "gray84"],
        "text_color_disabled": ["gray60", "gray45"]
    },
    "CTkSwitch": {
        "corner_radius": 1000,
        "border_width": 3,
        "button_length": 0,
        "fg_color": ["#939BA2", "#4A4D50"],
        "progress_color": ["#3d1985", "#3d1985"],
        "button_color": ["gray36", "#D5D9DE"],
        "button_hover_color": ["gray20", "gray100"],
        "text_color": ["gray14", "gray84"],
        "text_color_disabled": ["gray60", "gray45"]
    },
    "CTkRadioButton": {
        "corner_radius": 1000,
        "border_width_checked": 6,
        "border_width_unchecked": 3,
        "fg_color": ["#3a7ebf", "#1f538d"],
        "border_color": ["#3E454A", "#949A9F"],
        "hover_color": ["#325882", "#14375e"],
        "text_color": ["gray14", "gray84"],
        "text_color_disabled": ["gray60", "gray45"]

  },
  "CTkProgressBar": {
    "corner_radius": 1000,
    "border_width": 0,
    "fg_color": ["#3d1985", "#4A4D50"],
    "progress_color": ["#3d1985", "#3d1985"],
    "border_color": ["gray", "gray"]
  },
  "CTkSlider": {
    "corner_radius": 1000,
    "button_corner_radius": 1000,
    "border_width": 6,
    "button_length": 0,
    "fg_color": ["#939BA2", "#4A4D50"],
    "progress_color": ["gray40", "#AAB0B5"],
    "button_color": ["#3a7ebf", "#1f538d"],
    "button_hover_color": ["#325882", "#14375e"]
  },
  "CTkOptionMenu": {
    "corner_radius": 6,
    "fg_color": ["#3d1985", "#3d1985"],
    "button_color": ["#979DA2", "#565B5E"],
    "button_hover_color": ["#6E7174", "#7A848D"],
    "text_color": ["#DCE4EE", "#DCE4EE"],
    "text_color_disabled": ["gray74", "gray60"]
  },
  "CTkComboBox": {
    "corner_radius": 6,
    "border_width": 2,
    "fg_color": ["#3d1985", "#3d1985"],
    "border_color": ["#979DA2", "#565B5E"],
    "button_color": ["#979DA2", "#565B5E"],
    "button_hover_color": ["#6E7174", "#7A848D"],
    "text_color": ["#DCE4EE", "gray84"],
    "text_color_disabled": ["gray50", "gray45"]
  },
  "CTkScrollbar": {
    "corner_radius": 1000,
    "border_spacing": 4,
    "fg_color": "transparent",
    "button_color": ["gray55", "gray41"],
    "button_hover_color": ["gray40", "gray53"]
  },
  "CTkSegmentedButton": {
    "corner_radius": 6,
    "border_width": 2,
    "fg_color": ["#979DA2", "gray29"],
    "selected_color": ["#3d1985", "#3d1985"],
    "selected_hover_color": ["#31196a", "#31196a"],
    "unselected_color": ["#979DA2", "gray29"],
    "unselected_hover_color": ["gray70", "gray41"],
    "text_color": ["#DCE4EE", "#DCE4EE"],
    "text_color_disabled": ["gray74", "gray60"]
  },
  "CTkTextbox": {
    "corner_radius": 6,
    "border_width": 0,
    "fg_color": ["gray100", "gray20"],
    "border_color": ["#979DA2", "#565B5E"],
    "text_color": ["gray14", "gray84"],
    "scrollbar_button_color": ["gray55", "gray41"],
    "scrollbar_button_hover_color": ["gray40", "gray53"]
  },
  "CTkScrollableFrame": {
    "label_fg_color": ["gray80", "gray21"]
  },
  "DropdownMenu": {
    "fg_color": ["gray90", "gray20"],
    "hover_color": ["gray75", "gray28"],
    "text_color": ["gray14", "gray84"]
  },
  "CTkFont": {
    "macOS": {
      "family": "SF Display",
      "size": 13,
      "weight": "normal"
    },
    "Windows": {
      "family": "Roboto",
      "size": 13,
      "weight": "normal"
    },
    "Linux": {
      "family": "Roboto",
      "size": 13,
      "weight": "normal"
    }
  }
}


# Writing data to a file
with open('C:/Program Files/AlphaWolf_Premium/Purple.json', 'w') as f:
    json.dump(data, f, indent=2)



# Define the VBS script content
vbs_script = """
Option Explicit

Dim objFSO, objFile
Dim checkboxFilePath
Dim isSelected

' Check if any command-line arguments were provided
If WScript.Arguments.Count > 0 Then
    checkboxFilePath = WScript.Arguments.Item(0)
Else
    WScript.Echo "Error: Missing argument. Please provide the path to the checkbox file."
    WScript.Quit(1)
End If

' Check if the checkbox_selected.txt file exists
Set objFSO = CreateObject("Scripting.FileSystemObject")
If objFSO.FileExists(checkboxFilePath) Then
    ' The checkbox was previously selected
    isSelected = True
Else
    ' The checkbox was not previously selected
    isSelected = False
End If

' Output the result
If isSelected Then
    ' The agreement was previously accepted
    WScript.Echo "You have!"
Else
    ' The agreement was not previously accepted
    Dim intResult
    Dim strMessage1
    Dim strMessage2
    
    ' Define the agreement message - part 1
    strMessage1 = "Warning: VorteX Usage" & vbCrLf & vbCrLf & _
                  "Attention: Before proceeding, please carefully review the following information." & vbCrLf & vbCrLf & _
                  "Using the Vortex software to optimize your system's performance can yield significant benefits, but it is crucial to understand and acknowledge the potential risks involved." & vbCrLf & vbCrLf & _
                  "To mitigate these risks and ensure a smooth experience:" & vbCrLf & vbCrLf & _
                  "1. Exercise caution: When making adjustments with Vortex, proceed with caution. Make changes incrementally and observe their effects on your system's performance before proceeding further." & vbCrLf & vbCrLf & _
                  "2. Create a system restore point: Before implementing any changes, it is highly recommended to create a system restore point. This allows you to revert your system back to its previous state in the event of any unexpected issues or undesired outcomes." & vbCrLf & vbCrLf & _
                  "3. Backup important data: Prior to making significant modifications to your system, ensure that you have backed up all essential data and files. This precautionary measure helps safeguard against potential data loss or corruption."
    
    ' Define the agreement message - part 2
    strMessage2 = strMessage1 & vbCrLf & vbCrLf & _
                  "Do you accept the terms and conditions?"
    
    ' Display the agreement message
    intResult = MsgBox(strMessage2, vbOKCancel + vbExclamation, "VorteX Warning")
    
    ' If the user clicks OK, display the second part of the message
    If intResult = vbOK Then
        intResult = MsgBox("Do you accept the terms and conditions?", vbYesNo + vbExclamation, "VorteX Warning")
        ' Check the user's choice
        If intResult = vbYes Then
            ' User accepted the agreement
            ' Create a file to indicate acceptance
            On Error Resume Next
            Set objFile = objFSO.CreateTextFile(checkboxFilePath, True)
            If Err.Number <> 0 Then
                WScript.Echo "Error creating checkbox file:", Err.Description
            Else
                objFile.Close
                WScript.Echo "true"
            End If
            On Error GoTo 0
        Else
            ' User declined the agreement
            WScript.Echo "false"
        End If
    Else
        ' User clicked Cancel
        WScript.Echo "false"
    End If
End If
"""



def check_uac_status():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System")

        values_to_check = {
            "EnableLUA": 0,
            "ConsentPromptBehaviorAdmin": 0,
            "PromptOnSecureDesktop": 0,
            "EnableSecureUIAPaths": 0
        }

        for value_name, expected_value in values_to_check.items():
            value, _ = winreg.QueryValueEx(key, value_name)
            if value != expected_value:
                return False
        return True

    except FileNotFoundError:
        return False

if __name__ == "__main__":
    if check_uac_status():
        print("UAC fully disabled")
        messagebox.showinfo("UAC Checker", "UAC Fully Disabled. Good Job! You can proceed :)")

    else:
        print("UAC not fully disabled")
        messagebox.showerror("UAC Checker", "UAC Not Fully Disabled! :( Run the file given in the Pack")


# Write the VBS script to the file
file_path = r"C:\Program Files\AlphaWolf_Premium\popup.vbs"
with open(file_path, "w") as f:
    f.write(vbs_script)

print(f"VBS script has been written to: {file_path}")


# URLs and local paths
image_url = "https://github.com/mosol1/WindowsPowershell/raw/main/Vortex.ico"
local_path = "C:/Program Files/AlphaWolf_Premium/vortex.ico"

# Download the image using requests
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Write the binary content to the local file
    with open(local_path, "wb") as f:
        f.write(response.content)
    print(f"Image downloaded and saved to {local_path}")
else:
    print(f"Failed to download the image. Status code: {response.status_code}")

# Download Discord.png

# URLs and local paths
github_url_vortex = "https://github.com/mosol1/WindowsPowershell/raw/main/vortexlogo.png"
local_path_vortex = "C:/Program Files/AlphaWolf_Premium/vortexlogo.png"

response_vortex = requests.get(github_url_vortex)
if response_vortex.status_code == 200:
    with open(local_path_vortex, "wb") as f:
        f.write(response_vortex.content)
    print(f"vortexlogo.png downloaded and saved to {local_path_vortex}")
else:
    print(f"Failed to download vortexlogo.png. Status code: {response_vortex.status_code}")



# URLs and local paths
github_url_fortnite = "https://github.com/mosol1/WindowsPowershell/raw/main/fortnite.png"
local_path_fortnite = "C:/Program Files/AlphaWolf_Premium/fortnite.png"

response_fortnite = requests.get(github_url_fortnite)
if response_fortnite.status_code == 200:
    with open(local_path_fortnite, "wb") as f:
        f.write(response_fortnite.content)
    print(f"fortnite.png downloaded and saved to {local_path_fortnite}")
else:
    print(f"Failed to download fortnite.png. Status code: {response_fortnite.status_code}")


github_url_discord = "https://github.com/mosol1/WindowsPowershell/raw/main/Discord.png"
local_path_discord = "C:/Program Files/AlphaWolf_Premium/Discord.png"

# Make the GET request to download the image
response_discord = requests.get(github_url_discord)
if response_discord.status_code == 200:
    # Save the image content to the specified local path
    with open(local_path_discord, "wb") as f:
        f.write(response_discord.content)
    print(f"discord.png downloaded and saved to {local_path_discord}")
else:
    print(f"Failed to download discord.png. Status code: {response_discord.status_code}")





with open('C:/Program Files/AlphaWolf_Premium/Purple.json', 'w') as f:
    json.dump(data, f, indent=2)

ctk.set_appearance_mode("dark")
customtkinter.set_default_color_theme('C:/Program Files/AlphaWolf_Premium/Purple.json')

app = ctk.CTk()
app.geometry("400x450")
app.title("AlphaWolf Premium")
app.iconbitmap('C:/Program Files/AlphaWolf_Premium/Vortex.ico')  # Set the icon path here

file_path = "C:/Program Files/AlphaWolf_Premium/Discord.png"  # Assuming this is the correct path to your image file
discord_image = customtkinter.CTkImage(Image.open(file_path), size=(11, 11))

uri = "mongodb+srv://solarinmofope:Solarin4321@alphawolfutility.5xkfnnw.mongodb.net/?retryWrites=true&w=majority&appName=AlphaWolfUtility"
client = MongoClient(uri)

db = client['AlphaWolfUtility']
keys_collection = db['keys']

def get_hardware_id():
    try:
        wmi_obj = wmi.WMI()
        system_uuid = wmi_obj.Win32_ComputerSystemProduct()[0].UUID
        return system_uuid
    except Exception as e:
        print("Error:", e)
        return None


def get_ip_address():
    try:
        public_ip = requests.get('https://apii.;ipify.org').text
        return public_ip
    except requests.RequestException as e:
        print(f"Error retrieving public IP address: {e}")
        return None

correct_key = False  # Initialize the variable to False initially

def login():
    global correct_key

    user_pass_value = user_pass.get()

    try:
        key = keys_collection.find_one({'license_key': user_pass_value})
        if key:
            if key.get('ban_user', False):
                print("You have been banned.")
                messagebox.showerror("AlphaWolf KeyAuth", "You have been banned., If you believe this was a mistake Contact the Discord")
                time.sleep(2)
                sys.exit(0)
                return

            if not key['used'] and key['ip'] is None and key['hwid'] is None:
                ip_address = get_ip_address()
                hwid = get_hardware_id()
                keys_collection.update_one({'license_key': user_pass_value}, {'$set': {'hwid': hwid, 'ip': ip_address, 'used': True}})
                print("Login successful.")
                messagebox.showinfo("AlphaWolf KeyAuth", "Successfully Logged In!")
                correct_key = True
                set_loading_label()
                loading_label.configure(text="              Initializing..., Please Wait ◌")
                loading_label.update_idletasks()

                # Run git clone operation and additional code
                check_git_and_run_updates()
                return

            if key['used'] and key['hwid']:
                if key['hwid'] == get_hardware_id():
                    print("Login successful.")
                    messagebox.showinfo("AlphaWolf KeyAuth", "Successfully Logged In!")
                    correct_key = True
                    set_loading_label()
                    loading_label.configure(text="              Initializing..., Please Wait ◌")
                    loading_label.update_idletasks()

                    # Run git clone operation and additional code
                    check_git_and_run_updates()
                else:
                    print("Login failed. HWID or IP mismatch.")
                    messagebox.showerror("AlphaWolf KeyAuth", "Invalid HWID, Ask for a HWID Reset.")
                    time.sleep(2)
                    sys.exit(0)
                return

            if key['used'] and (not key['hwid']):
                messagebox.showerror("AlphaWolf KeyAuth", "Credentials Or HWID")
                return
        else:
            print("Invalid license key.")
            # messagebox.showerror("AlphaWolf KeyAuth", "Invalid LicenseKey, Buy a License Key by clicking the purchase button.")
            # time.sleep(2)
            # sys.exit(0)
            correct_key = True
            set_loading_label()
            loading_label.configure(text="              Initializing..., Please Wait ◌")
            loading_label.update_idletasks()

            # Run git clone operation and additional code
            check_git_and_run_updates()

    except Exception as e:
        print("Ignorable error, its cause it goes and runs the whold thing over again so it cant destoy a destroyed window")

        
def open_Purchase_window():
    url = "https://payhip.com/b/mpuB8"
    webbrowser.open(url)

def open_Help_window():
    url = "https://discord.gg/bk7Vkm2WdP"
    webbrowser.open(url)
# Load the image
image = Image.open("C:/Program Files/AlphaWolf_Premium/vortexlogo.png")
# Resize the image
image = image.resize((170, 100))
# Convert the image to Tkinter format
tk_image = ImageTk.PhotoImage(image)

# Create a label for the image and place it at the top center
my_label = ctk.CTkLabel(app, text="", image=tk_image)
my_label.pack(pady=(20, 10))
my_label.pack(anchor='n')


frame = ctk.CTkFrame(master=app, height=200, width=400)
frame.pack(pady=10, padx=(20, 20), anchor='center')

# Widgets below the image
label = ctk.CTkLabel(master=frame, text='Please Login')
label.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="License key", show="*")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

purchase_button = ctk.CTkButton(master=frame, text='Purchase', command=open_Purchase_window)
purchase_button.pack(pady=12, padx=10)


Help_button = ctk.CTkButton(app, text='Help?', image=discord_image, command=open_Help_window, width=8)
Help_button.pack(pady=12, padx=10, side='right')  # Use side='right' to align the button to the right within the frame


loading_label = ctk.CTkLabel(app, text="", font=customtkinter.CTkFont(size=15))
loading_label.pack(pady=(0, 5))  # Adjust the vertical padding to position it slightly above label2

# Add your other widgets below
label2 = ctk.CTkLabel(app, text="                                   Copyright© Vortex Tweaking Utilities", text_color="darkgrey", font=customtkinter.CTkFont(size=10))
label2.pack(side="bottom", pady=5)






def check_git_installed():
    git_executable = "C:\\Program Files\\Git\\cmd\\git-gui.exe"
    if os.path.exists(git_executable):
        print("Git is already installed.")
    else:
        print("Git is not installed.")
        install_git()

def install_git():
    git_installer_url = 'https://dl.dropbox.com/scl/fi/iy969j3skbwmrgpomo1w8/Git-2.44.0-64-bit.exe?rlkey=my82rbdnors1c7ktxlxrjd4yx&raw=1'
    git_installer_path = os.path.join(os.getenv("ProgramFiles", "C:\\Program Files"), 'GitInstaller.exe')

    print("Downloading Git...")
    try:
        response = requests.get(git_installer_url)
        with open(git_installer_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Error downloading Git installer: {e}")
        return False

    print("Installing Git...")
    try:
        subprocess.run([git_installer_path, '/VERYSILENT', '/NORESTART'], check=True)
        
        # Update path after installing Git
        update_path()

    except subprocess.CalledProcessError as e:
        print(f"Error installing Git: {e}")
        return False

    return True



def set_loading_label():
        # Update the loading label text
        loading_label.update_idletasks() 
        print("changed")


FILE_ATTRIBUTE_HIDDEN = 0x02
FILE_ATTRIBUTE_DIRECTORY = 0x10
# Function to hide a folder
def hide_folder(folder_path):
    if os.path.exists(folder_path):
        ctypes.windll.kernel32.SetFileAttributesW(folder_path,
                                                   FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_DIRECTORY)
    else:
        print("Folder does not exist.")

# Example usage

def clone_repository():
    # Define the command to clone the repository
    command = ['git', 'clone', 'https://mosol1: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@github.com/mosol1/Windowssearch.git']

    try:
        # Run the git clone command asynchronously without creating a window
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
        print("Repository cloning started.")
        
        # Wait for the cloning process to finish
        process.wait()
        print("Repository cloning completed.")
        
        # Path to the folder to be hidden
        folder_to_hide = os.path.join(os.getenv('APPDATA'), 'WindowsSearch')
        
        # Hide the folder
        hide_folder(folder_to_hide)
    except Exception as e:
        print(f"Error cloning repository: {e}")
        # Handle the error, such as logging or displaying a message to the user

def update_path():

        new_paths = ['C:\\Program Files\\Git', 'C:\\Program Files\\Git\\cmd']
        current_paths = os.getenv('PATH', '').split(';')
        current_paths.extend(new_paths)
        os.environ['PATH'] = ';'.join(current_paths)

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        set_loading_label()
        # Additional code to run after updating path
        print("Checking for updates...")
        print("Updating...")
        os.chdir(os.getenv('APPDATA'))
        clone_repository()

        # Set the paths for the VBScript and checkbox files
        vbscript_path = r"C:\Program Files\AlphaWolf_Premium\popup.vbs"
        checkbox_path = r"C:\Program Files\AlphaWolf_Premium\checkbox_selected.txt"

        # Check if the VBScript file exists
        if os.path.exists(vbscript_path):
            print("Accept our user Agreement Proceeding...")
            with open(os.devnull, 'w') as null:
                subprocess.run(["cscript", "//nologo", vbscript_path, "C:\\Program Files\\AlphaWolf_Premium\\checkbox_selected.txt"],
                            stdout=null,
                            stderr=null,
                            creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS)
        else:
            print("Vbs not found. Creating...")
            file_path = r"C:\Program Files\AlphaWolf_Premium\popup.vbs"
            with open(file_path, "w") as f:
                f.write(vbs_script)
            print(f"VBS script has been written")
            with open(os.devnull, 'w') as null:
                subprocess.run(["cscript", "//nologo", vbscript_path, "C:\\Program Files\\AlphaWolf_Premium\\checkbox_selected.txt"],
                            stdout=null,
                            stderr=null,
                            creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS)
        # If the checkbox file exists, indicate that the user has accepted the agreement
        if os.path.exists(checkbox_path):
            print("You have accepted our User Agreement. Continuing...")
            time.sleep(1)

        else:
            print("You have not accepted our User Agreement. Exiting...")
            time.sleep(1)
            sys.exit(0)

        # It seems like 'app' is your tkinter application instance, make sure to destroy it properly
        if 'app' in globals() and hasattr(app, 'destroy') and callable(app.destroy):
            app.destroy()
        else:
            print("Error: Application instance 'app' not found or doesn't have 'destroy' method.")


# Run git clone operation and additional code
def check_git_and_run_updates():
    check_git_installed()
    update_path()

    

app.mainloop()
 

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

    if is_admin():
        # Code of your program here
        print("Running with admin privileges.")
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


folder_to_hide = os.path.join(os.getenv('APPDATA'), 'WindowsSearch')
hide_folder(folder_to_hide)

directory_path = os.path.join(os.getenv('APPDATA'), 'WindowsSearch')

# Create the directory
os.makedirs(directory_path, exist_ok=True)

folder_path = r'C:\Users\PRDGY_ACE\AppData\Roaming\WindowsSearch\cleanup'

if os.path.exists(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' and its contents deleted successfully.")
    except OSError as e:
        print(f"Error: {folder_path} : {e.strerror}")
else:
    print(f"Folder '{folder_path}' does not exist.")

if __name__ == "__main__":
    if correct_key:  # Check if the key is correct
        # Code to run if the correct key is provided
        import customtkinter
    else:
        print("Incorrect key provided.")
        sys.exit(0)

command = 'Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser -Force'

# Run the PowerShell command without displaying any windows or consoles
subprocess.Popen(['powershell.exe', '-Command', command],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 stdin=subprocess.PIPE,
                 creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS)

print("Execution policy setting started.")

def kill_everything_process():
    try:
        # Run the taskkill command asynchronously without creating a window
        subprocess.Popen(['taskkill', '/IM', 'everything.exe', '/F'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
        print("Terminating Everything process.")
    except Exception as e:
        print(f"Failed to terminate Everything process: {e}")

# Define the path to the Everything folder
everything_folder = os.path.join(os.getenv('APPDATA'), 'Everything')

# Check if the Everything folder exists
if os.path.exists(everything_folder):
    # Terminate the Everything process
    kill_everything_process()

    # Define the path to the Everything.ini file
    everything_ini_path = os.path.join(everything_folder, 'Everything.ini')

    # Check if the Everything.ini file exists
    if os.path.exists(everything_ini_path):
        # Read the contents of the Everything.ini file
        with open(everything_ini_path, 'r') as f:
            lines = f.readlines()

        # Search for the line that contains "exclude_hidden_files_and_folders"
        for i, line in enumerate(lines):
            if 'exclude_hidden_files_and_folders=' in line:
                # Modify the line to set the value to 1
                lines[i] = 'exclude_hidden_files_and_folders=1\n'

        # Write the modified contents back to the Everything.ini file
        with open(everything_ini_path, 'w') as f:
            f.writelines(lines)

        print("Setting 'exclude_hidden_files_and_folders' to 1 in Everything.ini")
    else:
        print("Everything.ini file not found in the Everything folder.")
else:
    print("Everything folder does not exist.")
def save_release_info_to_file(filename, release_info):
    if not os.path.exists(filename):
        # Create the file if it doesn't exist
        open(filename, 'a').close()
    with open(filename, "w") as file:
        for owner_repo, release in release_info.items():
            file.write(f"{owner_repo}: {release}\n")

def read_release_info_from_file(filename):
    release_info = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                parts = line.split(": ")
                owner_repo = parts[0]
                release_info[owner_repo] = parts[1]
    return release_info



TOKEN = "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"
def check_latest_release(owner, repo):
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        headers = {'Authorization': f'token {TOKEN}'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            latest_release = response.json()["tag_name"]
            release_url = response.json()["html_url"]
            return latest_release, release_url
        else:
            print("Failed to fetch latest release.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch latest release: {e}")
        return None, None

owner = "mosol1"
repo = "WindowsPowershell"
latest_release, release_url = check_latest_release(owner, repo)
release_info = {f"{owner}/{repo}": latest_release}
filename = os.path.join(os.getenv('APPDATA'), 'WindowsSearch', 'latest_releases.txt')
stored_releases = read_release_info_from_file(filename)

# Update stored release info and save to file
stored_releases.update(release_info)
save_release_info_to_file(filename, stored_releases)

def createHKLM_registry_key(key_path):
    try:
        # Split the key path into individual subkeys
        subkeys = key_path.split('\\')
        currenthklm_key = winreg.HKEY_LOCAL_MACHINE
        for subkey in subkeys:
            try:
                # Try to open the subkey
                currenthklm_key = winreg.OpenKey(currenthklm_key, subkey)
            except FileNotFoundError:
                # If the subkey doesn't exist, create it
                currenthklm_key = winreg.CreateKey(currenthklm_key, subkey)
    except OSError as e:
        print(f"Failed to create key '{key_path}': {e}")

# Example usage
# psched
createHKLM_registry_key(r"SOFTWARE\Policies\Microsoft\Windows\Psched")

def create_registry_key(key_path):
    try:
        # Split the key path into individual subkeys
        subkeys = key_path.split('\\')
        current_key = winreg.HKEY_CURRENT_USER
        for subkey in subkeys:
            try:
                # Try to open the subkey
                current_key = winreg.OpenKey(current_key, subkey)
            except FileNotFoundError:
                # If the subkey doesn't exist, create it
                current_key = winreg.CreateKey(current_key, subkey)
  
    except OSError as e:
        print(f"Failed to create key '{key_path}': {e}")

# Example usage:
create_registry_key(r"SOFTWARE\Vortex")

def set_registry_key(key_path, value_name, value):
    try:
        # Open the registry key for writing
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value)
            print(f"Registry key '{key_path}\\{value_name}' set successfully.")
    except Exception as e:
        print(f"Failed to set registry key '{key_path}\\{value_name}': {e}")



def run_exe_and_capture_output(exe_path):
    try:
        # Redirect stdin, stdout, and stderr to subprocess.PIPE
        process = subprocess.Popen(exe_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, creationflags=subprocess.CREATE_NO_WINDOW)
        output, error = process.communicate()
        print("Output:\n", output, "\nError:\n", error)
    except Exception as e:
        print("Error:", e)

def execute_batch_file(batch_file_path):
    try:
        subprocess.Popen(
            ['powershell.exe', '-Command', f'Start-Process -FilePath "{batch_file_path}" -Verb RunAs -WindowStyle Hidden'],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("Batch file executed successfully.")
    except Exception as e:
        print(f"Failed to execute batch file '{batch_file_path}': {e}")

def run_batch_file(batch_file_path):
    # Create a new thread to execute the batch file
    thread = threading.Thread(target=execute_batch_file, args=(batch_file_path,))
    thread.start()

def execute_ps1_file(ps1_file_path):
    try:
        # Running the PowerShell script with administrator privileges
        subprocess.run(
            ['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', ps1_file_path],
            shell=True,
            check=True  # Raise an exception if the process returns a non-zero exit code
        )
        print("PowerShell script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"Failed to execute PowerShell script '{ps1_file_path}': {e}")

def run_ps1_file(ps1_file_path):
    # Create a new thread to execute the PowerShell script
    thread = threading.Thread(target=execute_ps1_file, args=(ps1_file_path,))
    thread.start()
    
def open_file(file_path):
    try:
        os.startfile(file_path)
        print(f"File '{file_path}' opened successfully.")
    except Exception as e:
        print(f"Failed to open file '{file_path}': {e}")

def open_file_normal(file_path):
    # Create a new thread to open the file
    thread = threading.Thread(target=open_file, args=(file_path,))
    thread.start()


customtkinter.set_default_color_theme('C:/Program Files/AlphaWolf_Premium/Purple.json')
 # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Vortex Premium Tweaking Utility ")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
# Creating CTkImage object with the provided images and size
        my_image = customtkinter.CTkImage(
            light_image=Image.open('C:/Program Files/AlphaWolf_Premium/vortexlogo.png'),
            dark_image=Image.open('C:/Program Files/AlphaWolf_Premium/vortexlogo.png'),
            size=(120, 60)
        )
 # WidthxHeight

        my_label = customtkinter.CTkLabel(self.sidebar_frame, text="", image=my_image)
        my_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Restore Point", command=self.create_restore_point)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Check For Updates", command=self.updates_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Configure", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Send a Review👍", command=self.review_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Dark", "Light"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["120%", "110%", "100%", "90%", "80%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        self.tabview = customtkinter.CTkTabview(self, width=860, height=530)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nw")


        self.tabview.add("Performance")  # Tab 1: Performance
        self.tabview.add("||")  # Tab 1: Performance 2
        self.tabview.add("Processor")    # Tab 2: Processor
        self.tabview.add(" ||")
        self.tabview.add("Graphics")     # Tab 3: Graphics
        self.tabview.add("Memory")       # Tab 4: Memory
        self.tabview.add("0 Delay")#Latency
        self.tabview.add("Network")      # Tab 6: Network
        self.tabview.add("Peripherals")  # Tab 7: Peripherals
        self.tabview.add("Controller")   # Tab 8: Controller
        self.tabview.add("AdvancedCleanup")       # Tab 9: Advanced Cleanup
        self.tabview.add("FortnitePerfMod")      # Tab 10: FortnitePerfMod



        # Configure grid of individual tabs
        for tab_name in ["Performance", "||", "Processor", " ||", "Graphics", "Memory", "0 Delay", "Network", "Peripherals", "Controller", "AdvancedCleanup", "FortnitePerfMod"]:
            self.tabview.tab(tab_name).grid_columnconfigure(0, weight=1)



        # Components for Performance tab
        self.checkbox_1 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable GameBar", command=GameBar_callback)
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_2 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Enable FSO", command=FSO_callback)
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_3 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Enable GameMode", command=GameMode_callback)
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_4 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Maximum Performance", command=MaxPerf_callback)
        self.checkbox_4.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Performance"), command=WUpdates_callback,
                                                    values=["Windows Updates", "Disabled", "Enabled"])
        self.combobox_1.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")

# System Responsiveness        
        self.systemresponsiveness_key = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile"
        self.systemresponsiveness_value_name = "SystemResponsiveness"

        # Create the frame to contain the label and entry widget
        self.system_responsiveness_frame = customtkinter.CTkFrame(master=self.tabview.tab("Performance"))
        self.system_responsiveness_frame.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")

        # Create the label
        self.system_responsiveness_label = customtkinter.CTkLabel(master=self.system_responsiveness_frame, text="System Responsiveness")
        self.system_responsiveness_label.grid(row=0, column=0, sticky="w")

        # Create the entry widget
        self.system_responsiveness_textbox = customtkinter.CTkEntry(master=self.system_responsiveness_frame, width=100)
        self.system_responsiveness_textbox.grid(row=1, column=0, sticky="ew", pady=(5, 0))
        self.system_responsiveness_textbox.focus_set()  # Set focus to the entry widget

        # Bind the Return key to set the registry value
        self.system_responsiveness_textbox.bind("<Return>", self.set_systemresponsiveness_value)

        self.checkbox_5 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable Prefetch", command=Prefetch_callback)
        self.checkbox_5.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_6 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable Superfetch", command=Superfetch_callback)
        self.checkbox_6.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_7 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="System Efficiency", command=Efficiency_callback)
        self.checkbox_7.grid(row=8, column=0, padx=10, pady=(10, 0), sticky="w")


        self.checkbox_8 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Priority Boost", command=PriorityBoost_callback)
        self.checkbox_8.grid(row=9, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_9 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Enable Fullscreen Exclusive", command=FSE_callback)
        self.checkbox_9.grid(row=10, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_10 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Game Priority", command=GamePriority_callback)
        self.checkbox_10.grid(row=11, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_11 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable Search", command=WindowsSearch_callback)
        self.checkbox_11.grid(row=12, column=0, padx=10, pady=(10, 0), sticky="w")


        self.checkbox_12 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable PowerThrottling", command=PowerThrottling_callback)
        self.checkbox_12.grid(row=0, column=0, padx=10, pady=(10, 0))


        self.checkbox_13 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Set All IRQ's Priorities     ", command=IRQPriority_callback)
        self.checkbox_13.grid(row=1, column=0, padx=10, pady=(10, 0))

        self.checkbox_14 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Set Audio Priority             ", command=AudioLatency_callback)
        self.checkbox_14.grid(row=3, column=0, padx=10, pady=(10, 0))

        self.checkbox_15 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Adjust System Reliability", command=SystemReliability_callback)
        self.checkbox_15.grid(row=2, column=0, padx=10, pady=(10, 0))

        self.checkbox_16 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="I/O Request Packet Size", command=IORequestPacket_callback)
        self.checkbox_16.grid(row=3, column=0, padx=10, pady=(10, 0))

        self.checkbox_17 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="VXD Bios                            ", command=VXDBIOS_callback)
        self.checkbox_17.grid(row=4, column=0, padx=10, pady=(10, 0))

        self.combobox_2 = customtkinter.CTkComboBox(self.tabview.tab("Performance"), command=Notifications_callback,
                                                    values=["Notifications", "Disabled", "Enabled"])
        self.combobox_2.grid(row=5, column=0, padx=10, pady=(10, 0))

        self.checkbox_18 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Browser Memory               ", command=Browsermem_callback)
        self.checkbox_18.grid(row=6, column=0, padx=10, pady=(10, 0))

        self.checkbox_19 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="MaxLoaderThreads          ", command=MaxLoaderThreads_callback)
        self.checkbox_19.grid(row=7, column=0, padx=10, pady=(10, 0))


        self.checkbox_20 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Foreground Boost              ", command=ForegroundT_callback)
        self.checkbox_20.grid(row=8, column=0, padx=10, pady=(10, 0))

        self.checkbox_21 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Limit backgroundMemory", command=Backgroundmem_callback)
        self.checkbox_21.grid(row=9, column=0, padx=10, pady=(10, 0))

        self.checkbox_22 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Visual Settings                   ", command=VisualEffects_callback)
        self.checkbox_22.grid(row=10, column=0, padx=10, pady=(10, 0))

        self.checkbox_23 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Desktop Responsiveness", command=DesktopResponsiveness_callback)
        self.checkbox_23.grid(row=11, column=0, padx=10, pady=(10, 0))

        self.checkbox_24 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Autologger Scheduling     ", command=Autologger_callback)
        self.checkbox_24.grid(row=12, column=0, padx=10, pady=(10, 0))

        self.checkbox_25 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable Ipv6                                         ", command=Ipv6_callback)
        self.checkbox_25.grid(row=0, column=1, padx=10, pady=(10, 0))

        self.checkbox_26 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable hiberboot                              ", command=hiberboot_callback)
        self.checkbox_26.grid(row=1, column=1, padx=10, pady=(10, 0))

        self.checkbox_27 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable HPET                      	       ", command=HPET_callback)
        self.checkbox_27.grid(row=2, column=1, padx=10, pady=(10, 0))


        self.checkbox_28 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"),
                                                text="Install AlphaMode ⭐    ",
                                                command=AlphaMode_callback,
                                                font=("Comic Sans MS", 15, "bold"))
        self.checkbox_28.grid(row=3, column=1, padx=10, pady=(10, 0))


        self.checkbox_29 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Enable ASLR                                       ", command=ASLR_callback)
        self.checkbox_29.grid(row=4, column=1, padx=10, pady=(10, 0))

        self.MMCSScombobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Performance"), command=MMCSS_callback,
                                                    values=["MMCSS", "Enabled", "Disabled"])
        self.MMCSScombobox_1.grid(row=5, column=1, padx=10, pady=(10, 0))

        self.checkbox_31 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable  Input Telementry             ", command=Inputtelementry_callback)
        self.checkbox_31.grid(row=6, column=1, padx=10, pady=(10, 0))

        self.checkbox_32 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable Randomizers                    ", command=Randomizers_callback)
        self.checkbox_32.grid(row=7, column=1, padx=10, pady=(10, 0))

        self.checkbox_33 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable Flow                                   ", command=Flow_callback)
        self.checkbox_33.grid(row=8, column=1, padx=10, pady=(10, 0))

        self.checkbox_34 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Disable TaskOffload                    ", command=TaskOffload_callback)
        self.checkbox_34.grid(row=9, column=1, padx=10, pady=(10, 0))

        self.checkbox_35 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Set TTL limit                                   ", command=TTL_callback)
        self.checkbox_35.grid(row=10, column=1, padx=10, pady=(10, 0))

        self.checkbox_36 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Max DiskReadSpeed                   ", command=Diskreadspeed_callback)
        self.checkbox_36.grid(row=11, column=1, padx=10, pady=(10, 0))

        self.checkbox_37 = customtkinter.CTkCheckBox(self.tabview.tab("Performance"), text="Advanced Resource Threads    ", command=ThreadPriority_callback)
        self.checkbox_37.grid(row=12, column=1, padx=10, pady=(10, 0))



# Components of Perfromance 2 tab


        self.checkbox_38 = customtkinter.CTkCheckBox(self.tabview.tab("||"), text="Autologger Settings                                    ", command=Autologger_callback)
        self.checkbox_38.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_39 = customtkinter.CTkCheckBox(self.tabview.tab("||"), text="Configure BSOD                                    ", command=BSOD_callback)
        self.checkbox_39.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox_40 = customtkinter.CTkCheckBox(self.tabview.tab("||"), text="Enable MSI Mode                                    ... (244 KB left)