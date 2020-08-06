import subprocess
import re
import time


print("[+] Please wait, Compiling the file to EXE ...")
subprocess.call("pyinstaller --onefile Dr0pFi.py", shell=True)

