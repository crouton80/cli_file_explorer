# CLI File Explorer 🗂️
A minimalist, keyboard-driven file explorer for the Windows command line. Navigate your filesystem with elegance and speed.

## ✨ Features

### Core Functionality

- **⌨️ Keyboard-Centric Navigation**
  - Seamless directory traversal with arrow keys
  - Quick file access and preview capabilities

### Visual Design

- **🎨 Color-Coded File Types**
  - **📂 Directories** │ Yellow
  - **📄 PDFs** │ Red
  - **🖼️ Images** │ Cyan
  - **📝 Text Files** │ Green
  - **📊 Office Docs** │ Magenta

### Interface

- **📺 Dual-Panel Layout**
  - File tree navigation on the left
  - Instant file preview on the right
  - Adjustable panel ratio with `[ ]` keys

### System Integration

- **🚀 Smart File Handling**
  - Launches files with system defaults
  - Instant text file preview
  - Detailed info for binary files

---

## 🛠️ Installation

### Prerequisites

Make sure you have the following installed:

```bash
pip install pyinstaller windows-curses pillow
```

Quick Setup
Get the Code
```bash
git clone https://github.com/yourusername/cli-file-explorer.git
cd cli-file-explorer
```
```bash
pyinstaller --onefile --name cli-file-explorer cli_explorer.py
```
System Integration (PowerShell Admin)
```powershell
$folder = "C:\Tools"
New-Item -ItemType Directory -Force -Path $folder
Copy-Item ".\dist\cli-file-explorer.exe" -Destination $folder
$oldPath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
$newPath = $oldPath + ";$folder"
[Environment]::SetEnvironmentVariable('Path', $newPath, 'Machine')
```

🎮 Controls

↑ ↓ Navigate items
Enter Open file/directory
Backspace Parent directory
[ ] Adjust panel width
Page Up/Down Scroll preview
Q Exit

💻 Development
Setup Dev Environment
Clone the repository
```bash
git clone https://github.com/yourusername/cli-file-explorer.git
cd cli-file-explorer
```
Install dependencies

```bash
pip install -r requirements.txt
```

Requirements

Windows OS
Python 3.x
Required packages:
windows-curses
Pillow (PIL)
