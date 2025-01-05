CLI File Explorer 🗂️
A minimalist, keyboard-driven file explorer for the Windows command line. Navigate your filesystem with elegance and speed.
✨ Features
Core Functionality

⌨️ Keyboard-Centric Navigation

Seamless directory traversal with arrow keys
Quick file access and preview capabilities



Visual Design

🎨 Color-Coded File Types
Copy📂 Directories     │ Yellow
📄 PDFs           │ Red
🖼️ Images         │ Cyan
📝 Text Files     │ Green
📊 Office Docs    │ Magenta


Interface

📺 Dual-Panel Layout

File tree navigation on the left
Instant file preview on the right
Adjustable panel ratio with [ and ] keys



System Integration

🚀 Smart File Handling

Launches files with system defaults
Instant text file preview
Detailed info for binary files



🛠️ Installation
Prerequisites
bashCopypip install pyinstaller windows-curses pillow
Quick Setup

Get the Code
bashCopygit clone https://github.com/yourusername/cli-file-explorer.git
cd cli-file-explorer

Build
bashCopypyinstaller --onefile --name cli-file-explorer cli_explorer.py

System Integration (PowerShell Admin)
powershellCopy$folder = "C:\Tools"
New-Item -ItemType Directory -Force -Path $folder
Copy-Item ".\dist\cli-file-explorer.exe" -Destination $folder
$oldPath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
$newPath = $oldPath + ";$folder"
[Environment]::SetEnvironmentVariable('Path', $newPath, 'Machine')


🎮 Controls
KeyAction↑ ↓Navigate itemsEnterOpen file/directoryBackspaceParent directory[ ]Adjust panel widthPage Up/DownScroll previewQExit
💻 Development
Setup Dev Environment
bashCopygit clone https://github.com/yourusername/cli-file-explorer.git
cd cli-file-explorer
pip install -r requirements.txt
Requirements

Windows OS
Python 3.x
Required packages:

windows-curses
Pillow (PIL)



🤝 Contributing
We welcome contributions! Here's how:

Fork the Project
Create your Feature Branch
bashCopygit checkout -b feature/AmazingFeature

Commit your Changes
bashCopygit commit -m 'Add some AmazingFeature'

Push to the Branch
bashCopygit push origin feature/AmazingFeature

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.
