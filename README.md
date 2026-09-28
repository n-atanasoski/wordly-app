# Wordly
A simple Python utility that lets you quickly look up the definition of any selected word using Cambridge Dictionary.

## What It Does
The app runs in the background and uses your clipboard to look up words without requiring you to manually open a browser or type the word.

---
## Installation
### 1. Clone the repository
```bash
git clone https://github.com/n-atanasoski/wordly-app.git
cd wordly-app
```
### 2. Create a virtual environment
This step is optional, but __recommended__.
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```
#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install the dependencies
```bash
pip install -r dependencies.txt
```
### 4. Run the application
Make sure your virtual environment is activated, then run:
```bash
python run.py
```
The application will now run in a new CMD window and respond to the keyboard shortcuts.

---
## Usage
Once the application is running:
- Select a word in any application.
- Press __Ctrl+C__.
- Press __Enter__.
- The Cambridge Dictionary definition will open in a new browser tab.

When you need to type normally without the app reacting to your shortcuts, press __Ctrl+Q__ to deactivate it.
Once deactivated, press Ctrl+Q again to reactivate the app.

Press __Esc__ to exit the application.

---
## Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Copy the selected word to the clipboard |
| `Enter` | Open the definition in a new browser tab |
| `Ctrl+Q` | Toggle the app on/off |
| `Esc` | Quit the application |

---
## Requirements
- Python 3.x
- An internet connection
- A web browser

Python dependencies are listed in __dependencies.txt__.
