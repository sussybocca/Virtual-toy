import os
from virtual_toy.utils import save_log, run_program, copy_to_vm

class VirtualEnvironment:
    def __init__(self, name="Unnamed VM"):
        self.name = name
        self.program_folder = None
        self.filesystem_folder = None
        self.desktop_animation = None
        self.boot_folder = None
        self.vm_folder = os.path.join(os.path.expanduser("~"), f"{self.name}_VM")
        if not os.path.exists(self.vm_folder):
            os.makedirs(self.vm_folder)
        save_log(f"Virtual Environment initialized: {self.name}")

    def set_program_folder(self, folder):
        self.program_folder = folder
        copy_to_vm(folder, os.path.join(self.vm_folder, "Programs"))
        save_log(f"Program folder set: {folder}")

    def set_filesystem_folder(self, folder):
        self.filesystem_folder = folder
        copy_to_vm(folder, os.path.join(self.vm_folder, "System"))
        save_log(f"File system folder set: {folder}")

    def set_desktop_animation(self, mp4_path):
        self.desktop_animation = mp4_path
        save_log(f"Desktop animation set: {mp4_path}")

    def set_boot_folder(self, folder):
        self.boot_folder = folder
        copy_to_vm(folder, os.path.join(self.vm_folder, "Boot"))
        save_log(f"Boot folder set: {folder}")

    def start_vm(self):
        save_log(f"Starting VM: {self.name}")
        # Simulate boot by loading boot.txt
        boot_txt = os.path.join(self.vm_folder, "Boot", "Boot.txt")
        if os.path.exists(boot_txt):
            with open(boot_txt, "r") as f:
                boot_code = f.read()
            save_log(f"Boot screen loaded: {boot_txt}")
            print(f"--- Boot Screen ---\n{boot_code}\n-----------------")
        else:
            save_log("Boot.txt missing!")

        # Optionally run all programs in Programs folder
        prog_folder = os.path.join(self.vm_folder, "Programs")
        if os.path.exists(prog_folder):
            for file in os.listdir(prog_folder):
                run_program(os.path.join(prog_folder, file))
        save_log(f"VM {self.name} started successfully")
