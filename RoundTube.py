"""
-------------------------------------------------------
[file name]
[program description]
-------------------------------------------------------
Author: Nicholas Hallman
ID: 150357790
Email: hall7790@mylaurier.ca
__updated__ = "2015-09-18"
-------------------------------------------------------
"""
import time
import webbrowser


delay = input("Type delay in seconds: ")
delay = int(delay)
repeat = input("How many iterations?")
repeat = int(repeat)
url = input("Paste URL: ")

for i in range(0, repeat):
    time.sleep(delay)
    webbrowser.open(url)
