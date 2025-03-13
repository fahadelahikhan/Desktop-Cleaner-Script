# File Organizer Script 📂

![Python Version](https://img.shields.io/badge/python-3.4%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A modern file organization tool that automatically sorts files into category-specific subfolders. Inspired by the need for clean directory structures in developer workflows and educational environments.

## 📋 About
This script organizes files in any specified folder by moving them into subfolders based on their file extensions. Designed for developers who value clean workspaces, it demonstrates practical use of Python's pathlib for robust file handling.

## ✨ Features
- Modern path handling with `pathlib` for cross-platform compatibility
- Prevents file overwrites by skipping existing items
- Creates subfolders *only* when needed (no empty directories)
- Handles all file types - from `.txt` to `.jpg`
- Clear console feedback with move/skip status

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/fahadelahikhan/An-Arithmetic-Formatter-Project.git
cd An-Arithmetic-Formatter-Project
```

### Basic Usage
1. Edit `target_folder` in the script to your desired path
2. Run:
```python
python main.py
```

## 💡 Example
After configuring `target_folder = Path(r'/Users/me/Documents')`:
```python
# Console output:
Moved: report.pdf -> PDF Files/
Skipped: cat.jpg already exists in JPG Files/
Moved: notes.txt -> TXT Files/
Rearranging Completed!!
```

## 🧠 How It Works
1. **Path Validation**: Checks if target folder exists
2. **File Processing**:
   - Iterates through all files in directory
   - Extracts file extension to determine category
   - Creates `[EXTENSION] Files` subfolder if missing
3. **Safe Moving**:
   - Uses `shutil.move` for actual file transfer
   - Skips files that already exist in destination

Files without extensions remain in the root directory. Hidden files (starting with `.`) are ignored.

## ⚖️ License
Distributed under the [MIT License](LICENSE).

---

> **Safety First**: While this script prevents overwrites, always back up critical files before running organization tools. Concurrent file operations in other programs may cause unexpected behavior.
