# Dr0pFi - Steal WiFi Passwords from Windows
Using this tool, You can capture all Saved WiFi Passwords stored on Windows Computer and mail them to your email!

# Note

`--> You need Python2 for compiling the Dr0pFi to a executable.`
`--> I thank Zaid Sabih as he taught me to make this kind of wonderful and useful programs.`

`--> I am not going to be responsible for any Illegal Purpose`      

# General Info

Using Dr0pFi, You can capture all WiFi Passwords from a Windows Computer and mail them to your Email, This is the beta version of my program, And soon a new Version will come out soon.

# Installation

--> To install Dr0pFi, You can use the git clone command else, Download it as zip.

`git clone https://github.com/Vedant-Bhalgama/Dr0pFi.git`
 
--> After you have downloaded it, Open CMD and type this command. This is going to install all the required packages for the program.

`pip -r install requirements.txt`


![requiremetns](https://user-images.githubusercontent.com/67494275/89538839-ae1a5f00-d818-11ea-8fe5-ece4564a9530.PNG)


# Usage 

--> To use the tool, First of all you need to edit the Email ID and Password. You need to replace **youremid** and **yourempass** with your real Email Credentials

For EG. My Email ID which I have taken over here is **fakemail@ gmail.com** and My Password which I have taken over here is **fakepass**


![fakeid](https://user-images.githubusercontent.com/67494275/89539697-b7f09200-d819-11ea-90c7-16de5a019abe.PNG)


--> Please make sure that **Less Secure Apps is turned on in your Gmail Account**, See the screenshot below! Go to this Link to Turn it on

`https://myaccount.google.com/lesssecureapps`


![Less_Secure_Apps](https://user-images.githubusercontent.com/67494275/89539923-fe45f100-d819-11ea-8d72-09b35bd8fcee.PNG)


# Build to EXE

NOTE: Before building, you must have win32 installed for Python, install this with pip via `pip install pypiwin32`

--> So, Simply open CMD on your Computer and then run the build.py using Python2. Build.py is going to compile our Dr0pFi.py to EXE. Refer to the screenshot below!


![Build](https://user-images.githubusercontent.com/67494275/89541419-f6874c00-d81b-11ea-80a2-3d15bed0530a.PNG)


--> After you compile it to EXE, You are going to see the EXE file in the **dist** folder.


![Drop](https://user-images.githubusercontent.com/67494275/89541480-0d2da300-d81c-11ea-9e5c-86c2a3ed237c.PNG)


# Final Output

--> After you send the File to the Target, After he/she executes it, You are going to receive a mail in which all Wifi Passwords are going to be there! **(You will receive Passwords only on that mail which you had edited in the script, Also make sure Less Secure Apps is turn on for your Google Account)**

--> Wifi Passwords Final Output

![Final Output](https://user-images.githubusercontent.com/67494275/89542144-e7ed6480-d81c-11ea-8cf2-d45f9e497dc8.PNG)
