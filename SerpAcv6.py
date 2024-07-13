import os
from pathlib import Path
import webbrowser
import pathlib
import time
import keyboard
import customtkinter as ctk
import tkinter as tk
import getpass
import tkinter.font as tkfont
from tkinter import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[36m'
    BLUE = '\033[35m'
    RED = '\033[32m'
    WHITE = '\033[31m'


list_file = []
path = 'C:\\'
disks = os.listdrives()
count_disks = len(disks)
user_name = getpass.getuser()

fordelete = []

Roaming = Path(os.environ["USERPROFILE"]) / "AppData\\Roaming"
Roaming = os.path.realpath(Roaming)

Disk_C = "C:\\"
Disk_C = os.path.realpath(Disk_C)

Local = Path(os.environ["USERPROFILE"]) / "AppData\\Local"
Local = os.path.realpath(Local)

Temp = "C:\\Windows\\Temp"
Temp = os.path.realpath(Temp)

Prefetch = "C:\\Windows\\Prefetch"
Prefetch = os.path.realpath(Prefetch)

RecycleBin = "C:\\$Recycle.Bin"
RecycleBin = os.path.realpath(RecycleBin)

ProgramFiles = "C:\\Program Files"
ProgramFiles = os.path.realpath(ProgramFiles)

ProgramFilesX86 = "C:\\Program Files (x86)"
ProgramFilesX86 = os.path.realpath(ProgramFilesX86)

Downloads = Path(os.environ["USERPROFILE"]) / "Downloads"
Downloads = os.path.realpath(Downloads)

global keywords
keywords = [
			"INTERIUM",
            "XONE",
            "xone",
            "Luno",
            "ExLoader",
            ".cfg",
            "Enigma",
            "En1gma",
            "naim",
            "AimStar",
            "Aimmy",
            "plague",
            "TKazer",
            "Ekkond",
            "Osiris",
            "Victoria",
            "W1nner",
            "NeverLose",
            ".ahk",
            "ExtrimHack",
            "MultiHack",
            "Nexusoftware",
            "skinchanger",
            "MaxHack",
            "ezHack",
            "Valthrun",
            "Aimware",
            "Aimware",
            "Asphyxia",
            "IMXNOOBX",
            "Orbit",
            "Primordial",
            "SDK2Changer",
            "Sensum",
            "Warware",
            "VRedux",
            "memesense",
            "gamesense",
            "fatality",
            "skeet",
            "cheat",
            # "чит",
            "neverlose",
            "CS2Test",
            "onetap",
            "Mason",
            "Fecurity",
            "Softhub",
            "WinX",
            "NixWare",
            "Predator",
            "OneMacro",
            "AXIOS",
            "Pussycat",
            "Pellix",
            "S0ul",
            "Antropomeda",
            "1LT",
            "PornHub",
            "SYNCWARE",
            "Aquila",
            "Easywin",
            "Ampetamine",
            "Nova",
            "MillionWare",
            "Kernel",
            "Detorus",
            "VTA",
            "MaSoN",
            "MASON",
            "Spurdo",
            "ProExt",
            "VREDUX",
            "Hellhit",
            "0x666",
            "SAPH",
            "AM",
            "Advance",
            "Sapphire",
            "AQUILA",
            "InterWebz",
            "R8",
            "PROCHEAT",
            "BAUNTI",
            "RAZERCLUB",
            "LOR",
            "hvh",
            "HVH",
            "Midnight",
            "NL",
            ]


def tt(text, delay):
    for i in text:
        print(end=i)
        time.sleep(delay)		
	

def folders():
	os.startfile(Disk_C)
	os.startfile(Roaming)
	os.startfile(Local)
	os.startfile(Prefetch)
	os.startfile(Temp)
	os.startfile(RecycleBin)
	os.startfile(ProgramFiles)
	os.startfile(ProgramFilesX86)
	os.startfile(Downloads)


#Открывает сайты читов
def history():
	print(bcolors.RED, "\nОткрытие сайтов...", bcolors.ENDC)
	webbrowser.open('https://midnight.im/', new=2)
	webbrowser.open('https://xone.fun/', new=2)
	webbrowser.open('https://neverlose.cc/', new=2)
	webbrowser.open('https://en1gma.tech/', new=2)
	webbrowser.open('https://m.youtube.com/', new=2)
	#Открытие истории
	time.sleep(1)
	keyboard.press_and_release('Ctrl+H')


def search_files(keywords):
    global path
    for path in disks:
        for root, dirs, files in os.walk(path):
            for file in files:
                for keyword in keywords:
                    if keyword in file:
                        print(f"\nFile found: {file}\n")
                        file_path = os.path.join(root, file)
                        print("   File directory :", file_path, "\n")
                        file_size = os.path.getsize(file_path)
                        print("  File Size is :", file_size, "bytes\n")

                        try:
                            p_file = pathlib.Path(file)
                            file_time = p_file.stat().st_mtime
                            print("Last update files : ", file_time)
                        except FileNotFoundError:
                            print( "The file cannot be read to find out the date of the change")
                            pass

                        print("\n--------------------------------------")


def search_directory(keywords):
    global path
    for path in disks:
        for root, dirs, files in os.walk(path):
            for directory in dirs:
                for keyword in keywords:
                    if keyword in directory:
                        print(f"\nFolder found : {directory}\n")
                        directory_path = os.path.join(root, directory)
                        print("   Folder folder :", directory_path, "\n")
                        directory_size = os.path.getsize(directory_path)
                        print("  Directory Size is :", directory_size, "bytes\n")

                        try:
                            p_directory = pathlib.Path(directory_path)
                            directory_time = p_directory.stat().st_mtime
                            print("Last update files : ", directory_time)
                        except FileNotFoundError:
                            print("The file cannot be read to find out the date of the change")
                            pass

                        print("\n--------------------------------------")

def search_files_small():
    search_files(keywords)

def search_folders_small():
    search_directory(keywords)

def itog():
    # Итог
    print("\n\n\n\n\n\n\nПрийдётся немного подождать, идёт сканирование всех дисков...\n\n")
    global disk
    for disk in disks:
        search_directories(disk)

def search_directories(path):
    for root, dirs, files in os.walk(path):
        for keyword in keywords:
            file_path = os.path.join(root, keyword)
            if os.path.exists(file_path):
                print(f"\nFile found: {keyword}\n", f"\nFile directory: {file_path}")
                print("--------------------------------------\n")

        for keyword in keywords:
            directory_path = os.path.join(root, keyword)
            if os.path.exists(directory_path):
                print(f"\nFolder found: {keyword}\n", f"\nFolder directory: {directory_path}")
                print("--------------------------------------\n")

#-----------------------------------------------------------------------------------------------------------------

# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("dark") 
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"    
 
appWidth, appHeight = 763, 300

float_value = 150

# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.title("Serp Anticheat")
        self.iconbitmap("..\\img\\icon.ico")
        self.geometry(f"{appWidth}x{appHeight}")
 
        # Hello {User}! Label
        self.nameLabel = ctk.CTkLabel(self,
                                      text=f"Hello {user_name}!", font=("Arciform", 30))
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")

        # Developers text Label
        self.DevelopersTextLabel = ctk.CTkLabel(self,
                                      text=f"Developers:", font=("Arciform", 20))
        self.DevelopersTextLabel.grid(row=0, column=5,
                            padx=20, pady=20,
                            sticky="ew")
        
        # Developers Label
        self.DevelopersLabel = ctk.CTkLabel(self,
                                      text=f"coylll-dev(Soul) - programmer and coder\nAntropomeda - helper\n1LT(ALT) - helper", font=("Arciform", 15))
        self.DevelopersLabel.grid(row=1, column=5,
                            padx=20, pady=0,
                            sticky="ew")

        # Developers Label
        self.MenuLabel = ctk.CTkLabel(self,
                                      text=f"-Menu-", font=("Comic-San", 25))
        self.MenuLabel.grid(row=1, column=2,
                            padx=20, pady=0,
                            sticky="ew")

        # Folders Button
        self.FoldersButton = ctk.CTkButton(self,
                                         text="Open folder", command=folders)
        self.FoldersButton.grid(row=2, column=0,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew", ipadx=40, ipady=10)
        
        # Web Button
        self.WebButton = ctk.CTkButton(self,
                                         text="Open web", command=history)
        self.WebButton.grid(row=2, column=2,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew", ipadx=40, ipady=10)
        
        # Scan files Button
        self.ScanFilesButton = ctk.CTkButton(self,
                                         text="Scan Files", command=search_files_small)
        self.ScanFilesButton.grid(row=3, column=0,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew", ipadx=40, ipady=10)
        # Scan folders Button
        self.ScanFoldersButton = ctk.CTkButton(self,
                                         text="Scan Files", command=search_folders_small)
        self.ScanFoldersButton.grid(row=3, column=2,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew", ipadx=40, ipady=10)
        
        # Scan all Button
        self.ScanAllButton = ctk.CTkButton(self,
                                         text="Scan Files", command=itog, hover_color="purple")
        self.ScanAllButton.grid(row=3, column=4,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew", ipadx=40, ipady=10)
 
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

app = App()
app.mainloop()