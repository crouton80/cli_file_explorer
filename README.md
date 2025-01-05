CLI File Explorer
A lightweight, keyboard-driven file explorer for the Windows command line interface. Navigate through your filesystem, preview files, and launch applications using just your keyboard.
![CLI File Explorer Screenshot]
<!-- Add a screenshot of your application here -->
Features

Keyboard Navigation: Move through directories and files using arrow keys
Split-Panel View: File tree on the left, file preview on the right
Color-Coded Files: Different colors for various file types:

Yellow: Directories
Red: PDF files
Cyan: Image files (.jpg, .png, etc.)
Green: Text files
Magenta: Office documents
White: Other files


File Preview: Instant preview for text files and file information for other formats
Adjustable Panel Size: Customize the split view ratio using [ and ] keys
System Integration: Launch files with their default applications

Installation

Install dependencies:

bashCopypip install pyinstaller windows-curses pillow

Clone the repository:

bashCopygit clone https://github.com/yourusername/cli-file-explorer.git
cd cli-file-explorer

Build the executable:

bashCopypyinstaller --onefile --name cli-file-explorer cli_explorer.py

Add to system PATH (Run PowerShell as Administrator):

powershellCopy$folder = "C:\Tools"
New-Item -ItemType Directory -Force -Path $folder
Copy-Item ".\dist\cli-file-explorer.exe" -Destination $folder
$oldPath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
$newPath = $oldPath + ";$folder"
[Environment]::SetEnvironmentVariable('Path', $newPath, 'Machine')
Usage
Launch from any terminal:
bashCopycli-file-explorer
Controls

↑/↓: Navigate through files and directories
Enter: Open file/directory
Backspace: Go up one directory level
[/]: Adjust panel split ratio
Page Up/Down: Scroll file preview
Q: Quit application

Requirements

Windows OS
Python 3.x
windows-curses
Pillow (PIL)

Development
To modify the source code:

Clone the repository
Install development dependencies:

bashCopypip install -r requirements.txt

Make your changes to cli_explorer.py
Rebuild using the provided build.bat

Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

License
Distributed under the MIT License. See LICENSE for more information.
Acknowledgments

Inspired by terminal-based file managers like ranger and midnight commander
Built with Python's curses library
