Installation Guide for Windows
==============================

**Step 1**

Download and install the latest python version at https://www.python.org/downloads/.

**Step 2**

After installation, search for Edit the system environmental variables. Click on the Environment Variables button.
Find the PATH variable in the system variables section, and press edit. Then, find the location of your python file by going to
C:\Users\YOUR NAME\AppData\Local\Programs\Python\YOUR PYTHON VERSION. Copy the location, go back to the edit environment
variables windows, press New, and paste the address in.

**Step 3**

As a confirmation, go to command prompt and type

    python
    
The command prompt should return two lines detailing your python version. Close and reopen the command prompt. Then, type

    python -m pip install requests bs4 ratelimit
    
After that, traverse to the directory of the script and run the program

    cd C:\Users\YOUR NAME\FILEPATH
    python f.py

Usage Guide
===========

The first parameter is the API Key. Request one at https://osu.ppy.sh/p/api, and copy and paste it into the command line.

The second parameter is the MP link to start finding from. Login to Osu!, start a new multiplayer match by yourself,
and retrieve the series of numbers at the end of the MP link and paste it into the command line.

The last (and potentially more) parameter(s) is the ID of the players that you want to find. If you are done with inputting
the ID of the players, simply do not type anything and just press enter.
