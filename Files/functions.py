from Tkinter import *
# from tkinter.scrolledtext import ScrolledText <-- Not sure if need?
import ttk
import os
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
    """
    Reads the config.txt file within the Res dir.
    reads a line and then places it inside a list, moves onto the next one.
    :return: List of options. 6 Options total.
    """
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

# [5] # Sorts the listing out for the Jira type in the dropdown menu
JiraList = ConfigureOptions()[5]
JiraList = JiraList.split(", ")
JiraList[0] = JiraList[0][12:]


def ConfirmButtonReturn(TimerStatus, TimerCount, SVNStatus, SVNPath,
                        LocalPath, JiraType, JiraNumber):
    """
    Grabs the options set by the user and assigns them to their respective
    parameter.
    :param TimerStatus: Tuple, Tick Box of the Timer State.
                        selected= ticked, ()= unticked
    :param TimerCount: String, Number inputted from user for the minute timer.
    :param SVNStatus: Tuple, Tick Box of the SVN State.
                      selected= ticked, ()= unticked
    :param SVNPath: String, Inputted path for SVN for saving inside SVN dir,
                    C:/...
    :param LocalPath: String, Inputted path for Local save copy, C:/...
    :param JiraType: String, Abbreviation of Jira type, EP= Eprais, etc...
    :param JiraNumber: String, Jira number entry, 426

    Example:
    [('selected',), '60', ('selected',), 'C:/Users/jfriend.SPIDEX/Desktop/SVN',
    'C:/Users/jfriend.SPIDEX/Desktop/Kami/JiraLogs', 'EP', '426']
    """

    TimerStatus = TimerStatus.state()
    TimerCount = TimerCount.get()
    SVNStatus = SVNStatus.state()
    SVNPath = SVNPath.get()
    LocalPath = LocalPath.get()
    JiraType = JiraType.get()
    JiraNumber = JiraNumber.get()

    DataList = [TimerStatus, TimerCount, SVNStatus,
                SVNPath, LocalPath, JiraType,
                JiraNumber]

    # print DataList <<< For debugging
    return DataList


def PrintMe():
    print "I am a placeholder!"
