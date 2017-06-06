from Files import MainMenu

try:
    from openpyxl import *
except ImportError:
    print "Oops!\nYou do not have OpenPyxl installed!"
    # There should a pop up saying you dont have openpyxl installed
    quit()

###############################################################################
# List of things to do!
#
# Make gui
#   needs to have a menu when you fire it to allow options to be changed
#       options can be edited so that the default is stored in a options file
#       options should be default timer, ...
#   needs a logical flow.
#
# Able to edit entries after being submitted
###############################################################################

# Settings for the root window (lock the resize, default size etc...
MainMenu.root.resizable(0, 0)  # Disable resizing
# GUI.root.geometry("1000x333")  # Setting size for window
MainMenu.root.wm_attributes("-topmost", 1)  # Window sits ontop of all windows
MainMenu.root.title("Kami Notes    QA Note Taker")  # Title of the window
# Change the below to use the relative pathway to the folder structure
# GUI.root.iconbitmap(r'Res\icon.ico')  # Path to icon
# GUI.root.overrideredirect(True)  # This makes it a borderless window
MainMenu.root.attributes("-toolwindow", 1)
MainMenu.root.grid_columnconfigure(4)
MainMenu.mainloop()
