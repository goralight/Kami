from Tkinter import *
# from tkinter.scrolledtext import ScrolledText <-- Not sure if need?
import ttk
import tkMessageBox
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
    # 6 = reporters name
    # 7 = setup

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

# [6] # Default value for the reporters name
ReporterName = ConfigureOptions()[6]
ReporterName = ReporterName[15:]

# [7] # Default value for the setup
SetupInfo = ConfigureOptions()[7]
SetupInfo = SetupInfo[7:]


def ConfirmButtonReturn(TimerStatus, TimerCount, SVNStatus, SVNPath,
                        LocalPath, JiraType, JiraNumber, ReportersName,
                        SetupEntryInfo):
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
    :param ReportersName: String, name of the reporter for the current testing
    :param SetupEntryInfo: String, current setup for the testing environment

    Example:
    [('selected',), '60', ('selected',), 'C:/Users/jfriend.SPIDEX/Desktop/SVN',
    'C:/Users/jfriend.SPIDEX/Desktop/Kami/JiraLogs', 'EP', '426', 'JFriend',
    'W10, S4B26, SQL2016, Chrome']
    """

    # List of getters for pulling data of where their respective location is
    # within the gui. TimerStatus checks the state of the timer checkbox and
    # assigns it to the var and so on...
    TimerStatus = TimerStatus.state()
    TimerCount = TimerCount.get()
    SVNStatus = SVNStatus.state()
    SVNPath = SVNPath.get()
    LocalPath = LocalPath.get()
    JiraType = JiraType.get()
    JiraNumber = JiraNumber.get()
    ReportersName = ReportersName.get()
    SetupEntryInfo = SetupEntryInfo.get()

    # Once all assigned place in a list to work with.
    DataList = [TimerStatus, TimerCount, SVNStatus,
                SVNPath, LocalPath, JiraType,
                JiraNumber, ReportersName, SetupEntryInfo]

    # Debuggin on whats being brought over
    # print DataList
    return DataList


def ValidationError(ErrorMessage):
    """
    Simple error popup window which has the title Validation Error and
    contains the error messages which is passed through as a parameter
    :param ErrorMessage: String of the errror
    :return: The popup window itself
    """
    tkMessageBox.showerror("Validation Error!", ErrorMessage)


def ClearWindow(*args):
    """
    Cleans the window, should input as many frames as is needed
    for just showing the root window. But this could also be used for
    clearing out just one frame.
    """
    for each in args:
        each.pack_forget()


# Placeholder function
def PrintMe():
    print "I am a placeholder!"
