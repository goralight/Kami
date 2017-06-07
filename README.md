# Kami Notes - 0.5.5
QA Note Taker. Designed for QA users who need to make quick notes on the bug testing they are completing. Made with JIRA / External save locations in mind. It is perfect for those needing to write down quick notes along side their testing to refer to later on.

Kami Notes is written in Python. It makes use of Python 2.7.11
If you wish to use Kami Notes you will need to download the correct version of python.

OpemPyxl is required for this tool. To install using pip, use the following command:

`pip install openpyxl`

and thats it!

Within the Res folder there is a config.txt - These are your options within the tool.

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
