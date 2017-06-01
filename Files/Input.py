from Tkinter import *
from tkinter import font
import tkFont
import ScrolledText
import tkMessageBox
import tkFileDialog
import ttk
import os
import time
import datetime
import winsound
import threading


class EntryItemClass:
    def __init__(self, frame):
        self.frame = frame

        self.LogEntry = ttk.Entry(self.frame, width=90,
                                  font=font.Font(family="Verdana", size=12))
        self.LogEntry.grid(column=0, row=1, columnspan=3, pady=(5, 5))


class SeeThroughSlider:
    def __init__(self, frame, root):
        self.frame = frame
        self.root = root

        self.SliderEntry = ttk.Scale(self.frame, from_=0.5, to=1, command=self.SetSeeThrough)
        self.SliderEntry.set(100)
        self.SliderEntry.grid(column=0, row=2, sticky=W)

    def SetSeeThrough(self, *args):
        ScaleEntryValue = round(self.SliderEntry.get(), 2)
        self.root.wm_attributes('-alpha', ScaleEntryValue)
        # print ScaleEntryValue


class SmallHistory:
    def __init__(self, frame):
        self.frame = frame
        self.HistoryCount = 1

        self.SeeMoreLabel = ttk.Label(self.frame, text="See History", cursor="hand2", foreground="#3D8CDF")
        if self.HistoryCount != 0:
            self.SeeMoreLabel.grid(column=0, row=2, columnspan=3)
        self.SeeMoreLabel.bind("<Button-1>", self.ShowHistory)

        u = tkFont.Font(self.SeeMoreLabel, self.SeeMoreLabel.cget("font"))
        u.configure(underline=True)
        self.SeeMoreLabel.configure(font=u)

    def ShowHistory(self, event):
        # Read the newly created bug log, find the last 3 by getting Historycount
        # adding that to the total lines found(?) and printing the last three, and then
        # Assigning that value to HistoryCount
        print "i was clicked!"


class TypeOfLog:
    def __init__(self, frame, root, colorframe):
        self.frame = frame
        self.root = root
        self.colorframe = colorframe

        self.WhichType = ["Note", "Bug", "Test", "Question", "Check", "Next Time"]
        # My Purple, red, green, yellow, blue, grey
        self.WhichTypeBGColor = ["#8150E2", "#C81616", "#14A019", "#f6f628", "#3D8CDF", "#474747"]
        self.Index = 0

        self.root.bind("<KeyRelease-Up>", self.UpSelectionLogType)
        self.root.bind("<KeyRelease-Down>", self.DownSelectionLogType)

        self.colorframe.configure(background=self.WhichTypeBGColor[self.Index], borderwidth=2)

        self.LoggingTypeLabel = Label(self.frame, text=self.WhichType[self.Index],
                                      font="Verdana", cursor="hand2")
        self.LoggingTypeLabel.grid(column=2, row=0, sticky=E)
        self.LoggingTypeLabel.bind("<ButtonRelease-1>", self.UpSelectionLogType)
        self.LoggingTypeLabel.bind("<ButtonRelease-3>", self.DownSelectionLogType)

    def UpSelectionLogType(self, event):
        if self.Index < len(self.WhichType)-1:
            self.Index += 1
            self.LoggingTypeLabel.configure(text=self.WhichType[self.Index])
            self.colorframe.configure(background=self.WhichTypeBGColor[self.Index])
        else:
            self.Index = 0
            self.LoggingTypeLabel.configure(text=self.WhichType[self.Index])
            self.colorframe.configure(background=self.WhichTypeBGColor[self.Index])

    def DownSelectionLogType(self, event):
        if self.Index > 0:
            self.Index -= 1
            self.LoggingTypeLabel.configure(text=self.WhichType[self.Index])
            self.colorframe.configure(background=self.WhichTypeBGColor[self.Index])
        else:
            self.Index = len(self.WhichType)-1
            self.LoggingTypeLabel.configure(text=self.WhichType[self.Index])
            self.colorframe.configure(background=self.WhichTypeBGColor[self.Index])


class CountDownTimer:
    def __init__(self, TimerStatus, TimerCount, frame):
        """
        Inits the CountDownTimer - This is used to tell the user how long is
        left on the countdown timer. Grabs the inputted time from the user in
        the timer entry
        :param TimerStatus: Grabbed from OptionTimer - see if the tick box is
                            selected or not. If it isnt the timer isnt drawn
                            but the logic is set in place still
        :param TimerCount:  Grabbed from TimerEntry and is the time in minutes
                            set by the user. It is * by 60 to turn the entry
                            from seconds to minutes so that it can be worked
                            with correctly. If the TimerCount < 20% of
                            remaining time it will bleep and turn font red
        :param frame:       Which frame the timer is drawn on
        """
        # TimerAlarm = datetime.timedelta(minutes=TimerAlarm)
        self.TimerCount = TimerCount
        self.TimerStatus = TimerStatus
        self.frame = frame

        self.TimerState = 1  # 1=Ticking, 0=paused
        self.TimerStatus = TimerStatus.state()
        self.TimerCount = TimerCount.get()
        self.TimerCount = int(self.TimerCount) * 60  # Make it into seconds. 60*60=3600seconds=1hour
        self.TimerAlarm = 0.2 * self.TimerCount  # change float for different percentage
        self.TimerAlarm = datetime.timedelta(seconds=self.TimerAlarm)
        self.TimerCount = datetime.timedelta(seconds=self.TimerCount)
        self.TimerCountLabel = ttk.Label(frame, text=self.TimerCount, font="Verdana", cursor="hand2")
        self.TimerCountLabel.bind("<ButtonRelease-1>", self.ChangeTimerState)
        if "selected" in self.TimerStatus:  # Only draws timer if state is true
            self.TimerCountLabel.grid(column=0, row=0, sticky=W)
        else:
            return
        self.frame.after(1000, self.Update)

    @staticmethod
    def BleepSound():
        for x in range(0, 3):
            winsound.Beep(3278, 500)

    def Update(self):
        if self.TimerState == 1:
            self.TimerCount = self.TimerCount - datetime.timedelta(seconds=1)
            self.TimerCountLabel.configure(text=self.TimerCount)
            if self.TimerCount == self.TimerAlarm:
                # New thread so that text isnt lost if typing when bleeping
                threading.Thread(target=self.BleepSound())  # Bleeps if < 20% remaining time
                self.TimerCountLabel.configure(foreground="red")
            if str(self.TimerCount) == "0:00:00":
                self.TimerCount = datetime.timedelta(seconds=0)
                self.TimerCountLabel.configure(text=self.TimerCount, font="Verdana 12 bold")
                threading.Thread(target=self.BleepSound())  # Bleeps if timer == 0:00:00
                self.TimerCountLabel.configure(foreground="#C81616")
                return
        else:
            return
        self.frame.after(1000, self.Update)  # Every 1s, configure & redraw
        # print self.TimerCount

    def ChangeTimerState(self, *args):
        if self.TimerState == 1:
            self.TimerState = 0
            self.TimerCountLabel.configure(foreground="#8150E2")
        elif self.TimerState == 0:
            self.TimerState = 1
            if self.TimerCount < self.TimerAlarm:
                self.TimerCountLabel.configure(foreground="#C81616")
            else:
                self.TimerCountLabel.configure(foreground="black")
            self.Update()
        else:
            "The Clocks broken!"
