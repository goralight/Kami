from Tkinter import *
from tkinter.scrolledtext import ScrolledText
import ttk
import os
#

# import Tkinter as tk
# import time
# from datetime import datetime
#
#
# class App():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.label = tk.Label(text="")
#         self.label.pack()
#         self.update_clock()
#         self.root.mainloop()
#
#     def update_clock(self):
#         now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
#         self.label.configure(text=now)
#         self.root.after(1, self.update_clock)
#
# app=App()

FirstCWD = os.path.dirname(os.path.realpath(__file__))
ResDir = FirstCWD[:-5]+"\Res"


def ConfigureOptions():
    with open(ResDir+"\config.txt") as options:
        lines = options.read().split("\n")
    return lines
    # 0 = enable timer tick value
    # 1 = default timer val
    # 2 = enable save to svn tick value
    # 3 = path to svn
    # 4 = path to local save
    # 5 = list of jira types

# [0] # Enable timer tick box
EnableTimerTickBox = ConfigureOptions()[0]
EnableTimerTickBox = EnableTimerTickBox[22:]
EnableTimerTickBox = int(EnableTimerTickBox)

# [1] # Default timer value
DefaultTimerValue = ConfigureOptions()[1]
DefaultTimerValue = DefaultTimerValue[15:]
DefaultTimerValue = int(DefaultTimerValue)

# [2] # Enable save to SVN tick box
EnableSaveToSVN = ConfigureOptions()[2]
EnableSaveToSVN = EnableSaveToSVN[17:]
EnableSaveToSVN = int(EnableSaveToSVN)

# [3] # Default value for the path to SVN
SVNDefaultPath = ConfigureOptions()[3]
SVNDefaultPath = SVNDefaultPath[18:]

# [4] # Default Path for local save
LocalSavePathway = ConfigureOptions()[4]
LocalSavePathway = LocalSavePathway[25:]

# [5] # Sorts the listing out for the jira type in the dropdown menu
JiraList = ConfigureOptions()[5]
JiraList = JiraList.split(",")
JiraList[0] = JiraList[0][12:]
# print JiraList


def returns():
    one = "1"
    two = "2"
    three = "3"

    return one, two, three

# print returns()[0]




def PrintMe():
    print "I am a placeholder!"
