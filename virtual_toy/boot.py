import os
from virtual_toy.utils import save_log

def load_boot_screen(folder_path):
    """
    Load the boot screen from the BUP folder.
    Expects Boot.txt in the folder.
    """
    boot_txt = os.path.join(folder_path, "Boot.txt")
    if not os.path.exists(boot_txt):
        raise FileNotFoundError("Boot.txt not found in the selected folder")
    
    with open(boot_txt, "r") as f:
        boot_code = f.read()
    
    save_log(f"Boot screen loaded from {boot_txt}")
    return boot_code
