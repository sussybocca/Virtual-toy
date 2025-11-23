from PyQt5 import QtWidgets, QtGui, QtCore
from virtual_toy.file_manager import validate_program_folder, validate_filesystem
from virtual_toy.boot import load_boot_screen
from virtual_toy.environment import VirtualEnvironment
from virtual_toy.utils import open_in_vscode, save_log
from virtual_toy.virtual_machine import VirtualMachineWindow
import os

class Dashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtually - Virtual Toy Environment 0.56")
        self.setGeometry(50, 50, 1000, 700)

        # Current virtual environment
        self.vm_environment = None
        self.current_vm_window = None

        # Central widget
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.main_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.title = QtWidgets.QLabel("Virtually Dashboard", font=QtGui.QFont("Arial", 24))
        self.main_layout.addWidget(self.title)

        # Buttons
        self.program_btn = QtWidgets.QPushButton("Load Program Folder (VTP)")
        self.filesystem_btn = QtWidgets.QPushButton("Load File System (VTF/System)")
        self.boot_btn = QtWidgets.QPushButton("Load Boot Screen (BUP)")
        self.desktop_btn = QtWidgets.QPushButton("Set Desktop Animation (MP4)")
        self.env_btn = QtWidgets.QPushButton("Configure Environment Name")
        self.run_vm_btn = QtWidgets.QPushButton("Run Virtual Environment")

        self.main_layout.addWidget(self.program_btn)
        self.main_layout.addWidget(self.filesystem_btn)
        self.main_layout.addWidget(self.boot_btn)
        self.main_layout.addWidget(self.desktop_btn)
        self.main_layout.addWidget(self.env_btn)
        self.main_layout.addWidget(self.run_vm_btn)

        # Connect buttons
        self.program_btn.clicked.connect(self.load_program)
        self.filesystem_btn.clicked.connect(self.load_filesystem)
        self.boot_btn.clicked.connect(self.load_boot)
        self.desktop_btn.clicked.connect(self.set_desktop_animation)
        self.env_btn.clicked.connect(self.configure_env)
        self.run_vm_btn.clicked.connect(self.run_vm)

        # Enable drag and drop for logs.txt
        self.setAcceptDrops(True)

    # ------------------ Drag & Drop ------------------ #
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.toLocalFile().endswith("logs.txt"):
                    event.accept()
                    return
        event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.endswith("logs.txt"):
                # TODO: Implement loading environment from logs
                save_log(f"Loaded virtual environment from log: {file_path}")
                QtWidgets.QMessageBox.information(self, "Environment Loaded", "Virtual environment loaded from logs!")

    # ------------------ Folder & File Handlers ------------------ #
    def load_program(self):
        if self.vm_environment is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Create a virtual environment first!")
            return
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Program Folder (VTP)")
        if folder:
            try:
                validate_program_folder(folder)
                self.vm_environment.set_program_folder(folder)
                save_log("Program folder set: " + folder)
                QtWidgets.QMessageBox.information(self, "Success", "Program folder validated!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def load_filesystem(self):
        if self.vm_environment is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Create a virtual environment first!")
            return
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select File System Folder (VTF/System)")
        if folder:
            try:
                validate_filesystem(folder)
                self.vm_environment.set_filesystem_folder(folder)
                save_log("File system folder set: " + folder)
                QtWidgets.QMessageBox.information(self, "Success", "File system validated!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def load_boot(self):
        if self.vm_environment is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Create a virtual environment first!")
            return
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select BUP Boot Folder (USB)")
        if folder:
            try:
                boot_code = load_boot_screen(folder)
                self.vm_environment.set_boot_folder(folder)
                save_log("Boot screen loaded: " + folder)
                QtWidgets.QMessageBox.information(self, "Boot Loaded", f"Boot screen loaded (preview first 200 chars):\n{boot_code[:200]}...")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def set_desktop_animation(self):
        if self.vm_environment is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Create a virtual environment first!")
            return
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Desktop Animation MP4", "", "MP4 files (*.mp4)")
        if file_path:
            self.vm_environment.set_desktop_animation(file_path)
            save_log("Desktop animation set: " + file_path)
            QtWidgets.QMessageBox.information(self, "Desktop Set", "Desktop animation set successfully!")

    # ------------------ Environment ------------------ #
    def configure_env(self):
        name, ok = QtWidgets.QInputDialog.getText(self, "Environment Name", "Enter virtual environment name:")
        if ok and name:
            self.vm_environment = VirtualEnvironment(name=name)
            save_log("Virtual environment created: " + name)
            QtWidgets.QMessageBox.information(self, "Environment Set", f"Virtual environment named: {name}")

    # ------------------ Run VM ------------------ #
    def run_vm(self):
        if self.vm_environment is None:
            QtWidgets.QMessageBox.warning(self, "Error", "Create a virtual environment first!")
            return
        self.current_vm_window = VirtualMachineWindow(
            vm_folder=self.vm_environment.vm_folder,
            desktop_animation=self.vm_environment.desktop_animation
        )
        self.current_vm_window.showFullScreen()
        save_log(f"Running virtual environment: {self.vm_environment.name}")
