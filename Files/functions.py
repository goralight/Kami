import tkMessageBox
import os
from shutil import copy
import pip

"""
Name:    functions.py
Desc:    File containing all of the global functions which are used throughout
         Kami. Handles the loading of the config file along with validation error
         messages, module installs with pip, storing the config options from the
         options window, etc
Imports: 
"""

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
    # 8 = log types
    # 9 = log type colors
    # 10 = charter type
    # 11 = show history number
    # 12 = save to html option
    # 13 = enable hide

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

# [8] # Log Type value list
Logtype = ConfigureOptions()[8]
Logtype = Logtype.split(", ")
Logtype[0] = Logtype[0][10:]

# [9] # Log Type background color linked to log type
LogTypeColor = ConfigureOptions()[9]
LogTypeColor = LogTypeColor.split(", ")
LogTypeColor[0] = LogTypeColor[0][19:]

# [10] # Charter Type List
CharterType = ConfigureOptions()[10]
CharterType = CharterType.split(", ")
CharterType[0] = CharterType[0][14:]

# [11] # Show History List
HistoryListCap = ConfigureOptions()[11]
HistoryListCap = HistoryListCap[21:]

# [12] # Save to HTML
SaveHTMLOption = ConfigureOptions()[12]
SaveHTMLOption = SaveHTMLOption[14:]
SaveHTMLOption = int(SaveHTMLOption)

# [13] # enable hide checkbox
HideFocusOption = ConfigureOptions()[13]
HideFocusOption = HideFocusOption[13:]
HideFocusOption = int(HideFocusOption)


def SaveSetUpChanges(TimerOptionParam, TimerParam,
                     SVNOptionParam, SVNPathParam,
                     LocalPathParam, ReporterParam,
                     SetUpEntryParam):
    """
    Saves what the user inputs as the setup to the config. Saves the user
    entering the data manually everytime the env changes.

    :param TimerOptionParam: Timer option from main menu after options have
                             been punched in
    :param TimerParam:       Timer int from main menu after punched in
    :param SVNOptionParam:   Save to svn option after punched in
    :param SVNPathParam:     Path for svn after punched in
    :param LocalPathParam:   Local save path after punched in
    :param ReporterParam:    reporter name after punched in
    :param SetUpEntryParam:  env entry from main menu after punched in
    """
    # print SetUpEntryParam.get()
    with open(ResDir+"\config.txt", "r") as config:
        data = config.readlines()
        config.close()

    # change line n on the txt with below. Needs to \n.
    if "selected" in TimerOptionParam.state():
        data[0] = "enable_timer_default: 1\n"
    else:
        data[0] = "enable_timer_default: 0\n"

    data[1] = "default_timer: {0}\n".format(TimerParam.get())

    if "selected" in SVNOptionParam.state():
        data[2] = "enable_save_svn: 1\n"
    else:
        data[2] = "enable_save_svn: 0\n"

    data[3] = "default_svn_path: {0}\n".format(SVNPathParam.get())
    data[4] = "default_local_save_path: {0}\n".format(LocalPathParam.get())
    data[6] = "reporter_name: {0}\n".format(ReporterParam.get())
    data[7] = "setup: {0}\n".format(SetUpEntryParam.get())

    with open(ResDir+"\config.txt", 'w') as config:
        config.writelines(data)
        config.close()


def ConfirmButtonReturn(TimerStatus, TimerCount, SVNStatus, SVNPath,
                        LocalPath, JiraType, JiraNumber, ReportersName,
                        SetupEntryInfo, CharterType, HTMLStatus):
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
    :param CharterType: String, Which charter type has been selected
    :param HTMLStatus: String, If a HTML copy will be created or not

    Example:
    [('selected',), '60', ('selected',), 'C:/Users/jfriend.SPIDEX/Desktop/SVN',
    'C:/Users/jfriend.SPIDEX/Desktop/Kami/JiraLogs', 'EP', '426', 'JFriend',
    'W10, S4B26, SQL2016, Chrome', 'BFV', ('selected',)]
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
    CharterTypeInfo = CharterType.get()
    HTMLStatus = HTMLStatus.state()

    # Once all assigned place in a list to work with.
    ConfigList = [TimerStatus, TimerCount, SVNStatus,
                  SVNPath, LocalPath, JiraType,
                  JiraNumber, ReportersName, SetupEntryInfo,
                  CharterTypeInfo, HTMLStatus]

    return ConfigList


def ValidationError(ErrorMessage):
    """
    Simple error popup window which has the title Validation Error and
    contains the error messages which is passed through as a parameter
    :param ErrorMessage: String of the error
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


def CreateHTML():
    print "make the html!"


def Die(MainLoop, ConfigList, ExcelLocal, BugNumber, FocusState):
    """
    Simple function to perform other processes before actually killing the
    script. Here could add saving / other close down features before it is
    killed from the user
    :param MainLoop: The Root frame to kill.
    :param ConfigList: List of settings, used to define what the user asked for
    :param ExcelLocal: Local path save of the excel just been created
    :param FocusState: state of the focus check box
    """
    # print "It closed and I printed before I died... YAY!"
    if "selected" in ConfigList[2]:
        if not os.path.exists(ConfigList[3]+"/"+BugNumber):
            os.makedirs(ConfigList[3]+"/"+BugNumber)
            copy(ExcelLocal, ConfigList[3]+"/"+BugNumber)
        else:
            copy(ExcelLocal, ConfigList[3]+"/"+BugNumber)

    if "selected" in ConfigList[10]:
        CreateHTML()

    # Saving Writting options
    with open(ResDir + "\config.txt", "r") as config:
        data = config.readlines()
        config.close()

    # Put all savings below
    if "selected" in FocusState:  # If hide is selected, save it
        data[13] = "enable_hide: 1\n"
    else:
        data[13] = "enable_hide: 0\n"

    with open(ResDir+"\config.txt", 'w') as config:  # Saving to config
        config.writelines(data)
        config.close()

    MainLoop.destroy()  # Same as using the W10 kill protocol

AboutInfo = """Written by John Friend (Goralight)
Email: goralight@gmail.com

Designed for QA team members for
quickly and effortlessly writing
down notes about their bug tracking or
other note taking processes.

Email me if you have any issues or
requests.

Github url:
https://github.com/goralight/Kami-Notes

\t        <3
"""


def DisplayAbout(*args):
    tkMessageBox.showinfo("About Kami Notes", AboutInfo)


def InstallModule(package):
    """
    Simple function to install the needed modules for the user if they don't
    have them installed. Requires pip to make use of it.
    :param package: List, string list of required packages
    """
    PipList = str(pip.get_installed_distributions())  # Get list of installed modules
    for item in package:
        if item not in PipList:
            print "Oops! You don't seem to have", item, "Installed!"
            print "Installing", item, ". . ."
            pip.main(['install', item])
            print ""
