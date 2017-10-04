# Kami Notes - 0.6.4

<sub>Kami Notes is opensource. If you wish to download it and make tweaks / edits to it you are free to do so. If you wish to show the world Kami, then can you please reference this GitHub page and name me as the orginal author. Thank you.<sub>

QA Note Taker. Designed for QA users who need to make quick notes on the bug testing they are completing. Made with JIRA / External save locations in mind. It is perfect for those needing to write down quick notes along side their testing to refer to later on.

Kami Notes is written in Python. It makes use of **Python 2.7.11**
And is designed for **Window10**.

OpenPyxl is required for this tool. Running Kami for the first will install it for you. Given that you have pip installed to your machine

Within the Res folder there is a config.txt - These are your options within the tool.

If you edit the setup entry within Kami, those updates will be applied to the config.txt.

| Option        | Input           | Note  |
| ------------- |-----------------|-------|
|enable_timer_default:|1/0 (int)|1 = Timer enabled. 0 = Timer Disabled|
|default_timer:|>10 (int)|Time in minutes. Higher than 10 minutes is required
|enable_save_svn:|1/0 (int)|1 = SVN enabled. 0 = Disabled|
|default_svn_path:|Pathway (str)|Path for the external save location|
|default_local_save_path:|Pathway (str)|Path for local save location|
|jira_types:|List (entry, entry2, entry3)|List of JIRA types. Seperated via a comma and space (, )|
|reporter_name:|Name (str)|Default name|
|setup:|Setup of Environment (str)|Current environment testbed|
|log_type:|List (entry, entry2, entry3)|List of note types. Seperated via a comma and space (, )|
|log_type_bg_color:|List (entry, entry2, entry3)|List of colors. Linked to log_type. Amount must match. Seperated via a comma and space (, )|
|charter_type:|List (entry, entry2, entry3)|List of Charter types. Seperated via a comma and space (, )|
|save_to_html:|1/0 (int)|1 = Save to Html enabled. 0 = Save to Html disabled|
|enable_hide:|1/0 (int)|1 = Hide enabled. 0 = Hide disabled. Hide allows Kami to set alpha to 0.5 when focus is lost from the main window.|
