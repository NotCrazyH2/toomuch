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

import webbrowser
import urllib.request
from tkinter import *
import tkinter.messagebox as messagebox
import os, json

src_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
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

        #with urllib.request.urlopen(version["file"]) as upd:
        #    with open(src_path, "wb+") as f:
        #        f.write(upd.read())
        webbrowser.open(version["file"])

        messagebox.showwarning("Animat-a-background", """Open the python file in your downloads.
                                
Made by CrazyH2 (https://github.com/crazyh2)
© Copyright 2024 CrazyH2. All rights reserved.""")

        #os.system(f'python animatedBackground_{version.version}.pyw')
        exit()

if __name__ == "__main__":
    Installer()
