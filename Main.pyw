from Files import functions
from Files import MainMenu

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
