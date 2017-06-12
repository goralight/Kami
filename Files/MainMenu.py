from functions import *
from Input import *
from ExcelFunctions import *
import tkFileDialog
import ttk

"""
Main menu for everything.
This is where the user will state any option changes which are
called by default.
Includes saving to SVN, path to SVN location, changing the timer, JIRA number
JIRA Link, etc...
"""

KamiVersion = "0.5.10"

# Must build a window to host the buttons and widgets you call
# root is the default var name for Tkinter main window. Root of all the stuffs
root = Tk()
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
OptionFramePadding = 12


class MainMenuFrames:
    def __init__(self, master):
        """
        Creates the 2 Frames used within the main menu.
        TitleFrame contains the title / Name of the software
        OptionsLabelFrame contains the options which can be changed by the user
        :param master: root window
        """
        # Need self if you want to call the attribute later on, see
        # Title = TitleLabel(MainMenu.TitleFrame)
        self.TitleFrame = ttk.Frame(master)
        self.OptionsLabelFrame = Frame(master)

        self.TitleFrame.pack(side=TOP,
                             fill="both",
                             expand=True)
        self.OptionsLabelFrame.pack(padx=12,
                                    pady=(24, 12))


class TitleLabel:
    def __init__(self, topframe):
        """
        Creates the title labels. Title, Subtitle and version number.
        Packs them in one after another ontop of each other
        :param topframe: TitleFrame (The top frame)
        """
        MainTitle = ttk.Label(topframe,
                              text="Kami Notes",
                              font=("Verdana", 24))
        SubTitle = ttk.Label(topframe,
                             text="QA Note Taker",
                             font="Verdana")
        VersionNumber = ttk.Label(topframe,
                                  text=KamiVersion,
                                  font=("Verdana", 8))
        MainTitle.pack()
        SubTitle.pack()
        VersionNumber.pack()


