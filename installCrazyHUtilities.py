# [
# 
# Script made by CrazyH2 (https://github.com/crazyh2)
# © Copyright 2024 CrazyH2. All rights reserved.
# 
# ]


def require(name, package = None):
    if package == None:
        package = name
    import os
    try:
        return __import__(name, fromlist=[''])
        print(f"""module '{name}' is installed""")
    except ModuleNotFoundError:
        print(f"""module '{name}' is not installed""")
        os.system(f"""pip install {package}""")
        try:
            return __import__(name, fromlist=[''])
            print(f"""module '{name}' is now installed""")
        except ModuleNotFoundError:
            print(f"""module '{name}' is not installing""")

require("tkinter")

from io import BytesIO
from zipfile import ZipFile
import urllib.request
from tkinter import *
import tkinter.messagebox as messagebox
import os, json

update_url = "https://raw.githubusercontent.com/NotCrazyH2/toomuch/refs/heads/main/versions.json"

class Installer:
    def __init__(self):
        self.root = Tk()
        self.root.title('Animat-a-background - CrazyH2 (github.com/crazyh2)')
        self.root.withdraw()

        messagebox.showwarning("Animat-a-background", """The software is installing.
                                
Made by CrazyH2 (https://github.com/crazyh2)
© Copyright 2024 CrazyH2. All rights reserved.""")
            
        self.install()

    def getVersions(self):
        with urllib.request.urlopen(update_url) as url:
            return json.load(url)
        
    def getLatestVersion(self):
        versions = self.getVersions()

        latest = max(versions, key=lambda ev: ev['version'])
        return latest

    def install(self):
        version = self.getLatestVersion()

        response = urllib.request.urlopen(version["file"])
        thezip = ZipFile(BytesIO(response.read()))

        thezip.extractall(path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'CrazyHUtilities'))

        if version["hash"] != generate_file_md5(os.path.join(os.environ['USERPROFILE']), "CrazyHUtilities"):
            messagebox.showwarning("Animat-a-background", """The software could not be verified. If you see this message report it!
                                            
            Made by CrazyH2 (https://github.com/crazyh2)
            © Copyright 2024 CrazyH2. All rights reserved.""")
            exit()

        messagebox.showwarning("Animat-a-background", """The software was installed.
                                
Made by CrazyH2 (https://github.com/crazyh2)
© Copyright 2024 CrazyH2. All rights reserved.""")

        #os.system(f'python animatedBackground_{version.version}.pyw')
        os.startfile(os.path.join(os.environ['USERPROFILE']), 'CrazyHUtilities')
        exit()

if __name__ == "__main__":
    Installer()
