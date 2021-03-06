from Files import functions

try:
    from Files import MainMenu
except ImportError:
    NeededModules = ["openpyxl", "html", "Pillow", "pyscreenshot"]
    functions.InstallModule(NeededModules)
    from Files import MainMenu

# Settings for the root window (lock the resize, default size etc...
MainMenu.root.resizable(0, 0)  # Disable resizing
MainMenu.root.geometry("+800+300")  # Setting spawn position
MainMenu.root.wm_attributes("-topmost", 1)  # Window sits ontop of all windows
MainMenu.root.title("Kami Notes")  # Title of the window

# Change the below to use the relative pathway to the folder structure
MainMenu.root.iconbitmap(r'Res\Images\icon.ico')  # Path to icon
# GUI.root.overrideredirect(True)  # This makes it a borderless window
# MainMenu.root.attributes("-toolwindow", 1)  # This makes it lose the minimize / expand buttons
MainMenu.root.grid_columnconfigure(4)
MainMenu.mainloop()