class OptionsContent:
    @staticmethod
    def naccheck(e, i, b):
        """
        This checks to see what the state of the tick box is, and then edits
        the entry, and button if there is one to edit.
        :param e: Short for entry, this is the entry next to the tickbox
        :param i: short for int, this is the state of the tick box 1/0
        :param b: short for button, the browse button basically
        """
        # If it is the SVN entry
        if "/" in e.get() or "\\" in e.get():
            if i.get() == 1:
                e.configure(state='normal')
                b.configure(state='normal')
            else:
                e.configure(state='disabled')
                b.configure(state='disabled')
        else:  # Else it is this timer entry
            if i.get() == 1:
                e.configure(state='normal')
            else:
                e.configure(state='disabled')

    def __init__(self, bottomframe, topframe):
        """
        The meat of the option content.
        :param bottomframe: The OptionLabelFrame, the bottom one.
        """

        # Please please change the below two fucntions as its bad...
        # Although dont think its possible :/
        def AskSVNDir():
            """
            This makes use of the tkFileDialog.askdirectory() function from
            TK. It populates the screen with a dir browser which will then
            return the path to the dir you selected.

            This is copied twice and shouldnt be... AskLocalDir()
            :return: Path of the selected dir from the popup window
            """
            dirname = tkFileDialog.askdirectory(**self.dir_opt)
            if dirname:
                var.set(dirname)

        def AskLocalDir():
            dirname = tkFileDialog.askdirectory(**self.dir_opt)
            if dirname:
                var2.set(dirname)

        # Was moved from CreateSVNEntry()
        # Stores the path of the browse buttons into these vars. var=SVN
        # var2=localpath
        var = StringVar(MainMenu.OptionsLabelFrame)
        var2 = StringVar(MainMenu.OptionsLabelFrame)

        # Options for browsing for a dir
        # Used by tkFileDialog.askdirectory
        # Options list: https://tkinter.unpythonic.net/wiki/tkFileDialog
        self.dir_opt = options = {}
        options["initialdir"] = "C:\\"
        options["mustexist"] = True
        options["parent"] = root

        # Entry for the time specified by the user for the timer length
        TimerEntry = ttk.Entry(bottomframe, width=6)
        TimerEntry.insert(END, DefaultTimerValue)  # Pulled from the config.txt
        OptionInt = IntVar()
        # In order to use this, need to set the
        # variable option within the widget defining.
        # see optiontimer "variable=OptionInt"

        # Defines the tickbox for asking the user if they would like to use the
        # Timer. Makes use of the naccheck function
        OptionTimer = ttk.Checkbutton(bottomframe,
                                      text="Enable Timer",
                                      state="normal",
                                      variable=OptionInt,
                                      command=lambda e=TimerEntry, i=OptionInt:
                                      self.naccheck(e, i, None))

        # This checks the config file, if the default for using the timer is
        # 1 it will set the entry to enabled otherwise itll set it to disabled
        if EnableTimerTickBox == 1:
            TimerEntry.configure(state="normal")
        else:
            TimerEntry.configure(state="disabled")

        # Similar to above, except if its 1 it will make the tick box ticked
        # no need for else as default is 0
        if EnableTimerTickBox == 1:
            OptionTimer.invoke()  # Makes it ticked on start up

        # Puts the optiontimer tick box inline
        OptionTimer.grid(padx=(5, 5), sticky=W)

        # Define the timer input label which is left of the entry itself
        TimerInputLabel = Label(bottomframe,
                                text="Enter Timer in Minutes")

        # Defines the browse button which allows the user to search for a dir
        # to place their jira log onto SVN. Makes use of the AskSVNDir function
        SVNBrowseButton = ttk.Button(bottomframe,
                                     text="Browse...",
                                     state="normal",
                                     command=AskSVNDir)

        # Defines the label which is to the left of the Jira number entry and
        # drop down menu
        JiraNumberLabel = ttk.Label(bottomframe,
                                    text="JIRA Log Number")
        # Allows to pull the value from the entry of the Jira entry
        JiraStr = StringVar()
        # Defines the dropdown menu. JiraList is pulled from the config.txt.
        # The first of the list is the first of the menu and then the rest
        # follow

        JiraTypeList = ttk.OptionMenu(bottomframe, JiraStr,
                                      JiraList[0], *JiraList)

        CharterStr = StringVar()

        CharterTypeList = ttk.OptionMenu(bottomframe, CharterStr,
                                         CharterType[0], *CharterType)

        # Defines the Entry for the Jira Number.
        JiraNumberEntry = ttk.Entry(bottomframe,
                                    width=6)
        # Defines the quit button which is at the very bottom left of the
        # window. Simply kills the root window thus killing everything
        QuitButton = ttk.Button(bottomframe,
                                text="Quit",
                                command=root.quit)

        # Draws the timer input label.
        TimerInputLabel.grid(row=0, column=3, sticky=W+E, padx=(0, 47))
        # Draws the Timer Entry
        TimerEntry.grid(row=0, column=3, padx=(5, 5), pady=(0, 5), sticky=E)

        def CreateSVNEntry(status):
            """
            Defines and draws the SVNPAth entry
            :param status: Leave as a empty string, it inits the var.set()
            :return: The SVN entry itself
            """
            var.set(status)
            SVNEntry = ttk.Entry(bottomframe, width=27, textvariable=var)
            SVNEntry.insert(END, SVNDefaultPath)  # Set by the config.txt
            SVNEntry.grid(row=1, column=2, padx=(5, 5), columnspan=2, sticky=E)
            return SVNEntry

        # Calls the creation and drawing of the SVN Entry
        CreateSVNEntry = CreateSVNEntry("")

        # Allows to store a int as SVNInt within the OptionSaveSVN
        SVNInt = IntVar()

        # Defines the tickbox for saving to SVN
        # Makes use of the naccheck functions
        OptionSaveSVN = ttk.Checkbutton(bottomframe,
                                        text="Save to SVN",
                                        state="normal",
                                        variable=SVNInt,
                                        command=lambda e=CreateSVNEntry,
                                        i=SVNInt, b=SVNBrowseButton:
                                        self.naccheck(e, i, b))

        # Checks the config and if set to one, set everything linked to on
        if EnableSaveToSVN == 1:
            CreateSVNEntry.configure(state="normal")
            SVNBrowseButton.configure(state="normal")
            OptionSaveSVN.invoke()
        else:  # else set it to off
            CreateSVNEntry.configure(state="disabled")
            SVNBrowseButton.configure(state="disabled")

        # Draws the tick box for save to svn
        OptionSaveSVN.grid(padx=(5, 5), row=1, sticky=W)

        # Draws the SVN browse for dir button
        SVNBrowseButton.grid(row=2, column=3,
                             padx=(0, 5),
                             pady=(1, 5), sticky=E)

        # defines the PathToLocalLabel, just displays the text
        PathToLocalLabel = ttk.Label(bottomframe,
                                     text="Local Save Path")

        def CreateLocalPathEntry(status):
            """
            Similar to CreateSVNEntry
            :param status: leave as a empty string, inits the var2.set()
            :return: the Local Path Entry itself
            """
            var2.set(status)
            PathToLocalEntry = ttk.Entry(bottomframe,
                                         width=27,
                                         textvariable=var2)
            PathToLocalEntry.insert(END, LocalSavePathway)
            PathToLocalEntry.grid(row=3, column=3,
                                  padx=(0, 5), pady=(0, 0), sticky=E)
            return PathToLocalEntry

        # Calls the defining and drawing of the Local Path entry
        CreateLocalPath = CreateLocalPathEntry("")

        # Defines the local path browse button, makes use of the AskLocalDir()
        PathToLocalBrowseButton = ttk.Button(bottomframe,
                                             text="Browse...",
                                             state="normal",
                                             command=AskLocalDir)

        def ConfirmButtonFunctions(*args):
            """
            This is used to make the confirm button run more than one function
            on clicking it. It also contains the validation of the data
            inputted from the user. Once the validation is sound it will then
            fire off the function to go to the actual logging part of Kami
            """
            ConfigList = ConfirmButtonReturn(OptionTimer,
                                             TimerEntry,
                                             OptionSaveSVN,
                                             CreateSVNEntry,
                                             CreateLocalPath,
                                             JiraStr,  # DropDown Menu
                                             JiraNumberEntry,
                                             ReporterNameEntry,
                                             SetupEntry,
                                             CharterStr,
                                             HTMLOption)

            # List of charas needed for a path to be a path
            PathValidation = ["\\", "/", ":"]

            # If timer is empty string, itll just switch it over to 0
            if ConfigList[1] == "":
                try:
                    ConfigList[1] = int(ConfigList[1])
                except ValueError:
                    ConfigList[1] = 0

            # If timer cant be converted to int, throw error
            try:
                ConfigList[1] = int(ConfigList[1])
            except ValueError:
                Error = "Only numbers allowed when setting a timer!"
                ValidationError(Error)
                print Error
                return

            # Validation for making timer be more than 10mins only if the tick
            # box for wanting a timer is enabled
            if ConfigList[1] < 10 and "selected" in ConfigList[0]:
                Error = "Timer must be set higher than 10 minutes!"
                ValidationError(Error)
                print Error
                return

            # Validation for saving to SVN enabled but no path given
            if "selected" in ConfigList[2] and ConfigList[3] == "":
                Error = "Can't have save to SVN enabled and empty path!"
                ValidationError(Error)
                print Error
                return

            # Validation for checking to see if the SVN path given is valid
            # given that the tick box for save to SVN to ticked
            if not any(x in ConfigList[3] for x in PathValidation) and "selected" in ConfigList[2]:
                Error = "Not a valid path! Please change the SVN path!"
                ValidationError(Error)
                print Error
                return

            # Validation to check the local save path is empty (must never be)
            if ConfigList[4] == "":
                Error = "Local save path can't be empty!"
                ValidationError(Error)
                print Error
                return

            # Validation for making sure the SVN path is valid. It compares the
            # list of charas needed for a path with the given path
            if not any(x in ConfigList[4] for x in PathValidation):
                Error = "Not a valid path! Please change the local save path!"
                ValidationError(Error)
                print Error
                return

            # Validation for making sure the Jira entry isnt empty as it is a
            # requirement to link the Jira log to the work youre testing
            if ConfigList[6] == "":
                Error = "The JIRA number log can't be empty!"
                ValidationError(Error)
                print Error
                return

            # If Jira entry cant be converted to a int, throw error.
            try:
                ConfigList[6] = int(ConfigList[6])
            except ValueError:
                Error = "Only numbers allowed for JIRA log number!"
                ValidationError(Error)
                print Error
                return

            # Validation for making sure the reporters name isnt empty
            if ConfigList[7] == "":
                Error = "Reporters name can't be empty! Fill in your name!"
                ValidationError(Error)
                print Error
                return

            # Validation for making sure the setup cant be empty
            if ConfigList[8] == "":
                Error = "Setup can't be empty! Fill in your setup!"
                ValidationError(Error)
                print Error
                return

            # Cleans the root window of the 2 frames being used.
            ClearWindow(bottomframe, topframe)

            # print ConfigList  # Debugging

            # Removes the function linked to enter, see below
            root.unbind("<Return>")
            # Changes title to the JIRA number
            InputTitle = JiraStr.get() + "-" + JiraNumberEntry.get()
            root.title("Kami Notes    " + InputTitle)

            # Creates frame for writing stuff
            WritingFrame = Frame(root)
            ColorFrame = Frame(root, height=15, highlightbackground="#474747",
                               highlightthickness=1)
            ShowMoreFrame = Frame(root)

            Excel = InitExcel(ConfigList)  # Not sure if need this to be a var
            ColorFrame.pack(padx=(5, 5), pady=(5, 5), fill=X)
            WritingFrame.pack(padx=(5, 5), pady=(5, 5))

            CountDownTimerVar = CountDownTimer(OptionTimer, TimerEntry, WritingFrame)
            TypeOfLogVar = TypeOfLog(WritingFrame, root, ColorFrame, Logtype, LogTypeColor)
            EntryItemClass(WritingFrame, root, TypeOfLogVar.LoggingTypeLabel,
                           CountDownTimerVar.TimerCountLabel, Excel.CurrentWorkingExcelPath,
                           ConfigList)
            SmallHistory(WritingFrame, ShowMoreFrame, HistoryListCap)
            SeeThroughSlider(WritingFrame, root)

            root.protocol("WM_DELETE_WINDOW", lambda: Die(root, ConfigList, Excel.CurrentWorkingExcelPath))

        # Makes it so you can hit enter instead of clicking confirm
        root.bind("<Return>", ConfirmButtonFunctions)

        # Defines the confirm button, makes use of the ConfirmButtonFunctions()
        ConfirmButton = ttk.Button(bottomframe,
                                   text="Confirm",
                                   command=lambda: ConfirmButtonFunctions(),
                                   state="active",
                                   default="active")

        # Draws the PathToLocalLabel Label
        PathToLocalLabel.grid(row=3, column=0,
                              sticky=W, padx=(5, 0),
                              pady=(0, 5))

        # Draws the LoackPath Button
        PathToLocalBrowseButton.grid(row=4, column=3,
                                     padx=(0, 5), pady=(0, 5), sticky=E)

        # Draws the Jira Label
        JiraNumberLabel.grid(row=5, column=0,
                             sticky=W, padx=(5, 0),
                             pady=(0, 5))

        # Draws the Drop down menu
        JiraTypeList.grid(row=5, column=3,
                          sticky=E, padx=(0, 55),
                          pady=(0, 0))

        # Draws the Jira Number entry
        JiraNumberEntry.grid(row=5, column=3,
                             sticky=E, padx=(0, 7),
                             pady=(0, 0))

        ChaterLabel = ttk.Label(bottomframe,
                                text="Charter Type")

        ChaterLabel.grid(row=6, sticky=W, padx=(5, 0), pady=(0, 5))

        CharterTypeList.grid(row=6, column=3,
                             sticky=E, padx=(0, 7),
                             pady=(5, 5))

        # Defines the reporter name label
        ReporterNameLabel = ttk.Label(bottomframe,
                                      text="Reporters Name")

        # Defines the Report name Entry
        ReporterNameEntry = ttk.Entry(bottomframe, width=27)
        ReporterNameEntry.insert(END, ReporterName)  # Placeholder via config

        # Draws the reporter name Label
        ReporterNameLabel.grid(row=8, sticky=W, padx=(5, 0), pady=(0, 5))

        # Defines the setup label
        SetupLabel = ttk.Label(bottomframe,
                               text="Setup")

        # Defines the setup Entry and places
        SetupEntry = ttk.Entry(bottomframe, width=27)
        SetupEntry.insert(END, SetupInfo)  # Placeholder text defined by config

        # Draws the entry for the reporter name
        ReporterNameEntry.grid(row=8, column=3,
                               sticky=E, padx=(0, 7),
                               pady=(0, 5))

        # Draws the setup label text
        SetupLabel.grid(row=9, sticky=W, padx=(5, 0), pady=(0, 5))

        # Draws the Setup Entry
        SetupEntry.grid(row=9, column=3,
                        sticky=E, padx=(0, 7),
                        pady=(0, 5))

        # This is how checkboxes should be done. Without intVar \/
        HTMLOption = ttk.Checkbutton(bottomframe,
                                     text="Generate HTML",
                                     state="normal",)

        if SaveHTMLOption == 1:  # if config = 1, make it remove box and make ticked
            HTMLOption.state(["!alternate", "selected"])
        else:  # else just make it blank
            HTMLOption.state(["!alternate"])

        HTMLOption.grid(row=10, column=3,
                        sticky=E, padx=(0, 6),
                        pady=(0, 5))

        # Draws the Quit button
        QuitButton.grid(row=11, column=0,
                        sticky=W, padx=(5, 0),
                        pady=(0, 5))

        # Draws the Confirm button
        ConfirmButton.grid(row=11, column=3,
                           sticky=W+E, padx=(0, 5),
                           pady=(0, 5))

        # TODO: Need to refactor the shit out of this
        # This is messy af - you need to move the lines around and make it
        # easier to read and follow, instead of it looking hacky as php code

MainMenu = MainMenuFrames(root)
Title = TitleLabel(MainMenu.TitleFrame)
Options = OptionsContent(MainMenu.OptionsLabelFrame, MainMenu.TitleFrame)
