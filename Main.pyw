from Files import MainMenu
import os


###############################################################################
# List of things to do! #
#
# Make gui
#   needs to have a menu when you fire it to allow options to be changed
#       options can be edited so that the default is stored in a options file
#       options should be default timer, ...
#   needs a logical flow.
#   when you get past the options itll display the text box
#   Make gui take priority (always on top)
#   un sizable (static)
#
# Able to edit entries after being submitted
# Timer - length can be edited in the options file and when firing up
# Pause timer
# Alarm when you are a minute (can be edited) away from the timer
#                             (% of the time left? like 20% of time left?)
#
###############################################################################

# Settings for the root window (lock the resize, default size etc...
MainMenu.root.resizable(0, 0)  # Disable resizing
# GUI.root.geometry("1000x333")  # Setting size for window
MainMenu.root.wm_attributes("-topmost", 1)  # Window sits ontop of all windows
MainMenu.root.title("Kami - QA Note Taker")  # Title of the window
# Change the below to use the relative pathway to the folder structure
# GUI.root.iconbitmap(r'Res\icon.ico')  # Path to icon
# GUI.root.overrideredirect(True)  # This makes it a borderless window
MainMenu.root.attributes("-toolwindow", 1)
MainMenu.root.grid_columnconfigure(4)
MainMenu.mainloop()
