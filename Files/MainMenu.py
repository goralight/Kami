from Tkinter import *
from functions import *
from tkinter.scrolledtext import ScrolledText
import tkFileDialog
import ttk

"""
Main menu for everything.
This is where the user will state any option changes which are
called by default.
Includes saving to SVN, path to SVN location, changing the timer, JIRA number
JIRA Link, etc...
"""

KamiVersion = "0.1"

# Must build a window to host the buttons and widgets you call
# root is the default var name for Tkinter main window. Root of all the stuffs
root = Tk()
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
OptionFramePadding = 12


class MainMenuFrames:
    def __init__(self, master):
        # Need self if you want to call the attribute later on, see
        # Title = TitleLabel(MainMenu.TitleFrame)
        self.TitleFrame = ttk.Frame(master)
        self.OptionsLabelFrame = ttk.LabelFrame(master, text="Options")

        self.TitleFrame.pack(side=TOP,
                             fill="both",
                             expand=True)
        self.OptionsLabelFrame.pack(padx=OptionFramePadding,
                                    pady=OptionFramePadding)


class TitleLabel:
    def __init__(self, topframe):
        MainTitle = ttk.Label(topframe,
                              text="Kami",
                              font=("Arial", 24))
        SubTitle = ttk.Label(topframe,
                             text="QA Note Taker",
                             font="Arial")
        VersionNumber = ttk.Label(topframe,
                                  text=KamiVersion,
                                  font=("Arial", 8))
        MainTitle.pack()
        SubTitle.pack()
        VersionNumber.pack()


class OptionsContent:
    def naccheck(self, e, i, b):
        if ":/" in e.get() or ":\\" in e.get():
            if i.get() == 1:
                e.configure(state='normal')
                b.configure(state='normal')
            else:
                e.configure(state='disabled')
                b.configure(state='disabled')
        else:
            if i.get() == 1:
                e.configure(state='normal')
            else:
                e.configure(state='disabled')

    def __init__(self, bottomframe):

        # Please please change the below two fucntions as its bad...
        def AskSVNDir():
            dirname = tkFileDialog.askdirectory(**self.dir_opt)
            if dirname:
                var.set(dirname)

        def AskLocalDir():
            dirname = tkFileDialog.askdirectory(**self.dir_opt)
            if dirname:
                var2.set(dirname)

        # Was moved from CreateSVNEntry()
        var = StringVar(MainMenu.OptionsLabelFrame)
        var2 = StringVar(MainMenu.OptionsLabelFrame)

        # Options for browsing for a dir
        self.dir_opt = options = {}
        options["initialdir"] = "C:\\"
        options["mustexist"] = False
        options["parent"] = root

        TimerEntry = ttk.Entry(bottomframe, width=6)
        TimerEntry.insert(END, DefaultTimerValue)
        OptionInt = IntVar()
        # In order to use this, need to set the
        # variable option within the widget defining.
        # see optiontimer "variable=OptionInt"

        OptionTimer = ttk.Checkbutton(bottomframe,
                                      text="Enable Timer",
                                      state="normal",
                                      variable=OptionInt,
                                      command=lambda e=TimerEntry, i=OptionInt:
                                      self.naccheck(e, i, None))

        if EnableTimerTickBox == 1:
            OptionTimer.configure(state="active")
            TimerEntry.configure(state="normal")
        else:
            TimerEntry.configure(state="disabled")

        if EnableTimerTickBox == 1:
            OptionTimer.invoke()  # Makes it ticked on start up

        TimerInputLabel = Label(bottomframe,
                                text="Enter Timer in Minutes")

        SVNBrowseButton = ttk.Button(bottomframe,
                                     text="Browse...",
                                     state="normal",
                                     command=AskSVNDir)
        JiraNumberLabel = ttk.Label(bottomframe,
                                    text="JIRA Log Number")
        v = StringVar(root)
        v.set("one")
        JiraTypeList = ttk.OptionMenu(bottomframe, v, JiraList[0], *JiraList)
        JiraNumberEntry = ttk.Entry(bottomframe,
                                    width=6)
        QuitButton = ttk.Button(bottomframe,
                                text="Quit",
                                command=root.quit)
        ConfirmButton = ttk.Button(bottomframe,
                                   text="Confirm",
                                   command=PrintMe,
                                   state="activate",
                                   default="active")

        OptionTimer.grid(sticky=W)

        TimerInputLabel.grid(row=0, column=3, sticky=W+E, padx=(0, 47))
        TimerEntry.grid(row=0, column=3, padx=(5, 5), pady=(0, 1), sticky=E)

        def CreateSVNEntry(status):
            text = status
            var.set(text)
            SVNEntry = ttk.Entry(bottomframe, width=27, textvariable=var)
            SVNEntry.insert(END, SVNDefaultPath)
            SVNEntry.grid(row=1, column=2, padx=(5, 5), columnspan=2, sticky=E)
            return SVNEntry

        SVNEntry = CreateSVNEntry("")

        SVNInt = IntVar()
        OptionSaveSVN = ttk.Checkbutton(bottomframe,
                                        text="Save to SVN",
                                        state="normal",
                                        variable=SVNInt,
                                        command=lambda e=SVNEntry,
                                        i=SVNInt, b=SVNBrowseButton:
                                        self.naccheck(e, i, b))

        if EnableSaveToSVN == 1:
            OptionSaveSVN.configure(state="active")
            SVNEntry.configure(state="normal")
            SVNBrowseButton.configure(state="normal")
            OptionSaveSVN.invoke()
        else:
            SVNEntry.configure(state="disabled")
            SVNBrowseButton.configure(state="disabled")

        OptionSaveSVN.grid(row=1, sticky=W)

        SVNBrowseButton.grid(row=2, column=3,
                             padx=(0, 5), sticky=E)

        PathToLocalLabel = ttk.Label(bottomframe,
                                     text="Local Save Path")

        def CreateLocalPathEntry(status):
            text = status
            var2.set(text)
            PathToLocalEntry = ttk.Entry(bottomframe,
                                         width=27,
                                         textvariable=var2)
            PathToLocalEntry.insert(END, LocalSavePathway)
            PathToLocalEntry.grid(row=3, column=3,
                                  padx=(0, 5), sticky=E)
            return PathToLocalEntry

        CreateLocalPathEntry("")

        PathToLocalBrowseButton = ttk.Button(bottomframe,
                                             text="Browse...",
                                             state="normal",
                                             command=AskLocalDir)

####################################
        PathToLocalLabel.grid(row=3, column=0,
                              sticky=W, padx=(5, 0),
                              pady=(0, 5))

        PathToLocalBrowseButton.grid(row=4, column=3,
                                     padx=(0, 5), sticky=E)

        JiraNumberLabel.grid(row=5, column=0,
                             sticky=W, padx=(5, 0),
                             pady=(0, 5))
        JiraTypeList.grid(row=5, column=3,
                          sticky=E, padx=(0, 55))
        JiraNumberEntry.grid(row=5, column=3,
                             sticky=E, padx=(0, 7))

        QuitButton.grid(row=6, column=0,
                        sticky=W, padx=(5, 0),
                        pady=(0, 5))
        ConfirmButton.grid(row=6, column=3,
                           sticky=W+E, padx=(0, 5),
                           pady=(0, 5))


MainMenu = MainMenuFrames(root)
Title = TitleLabel(MainMenu.TitleFrame)
Options = OptionsContent(MainMenu.OptionsLabelFrame)
