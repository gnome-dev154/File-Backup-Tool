🗂️ File Backup Tool
A simple command-line tool to search, copy, and archive files on your system — fast and with no dependencies beyond Python.

✨ Features
🔍 Search for files by name/query from any directory
📁 Copy matched files to a new folder (with metadata preserved)
🗜️ Archive matched files into a timestamped .zip backup
⏱️ Filter files by how recently they were created

📁 Project Structure
file-backup-tool/
├── app.py                  # Main entry point
└── tools/
    ├── search_tools.py     # File search logic
    └── backup/
        ├── copy_tools.py   # File copying with metadata
        └── archive_tools.py # Zip archiving logic

Requirements
Python 3.10+

Run the tool
bashpython app.py

🛠️ How It Works
When you run the program, it will ask you a few questions:
1. Where to search?
Enter path (empty input - cwd)
>>
Press Enter to search in the current directory, or type a custom path.
2. What to search for?
Looking for
>> report
3. How recent should the files be?
How much time was it created? (empty - search any file)
>> 24
Enter a number in hours (e.g. 24 = files created in the last 24 hours). Leave empty to match all files.
4. Choose an action:
Copy - 1, Archive - 2, Exit - 0
>>
CommandAction1Copy matched files to a new copy/ folder2Copy + zip matched files into a timestamped archive0Exit without doing anything

📦 Output Examples
Copy: Creates a folder like copy/ in the current directory
Archive: Creates a .zip file like backup - 2025-06-01_14-30-00.zip
