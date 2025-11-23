import os
import subprocess
import shutil
import datetime
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

LOG_FOLDER = os.path.join(os.path.expanduser("~"), "Desktop", "VirtualToyLogs")
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)
LOG_FILE = os.path.join(LOG_FOLDER, "logs.txt")

# ------------------ Logging ------------------ #
def save_log(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {message}\n")

def clear_log():
    with open(LOG_FILE, "w") as f:
        f.write("")

# ------------------ VS Code ------------------ #
def open_in_vscode(file_path):
    if os.path.exists(file_path):
        subprocess.Popen(["code", file_path])
    else:
        raise FileNotFoundError(f"{file_path} not found.")

# ------------------ Program Execution ------------------ #
def run_program(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    
    save_log(f"Executing program: {file_path}")
    ext = os.path.splitext(file_path)[1]
    try:
        if ext == ".py":
            subprocess.Popen(["python", file_path])
        elif ext == ".js":
            subprocess.Popen(["node", file_path])
        elif ext == ".cs":
            subprocess.Popen(["dotnet", "run", file_path])
        else:
            save_log(f"Unsupported program type: {ext}")
    except Exception as e:
        save_log(f"Error executing {file_path}: {e}")

# ------------------ Virtual Desktop ------------------ #
def play_desktop_animation(mp4_path, media_player: QMediaPlayer):
    if not os.path.exists(mp4_path):
        raise FileNotFoundError(f"{mp4_path} not found.")
    media_player.setMedia(QMediaContent(QUrl.fromLocalFile(mp4_path)))
    media_player.setVolume(50)
    media_player.play()
    save_log(f"Playing desktop animation: {mp4_path}")

# ------------------ VM Folder Utilities ------------------ #
def copy_to_vm(src_folder, vm_folder):
    if not os.path.exists(src_folder):
        raise FileNotFoundError(f"{src_folder} not found")
    if not os.path.exists(vm_folder):
        os.makedirs(vm_folder)
    for item in os.listdir(src_folder):
        s = os.path.join(src_folder, item)
        d = os.path.join(vm_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    save_log(f"Copied contents from {src_folder} to VM folder {vm_folder}")
